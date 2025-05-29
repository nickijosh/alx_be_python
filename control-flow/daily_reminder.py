# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the Task Based on Priority and Time Sensitivity
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Make sure to complete it soon.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires attention today.")
        else:
            print(f"Note: '{task}' is a medium priority task. Try to fit it into your schedule.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task but it still requires attention today.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority entered. Please enter high, medium, or low.")
