phonebook = {
    # root key
    "0620 1234 567": {"name": "Csaba", "address":"Budapest", "email": "csaba@gmail.com"},
    "0620 2345 678": {"name": "Kriszta", "address":"Pécs", "email": "kriszta@gmail.com"},
    "0620 3456 789": {"name": "Tamás", "address":"Miskolc", "email": "tamas@gmail.com"}
}

# add item to a dictionary
phonebook["0620 9874 654"] = {"name": "Géza", "address":"Eger", "email": "geza@gmail.com"}

print(phonebook["0620 9874 654"])

# update item in dictionary
phonebook["0620 1234 567"]["address"] = "Pécs"
phonebook["0620 1234 567"]["age"] = 32

# remove item from dictionary
del phonebook["0620 1234 567"]

print()