# Introduction the Python reduce() function
"""
from functools import reduce

def sum(a, b):
    print(f"a={a}, b={b}, {a} + {b} ={a+b}")
    return a + b


scores = [75, 65, 80, 95, 50]
total = reduce(sum, scores)
print(total)


# Using lambda
scores = [75, 65, 80, 95, 50]
total = reduce(lambda a, b: a + b, scores)

print(total)




# Summary

# The reduce() function applies the fn function of two arguments cumulatively to the items of the list, from left to right, to reduce the list into a single value.

# Unlike the map() and filter() functions, the reduce() isn’t a built-in function in Python. In fact, the reduce() function belongs to the functools module.

# To use the reduce() function, you need to import it from the functools
"""



# List Comprehension

numbers = [1, 2, 3, 4, 5]
squares = [number**2 for number in numbers]

print(squares)

# A list comprehension consists of the following parts:

# An input list (numbers)
# A variable that represents the elements of the list (number)
# An output expression (number**2) that returns the elements of the output list from the elements of the input list.


# Python list comprehension with if condition

mountains = [
    ['Makalu', 8485],
    ['Lhotse', 8516],
    ['Kanchendzonga', 8586],
    ['K2', 8611],
    ['Everest', 8848]
]

highest_mountains = [m for m in mountains if m[1] >= 8600]

print(highest_mountains)