# Date: 12/25/2024 #
# 1. This script calls a basic function that converts Fahrenheit to Celsius.   #
# 2. User Input for Fahrenhiet (degrees)--> then converted to an integer.      #
# 2. It prints the result, then restarts the script (unless user types 'exit') #

def get_integer_input(): ## Looped function for checking user input for accepted integers.
    while True:
        user_input = input("Enter the temperature in Fahrenheit (degrees) | 'q' to exit--: ")
        if user_input.lower() == "q":
            return None
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter an integer.")

def convert_to_celsius(f): ## Function for Temperature Conversion: ##
    return (f - 32) / 1.8

while True:
    f = get_integer_input()
    if f is None:
        print("Exiting")
        break
    c = convert_to_celsius(f)
    print((f), ("degrees Fahrenheit is"), (c), ("degrees Celsius"))
## print(f"{f} Degrees Fahrenheit is {c:.2f} Degrees Celsius.")       ## Two decimal places dsiplayed.
