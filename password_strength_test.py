# This program is to check the strength of the password being input by the user

special_char = {'!', '@', '#', '$', '%', '^', '&', '*'} # Global variable


def validate_password():
    # We are starting the function with a while loop so the user can re-enter until correct conditions are met.
    while True:
        flag = 0    # variable used to track number of conditions met. 
        password = str(input("Enter a Password: "))
    
        # 1st condition: Checking length of password to be >= 8 char.
        if len(password) >= 8:
            flag += 1
        else:
            print("Password must be at least 8 characters")
            continue # rollback to start of while loop when conditions are not met. Helps reset flag value to zero.

        # 2nd condition: Checking if password has atleast 1 uppercase char.
        for c in password:
            if c.isupper():
                flag += 1
                break
        else: 
            print("Password must contain at least ONE uppercase character")
            continue

        # 3rd condition: Atleast 1 lowercase char.
        for c in password:
            if c.islower():
                flag += 1
                break
        else:
            print("Password must contain at least ONE lowercase character")
            continue

        # 4th condition: Atleast 1 number in password.
        for num in password:
            if num.isdigit():
                flag += 1
                break
        else:
            print("Password must contain at least ONE number")
            continue

        # 5th condition: Atleast 1 special character in password.
        if special_char & set(password):
            flag += 1
        else:
            print("Password must contain at least ONE special character")
            continue
            
        # When all conditions are met, flag = 5 and returns the password.
        if flag == 5:
            print("\n----------Password is valid!----------")
            return password
        

validate_password()