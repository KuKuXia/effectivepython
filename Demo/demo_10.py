from common_utils import *

# Example 1
fresh_fruit = {
    'apple': 10,
    'banana': 8,
    'lemon': 5
}

for name, count in fresh_fruit.items():
    print(f'{name} is {count}.')


# Example 2
def make_lemonade(count):
    print(f'Making {count} lemons into lemonade.')


def out_of_stock():
    print('Out of stock!')


count = fresh_fruit.get('lemon', 0)
if count:
    make_lemonade(count)
else:
    out_of_stock()


# Example 3
# Python 3.8 才支持 assignment expressions
# if count := fresh_fruit.get('lemon', 0):
#     make_lemonade(count)
# else:
#     out_of_stock()

# Example 4
def make_cider(count):
    print(f'Making cider with {count} apples')


count = fresh_fruit.get('apple', 0)
if count >= 4:
    make_cider(count)
else:
    out_of_stock()


# Example 5
# if (count:= fresh_fruit.get('apple', 0)) >= 4:
#     make_cider(count)
# else:
#     out_of_stock()

# Example 6
def slice_bananas(count):
    print(f'Slicing {count} bananas')
    return count * 4


class outofBananas(Exception):
    pass


def make_smoothies(count):
    print(f'Making a smoothies with {count} banana slices')


pieces = 0
count = fresh_fruit.get('banana', 0)
if count >= 2:
    pieces = slice_bananas(count)
try:
    smoothies = make_smoothies(pieces)
except  outofBananas:
    out_of_stock()

# Example 7
count = fresh_fruit.get('banana', 0)
if count >= 2:
    pieces = slice_bananas(count)
else:
    pieces = 0

try:
    smoothies = make_smoothies(pieces)
except outofBananas:
    out_of_stock()

# Example 8
# pieces = 0
# if (count := fresh_fruit.get('banana', 0)) >= 2:
#     pieces = slice_bananas(count)
#
# try:
#     smoothies = make_smoothies(pieces)
# except outofBananas:
#     out_of_stock()

# Example 9
# if (count := fresh_fruit.get('banana', 0)) >= 2:
#     pieces = slice_bananas(count)
# else:
#     pieces = 0
#
# try:
#     smoothies = make_smoothies(pieces)
# except outofBananas:
#     out_of_stock()

# Example 10
count = fresh_fruit.get('banana', 0)
if count >= 2:
    pieces = slice_bananas(count)
    to_enjoy = make_smoothies(pieces)
else:
    count = fresh_fruit.get('apple', 0)
    if count >= 4:
        to_enjoy = make_cider(count)
    else:
        count = fresh_fruit.get('lemon', 0)
        if count:
            to_enjoy = make_lemonade(count)
        else:
            to_enjoy = 'Nothing'

# Example 11
# if (count := fresh_fruit.get('banana', 0)) >= 2:
#     pieces = slice_bananas(count)
#     to_enjoy = make_smoothies(pieces)
# elif (count := fresh_fruit.get('apple', 0)) >= 4:
#     to_enjoy = make_cider(count)
# elif count := fresh_fruit.get('lemon', 0):
#     to_enjoy = make_lemonade(count)
# else:
#     to_enjoy = 'Nothing'

# Example 12
FRUIT_TO_PICK = [
    {'apple': 1, 'banana': 3},
    {'lemon': 2, 'lime': 5},
    {'orange': 3, 'melon': 2},
]


def pick_fruit():
    if FRUIT_TO_PICK:
        return FRUIT_TO_PICK.pop(0)
    else:
        return []


def make_juice(fruit, count):
    return [(fruit, count)]


bottles = []
fresh_fruit = pick_fruit()
while fresh_fruit:
    for fruit, count in fresh_fruit.items():
        batch = make_juice(fruit, count)
        bottles.extend(batch)
    fresh_fruit = pick_fruit()

print(bottles)

# Example 13
FRUIT_TO_PICK = [
    {'apple': 1, 'banana': 3},
    {'lemon': 2, 'lime': 5},
    {'orange': 3, 'melon': 2},
]

bottles = []
while True:  # Loop
    fresh_fruit = pick_fruit()
    if not fresh_fruit:  # And a half
        break
    for fruit, count in fresh_fruit.items():
        batch = make_juice(fruit, count)
        bottles.extend(batch)

print(bottles)

#
# # Example 14
# FRUIT_TO_PICK = [
#     {'apple': 1, 'banana': 3},
#     {'lemon': 2, 'lime': 5},
#     {'orange': 3, 'melon': 2},
# ]
#
# bottles = []
# while fresh_fruit := pick_fruit():
#     for fruit, count in fresh_fruit.items():
#         batch = make_juice(fruit, count)
#         bottles.extend(batch)
#
# print(bottles)
