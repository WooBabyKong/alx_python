#!/usr/bin/python3
numbers = ['{:02}'.format(i) for i in range(100)]
print(', '.join(numbers))