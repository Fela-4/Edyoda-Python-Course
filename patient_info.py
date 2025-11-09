# This program is to re-organize user input in a proper format


# Here, this function is made for age, weight and height which are all numbers
# hence the reason name(string) is excluded
# the function helps in avoiding repition in code and makes it cleaner and more efficient

def get_valid_input(user_input, data_type):
    while True:                                             # while loop and try/except used to avoid incorrect input
        try:
            value = data_type(input(user_input))

            if value <= 0:
                print("Enter a number greater than zero!")
            else:
                return value                                # value is assigned to the variable
                
        except ValueError:
            print("INVALID INPUT! Enter a number!")


while True:
    name = str(input("Enter your Full Name: ")).strip().upper()     # .strip() is used to remove white spaces
    
    if len(name.split()) < 2:                                       # Makes sure it consists of more than 1 string
        print("Please enter your full name (First and Last)")

    elif len(name.split()) > 2:                                     # in case they enter their middle name or more
        print("Please enter only First and Last Name")
    else:
        break


age = get_valid_input("Enter your Age: ", int)
weight = get_valid_input("Enter your Weight(kgs): ", float)
height = get_valid_input("Enter you Height(cms): ", float)


while True:
    insurance_input = str(input("Do you have insurance? (yes/no): ")).strip().lower()
    if insurance_input == "yes":
        insurance: bool = True 
        break

    elif insurance_input == "no":
        insurance: bool = False
        break
    else:
        print("Invalid INPUT!")


first_name = name.split(" ",1)[0]
last_name = name.split(" ",1)[1]
weight_lbs = round(weight * 2.20462, 1)     # round() to round up the decimal

if insurance:
    insurance_status = "Insured"
else:
    insurance_status = "Uninsured"


print("\nPatient Information: ")
print(f"""
First Name: {first_name}
Last Name: {last_name}
Age: {age} Years
Weight: {weight} kgs / {weight_lbs} lbs
Height: {height} cm
Insurance: {insurance_status}
""")
