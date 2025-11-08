# Program to demonstrate various string operations
# to format and display customer data.

import string


# Input by user for the customer's details
print("Enter the following fields: ")
first_name = str(input("First Name: ")).lower() # .lower() converts the string to lowercases
last_name = str(input("Last Name: ")).lower()
email_id = str(input("Email address: ")).lower()


# making sure they are not missing '@' by mistake for .split()
while '@' not in email_id:
    email_id = input("Enter correct email address: ")


# using .title() to change the first letter of the word to uppercase
first_name = first_name.title()
last_name = last_name.title()


# Creating a formatted customer ID by combining the 3 datas
formatted_id = (
    last_name[:3].upper() +         # as example provided was "DOE4ema", i guess we convert the lastname to uppercases
    str(len(first_name)) +          # since len(var) becomes an int datatype, needs to be converted to str for concat
    email_id.split("@", 1)[1][:3]   # using slicing method to get the first 3 and last letters of specified variables
    )
print(f"Formatted id: {formatted_id}")

