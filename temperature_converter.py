# Program to emulate a weather application
# displaying result in either Celsius or Farenheit


# Here i am initializing them as None to exclude them in the loop
temp, temp_type = None, None

while True:
    if temp is None:
        # Making sure incorrect inputs are handled 
        try:
            temp = float(input("Enter temperature: "))
            
        except ValueError:
            print("Enter a valid number\n")
            continue

    
    if temp_type is None:
        # .strip() is used to remove blank/white spaces and upper() for less complicated str comparision
        temp_type = str(input("Enter 'C' for Celcius and 'F' for Farenheit: ")).strip().upper()

        # making sure to get the correct input
        while temp_type not in ('C', 'F'):
            temp_type = str(input("Invalid Input!. Please Enter 'C' or 'F': ")).strip().upper()


    if temp_type == 'C':
        print(f"\nTemperature is {temp} Celcius!")
        temp = (temp * (9/5)) + 32
        print(f"Converted to {temp} Farenheit!\n")
        temp_type = 'F' # for re-conversion
 
    elif temp_type == 'F':
        print(f"\nTemperature is {temp} Farenheit!")
        temp = (temp - 32) * (5/9)
        print(f"Converted to {temp} Celcius!\n")
        temp_type = 'C' # for re-conversion

    
    try:
        choice = int(input("Enter 1 for re-conversion of temperature\nEnter anything else to exit: "))
    except ValueError:
        choice = 0 # defaulting the value to 0 incase they enter any character or symbols
    
    if choice != 1:
        break