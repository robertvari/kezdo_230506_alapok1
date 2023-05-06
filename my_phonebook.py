phonebook = {}

phone = input("What is your phone number?")
name = input("What is your name?")
address = input("Where do you live?")
email = input("What is your email address?")

phonebook[phone] = {
    "name": name,
    "address": address,
    "email": email
}