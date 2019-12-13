from common_utils import *

# Example 1
names = ['Cecilia', 'Lise', 'Marie']
counts = [len(n) for n in names]
print(counts)

# Example 2
longest_name = None
max_count = 0

for i in range(len(names)):
    count = counts[i]
    if count > max_count:
        longest_name = names[i]
        max_count = count

print(longest_name)

# Example 3
longest_name = None
max_count = 0
for i, name in enumerate(names):
    count = counts[i]
    if count > max_count:
        longest_name = name
        max_count = count
assert longest_name == 'Cecilia'

# Example 4
longest_name = None
max_count = 0
for name, count in zip(names, counts):
    if count > max_count:
        longest_name = name
        max_count = count
assert longest_name == 'Cecilia'

# Example 5
names.append('Rosalind')

for name, count in zip(names, counts):
    print(name)

# Example 6
import itertools

for name, count in itertools.zip_longest(names, counts):
    print(f'{name}: {count}')
