# Python-calculator
import math

print("===== Advanced Calculator =====")

while True:
    print("\nChoose Operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Sin")
    print("8. Cos")
    print("9. Tan")
    print("10. Log")
    print("11. Factorial")
    print("12. Exit")

    choice = input("Enter choice: ")

    if choice == "12":
        print("Calculator Closed")
        break

    # Addition
    elif choice == "1":
        a = float(input("First Number: "))
        b = float(input("Second Number: "))
        print("Result =", a + b)

    # Subtraction
    elif choice == "2":
        a = float(input("First Number: "))
        b = float(input("Second Number: "))
        print("Result =", a - b)

    # Multiplication
    elif choice == "3":
        a = float(input("First Number: "))
        b = float(input("Second Number: "))
        print("Result
