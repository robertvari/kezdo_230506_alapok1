username = "kisscsaba"
password = "testpas123"

input_username = input("Username?")
input_password = input("Password?")


#                         False
#          False                         True
if username == input_username and password == input_password:
    print(f"Wellcome back {username}!")
else:
    print("Username and/or password was not correct.")