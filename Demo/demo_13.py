from common_utils import *

# Example 1
try:
    car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]
    car_ages_descending = sorted(car_ages, reverse=True)
    oldest, second_oldest = car_ages_descending[0], car_ages_descending[1]
except:
    logging.exception('Excepted')
else:
    print(oldest, second_oldest)

# Example 2
oldest = car_ages_descending[0]
second_oldest = car_ages_descending[1]
others = car_ages_descending[2:]
print(oldest, second_oldest, others)

# Example 3
oldest, second_oldest, *others = car_ages_descending
print(oldest, second_oldest, others)

oldest, *others, youngest = car_ages_descending
print(oldest, youngest, others)

*others, second_youngest, youngest = car_ages_descending
print(youngest, second_youngest, others)

# Example 5

# try:
#     # This will not compile
#     source = """*others = car_ages_descending"""
#     eval(source)
# except :
#     logging.exception('Expected')
# else:
#     assert False

# Example 6
# try:
#     # This will not compile
#     source = """first, *middle, *second_middle, last = [1, 2, 3, 4]"""
#     eval(source)
# except:
#     logging.exception('Expected')
# else:
#     assert False

# Example 7
car_inventory = {
    'Downtown': ('Silver Shadow', 'Pinto', 'DMC'),
    'Airport': ('Skyline', 'Viper', 'Gremlin', 'Nova'),
}

((loc1, (best1, *rest1)),
 (loc2, (best2, *rest2))) = car_inventory.items()

print(f'Best at {loc1} is {best1}, {len(rest1)} others')
print(f'Best at {loc2} is {best2}, {len(rest2)} others')

# Example 8
short_list = [1, 2]
first, second, *rest = short_list
print(first, second, rest)

# Example 9
it = iter(range(1, 3))
firse, second = it
print(f'{first} and {second}')


# Example 10
def generate_csv():
    yield ('Date', 'Make', 'Model', 'Year', 'Price')
    for i in range(100):
        yield ('2019-03-25', 'Honda', 'Fit', '2010', '$3400')
        yield ('2019-03-26', 'Ford', 'F150', '2008', '$2400')


# Example 11
all_csv_rows = list(generate_csv())
header = all_csv_rows[0]
rows = all_csv_rows[1:]
print('CSV Header:', header)
print('Row count: ', len(rows))

it = generate_csv()
header, *rows = it
print('CSV Header: ', header)
print('Row count: ', len(rows))
