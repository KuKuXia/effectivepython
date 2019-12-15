from common_utils import *

# Example 1
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print('Middle two: ', a[3:5])
print('All but ends: ', a[1:7])

# Example 2
assert a[:5] == a[0:5]

# Example 3
assert a[5:] == a[5: len(a)]

# Example 4
print(a[:])
print(a[:5])
print(a[:-1])
print(a[4:])
print(a[-3:])
print(a[2:5])
print(a[2:-1])
print(a[-3:-1])

# #xample 6
frist_twenty_items = a[:20]
last_twenty_items = a[-20:]

# Example 7
try:
    a[20]
except:
    logging.exception('Expected')
else:
    assert False

# Example 8
b = a[3:]
print('Before:   ', b)
b[1] = 99
print('After:    ', b)
print('No change:', a)

# Example 9
print('Before ', a)
a[2:7] = [99, 22, 14]
print('After  ', a)

# Example 10

print('Before ', a)
a[2:3] = [47, 11]
print('After ', a)

# Example 11
b = a[:]
assert b == a and b is not a

print(id(a))
print(id(b))

# Example 12
b = a
print('Before a', a)
print('Before b', b)
a[:] = [101, 102, 103]
assert a is b  # Still the same list object
print('After a ', a)  # Now has different contents
print('After b ', b)  # Same list, so same contents as a
