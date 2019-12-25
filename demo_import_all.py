__all__ = ['Encoder', 'Decoder', 'Loss', 'Circle', 'Triangle', 'Rectangle']


class Encoder:
    ...


class Decoder:
    ...


class Loss:
    ...


class Circle(object):
    def __init__(self, r):
        self.r = r

    def area(self):
        return self.r ** 2 * 3.14


class Rectangle(object):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_area(self):
        return self.w * self.h


class Triangle(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_the_area(self):
        a, b, c = self.a, self.b, self.c
        p = (a + b + c) / 2
        area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return area
