my_driends = []

# add item to a list
my_driends.append("Csaba")
my_driends.append("Kriszta")
my_driends.append("Tamás")

my_driends.insert(0, "Csilla")

fruits = ["apple", "lemon", "banana"]
my_driends.extend(fruits)

# remove items from list
print(my_driends)
my_driends.remove('Tamás')

del my_driends[0]
print(my_driends)

# update item
my_driends[2] = "Béla"
print(my_driends)