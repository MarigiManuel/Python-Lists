# Lists for integers

numbers = [1, 3, 2, 7, 9, 4]
print(numbers)

# List for strings

colors = ['red', 'green', 'blue']
print(colors)

# A list can contain other lists.

coordinates = [[0, 0], [100, 100], [200, 200]]
print(coordinates)

# Accessing elements in a list

numbers = [1, 3, 2, 7, 9, 4]

print(numbers[0])      # Prints the first element
print(numbers[1])      # Prints the second element
print(numbers[5])      # Prints the sixth/last element
print(numbers[-1])     # Prints starting from the last element

#  Modifying elements in a list

numbers = [1, 3, 2, 7, 9, 4]
numbers[0] = 10                   # Changes first element (1) to 10

print(numbers)

# The following shows how to multiply the second element by 10

numbers = [1, 3, 2, 7, 9, 4]
numbers[1] = numbers[1]*10

print(numbers)

# And the following divides the third element by 2.

numbers = [3, 6, 7, 1, 9, 2]
# numbers[2] = numbers[2] / 2      # Same results
numbers[2] /= 2

print(numbers)

# Adding elements to the list. Uses the append() method

numbers = [34, 2, 1, 90, 45]
numbers.append(50)

print(numbers)

# To add number inside a list, use insert() method

numbers = [23, 4, 7, 89, 12]
numbers.insert(2, 44)          # inserts the number 44 at index 2 of the numbers list

print(numbers)


# Removing elements from a list.

numbers = [4, 5, 9, 4, 12, 11]
del numbers[4]                  # Deletes the 5th element (12)
last = numbers.pop()            # Removes the last element
second = numbers.pop(1)         # Removes the second element

print(last)
print(second)
print(numbers)


# To remove an element by value, you use the remove() method. 
# Note that the remove() method removes only the first element it encounters in the list.

numbers = [3, 1, 99, 23, 2, 3]
numbers.remove(3)                    # Removes 3 from the list... only the first 3 it encounters.

print(numbers)


# The following code removes all instances of 3, but do not use the remove() method.

numbers = [3, 1, 99, 3, 2, 3, 2, 3]

# Using list comprehension to create a new list without 3
numbers_without_3 = [num for num in numbers if num != 3]

print(numbers_without_3)  # Output: [1, 99, 23, 2]






# Summary on Lists

# A list is an ordered collection of items.
# Use square bracket notation [] to access a list element by its index. The first element has an index 0.
# Use a negative index to access a list element from the end of a list. The last element has an index -1.
# Use list[index] = new_value to modify an element from a list.
# Use append() to add a new element to the end of a list.
# Use insert() to add a new element at a position in a list.
# Use pop() to remove an element from a list and return that element.
# Use remove() to remove an element from a list.
