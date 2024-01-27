# print('Keep going, buddy!')

# Using the list slice to get a sublist from the colors list.

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
sub_colors = colors[1 : 4]          

print(sub_colors)

# Using Python List slice to get the n-first elements from a list.

names = ['Marigi', 'Manuel', 'Iresa', 'Nate', 'Milly', 'Asnah']
sub_names = names[ : 4]              # Prints the first 4 elements.

print(sub_names)

# Using Python List slice to get the n-last elements from a list.
names = ['Marigi', 'Manuel', 'Iresa', 'Nate', 'Milly', 'Asnah']
last_names = names[-3 : ]             # Prints the last 3 elements.

print(last_names)

# Using Python List slice to get every nth element from a list
countries = ['Kenya', 'Tanzania', 'Uganda', 'Rwanda', 'Burundi', 'DRC', 'Somalia', 'Zambia']
fav_coutries = countries[ :: 2]       # Uses the step(::) to return a sublist that includes every 2nd element of the countries list.

print(f'Your favorite countries are: {fav_coutries}')

# Using Python List slice to reverse a list.
names = ['Marigi', 'Manuel', 'Iresa', 'Nate', 'Milly', 'Asnah']
reversed_names = names[ :: -1]    # Note that the step agurment must be there!

print(reversed_names)

# Using Python List slice to substitute part of a list.
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
colors[0:2] = ['black', 'white']

print(colors)

###
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
colors[3:6] = ['black', 'white']

print(colors)                 # Notice that Indigo is overwritten.

# Using Python List slice to partially replace and resize a list

subjects = ['Maths', 'English', 'Physics', 'Chem', 'Geography', 'History']

print(f'This list has {len(subjects)} elements')

subjects[0 : 2] = ['Computer', 'Kiswahili', 'French']    # Changed the first two elements and added 1 more element(French)

print(subjects)
print(f'This list has {len(subjects)} elements')

# Using Python list slice to delete elements

subjects = ['Maths', 'English', 'Physics', 'Chem', 'Geography', 'History']
del subjects[2:5]           # delete the 3rd, 4th, and 5th elements.
#del subjects[-1: ]         # delete the last element.

print(subjects)





# SUMMARY

# Lists support the slice notation that allows you to get a sublist from a list:

# sub_list = list[begin: end: step]             # Syntax used.

# In this syntax, the begin, end, and step arguments must be valid indexes. And they’re all optional.

# The begin index defaults to zero. The end index defaults to the length of the list. And the step index defaults to 1.

# The slice will start from the begin up to the end in the step of step.

# The begin, end, and step can be positive or negative. 
# Positive values slice the list from the first element to the last element while negative values slice the list from the last element to the first element.

# In addition to extracting a sublist, you can use the list slice to change the list such as updating, resizing, and deleting a part of the list.