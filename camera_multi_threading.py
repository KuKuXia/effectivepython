import os
import struct
import threading
from concurrent.futures import ThreadPoolExecutor
from http.server import BaseHTTPRequestHandler
from socketserver import ThreadingTCPServer
from threading import Thread, RLock

import cv2
import time

"""
一个多线陈web视频监控服务器，需要对请求连接数进行限制，以防止恶意用户发起大量连接导致服务器创建大量线程，最终因为资源耗尽而瘫痪。

可以使用线程池，替代原来的每次请求创建线程
使用标准库中concurrent.futures下的ThreadPoolExecutor对象的submit和map方法可以用来启动线程池中线程执行任务
"""


def thread_pool():
    executor = ThreadPoolExecutor(3)

    def f(a, b):
        print('f', a, b)
        time.sleep(10)
        return a ** b

    future = executor.submit(f, 2, 3)
    print(future.result())
    result = executor.map(f, [2, 3, 5, 7, 8], [4, 5, 6, 9, 10])
    for i in result:
        print(i)


class ThreadingPoolTCPServer(ThreadingTCPServer):
    def __init__(self, server_address, RequestHandlerClass, bind_and_activate=True, max_thread_num=100):
        super(ThreadingPoolTCPServer, self).__init__(server_address, RequestHandlerClass,
                                                     bind_and_activate=bind_and_activate)
        self.executor = ThreadPoolExecutor(max_workers=max_thread_num)

    def process_request(self, request, client_address):
        """Start a new thread to process the request."""
        self.executor.submit(self.process_request_thread, request, client_address)


class JpegStreamer(Thread):
    def __init__(self, camera):
        Thread.__init__(self)
        self.cap = cv2.VideoCapture(camera)
        self.lock = RLock()
        self.pipes = {}

    def register(self):
        pr, pw = os.pipe()
        self.lock.acquire()
        self.pipes[pr] = pw
        self.lock.release()
        return pr

    def unregister(self, pr):
        self.lock.acquire()
        pw = self.pipes.pop(pr)
        self.lock.release()
        os.close(pr)
        os.close(pw)

    def capture(self):
        cap = self.cap
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                # ret, data = cv2.imencode('.jpg', frame)
                ret, data = cv2.imencode('.jpg', frame, (cv2.IMWRITE_JPEG_QUALITY, 40))
                yield data.tostring()

    def send(self, frame):
        n = struct.pack('l', len(frame))
        self.lock.acquire()
        if len(self.pipes):
            # _, pipes, _ = select([], iter(self.pipes.values()), [], 1)
            pipes = self.pipes.values()
            for pipe in pipes:
                os.write(pipe, n)
                os.write(pipe, frame)
        self.lock.release()

    def run(self):
        for frame in self.capture():
            self.send(frame)


# threading.local函数可以创建线程本地数据空间，其下属性对每个线程独立成长
class JpegRetriever(object):
    def __init__(self, streamer):
        self.streamer = streamer
        self.local = threading.local()

    def retrieve(self):
        while True:
            ns = os.read(self.local.pipe, 8)
            n = struct.unpack('l', ns)[0]
            data = os.read(self.local.pipe, n)
            yield data

    def __enter__(self):
        if hasattr(self.local, 'pipe'):
            raise RuntimeError()

        self.local.pipe = streamer.register()
        return self.retrieve()

    def __exit__(self, *args):
        self.streamer.unregister(self.local.pipe)
        del self.local.pipe
        return True


class Handler(BaseHTTPRequestHandler):
    retriever = None

    @staticmethod
    def setJpegRetriever(retriever):
        Handler.retriever = retriever

    def do_GET(self):
        if self.retriever is None:
            raise RuntimeError('no retriver')

        if self.path != '/':
            return

        self.send_response(200)
        self.send_header('Content-type', 'multipart/x-mixed-replace;boundary=abcde')
        self.end_headers()

        with self.retriever as frames:
            for frame in frames:
                self.send_frame(frame)

    def send_frame(self, frame):
        s = '--abcde\r\n'
        s += 'Content-Type: image/jpeg\r\n'
        s += 'Content-Length: %s\r\n\r\n' % len(frame)
        self.wfile.write(s.encode('ascii'))
        self.wfile.write(frame)


if __name__ == '__main__':
    streamer = JpegStreamer(0)
    streamer.start()

    retriever = JpegRetriever(streamer)
    Handler.setJpegRetriever(retriever)

    print('Start server...')
    # httpd = ThreadingTCPServer(('', 9000), Handler)
    httpd = ThreadingPoolTCPServer(('', 9000), Handler, max_thread_num=3)
    httpd.serve_forever()
    # thread_pool()
