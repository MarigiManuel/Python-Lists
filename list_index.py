# To find the index of an element in a list, you use the index() function.
names = ['Manuel', 'Marigi', 'Iresa', 'Nate', 'Mahiri']
x = names.index('Iresa')

print(x)

# If you attempt to find an element that doesn’t exist in the list using the index() function, you’ll get an error.
names = ['Manuel', 'Marigi', 'Iresa', 'Nate', 'Mahiri']
name = 'Nate'

if name in names:
    result = names.index(name)
    print(f'{name} is index: {result}')
else:
    print(f'{name} is not in the list!')

    
# Iterables

str = 'Iterables'
for ch in str:
    print(ch)

ranks = ['high', 'medium', 'low']

for rank in ranks:
    print(rank)

for index in range(3):
    print(index)