"""
This script is copied from:
Link: https://www.techbeamers.com/essential-python-tips-tricks-programmers/
"""
import socket
import sys
import threading

from demo_import_all import *


# Inplace swapping of two numbers
def inplace_swapping_of_two_numbers(a, b):
    print(f"Original a: {a}, b: {b}")
    a, b = b, a
    print(f"After swapping, a: {a}, b: {b}")


# Chaining of comparison operations
def chaining_of_comparison_operations():
    n = 10
    print(1 < n < 20)
    print(1 > n > 9)


#  Use Of Ternary Operator For Conditional Assignment.
# [on_true] if [expression] else [on_false]
def ternary_operator_for_conditional_assignment(a, b, c):
    print([m ** 2 if m > 10 else m ** 4 for m in range(20)])
    return a if a <= b and a <= c else (b if b <= a and b <= c else c)


# Work with multi-line strings
def multi_line_strings():
    multi_str = 'Who am I' \
                'Where row_id < 5'
    multi_str_2 = ("Hello World"
                   "I'm from earth"
                   "order by age ")
    print(multi_str)
    print(multi_str_2)


# Storing elements of a list into new variables
def unpacking_list():
    a = [1, 2, 3]
    x, y, z = a
    print(f"x: {x}, y: {y}, z:{z}")


# Print the file path of imported modules
def print_file_path():
    print(threading)
    print(socket)


# Use the interactive "_" operator
# In the python console, whenever we test an expression or call a function,
# the result dispatches to a temporary name, _(an underscore)

# Dictionary/set comprehensions
def dictionary_and_set_comprehensions():
    test_dict = {i: i ** 2 for i in range(10)}
    test_set = {i ** 2 for i in range(10)}
    print(test_dict)
    print(test_set)


# Setup file sharing
# for python 3:
# python -m http.server
# for python 2:
# python -m SimpleHTTPServer

# Inspect an object in python
def inspect_an_object():
    test = [1, 8, 3, 4, 5, 5]
    print(dir(test))
    test.sort()
    print(test)


# Simplify if statement
# if m in {1,3,5,7}, use set, because it can access each element by O(1)

# Detect python version at runtime
def detect_python_version_at_runtime():
    import sys
    print(sys.version_info)
    if sys.version_info <= (3, 6):
        print("Sorry, you aren't running on python 3.5\n")
        print("Please upgrade to 3.6.\n")
        sys.exit()


# Combine multiple strings
def combine_multiple_strings():
    test = ['I', 'like', 'python', 'automation']
    print(' '.join(test))


# Four ways to reverse string/list
def reverse_string_or_list():
    test_list = [1, 3, 5, 6]

    # Reverse the list itself
    test_list.reverse()
    print(test_list)

    # Reverse while iterating in a loop
    for element in reversed([1, 3, 5, 6]):
        print(element, end=' ')

    # Reverse a string in line
    print("\n" + "Test string"[::-1])

    # Reverse a list in line
    print([1, 3, 5, 6][::-1])


# Play with enumeration
def enumeration_test():
    testlist = [10, 20, 30]
    for i, value in enumerate(testlist):
        print(f"index: {i}, value: {value}")


# Use of enums in python
class Shapes:
    Circle, Square, Triangle, Quadrange = range(4)


# Return multiple values from functions
def return_multiple_values_from_functions():
    return 1, 2, 3, 4


def enum_test():
    print(Shapes.Circle)
    print(Shapes.Square)
    print(Shapes.Triangle)
    print(Shapes.Quadrange)


# Unpack function arguments using the splat operator
def unpack_function_arguments_using_the_splat_operator(x, y, z):
    print(x, y, z)


def unpack_function_arguments_test():
    test_dict = {'x': 1, 'y': 2, 'z': 3}
    test_list = [10, 20, 30]
    unpack_function_arguments_using_the_splat_operator(*test_dict)
    unpack_function_arguments_using_the_splat_operator(**test_dict)
    unpack_function_arguments_using_the_splat_operator(*test_list)


# Using a dictionary to store a switch
def store_expressions_using_dictionary():
    stdcalc = {
        'sum': lambda x, y: x + y,
        'subtract': lambda x, y: x - y
    }
    print(stdcalc['sum'](9, 3))
    print(stdcalc['subtract'](9, 3))


# Calculate the factorial of any number in one line
def the_factorial_of_any_number(number=3):
    import functools
    result = (lambda k: functools.reduce(int.__mul__, range(1, k + 1), 1))(number)
    print(result)


# Find the most frequent value in list
def most_frequent_value_in_list():
    test = [1, 2, 3, 4, 5, 6, 7, 8, 5, 3, 2, 3, 44, 5, 5, 65, 6, 2]
    print(max(set(test), key=test.count))


# Reset recursion limit
# Python restricts recursion limit to 1000, we can though reset its value
def reset_recursion_limit():
    x = 5000
    print(sys.getrecursionlimit())

    sys.setrecursionlimit(x)
    print(sys.getrecursionlimit())


# Check the memory usage of an object
def check_the_memory_usage_of_an_object():
    print(sys.getsizeof(1))
    print(sys.getsizeof('a'))
    print(sys.getsizeof([1, 2, 3]))
    print(sys.getwindowsversion())


# Use __slots__ to reduce memory overheads
def reduce_memory_overheads_using_slots():
    class FileSystem:
        def __init__(self, files, folders, devices):
            self.files = files
            self.folders = folders
            self.devices = devices

    class FileSystemReduced:
        __slots__ = ['files', 'folders', 'devices']

        def __init__(self, files, folders, devices):
            self.files = files
            self.folders = folders
            self.devices = devices

    print(sys.getsizeof(FileSystem))
    print(sys.getsizeof(FileSystemReduced))


# Lambda to limit print function
def lambda_to_limit_print_function():
    limit_print = lambda *args: print(' '.join(map(str, args)))
    limit_print('python', 'tips', 1000, 10001)


# Create a dictionary from two related sequences
def create_a_dictionary_from_two_related_sequences():
    a = [1, 2, 3]
    b = [4, 5, 6]
    print(dict(zip(a, b)))


# In line search for multiple prefixes in a string
def in_line_search():
    print("http://www.googlg.com".startswith(("http://", "https://")))
    print("http://www.google.co.uk".endswith(('.com', '.co.uk')))


# Form a unified list without using any loops
def unified_list():
    import itertools
    test = [[-1, -2], [30, 40], [[2, 3], [3, 45.9], 4, 6], [23, 3]]
    print(list(itertools.chain.from_iterable(test)))


# A true switch-case statement in python
def switch_case_test():
    def switch_case(x):
        return switch_case._system_dict.get(x, None)

    switch_case._system_dict = {'files': 10, 'folders': 5, 'devices': 2}

    print(switch_case('default'))
    print(switch_case('devices'))


# Lambda, map, filter, reduce
# Lambda functions are meant for one time use.
# Each time lambda x: dosomething(x) is called, the function has to be created,
# which hurts the performance if you call lambda x: dosomething(x) multiple times (e.g. when you pass it inside reduce).
def lambda_map_filter_reduce():
    def square_fn(x):
        return x * x

    squared_ld = lambda x: x * x
    for i in range(10):
        assert square_fn(i) == squared_ld(i)
    nums = [1, 2, 3, 4, 5]
    nums_squared = [i ** 2 for i in nums]
    print(nums_squared)
    nums_squared_1 = map(square_fn, nums)
    nums_squared_2 = map(lambda x: x ** 2, nums)
    print(f'nums_squared_1: {list(nums_squared_1)}, nums_squared_2: {list(nums_squared_2)}')

    def mean_sqared_error():
        a, b = 3, -0.5
        xs = [2, 3, 4, 5]
        labels = [6.4, 8.9, 10.9, 15.3]
        # Method 1: using a loop
        errors = []
        for i, x in enumerate(xs):
            errors.append((a * xs[i] + b - labels[i]) ** 2)
        print(sum(errors) ** 0.5 / len(xs))

        # Methods 2: using map
        # Note that objects returned by map and filter are iterators
        # which means that their values aren't stored but generated as needed
        # After you've called sum(diffs), diffs becomes empty.
        # If you want to keep all elements in diffs, convert it to a list using list(diffs).
        diffs = map(lambda x, y: (a * x + b - y) ** 2, xs, labels)
        print(sum(diffs) ** 0.5 / len(xs))

        # 将满足特定条件的元素取出来
        bad_pred = filter(lambda x: x > 0.6, errors)
        print(list(bad_pred))

        # 对列表中的元素依次执行动作
        product = 1
        for num in nums:
            product *= num
        print(product)

        from functools import reduce
        product = reduce(lambda x, y: x * y, nums)
        print(product)

    mean_sqared_error()


# List
def list_function():
    # Unpacking
    elements = [1, 2, 3, 4]
    a, b, c, d = elements
    print(a, b, c, d)

    a, *new_elements, d = elements
    print(a, new_elements, d)

    # Slicing
    elements = list(range(10))
    print(elements)
    # The syntax [x:y:z] means "take every zth element of a
    # list from index x to index y".
    print(elements[::-1])
    print(elements[::2])
    print(elements[-2::-2])

    del elements[::2]
    print(elements)

    # Insertion
    elements = list(range(10))
    elements[0] = 10
    print(elements)
    elements[1:2] = [20, 30, 40]
    print(elements)
    elements[1:1] = [0.2, 0.3, 0.4]
    print(elements)

    # Flattening
    list_of_lists = [[1], [2, 3], [4, 5, 6]]
    a = sum(list_of_lists, [])
    print(a)

    # Flatten a nested lists
    nested_lists = [[1, 2], [[3, 4], [5, 6], [[7, 8], [9, 10], [[11, [12, 13]]]]]]
    flatten = lambda x: [y for l in x for y in flatten(l)] if type(x) is list else [x]
    print(flatten(nested_lists))


# List vs generator
def list_vs_generator():
    tokens = ['i', 'want', 'to', 'go', 'to', 'school']

    def ngrams(tokens, n):
        length = len(tokens)
        grams = []
        for i in range(length - n + 1):
            grams.append(tokens[i:i + n])
        return grams

    print(ngrams(tokens, 3))

    # In the above example, we have to store all the n-grams at the same time.
    # If the text has m tokens, then the memory requirement is O(nm), which can be problematic when m is large.
    # Instead of using a list to store all n-grams,
    # we can use a generator that generates the next n-gram when it's asked for.
    # This is known as lazy evaluation. We can make the function ngrams returns a generator using the keyword yield.
    # Then the memory requirement is O(m+n).
    def ngrams(tokens, n):
        length = len(tokens)
        for i in range(length - n + 1):
            yield tokens[i:i + n]

    ngram_generator = ngrams(tokens, 3)
    print(ngram_generator)
    for i in ngram_generator:
        print(i)

        # Another way to generate n-grams is to use slices to create lists: [0, 1, ..., -n], [1, 2, ..., -n+1], ..., [n-1, n, ..., -1], and then zip them together.
        #
        def ngram_2(tokens, n):
            length = len(tokens)
            slices = (tokens[i:length - n + i + 1] for i in range(n))
            return zip(*slices)

        ngram_generator = ngram_2(tokens, 3)
        print(ngram_generator)

        for ngram in ngram_generator:
            print(ngram)


# Classes and magic methods
# In Python, magic methods are prefixed and suffixed with the double underscore __, also known as dunder.
def class_and_magic_function():
    class Node:
        """ A struct to denote the node of a binary tree.
        It contains a value and pointers to left and right children.
        """
        """
        For classes like Node where we know for sure all the attributes they can support (in the case of Node, they are value, left, and right), we might want to use __slots__ to denote those values for both performance boost and memory saving. 
        """
        __slots__ = ('value', 'left', 'right')

        def __init__(self, value, left=None, right=None):
            self.value = value
            self.left = left
            self.right = right

        def __repr__(self):
            strings = [f'value: {self.value}', f'left: {self.left.value}' if self.left else 'left: None',
                       f'right: {self.right.value}' if self.right else 'right: None']
            return ', '.join(strings)

        def __eq__(self, other):
            return self.value == other.value

        def __lt__(self, other):
            return self.value < other.value

        def __ge__(self, other):
            return self.value >= other.value

    left_node = Node(4)
    root = Node(5, left_node)
    print(root)  # value: 5, left: 4, right: None
    print(left_node == root)  # False
    print(left_node < root)  # True
    print(left_node >= root)  # False


# Local namespace, object's attributes
def local_namesspaces_and_object_attributes():
    class Model1:
        def __init__(self, hidden_size=100, num_layers=3, learning_rate=3e-4):
            print(locals())
            self.hidden_size = hidden_size
            self.num_layers = num_layers
            self.learning_rate = learning_rate

    model1 = Model1()
    # All attributes of an object are stored in its __dict__.

    print(model1.__dict__)

    # Note that manually assigning each of the arguments to an attribute can be quite tiring when the list of the
    # arguments is large. To avoid this, we can directly assign the list of arguments to the object's __dict__.
    class Model2:
        def __init__(self, hidden_size=100, num_layers=3, learning_rate=3e-4):
            params = locals()
            del params['self']
            self.__dict__ = params

    model2 = Model2()
    print(model2.__dict__)

    class Model3:
        def __init__(self, **kwargs):
            self.__dict__ = kwargs

    model3 = Model3(hidden_size=100, num_layers=3, learning_rate=3e-4)
    print(model3.__dict__)


# 使用__all__仅仅导入特定函数和类
def import_all_demo():
    try:
        a = helper()  # 因为在
    except:
        a = Encoder()
        print('只导入了特定的函数')


if __name__ == '__main__':
    # inplace_swapping_of_two_numbers(5, 8)
    # chaining_of_comparison_operations()
    # print(ternary_operator_for_conditional_assignment(1, 0, 1))
    # print(ternary_operator_for_conditional_assignment(100, 22, 99))
    # multi_line_strings()
    # Debugging the script
    # pdb.set_trace()
    # unpacking_list()
    # print_file_path()
    # dictionary_and_set_comprehensions()
    # inspect_an_object()
    # detect_python_version_at_runtime()
    # combine_multiple_strings()
    # reverse_string_or_list()
    # enumeration_test()
    # enum_test()
    # a, b, c, d = return_multiple_values_from_functions()
    # print(a, b, c, d)
    # unpack_function_arguments_test()
    # store_expressions_using_dictionary()
    # the_factorial_of_any_number(number=6)
    # most_frequent_value_in_list()
    # reset_recursion_limit()
    # check_the_memory_usage_of_an_object()
    # reduce_memory_overheads_using_slots()
    # lambda_to_limit_print_function()
    # create_a_dictionary_from_two_related_sequences([1, 2, 3, 4, 5], [6, 7, 8, 9])
    # in_line_search()
    # unified_list()
    # switch_case_test()
    # lambda_map_filter_reduce()
    # list_function()
    # list_vs_generator()
    # class_and_magic_function()
    # local_namesspaces_and_object_attributes()
    import_all_demo()
