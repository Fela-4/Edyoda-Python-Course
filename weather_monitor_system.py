# This program is to alert the user of the condition of weather temperature



# using try/except to make sure input datatype is correct
while True:
    try:
        temp = float(input("Enter current Temperature(in Celsius): "))
        break
    except ValueError:
        print("INVALID INPUT! Enter a number")

# The sequence matters since if i put the 3rd condition first, there will be multiple warning outputs
if temp < 0:
    print("WARNING!!! EXTREME COLD WEATHER CONDITION! TAKE PRECAUTION!")

elif temp > 40:
    print("WARNING!!! EXTREME HOT WEATHER CONDITION! TAKE PRECAUTION!")

elif temp < 15:
    print("Cold warning! Temperature is low.")

elif temp > 25:
    print("Heat Warning! Temperature is high.") 
        
elif 15 < temp < 25:
    print("Conditions are comfortable.")

elif temp == 15 or temp == 25:              # could also be just else:
    print("Temperature is at threshold.")



