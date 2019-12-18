from common_utils import *

# Example 1
counters = {
    'pumpernickel': 2,
    'sourdough': 1,
}

# Example 2
key = 'wheat'

if key in counters:
    count = counters[key]
else:
    count = 0

counters[key] = count + 1

print(counters)

# Example 3
key = 'brioche'

try:
    count = counters[key]
except KeyError:
    count = 0

counters[key] = count + 1

print(counters)

# Example 4
key = 'multigrain'

count = counters.get(key, 0)
counters[key] = count + 1

print(counters)

# Example 5
key = 'baguette'

if key not in counters:
    counters[key] = 0
counters[key] += 1

key = 'ciabatta'

if key in counters:
    counters[key] += 1
else:
    counters[key] = 1

key = 'ciabatta'

try:
    counters[key] += 1
except KeyError:
    counters[key] = 1

print(counters)

# Example 6
votes = {
    'baguette': ['Bob', 'Alice'],
    'ciabatta': ['Coco', 'Deb'],
}

key = 'brioche'
who = 'Elmer'

if key in votes:
    names = votes[key]
else:
    votes[key] = names = []

names.append(who)
print(votes)

#  Example 7
key = 'rye'
who = 'Felix'

try:
    names = votes[key]
except KeyError:
    votes[key] = names = []

names.append(who)

print(votes)

# Example 8
key = 'wheat'
who = 'Gertrude'

names = votes.get(key)
if names is None:
    votes[key] = names = []

names.append(who)

print(votes)

# Example 10
key = 'cornbread'
who = 'Kirk'

names = votes.setdefault(key, [])
names.append(who)

print(votes)

# Example 11
data = {}
key = 'foo'
value = []
data.setdefault(key, value)
print('Before:', data)
value.append('hello')
print('After: ', data)

# Example 12
key = 'dutch crunch'

count = counters.setdefault(key, 0)
counters[key] = count + 1

print(counters)
