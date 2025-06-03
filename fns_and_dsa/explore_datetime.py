# Import the necessary classes from the datetime module
from datetime import datetime, timedelta

# Part 1: Function to display the current date and time
def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()

    # Format the date and time to "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

    # Print the result
    print(f"Current date and time: {formatted_date}")

# Part 2: Function to calculate a future date based on days added
def calculate_future_date():
    try:
        # Prompt the user to enter a number of days
        days_to_add = int(input("Enter the number of days to add to the current date: "))

        # Get the current date and time
        current_date = datetime.now()

        # Calculate the future date by adding timedelta
        future_date = current_date + timedelta(days=days_to_add)

        # Format and print the future date
        print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    except ValueError:
        # Handle the case where input is not a valid integer
        print("Invalid input. Please enter a valid number of days.")

# Run the functions
if __name__ == "__main__":
    display_current_datetime()  # Show the current date and time
    calculate_future_date()     # Ask user for input and calculate future date
