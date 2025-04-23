# Simple List Manager
my_list = []

# Display the menu to the user
def display_menu():
    print("\nList Manager Menu:")
    print("1. Add item")
    print("2. Remove item")
    print("3. Display all items")
    print("4. Search for an item")
    print("5. Sort the list")
    print("6. Exit")
    
# Function to add an item to the list
def add_item():
    item = input("Enter the item to add: ")
    my_list.append(item)
    print(f"{item} has been added to the list.")
    
# Function to remove an item from the list
def remove_item():
    item = input("Enter the item to remove: ")
    if item in my_list:
        my_list.remove(item)
        print(f"{item} has been removed from the list.")
    else:
        print(f"{item} not found in the list.")

# Function to display all items in the list
def display_items():
    if my_list:
        print("\nItems in the list:")
        for i, item in enumerate(my_list, 1):
            print(f"{i}. {item}")
    else:
        print("The list is empty.")
        
# Function to search for an item in the list
def search_item():
    item = input("Enter the item to search for: ")
    if item in my_list:
        print(f"{item} found in the list at position {my_list.index(item) + 1}.")
    else:
        print(f"{item} not found in the list.")

# Function to sort the list
def sort_list():
    my_list.sort()
    print("The list has been sorted.")

# Main program loop
def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            add_item()
        elif choice == "2":
            remove_item()
        elif choice == "3":
            display_items()
        elif choice == "4":
            search_item()
        elif choice == "5":
            sort_list()
        elif choice == "6":
            print("Exiting the List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function
main()
