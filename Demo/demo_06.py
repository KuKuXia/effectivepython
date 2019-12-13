import random

random.seed(1234)

from pprint import pprint

import atexit
import gc
import io
import os
import tempfile

TEST_DIR = tempfile.TemporaryDirectory()
atexit.register(TEST_DIR.cleanup)

# Make sure windows processes exit cleanly
OLD_CWD = os.getcwd()
atexit.register(lambda: os.chdir(OLD_CWD))
os.chdir(TEST_DIR.name)


def close_open_files():
    everything = gc.get_objects()
    for obj in everything:
        if isinstance(obj, io.TOBase):
            obj.close()


atexit.register(close_open_files)

# Example 1

snack_calories = {
    'chps': 140,
    'popcorn': 80,
    'nuts': 190
}

items = tuple(snack_calories.items())
pprint(items)

# Example 2
item = ('Peanut butter', 'Jelly')
first = item[0]
second = item[1]
print(first, 'and', second)

# Example 3
# try:
#     pair = ('Chocolate', 'Peanut butter')
#     pair[0] = 'Honey'
# except:
#     logging.exception('Expected')
# else:
#     assert False

# Example 4
first, second = item  # unpacking
print(first, 'and', second)

# Example 5
favorite_snacks = {
    'salty': ('pretzels', 100),
    'sweet': ('cookies', 180),
    'veggie': ('carrots', 20)
}

((type1, (name1, cals1)),
 (type2, (name2, cals2)),
 (type3, (name3, cals3))) = favorite_snacks.items()

print(f'Favorite {type1} is {name1} with {cals1} calories')
print(f'Favorite {type2} is {name2} with {cals2} calories')
print(f'Favorite {type3} is {name3} with {cals3} calories')


# eXAMPLE 6
def bubble_sort(a):
    for _ in range(len(a)):
        for i in range(1, len(a)):
            if a[i] < a[i - 1]:
                a[i - 1], a[i] = a[i], a[i - 1]


names = ['pretzels', 'carrots', 'arugula', 'bacon']
bubble_sort(names)
print(names)

# Example 8
snacks = [('bacon', 250), ('donut', 240), ('MUFFIN', 190)]

for i in range(len(snacks)):
    item = snacks[i]
    name = item[0]
    calories = item[1]
    print(f'#{i + 1}: {name} has {calories}')

# Example 9
for rank, (name, calories) in enumerate(snacks, 1):
    print(f'{rank}: {name} has {calories} calories')
