# This function displays the options menu to the user
def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

# The main function controls the flow of the shopping list manager
def main():
    # Initialize an empty list to store shopping items
    shopping_list = []

    # Start an infinite loop to keep showing the menu until the user exits
    while True:
        display_menu()  # Show the options
        choice = input("Enter your choice: ")  # Take user input

        # If the user chooses to add an item
        if choice == '1':
            item = input("Enter the item to add: ").strip()  # Get the item name
            if item:
                shopping_list.append(item)  # Add the item to the list
                print(f"'{item}' has been added to the shopping list.")
            else:
                print("Item cannot be empty.")  # Handle empty input

        # If the user chooses to remove an item
        elif choice == '2':
            item = input("Enter the item to remove: ").strip()  # Get item name
            if item in shopping_list:
                shopping_list.remove(item)  # Remove the item if found
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"'{item}' not found in the shopping list.")  # Item not found

        # If the user chooses to view the list
        elif choice == '3':
            if shopping_list:
                print("\nCurrent Shopping List:")
                # Loop through and print all items in the list with numbering
                for idx, item in enumerate(shopping_list, 1):
                    print(f"{idx}. {item}")
            else:
                print("The shopping list is empty.")  # Handle empty list case

        # If the user chooses to exit
        elif choice == '4':
            print("Goodbye!")  # Exit message
            break  # Break out of the loop to end the program

        # If the user enters an invalid option
        else:
            print("Invalid choice. Please try again.")  # Error handling

# Run the main function when the script is executed directly
if __name__ == "__main__":
    main()
