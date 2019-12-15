from common_utils import *

# Example 1
x = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
odds = x[::2]
evens = x[1::2]
print(odds)
print(evens)

# Example 2
x = b'mongoose'
y = x[::-1]
print(y)

# Example 3
x = '寿司'
y = x[::-1]
print(y)

# Example 4
# try:
#     w = '寿司'
#     x = w.encode('utf-8')
#     y = x[::-1]
#     z = y.decode('utf-8')
# except:
#     logging.exception('Expected')
# else:
#     assert False

# Example 5
x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(x[::2])
print(x[::-2])

# Example 6

print(x[2::2])
print(x[-2::-2])
print(x[-2:2:-2])
print(x[2:2:-2])

# Example 7
y = x[::2]
z = y[1:-1]
print(x)
print(y)
print(z)
