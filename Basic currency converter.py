def display_menu():
    print("\n \t Currency Converter")
    print("1. Convert US Dollar(USD) to BDT")
    print("2. Convert Indian Rupee(INR) to BDT")
    print("3. Convert Saudi Riyal(SAR) to BDT")
    print("4. Quit") 

def convert_usd_to_bdt():
    usd = float(input("Enter amount in USD: "))
    exchange_rate = 110.0 
    bdt = usd * exchange_rate
    print(f"{usd} USD is {bdt} BDT")

def convert_inr_to_bdt():
    inr = float(input("Enter amount in INR: "))
    exchange_rate = 1.4  
    bdt = inr * exchange_rate
    print(f"{inr} INR is {bdt} BDT")
    
def convert_sar_to_bdt():
    sar = float(input("Enter amount in SAR: "))
    exchange_rate = 31  
    bdt = sar * exchange_rate
    print(f"{sar} SAR is {bdt} BDT")

greeting = "Welcome to the Currency Converter!"
print(greeting)

running = True
while running:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        convert_usd_to_bdt()
    elif choice == '2':
        convert_inr_to_bdt()
    elif choice == '3':
        convert_sar_to_bdt()
    elif choice == '4':
        print("Goodbye!")
        running = False
    else:
        print("Invalid choice. Please try again.")

