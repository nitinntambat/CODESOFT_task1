# Simple Calculator

print("====== SIMPLE CALCULATOR ======")

# Taking input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Displaying available operations
print("\nSelect operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Modulus (%)")

# Taking operation choice from user
choice = input("\nEnter your choice (1/2/3/4/5): ")

# Performing the operation based on user input
if choice == '1' or choice == '+':
    result = num1 + num2
    print(f"\nResult: {num1} + {num2} = {result}")

elif choice == '2' or choice == '-':
    result = num1 - num2
    print(f"\nResult: {num1} - {num2} = {result}")

elif choice == '3' or choice == '*':
    result = num1 * num2
    print(f"\nResult: {num1} × {num2} = {result}")

elif choice == '4' or choice == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"\nResult: {num1} ÷ {num2} = {result}")
    else:
        print("\nError: Division by zero is not allowed.")

elif choice == '5' or choice == '%':
    result = num1 % num2
    print(f"\nResult: {num1} % {num2} = {result}")

else:
    print("\nInvalid choice! Please select a valid operation.")

print("\n====== END OF CALCULATION ======")
