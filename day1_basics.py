print("Mini Script for Practice")
print("1. Add two numbers")
print("2. Find area of a circle")
print("3. Convert Celsius -> Fahrenheit")
print("4. Exit")

while True:
    choice = int(input("\nEnter your choice (1-4): "))
    if choice == 1:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Answer is:", num1 + num2)
    elif choice == 2:
        r = float(input("Enter radius of circle: "))
        print("Area of circle is:", 3.14159 * r * r)
    elif choice == 3:
        c = float(input("Enter temperature in Celsius: "))
        f = (c * 9/5) + 32
        print("Temperature in Fahrenheit is:", f, "F")
    elif choice == 4:
        print("Exiting program... Goodbye ")
        break
    else:
        print("INVALID OPERATION! Please choose 1-4.")
























