# Unpack a list by assigning its elements to variables in a single line of code.
my_list = [1, 2, 3]
a, b, c = my_list

print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

friends = ['Willy', 'Kevo', 'Nicko', 'Symo']
a, b, c, d = friends

print(d)    # Symo
print(b)    # Kevo

# Extended Unpacking:
# If you have more variables than elements in the list, 
# you can use an asterisk * to collect the remaining elements into a separate list.

my_list = [1, 2, 3, 4, 5]
a, b, *rest = my_list

print(a)    # Output: 1
print(b)    # Output: 2
print(rest) # Output: [3, 4, 5]

friends = ['Willy', 'Kevo', 'Nicko', 'Symo']
a, *others = friends

print(a)
print(others)

# Ignoring elements
# You can use an underscore _ to ignore the unwanted elements.
numbers = [21, 23, 2, 1, 5, 7, 8, 98, 67]
a1, _, a3, _, a5, *rest = numbers

print(a1)      # Prints 21
print(a3)      # Prints 2
print(rest)    # Prints [7, 8, 98, 67]

# Unpack nested lists to access their individual elements.

nested_list = [1, [2, 3], 4]
a, (b, c), d = nested_list

print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3
print(d)  # Output: 4




# Using a for loop to iterate over the list.

values = [5, 3, 1, 7, 9, 3]
for value in values:
    print(value)

###
cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']

for city in cities:
    print(city)

# Using Python for loop to iterate over a list with index
# The enumerate() function returns a tuple that contains the current index and element of the list.

numbers = [4, 3, 1, 8, 76]
for x in enumerate(numbers):
    print(x)

####
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
for month in enumerate(months):
    print(month)

# To access the index, you can unpack the tuple within the for loop statement like this.
cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']

for index, city in enumerate(cities):
    print(f"{index}: {city}")

# The enumerate() function allows you to specify the starting index which defaults to zero.
# The following example uses the enumerate() function with the index that starts from one:

cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']

for index, city in enumerate(cities,1):
    print(f"{index}: {city}")






# Summary
    
# Use a for loop to iterate over a list.
# Use a for loop with the enumerate() function to access indexes.