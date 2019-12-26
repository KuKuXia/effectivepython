from random import randint

# 为元组中的每个元素命名，提高程序可读性
# 方法1：使用枚举作为index
# 方法2：使用collections。namedtuple带有名称的元组实现
import xlwt


def tuple_naming():
    def enum_naming():
        NAME, AGE, GENDER, EMAIL = range(4)

        student = ['Jim', 16, 'male', 'jime9898@gmail.com']

        # Name
        print(student[NAME])

        # Age
        print(student[AGE])

        # Gender
        print(student[GENDER])

        # Email
        print(student[EMAIL])

    def named_tuple_naming():
        from collections import namedtuple
        Student = namedtuple('Student', ['name', 'age', 'gender', 'email'])
        s = Student('Jim', 16, 'male', 'jim123@gmail.com')
        print(s)
        s2 = Student(name='Tomm', age=16, gender='male', email='tom123@gmail.com')
        print(s.name)
        print(s.age)
        print(s.gender)
        print(s.email)
        print(isinstance(s, tuple))

    enum_naming()
    named_tuple_naming()


# 如何统计序列或者文件中元素出现的频度
# 方法1： 循环遍历序列实现
# 方法2： 利用counter实现
def element_couonter():
    from collections import Counter
    data = [randint(0, 20) for x in range(30)]

    def loop_counter():
        c = dict().fromkeys(data, 0)
        for x in data:
            c[x] += 1
        print(c)

    def counter():
        c2 = Counter(data)
        print(c2)
        # 频率最高的n个数据
        print(c2.most_common(3))

    def word_counter():
        import re
        txt = open('./linux_kernel_coding_style').read()
        c3 = Counter(re.split('\w+', txt))
        print(c3[' '])
        print(c3.most_common(10))

    loop_counter()
    counter()
    word_counter()


# 如何根据字典中值的大小，对字典中的项排序
# 方法1： 利用zip将字典数据转换为元组
# 方法2： 传递sorted函数的key参数
def sort_by_value():
    data = {x: randint(60, 100) for x in 'xyzabcdefg'}
    print(data)
    print(sorted(data))

    # 使用dict将key与value调换位置，然后重新使用sorted
    reversed_data = dict(zip(data.values(), data.keys()))
    print(reversed_data)
    print(sorted(reversed_data))

    # 使用带有参数key的sorted
    print(sorted(data.items(), key=lambda x: x[1], reverse=True))


# 如何快速找到多个字典中的公共键
# 方法1：使用loop循环遍历所有的字典集合，查找共同的键
# 方法2：使用字典的viewkeys()方法，得到一个字典keys的集合
# 方法3：使用map函数，得到所有字典的keys的集合，然后使用reduce函数，取所有字典的keys的集合的交集
def common_keys_between_dictionaries():
    from random import randint, sample
    s1 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
    s2 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
    s3 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
    print(s1)
    print(s2)
    print(s3)

    # 使用loop实现，返回list
    def loop():
        result = []
        for k in s1:
            if k in s2 and k in s3:
                result.append(k)
        print(result)

    # 使用dict的viewkeys实现，返回集合
    def viewkeys():
        print(s1.keys() & s2.keys() & s3.keys())

    # 使用map-reduce的方法实现
    def map_reducea():
        from functools import reduce
        print(reduce(lambda a, b: a & b, map(dict.keys, [s1, s2, s3])))

    loop()
    viewkeys()
    map_reducea()


# 如何让字典根据插入顺序保持有序
# 方法：使用collections.OrderedDict代替内置Dict
def keep_dict_ordered():
    from collections import OrderedDict
    data = OrderedDict()
    data['Jim'] = (1, 35)
    data['Leo'] = (2, 40)
    data['Bob'] = (3, 45)
    data['James'] = (4, 47)
    print(data)

    def player_timer():
        from time import time
        data = OrderedDict()
        players = list('ABCDEFGH')
        start = time()

        for i in range(8):
            input()
            player = players.pop(randint(0, 7 - i))
            end = time()
            delta_time = round(end - start, 2)
            print(i + 1, player, delta_time)
            data[player] = (i + 1, delta_time)
        print('-' * 20)
        for k, v in data.items():
            print(k, v)

    player_timer()


# 如何实现用户的历史记录的功能
# 方法：使用标准库collections中的deque， 它是一个双端循环队列
# 程序推出前，可以使用pickle将队列对象存入文件，再次运行程序时将其导入

def user_history():
    from collections import deque
    N = randint(0, 100)
    history = deque([], 5)

    def guess(k):
        if k == N:
            print('right')
            return True
        elif k < N:
            print(f"{k} is less-than N.")
        else:
            print(f"{k} is greater-than N")
        return False

    while True:
        line = input("please input a number")
        if line.isdigit():
            k = int(line)
            history.append(k)
            if guess(k):
                break

        elif line in ["history", 'h']:
            print(list(history))


# 保存和导入数据
def pickle_usage():
    import pickle
    a = [randint(1, 20) for _ in range(30)]
    print(a)
    pickle.dump(a, open('./test_dump', 'wb'))
    del a
    b = pickle.load(open('./test_dump', 'rb'))
    print(b)


# 可迭代与迭代器对象
# 迭代器对象WeatherIterator，next方法每次返回一个城市气温
# 可迭代对象WeatherIterable，__iter__方法返回一个迭代器对象
def iterator_object():
    import requests
    from collections import Iterable, Iterator

    class WeatherIterator(Iterator):
        def __init__(self, cities):
            self.cities = cities
            self.index = 0

        def getweather(self, city):
            r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
            data = r.json()['data']['forecast'][0]
            return '%s: %s, %s' % (city, data['low'], data['high'])

        def __next__(self):
            if self.index == len(self.cities):
                raise StopIteration
            city = self.cities[self.index]
            self.index += 1
            return self.getweather(city)

    class WeatherIterable(Iterable):
        def __init__(self, cities):
            self.cities = cities

        def __iter__(self):
            return WeatherIterator(self.cities)

    for x in WeatherIterable([u'北京', u'济南', u'上海', u'杭州', u'深圳']):
        print(x)


# 使用生成器实现可迭代和迭代器对象
def generator_object():
    class PrimeNumber():
        def __init__(self, start, end):
            self.start = start
            self.end = end

        def isPrimeNum(self, k):
            if k < 2:
                return False
            for i in range(2, k):
                if k % i == 0:
                    return False
            return True

        def __iter__(self):
            for k in range(self.start, self.end + 1):
                if self.isPrimeNum(k):
                    yield k

    for x in PrimeNumber(1, 100):
        print(x)


# 如何进行和实现反向迭代
# 方法：实现方向迭代协议的__reversed__方法， 它返回一个方向迭代器
def reversed_iterater():
    class FloatRange:
        def __init__(self, start, end, step=0.1):
            self.start = start
            self.end = end
            self.step = step

        def __iter__(self):
            t = self.start
            while t <= self.end:
                yield t
                t += self.step

        def __reversed__(self):
            t = self.end
            while t >= self.start:
                yield t
                t -= self.step

    for x in FloatRange(1, 4, 0.5):
        print(x, end=' ')
    print()

    for x in reversed(FloatRange(1, 4, 0.5)):
        print(x, end=' ')
    print()


# 如何对迭代器进行切片操作
# 使用标准库中的itertools.islice，它能返回一个迭代对象切片的生成器
def slicing_iterator():
    from itertools import islice
    file = open('linux_kernel_coding_style', 'rb')
    # 获取文件100到110行内容
    print('100 to 110 lines')
    for line in islice(file, 100, 110):
        print(line)

    # 获取文件前10行内容
    print("the first 10 lines")
    for line in islice(file, 10):
        print(line)

    print('2200 to the last line')
    # 获取文件00到最后的内容
    for line in islice(file, 930, None):
        print(line)


# 如何在一个for语句中迭代多个可迭代对象
# 方法：使用内置函数zip，它能将多个可迭代对象合并，每次迭代返回一个元组
# 方法2：使用标准库中的itertools.chain，它能将多个可迭代对象连接
def multiple_iterators():
    # 计算多个科目的总分
    def sum_of_multi_subject():
        chinese = [randint(60, 100) for _ in range(40)]
        english = [randint(60, 100) for _ in range(40)]
        math = [randint(60, 100) for _ in range(40)]
        art = [randint(60, 100) for _ in range(40)]

        # 并行处理多个迭代对象，进行加法运算
        total_scores = []
        for scores in zip(chinese, english, math, art):
            total_scores.append(sum(scores))
        print(total_scores)

    # 选出多个班级中90分以上的人
    def score_greater_than_90():
        from itertools import chain
        class_1 = [randint(60, 100) for _ in range(40)]
        class_2 = [randint(60, 100) for _ in range(50)]
        class_3 = [randint(60, 100) for _ in range(60)]
        class_4 = [randint(60, 100) for _ in range(70)]

        # 将多个迭代对象串行连接，逐个进行计算
        result = []
        for x in chain(class_1, class_2, class_3, class_4):
            if x > 90:
                result.append(x)

        print(result)

    sum_of_multi_subject()
    score_greater_than_90()


# 如何拆分含有多种分隔符的字符串
# 方法1：连续使用str.split()方法，每次处理一种分隔符号
# 方法2：使用正则表达式的re.split()方法，一次性拆分字符串
def split_multi_seperators():
    data = 'ab;cj|efg|hi,,jkl||mn\topq;rst,uvw\txyz'

    # 连续依次使用split方法
    def seperate_using_split_multiple_times(data, ds):
        # 注意，在python3中map返回的是一个迭代器对象，如果要得到结果需要list一下
        res = [data]
        for d in ds:
            t = []
            list(map(lambda x: t.extend(x.split(d)), res))
            res = t
        # 清楚空字符串
        res = [x for x in res if x]
        print(res)

    # 使用正则表达式的方法一次性同时处理多个分隔符
    def re_split():
        import re
        result = re.split(r'[,;\t|]+', data)
        print(result)

    seperate_using_split_multiple_times(data, ';,|\t')
    re_split()


# 如何判断字符串a是否以字符串b开头或者结尾
# 方法：使用字符串的str.startswith()和str.endswith()方法
# 注意：多个匹配时参数使用元组
def string_start_or_end():
    import os, stat
    files = [name for name in os.listdir('./test_dir/') if name.endswith(('.sh', '.py'))]
    print(files)
    for file in files:
        file_st_mode = os.stat('./test_dir/' + file).st_mode
        print("Before: ", oct(file_st_mode))
        os.chmod('./test_dir/' + file, file_st_mode | stat.S_IXUSR)
        file_st_mode = os.stat('./test_dir/' + file).st_mode
        print("After: ", oct(file_st_mode))


# 如何调整字符串中文本的格式
# 使用正则表达式re.sub()方法做字符串替换，利用正则表达式的捕获组，捕获每个部分内容，在替换字符串中调整各个捕获组的顺序
def change_time_format():
    import re
    data = '2016-05-23 10:59:27 status half-configured libc-bin:amd64 2.19-0ubuntu6.5'
    changed_data_1 = re.sub('(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', data)
    changed_data_2 = re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})', r'\g<month>/\g<day>/\g<year>', data)
    print(data)
    print(changed_data_1)
    print(changed_data_2)


# 如何将 多个小字符串拼接成一个大的字符串
# 方法1：迭代列表，连续使用+操作一次拼接每一个字符串
# 方法2：使用str.join()方法，更加快速的拼接列表中的所有字符串
def join_elements_of_list():
    data = [1, 2, 3, 4, 5, 6, 67]

    # 使用+方法一个一个连接，中间会产生多个中间变量，效率低
    s = ''
    for i in data:
        s += str(i)
    print(s)
    # 使用join方法快速连接
    print(''.join(map(str, data)))


# 如何将字符串进行左右、居中对齐
# 方法1：使用字符串额str.ljust()，str.rjust(),str.center()进行左右、居中对齐
# 方法2：使用format()方法，传递类似'<20','>20','^20'参数完成同样任务
def str_just():
    data = 'abc'
    print(data.ljust(20, '-'))
    print(data.rjust(20, '*'))
    print(data.center(20, '%'))
    print(format(data, '>20'))
    print(format(data, '<20'))
    print(format(data, '^20'))

    data = {'chinese': 12,
            'english_123': 123,
            'art': 12,
            'math_123': 123}
    w = max(list(map(len, data.keys())))
    for k in data:
        print(k.ljust(w, ' '), ':', data[k])


# 如何去掉字符串中不需要的字符串
# 方法1：字符串strip(),rstrip(),lstrip()方法
# 方法2: 使用切片+拼接的方式，删除特定区间的字符
# 方法3：字符串的replace()方法或者正则表达式re.sub删除任意位置字符
# 方法4：字符串translate()方法，可以同时删除多种不同字符
def strip_chars():
    data = '--+++ab90***bc==--++   '
    # 利用strip删除左右两边的字符
    print(data.strip())
    print(data.lstrip())
    print(data.rstrip())
    print(data.strip('-+'))

    # 利用切片选择需要位置的字符
    print(data[5:9] + data[12:14])

    # 利用replace删除任意位置的单个字符
    data = '\t123\t123\tab\tasjfl\t'
    print(data.replace('\t', ''))

    # 利用正则表达式re。sub删除任意位置字符
    import re
    data = '\tas\rasdfklj\tasd\tsdf\rjdl\tasljd\rsd'
    print(re.sub('[\t\r]', '', data))

    # 利用str的translate方法
    data = 'abc12345xyz'
    print(data.translate(str.maketrans('abcxyz', 'xyzabc')))

    data = 'abd\rbasdj\tsdjl\tsdasdf\n'
    print('read this short text'.translate(str.maketrans('aeiou', '     ')))
    print(data.translate(str.maketrans('\r\t\n', '   ')))


# 如何读取文本文件
# 字符串语义发生了变化
# Python2      Python3
# str      >>    bytes
# unicode  >>    str
# Python2: 写入文件前对unicode编码，读入文件后对二进制字符串解码
# Python3: open函数指定't'的文本模式，endcoding指定编码格式
def open_sace_files():
    s = u'你好'
    encoded_s_1 = s.encode('utf8')
    encoded_s_2 = s.encode('gbk')
    print(encoded_s_1)
    print(encoded_s_2)
    # 注意编解码需要一致
    decoded_s_1 = encoded_s_1.decode('utf8')
    decoded_s_2 = encoded_s_2.decode('gbk')
    print(decoded_s_1)
    print(decoded_s_2)

    def py2_save_file():
        # 在Python2中运行
        file = open('test_dir/py2.txt', 'w')
        file.write(s.encode('gbk'))
        file.close()

        file = open('test_dir/py2.txt', 'r')
        s_loaded = file.read()
        print(s_loaded)
        # 需要解码
        # print(s_loaded.decode('gbk'))

    def py3_save_file():
        file = open('test_dir/py2.txt', 'wt', encoding='utf8')
        file.write(u'你好，我爱编程！')
        file.close()

        file = open('test_dir/py2.txt', 'rt', encoding='utf8')
        s_loaded = file.read()
        print(s_loaded)

    py3_save_file()


# 如何设置文件的缓冲
# 将文件内容写入到硬件设备时，使用系统调用，这类I/O操作的时间很长，为了减少
# I/O操作次数，文件通常使用缓冲区，有足够多的数据才进行系统调用，缓冲行为分
# 为：
# 全缓冲: open()函数的buffering设置为大于1的整数n，n为缓冲区大小
# 行缓冲: open()函数的buffering设置为1
# 无缓冲:open函数的buffering设置为0

def set_file_buffer():
    # linux下测试
    file = open('test_dir/file_buffer.txt', 'w', buffering=1000)
    file.write('abc')
    file.write('+' * 997)


# 如何访问文件的状态
# 系统调用：标准库中os模块下的三个系统调用stat，fstat，lstat获取文件状态
# 快捷函数：标准库中os.path下一些函数，使用起来更加简洁
def file_status():
    import os
    print(os.stat('test_dir/a.sh'))
    print(os.path.isdir('test_dir'))
    # 获取文件的绝对路径前半部分
    print(os.path.abspath('test_dir/a.sh').split('.')[0])


# 如何使用临时文件
# 使用标准库中的tempfile下的TemporaryFile, NamedTemporaryFile
def temporary_file():
    from tempfile import TemporaryFile, NamedTemporaryFile
    # 文件系统中没有名字，找不到，只能在一个进程中访问
    file = TemporaryFile()
    file.write(b'abdef' * 100000)
    file.seek(0)
    print(file.read(100))
    print('-' * 20)
    print(file.read(100))

    # 文件系统中有名字，可以找到，将delete参数设置为false，即使当前进程不需要改临时文件，也不会立即删除该文件，因此可以设置让多个进程同时访问
    named_temp_file = NamedTemporaryFile(delete=False)
    named_temp_file.write(b'abc' * 100)
    print(named_temp_file.name)


# 如何读取csv数据
# 使用标准库中的csv模块，可以使用其中reader和writer完成csv文件读写
def read_csv_demo():
    import csv

    with open('test_dir/card.csv', encoding='utf8', mode='rt') as file:
        reader = csv.reader(file)
        with open('test_dir/card_copy.csv', 'wt', encoding='utf8') as file_copy:
            writer = csv.writer(file_copy)
            header = next(reader)
            writer.writerow(header)
            for row in reader:
                if row[2] > '1997-10-13':
                    break
                writer.writerow(row)
            file_copy.flush()
    print('End')


# 如何读写json数据
# 使用标准库中的json模块，其中loads，dumps函数可以完成json数据的读写
def json_laod_and_save():
    import json
    data = [1, 2, [2, 3], 'abc', {'name': 'james', 'age': 19, 'gender': None}]
    a = json.dumps(data, sort_keys=True, separators=[',', ':'])
    print(a)
    print(json.loads('[1,2,[2,3],"abc",{"age":19,"gender":null,"name":"james"}]'))

    # json.load()和json.dump()针对一个文件描述符
    with open('test_dir/json_demo.txt', 'w') as file:
        json.dump(data, file)

    with open('test_dir/json_demo.txt', 'r') as file:
        load_json = json.load(file)
        print(load_json)


# 如何解析简单的xml文档
# xml是一种十分常用的标记性语言，可提供统一的方法来描述应用程序的结构化数据
# 可以使用标准库中的xml.etree.ElementTree其中的parse函数可以解析xml文档
def parse_xml():
    from xml.etree.ElementTree import parse
    file = open('test_dir/demo.xml')
    et = parse(file)
    root = et.getroot()
    print(root.tag)
    print(root.attrib)
    print(root.text)
    for child in root:
        print(child.get('name'))

    # 查找所有名字为note的节点
    print(root.findall('note'))
    # 查找当前节点下的一级节点
    for note in root.iterfind('note'):
        print(note.get('name'))

    # 查找当前节点下的所有下级节点
    for e in root.iter():
        print(e)

    # 查找当前节点下所有子级特定名称的节点
    for e in root.iter('from'):
        print(e)


# 如何构建xml文档
# 可以使用标准库中的xml.etree.ElementTree其中的write函数可以写入文件
def make_a_xml():
    from xml.etree.ElementTree import Element, ElementTree, tostring

    e = Element('Data')
    print(e.tag)
    e.set('name', 'abc')
    print(tostring(e))
    e2 = Element('Row')
    e3 = Element('Open')
    e3.text = '8.08'
    e2.append(e3)
    print(tostring(e2))
    e.append(e2)
    print(tostring(e))

    et = ElementTree(e)
    et.write('test_dir/demo_2.xml')


# 将csv文件写入到xml文件中
def pretty(e, level=0):
    if len(e) > 0:
        e.text = '\n' + '\t' * (level + 1)
        for child in e:
            pretty(child, level + 2)
            child.tail = child.tail[:-1]
    e.tail = '\n' + '\t' * level


def csv_to_the_xml(csv_file_name, xml_file_name):
    import csv
    from xml.etree.ElementTree import Element, ElementTree
    reader = csv.reader(csv_file_name)
    headers = next(reader)
    headers = list(map(lambda h: h.replace(' ', ''), headers))
    # print(headers)

    root = Element('Data')
    for row in reader:
        eRow = Element('Row')
        root.append(eRow)
        for tag, text in zip(headers, row):
            e = Element(tag)
            e.text = text
            eRow.append(e)
    pretty(root)
    e_root = ElementTree(root)
    e_root.write(xml_file_name)
    print("Saved the xml file in ", xml_file_name)


def csv_to_xml():
    with open('test_dir/card.csv', 'rt', encoding='utf8') as csv_file:
        csv_to_the_xml(csv_file, 'test_dir/card.xml')
    print('csv_to_xml, done!')


# 如何读写excel文件
# 使用第三方库xlrd和xlwt，这两个库分别用于excel读写操作
def excel_read_and_write():
    import xlrd
    book = xlrd.open_workbook('test_dir/demo.xlsx')
    print(book.sheets())
    sheet = book.sheet_by_index(0)
    print(sheet.nrows)
    print(sheet.ncols)
    print(sheet.cell(0, 0))
    print(sheet.row(1))
    print(sheet.row_values(1, 1))

    def read_and_write():
        rbook = xlrd.open_workbook('test_dir/demo.xlsx')
        rsheet = rbook.sheet_by_index(0)

        nc = rsheet.ncols
        rsheet.put_cell(0, nc, xlrd.XL_CELL_TEXT, u'总分', None)

        for row in range(1, rsheet.nrows):
            # 除去第一列之后的行元素和
            t = sum(rsheet.row_values(row, 1))
            rsheet.put_cell(row, nc, xlrd.XL_CELL_NUMBER, t, None)

        wbook = xlwt.Workbook(encoding='utf8')
        wsheet = wbook.add_sheet(rsheet.name)
        # style = xlwt.easyxf('align: vertical center, horizontal center')

        for r in range(rsheet.nrows):
            for c in range(rsheet.ncols):
                wsheet.write(r, c, rsheet.cell_value(r, c))

        wbook.save('./test_dir/output.xls')

    read_and_write()


# 如何派生内置不可变类型并修改其实例化行为
# 定义类IntTuple继承内置tuple，并且实现__new__，修改实例化行为
def change_the_immutable_object():
    class IntTuple(tuple):
        def __new__(cls, iterable):
            g = (x for x in iterable if isinstance(x, int) and x > 0)
            print('__new__ called')
            return super(IntTuple, cls).__new__(cls, g)

        def __init__(self, iterable):
            # Before
            super(IntTuple, self).__init__()
            # After

    t = IntTuple([1, -1, 'abc', 6, ['x', 'y'], 3])
    print(t)
    print('ended')


# 如何为创建大量实例节省内存
# 定义类的__slots__属性，它是用来声明实例属性名字的列表
def saving_memory_using_slots():
    class Player1(object):
        def __init__(self, uid, name, status=0, level=1):
            params = locals()
            del params['self']
            self.__dict__ = params

    class Player2(object):
        __slots__ = ['uid', 'name', 'status', 'level']

        def __init__(self, uid, name, status=0, level=1):
            self.uid = uid
            self.name = name
            self.status = status
            self.level = level

    p1 = Player1('0001', 'Jim', status=0, level=2)
    p2 = Player2('0002', 'Tom', status=3, level=4)
    import sys
    print(sys.getsizeof(p1))
    print(sys.getsizeof(p2))
    print(set(dir(p1)) - set(dir(p2)))
    print(p1.__dict__)
    print(p2.__slots__)


# 如何让对象支持上下文管理
# 上下文管理：比如打开文件，进行操作后需要关闭文件
# 实现上下文管理协议，需要定义实例的__enter__, __exit__方法，他们分别在with开始和结束时被调用
def context_management():
    from socket import socket, AF_INET, SOCK_STREAM

    class LazyConnection:
        """
        编写上下文管理器的主要原理是你的代码会放到 with 语句块中执行。 当出现 with 语句的时候，对象的 __enter__() 方法被触发，
        它返回的值(如果有的话)会被赋值给 as 声明的变量。然后，with 语句块里面的代码开始执行。 最后，__exit__() 方法被触发进行清理工作。
        """

        def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
            self.address = address
            self.family = family
            self.type = type
            self.connections = []

        def __enter__(self):
            sock = socket(self.family, self.type)
            sock.connect(self.address)
            self.connections.append(sock)
            return sock

        def __exit__(self, exc_ty, exc_val, tb):
            connection = self.connections.pop()
            print('connection closed')
            connection.close()

    conn = LazyConnection(('www.python.org', 80))
    from functools import partial
    with conn as s1:
        # conn.__enter__() executes: connection open
        s1.send(b'GET /index.html HTTP/1.0\r\n')
        s1.send(b'Host: www.python.org\r\n')
        s1.send(b'\r\n')
        resp = b''.join(iter(partial(s1.recv, 8192), b''))
        print('response 1: ', resp)
        # conn.__exit__() executes: connection closed
        with conn as s2:
            s2.send(b'GET /index.html HTTP/1.0\r\n')
            s2.send(b'Host: www.python.org\r\n')
            s2.send(b'\r\n')
            resp = b''.join(iter(partial(s2.recv, 8192), b''))
            print('response 2: ', resp)
            # s1 and s2 are independent sockets


# 如何创建可管理的对象属性
# 形式上是属性访问，但是实际上调用方法
# 方法：使用property函数为类创建可管理属性，fget/fset/fdel对应相应属性访问
def manageable_object_property():
    from math import pi
    class Circle(object):

        def __init__(self, radius):
            self.radius = radius

        def get_radius(self):
            return round(self.radius, 3)

        def set_radius(self, value):
            if not isinstance(value, (int, float)):
                raise ValueError('Wrong type.')
            self.radius = value

        def get_area(self):
            return self.radius ** 2 * pi

        R = property(get_radius, set_radius)

    c = Circle(1.2)
    print(c.R)
    c.R = 20
    print(c.R)


# 如何让类支持比较操作
# 方法1： 类的比较运算符重载，需要实现以下方法：
# __it__, __le__, __gt__, __ge__, __eq__, __ne__
# 方法2： 使用标准库下的functools下的类装饰器total_ordering可以简化该过程
def comparison_operation():
    from functools import total_ordering
    from abc import abstractmethod

    @total_ordering
    class Shape(object):
        @abstractmethod
        def area(self):
            pass

        def __lt__(self, obj):
            print('in __lt__')
            if not isinstance(obj, Shape):
                raise TypeError('Obj is not Shape')
            return self.area() < obj.area()

        def __eq__(self, obj):
            print('in __eq__')
            if not isinstance(obj, Shape):
                raise TypeError('Obj is not Shape')
            return self.area() <= obj.area()

    class Rectangle(Shape):
        def __init__(self, w, h):
            self.w = w
            self.h = h

        def area(self):
            return self.w * self.h

    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius

        def area(self):
            return self.radius ** 2 * 3.14

    r1 = Rectangle(5, 3)
    r2 = Rectangle(4, 4)
    c1 = Circle(5)
    print(f'r1: {r1.area()}, r2: {r2.area()}, c1: {c1.area()}')
    print(r1 < c1)
    print(r2 == c1)
    # print(c1 > 1) # raise type error


# 如何使用描述符对实例属性做类型检查
# 使用描述符来实现需要类型检查的属性
# 分别实现__get__, __set__, __delete__方法
# 在__set__内使用isinstance函数做类型检查
def type_check():
    class Attr(object):
        def __init__(self, name, type_):
            self.name = name
            self.type_ = type_

        def __get__(self, instance, owner):
            print('in __get__', instance, owner)
            return instance.__dict__[self.name]

        def __set__(self, key, value):
            print('in __set__')
            if not isinstance(value, self.type_):
                raise TypeError('expected an %s' % self.type_)
            key.__dict__[self.name] = value

        def __delete__(self, instance):
            print('in __delete__')
            del instance.__dict__[self.name]

    class Person(object):
        name = Attr('name', str)
        age = Attr('age', int)
        height = Attr('height', float)

    a = Person()
    a.name = 'Bob'
    print(a.name)
    a.age = 20


# 如何在环状数据结构中管理内存
# 使用标准库weakref，它可以创建一种能访问对象但是不增加引用计数的对象
def manage_the_memory_of_circle_data_structure():
    import weakref
    class Data(object):
        def __init__(self, value, owner):
            self.owner = weakref.ref(owner)
            self.value = value

        def __str__(self):
            return f'{self.owner()} data, value is {self.value}'

        def __del__(self):
            print('in Data.__del__')

    class Node(object):
        def __init__(self, value):
            self.data = Data(value, self)

        def __del__(self):
            print('in Node.__del__')

    node = Node(100)
    del node


# 如何通过实例方法名字的字符串调用方法
# 使用内置函数getattr，通过名字在实例上获取方法对象，然后调用

def different_method_names():
    from demo_import_all import Circle, Triangle, Rectangle

    def get_area(shape):
        for name in ('area', 'get_the_area', 'get_area'):
            f = getattr(shape, name, None)
            if f:
                return f()

    shape1 = Circle(2)
    shape2 = Triangle(3, 4, 5)
    shape3 = Rectangle(4, 5)
    shapes = [shape1, shape2, shape3]
    print(list(map(get_area, shapes)))


# 如何使用多线程
# 使用标准库threading.Thread创建线程，在每一个线程中下载并且转换一只股票
def multi_threading():
    import requests
    from io import StringIO
    from note_demo import cookies
    from threading import Thread

    def download(url):
        s = requests.Session()
        response = s.get(
            "https://query1.finance.yahoo.com/v7/finance/download/000001.SZ?period1=1545803369&period2=1577339369&interval=1d&events=history&crumb=60oUVJrpMif",
            cookies=cookies, verify=False)

        if response.ok:
            return StringIO(response.text)

    def handle(sid):
        print(f"Download...{sid}")
        url = 'https://finance.yahoo.com/quote/%s.SZ'
        url %= str(sid).rjust(6, '0')
        rf = download(url)
        if rf is None: return
        print("Convert to xml...(%d)" % sid)
        xml_file_name = str(sid).rjust(6, '0') + '.xml'
        with open(xml_file_name, 'wb') as wf:
            csv_to_the_xml(rf, 'test_dir/finance/' + xml_file_name)

    # 简单使用
    t = Thread(target=handle, args=(1,))
    t.start()

    # 常见是新建一个类实现
    class MyThread(Thread):
        def __init__(self, sid):
            super().__init__()
            self.sid = sid

        def run(self):
            handle(self.sid)

    threads = []
    for i in range(1, 11):
        t = MyThread(i)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('\nMain thread done!')

    # 如何线程间通信
    # 由于全局解释器锁的存在，多线程进行CPU密集型操作并不能提高执行效率，因此：
    # 使用多个DownloadThread线程进行下载，（I/O操作）
    # 使用一个ConvertThread线程进行转换，（CPU密集型操作）
    # Download线程把下载数据放入队列，Convert线程从队列中提取数据
    # 典型的生产者消费者模型

    # 使用标准库中Quene.Queue，它是一个线程安全的队列
    # from collections import deque
    from Queue import Queue
    # 共享数据队列
    q = Queue()

    class DownloadThread(Thread):
        def __init__(self, sid):
            super(DownloadThread, self).__init__()
            self.sid = sid
            self.url = 'https://finance.yahoo.com/quote/%s.SZ'
            self.url %= str(sid).rjust(6, '0')

        def download(self, url):
            s = requests.Session()
            response = s.get(
                "https://query1.finance.yahoo.com/v7/finance/download/000001.SZ?period1=1545803369&period2=1577339369&interval=1d&events=history&crumb=60oUVJrpMif",
                cookies=cookies, verify=False)

            if response.ok:
                return StringIO(response.text)

        def run(self):
            data = self.download(self.url)
            # 多线程访问同一个队列不安全，需要添加锁

            q.append((self.sid, data))

    class CovertThread(Thread):
        def __init__(self):
            super(CovertThread, self).__init__()

        def csv_to_xml(self, csv_file, xml_file):
            csv_to_the_xml(csv_file, xml_file)

        def run(self):
            # 1. sid, data

            # 2.
            file_name = str(sid).rjust(6, '0') + '.xml'
            with open(file_name, 'wb') as wf:
                self.csv_to_xml(data, wf)

if __name__ == '__main__':
    # tuple_naming()
    # element_couonter()
    # sort_by_value()
    # common_keys_between_dictionaries()
    # keep_dict_ordered()
    # user_history()
    # pickle_usage()
    # iterator_object()
    # generator_object()
    # reversed_iterater()
    # slicing_iterator()
    # multiple_iterators()
    # split_multi_seperators()
    # string_start_or_end()
    # change_time_format()
    # join_elements_of_list()
    # str_just()
    # strip_chars()
    # open_sace_files()
    # set_file_buffer()
    # file_status()
    # temporary_file()
    # read_csv_demo()
    # json_laod_and_save()
    # parse_xml()
    # make_a_xml()
    # csv_to_xml()
    # excel_read_and_write()
    # change_the_immutable_object()
    # saving_memory_using_slots()
    # context_management()
    # manageable_object_property()
    # comparison_operation()
    # type_check()
    # manage_the_memory_of_circle_data_structure()
    # different_method_names()
    multi_threading()
