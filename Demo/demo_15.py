import logging

from common_utils import *

baby_names = {
    'cat': 'kitten',
    'dog': 'puppy'
}

print(baby_names)

# Example 4
print(list(baby_names.keys()))
print(list(baby_names.values()))
print(list(baby_names.items()))
print(baby_names.popitem())


# Example 6
def my_func(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} = {value}')


my_func(goose='gosling', kangaroo='joey')


# Example 8
class MyClass:
    def __init__(self):
        self.alligator = 'hatchling'
        self.elephant = 'calf'


a = MyClass()
for key, value in a.__dict__.items():
    print(f'{key} = {value}')

# Example 9
votes = {
    'otter': 1281,
    'polar bear': 587,
    'fox': 863
}


# Example 10

def populate_ranks(votes, ranks):
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name] = i


# Example 11
def get_winner(ranks):
    return next(iter(ranks))


# Example 12
ranks = {}
populate_ranks(votes, ranks)
print(ranks)
winner = get_winner(ranks)
print(winner)

# Example 13
from collections.abc import MutableMapping


class SortedDict(MutableMapping):
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.data[key] = value

    def __delitem__(self, key):
        del self.data[key]

    def __iter__(self):
        keys = list(self.data.keys())
        keys.sort()
        for key in keys:
            yield key

    def __len__(self):
        return len(self.data)


my_dict = SortedDict()
my_dict['otter'] = 1
my_dict['cheeta'] = 2
my_dict['anteater'] = 3
my_dict['deer'] = 4

assert my_dict['otter'] == 1
assert 'cheeta' in my_dict

del my_dict['cheeta']
assert 'cheeta' not in my_dict

expected = [('anteater', 3), ('deer', 4), ('otter', 1)]
assert list(my_dict.items()) == expected

assert not isinstance(my_dict, dict)

# Example 14
sorted_ranks = SortedDict()
populate_ranks(votes, sorted_ranks)
print(sorted_ranks.data)
winner = get_winner(sorted_ranks)
print(winner)


# Example 15
def get_winner(ranks):
    for name, rank in ranks.items():
        if rank == 1:
            return name


winner = get_winner(sorted_ranks)
print(winner)

# Example 16
try:
    def get_winner(ranks):
        if not isinstance(ranks, dict):
            raise TypeError('must provide a dict instance')
        return next(iter(ranks))


    assert get_winner(ranks) == 'otter'
    get_winner(sorted_ranks)
except:
    logging.exception('Expected')
else:
    assert False
