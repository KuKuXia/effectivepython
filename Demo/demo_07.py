from random import randint

from common_utils import *

random_bits = 0

for i in range(32):
    if randint(0, 1):
        random_bits |= 1 << i
print(bin(random_bits))

# Example 2
flavor_list = ['vanilla', 'chocolate', 'pecan', 'strawberry']

for flavor in flavor_list:
    print(f'{flavor} is delicious')

# Example 3
for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print(f'{i + 1}: {flavor}')

# Example 4
it = enumerate(flavor_list)
print(next(it))
print(next(it))

# Example 5
for i, flavor in enumerate(flavor_list):
    print(f'{i + 1}: {flavor}')

# Example 6
for i, flavor in enumerate(flavor_list, 5):
    print(f'{i}: {flavor}')
