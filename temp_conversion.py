def celsius_to_fahrenheit(celcius):
    return (celcius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


while True:
    print("\n1. Celsius to Fahrenheit \n2. Fahrenheit to Celsius \n3. exit\n")
    choice = input("choose a conversion (1-3): ")

    if choice == "1":
        celsius_input = float(input("Enter temperature in Celsius: "))
        result = celsius_to_fahrenheit(celsius_input)
        print(f"{celsius_input} C is {result:.1f} F") #.2f means that you want a float number to be printed with maximum of 2 digits after the .
    
    elif choice =="2":
        fahrenheit_input = float(input("Enter the temperature in fahrenheit: "))
        result = fahrenheit_to_celsius(fahrenheit_input)
        print(f"{fahrenheit_input} F is {result:.1f} C")
    
    elif choice == "3":
        print("Exiting ...")

        break
    else:
        print("Invalid choice")
print("Bye!")
    
#### OR IT CAN BE DONE LIKE BELOW########

def celsius_to_fahrenheit(celcius):
    return (celcius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


while True:
    print("\n1. Celsius to Fahrenheit \n2. Fahrenheit to Celsius \n3. exit\n")
    choice = input("choose a conversion (1-3): ")

    if choice == "1":
        celsius_input = float(input("Enter temperature in Celsius: "))
        print(f"{celsius_input} C is {celsius_to_fahrenheit(celsius_input):.1f} F") #.1f means that you want a float number to be printed with maximum of 1 digits after the .
    
    elif choice =="2":
        fahrenheit_input = float(input("Enter the temperature in fahrenheit: "))
        print(f"{fahrenheit_input} F is {fahrenheit_to_celsius(fahrenheit_input):.1f} C")
    
    elif choice == "3":
        print("Exiting ...")

        break
    else:
        print("Invalid choice")
print("Bye!")
    