import logging

from common_utils import *

# Example 1
numbers = [93, 86, 11, 68, 70]
numbers.sort(reverse=True)
print(numbers)


# Example 2
class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f'Tool({self.name!r}, {self.weight})'


tools = [
    Tool('level', 3.5),
    Tool('hammer', 1.25),
    Tool('screwdriver', 0.5),
    Tool('Chisel', 0.25)
]

# Example 3
try:
    tools.sort()
except:
    logging.exception('Excepted')
else:
    assert False

# Example 4
print('Unsorted', repr(tools))
tools.sort(key=lambda x: x.name)
print('\nSorted: ', tools)

# Example 5
tools.sort(key=lambda x: x.weight)
print('By weight', tools)

# Example 6
places = ['home', 'work', 'New York', 'Paris']
places.sort()
print('Case sensitive: ', places)
places.sort(key=lambda x: x.lower())
print("Case insensitive: ", places)

# Example 7
power_tools = [
    Tool('drill', 4),
    Tool('circular saw', 5),
    Tool('jackhammer', 40),
    Tool('sander', 4),
]

# Example 8
saw = (5, 'circular saw')
jackhammer = (40, 'jackhammer')
assert not (jackhammer < saw)  # Matches expectations

# Example 9
drill = (4, 'drill')
sander = (4, 'sander')
assert drill[0] == sander[0]  # Same weight
assert drill[1] < sander[1]  # Alphabetically less
assert drill < sander  # Thus, drill comes first

# Example 10
power_tools.sort(key=lambda x: (x.weight, x.name))
print(power_tools)

# Example 11
power_tools.sort(key=lambda x: (x.weight, x.name),
                 reverse=True)  # Makes all criteria descending
print(power_tools)

# Example 12
power_tools.sort(key=lambda x: (-x.weight, x.name))
print(power_tools)

# Example 13
try:
    power_tools.sort(key=lambda x: (x.weight, -x.name),
                     reverse=True)
except:
    logging.exception('Expected')
else:
    assert False

# Example 14
power_tools.sort(key=lambda x: x.name)  # Name ascending

power_tools.sort(key=lambda x: x.weight,  # Weight descending
                 reverse=True)

print(power_tools)

# Example 15
power_tools.sort(key=lambda x: x.name)
print(power_tools)

# Example 16
power_tools.sort(key=lambda x: x.weight,
                 reverse=True)
print(power_tools)
