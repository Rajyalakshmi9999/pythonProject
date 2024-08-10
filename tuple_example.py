num_tuple = 2, 4, 5, 7, 8, 10, 66, 55,  87,87
print(num_tuple[:3])
print(num_tuple[4:])
print(num_tuple[-3:])
print(num_tuple[2:5])
print(num_tuple[3:5])
print(num_tuple[1:7])
print(num_tuple[1:9])
print(num_tuple[2:3])
print(num_tuple[1:8])
# appending two tuples
tuple_1 = (1, 2)
tuple_2 = (3, 4)
print(tuple_1 + tuple_2)
# multiply
my_tuple = (1, 7, 9, 8)
print(my_tuple * 2)
# zipping
first_names = ('Simon', 'Sarah', 'Mehdi', 'Fatime')
last_names = ('Sinek', 'Smith', 'Lotfinejad', 'Lopes')
ages = (49, 55, 39, 33)
zipped = zip(first_names, last_names,ages)
print(zipped)
customers = tuple(zipped)
print(customers)
# Differnce
import sys
a_list = ['abc', 'xyz', 123, 231, 13.31, 0.1312]
a_tuple = ('abc', 'xyz', 123, 231, 13.31, 0.1312)
print('The list size:', sys.getsizeof(a_list), 'bytes')
print('The tuple size:', sys.getsizeof(a_tuple), 'bytes')
# immutability makes significant optimization when working with a large amount of data.
# Swappimg
x = 19
y = 91
print('Before swapping:')
print(f'x = {x}, y = {y}')
(x, y) = (y, x)
print('After swapping:')
print(f'x = {x}, y = {y}')




