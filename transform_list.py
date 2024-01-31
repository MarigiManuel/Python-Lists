# Python map() function

def values(value):
    return value * 2

numbers = [30, 20, 50]
iterable = map(values, numbers)

print(list(iterable))

#Using Lambda function
values = [2, 1, 5]
y = map(lambda value: value * 2, values)

print(list(y))

# Using the Python map() function for a list of strings
# The following example uses the map() function to return a new list where each element is transformed into the proper case:

cities = ['nairobi', 'kisumu', 'nakuru', 'mombasa']
new_cities = map(lambda city: city.capitalize(), cities)

print(list(new_cities))

# Using the Python map() function to a list of tuples

fruits = [['Orange', 20],
          ['Apple', 40],
          ['Mango', 30]]
tax = 0.02

fav_fruits = map(lambda fruit: [fruit[0], fruit[1], fruit[1] * tax], fruits)

print(list(fav_fruits))

# The code calculates 2% for each fruit.
# It adds the tax amount as the new item in the list.



# Python filter() function

scores = [70, 60, 80, 90, 50]

filtered = []

for score in scores:
    if score >= 70:
        filtered.append(score)

print(filtered)



# Using the Python filter() function to filter a list of tuples.
# Each element in a list is a tuple that contains the country’s name and population.

# To get all the countries whose populations are greater than 300 million, you can use the filter() function as follows:

countries = [
    ['China', 1394015977],
    ['United States', 329877505],
    ['India', 1326093247],
    ['Indonesia', 267026366],
    ['Bangladesh', 162650853],
    ['Pakistan', 233500636],
    ['Nigeria', 214028302],
    ['Brazil', 21171597],
    ['Russia', 141722205],
    ['Mexico', 128649565]
]

populated = filter(lambda c: c[1] > 300000000, countries)

print(list(populated))
