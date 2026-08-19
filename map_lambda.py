
#1. Find the square
numbers = [1, 2, 3, 4, 5]
print(list(map(lambda x: x*x, numbers)))

#2. Capitalize it
names=['ali', 'vali', 'odil']
print(list(map(lambda word: word.capitalize(), names)))

#3. +15%
costs = [100, 250, 500, 1000]
print(list(map(lambda x: x*1.15, costs)))
