from random import randint


# 为元组中的每个元素命名，提高程序可读性
# 方法1：使用枚举作为index
# 方法2：使用collections。namedtuple带有名称的元组实现
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
    strip_chars()
