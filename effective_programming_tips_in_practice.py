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


if __name__ == '__main__':
    tuple_naming()
    element_couonter()
    sort_by_value()
    common_keys_between_dictionaries()
    # keep_dict_ordered()
    # user_history()
    pickle_usage()
