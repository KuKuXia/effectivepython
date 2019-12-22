"""
This script is copied from:
Link: https://www.techbeamers.com/essential-python-tips-tricks-programmers/
"""
import socket
import sys
import threading


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
    multiStr = 'select * from multi_row ' \
               'Where row_id < 5'
    multiStr_2 = ("select * from multi_row "
                  "where row_id < 5 "
                  "order by age ")
    print(multiStr)
    print(multiStr_2)


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
# In the python console, whenever we test an expression or call a function, the result dispatches to a temporary name, _(an underscore)

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
    testDict = {'x': 1, 'y': 2, 'z': 3}
    testList = [10, 20, 30]
    unpack_function_arguments_using_the_splat_operator(*testDict)
    unpack_function_arguments_using_the_splat_operator(**testDict)
    unpack_function_arguments_using_the_splat_operator(*testList)


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
    iprint = lambda *args: print(' '.join(map(str, args)))
    iprint('python', 'tips', 1000, 10001)


# Create a dictionary from two related sequences
def create_a_dictionary_from_two_related_sequences(a=[1, 2, 3], b=[4, 5, 6]):
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


if __name__ == '__main__':
    inplace_swapping_of_two_numbers(5, 8)
    chaining_of_comparison_operations()
    print(ternary_operator_for_conditional_assignment(1, 0, 1))
    print(ternary_operator_for_conditional_assignment(100, 22, 99))
    multi_line_strings()
    # Debugging the script
    # pdb.set_trace()
    unpacking_list()
    print_file_path()
    dictionary_and_set_comprehensions()
    inspect_an_object()
    detect_python_version_at_runtime()
    combine_multiple_strings()
    reverse_string_or_list()
    enumeration_test()
    enum_test()
    a, b, c, d = return_multiple_values_from_functions()
    print(a, b, c, d)
    unpack_function_arguments_test()
    store_expressions_using_dictionary()
    the_factorial_of_any_number(number=6)
    most_frequent_value_in_list()
    reset_recursion_limit()
    check_the_memory_usage_of_an_object()
    reduce_memory_overheads_using_slots()
    lambda_to_limit_print_function()
    create_a_dictionary_from_two_related_sequences([1, 2, 3, 4, 5], [6, 7, 8, 9])
    in_line_search()
    unified_list()
    switch_case_test()
