def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y
def exponent(x, y):
    return x ** y

print("\t Welcome to the Basic Calculator!")
print("Select an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exponent")

while True:
    choice = input("Enter choice(1/2/3/4/5): ")

    if choice in ('1', '2', '3', '4','5'):
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
        elif choice == '5':
            result = exponent(num1, num2)
            print(f"{num1} ^ {num2} = {result}")
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            print("\t Thanks for calculating.")
            break
    else:
        print("Invalid choice! Please select a valid operation.")

