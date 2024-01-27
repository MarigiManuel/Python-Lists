
# Using the Python List sort() method to sort a list of numbers

numbers = [23, 32, 1, 6, 87, 6, 45, 34]
numbers.sort()                  # Prints from lowest to highest
print(numbers)

numbers.sort(reverse= True)      # Prints from highest to lowest.
print(numbers) 


# Using the Python List sort() method to sort a list of strings

guests = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer']
guests.sort()                 # Sorts the strings alphabetically.

print(guests)

guests = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer']
guests.sort(reverse=True)     # Sorts the list in the reverse alphabetical order.

print(guests)

# Using the Python List sort() method to sort a list of tuples

companies = [('Google', 2019, 134.81),
             ('Apple', 2019, 260.2),
             ('Facebook', 2019, 70.7)]


# define a sort key
def sort_key(company):
    return company[2]



# sort the companies by revenue
companies.sort(key=sort_key, reverse=True)

# show the sorted companies
print(companies)

# Example two

students_scores = [('Anne', 'English', 88),
                   ('Tim', 'Hist', 81),
                   ('Manuel', 'Maths', 94),
                   ('Iresa', 'Chem', 75),]
def student_score(score):
    return score[2]

students_scores.sort(key=student_score, reverse=True)

print(students_scores)

# Using lambda expression
# lambda arguments: expression

students_scores = [('Anne', 'English', 88),
                   ('Tim', 'Hist', 81),
                   ('Manuel', 'Maths', 94),
                   ('Iresa', 'Chem', 75),]

students_scores.sort(key=lambda score: score[2], reverse=True)

print(students_scores)

# Understanding Lambda functions
def score(x):
    scores = x * 3
    return scores
    
x = score(4)
print(x)

score = lambda x: x * 5
x = score(3)
print(x)




# Summary

# Use the Python List sort() method to sort a list in place.
# The sort() method sorts the string elements in alphabetical order.
# It also sorts the numeric elements from smallest to largest.
# Use the sort(reverse=True) to reverse the default sort order.