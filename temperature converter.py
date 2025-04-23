def c_to_f(celsius):
    return (celsius * 9/5) + 32

def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Temperature Converter")
    print("Choose conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        temp = float(input("Enter temperature in Celsius: "))
        print(f"{temp}°C is {c_to_f(temp):.2f}°F")
    
    elif choice == "2":
        temp = float(input("Enter temperature in Fahrenheit: "))
        print(f"{temp}°F is {f_to_c(temp):.2f}°C")
    
    else:
        print("Invalid choice. Please enter 1 or 2.")

main() 
