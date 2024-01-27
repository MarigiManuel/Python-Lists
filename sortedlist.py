# print('I am proud of my progress!')

# Using Python sorted() function to sort a list of numbers.

numbers = [23, 5, 8, 0, 43, 21, 1]
# numbers.sort(reverse=True)
sorted_numbers = sorted(numbers, reverse=True)

print(numbers)                         # Prints the original list.
print(sorted_numbers)                  # Prints the sorted list.

# Using Python sorted() function to sort a list of strings

guests = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer']
sorted_guests = sorted(guests)                          # Prints in alphabetical order.

print(guests)
print(sorted_guests)

# # # # # #
my_achievements = ['PHD', 'Masters', 'Degree', 'Diploma', 'Certificate']
achievements = sorted(my_achievements, reverse=True)     # Prints in reverse alphabetical order.

print(achievements)



# Summary
# Use the sorted() function to return a new sorted list from a list.
# Use the sorted() function with the reverse argument sets to True to sort a list in the reverse sort order.