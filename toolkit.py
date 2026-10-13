# toolkit.py

def number_guessing_game():
    """Tool 1: A number-guessing game using a loop and conditionals."""
    print("\n--- Number Guessing Game ---")
    secret_number = 7
    attempts = 0
    
    while True:
        try:
            guess = int(input("Guess a number between 1 and 10 (or 0 to exit): "))
            if guess == 0:
                print("Exiting game...")
                break
            
            attempts += 1
            if guess == secret_number:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                break
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Please enter a valid integer.")

def dynamic_todo_list():
    """Tool 2: A task manager using a list that changes during runtime."""
    print("\n--- Dynamic Todo List ---")
    todo_list = []
    
    while True:
        action = input("Type 'add' to insert a task, 'show' to view tasks, or 'done' to return to main menu: ").strip().lower()
        if action == "add":
            task = input("Enter the task description: ").strip()
            if task:
                todo_list.append(task)
                print(f"Task '{task}' added successfully!")
        elif action == "show":
            if not todo_list:
                print("Your todo list is currently empty.")
            else:
                print("Your Current Tasks:")
                for idx, t in enumerate(todo_list, start=1):
                    print(f"{idx}. {t}")
        elif action == "done":
            print("Returning to main menu...")
            break
        else:
            print("Invalid command. Please try again.")

def tip_calculator():
    """Tool 3: A simple tip calculator using conditionals and f-strings."""
    print("\n--- Simple Tip Calculator ---")
    try:
        bill = float(input("Enter the total bill amount ($): "))
        service = input("How was the service? (good / fair / poor): ").strip().lower()
        
        if service == "good":
            tip_percent = 0.20
        elif service == "fair":
            tip_percent = 0.15
        elif service == "poor":
            tip_percent = 0.10
        else:
            print("Unknown service rating. Defaulting to 15% tip.")
            tip_percent = 0.15
            
        tip_amount = bill * tip_percent
        total_bill = bill + tip_amount
        
        print(f"Bill: ${bill:.2f} | Tip ({int(tip_percent * 100)}%): ${tip_amount:.2f} | Total: ${total_bill:.2f}")
    except ValueError:
        print("Invalid numerical input. Please enter valid amounts.")

def main():
    """Main program loop displaying the menu."""
    print("Welcome to your Personal Mini-Toolkit!")
    
    while True:
        print("\n=== PERSONAL MINI-TOOLKIT ===")
        print("1. Number Guessing Game")
        print("2. Dynamic Todo List")
        print("3. Simple Tip Calculator")
        print("4. Quit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            number_guessing_game()
        elif choice == "2":
            dynamic_todo_list()
        elif choice == "3":
            tip_calculator()
        elif choice == "4":
            print("\nThank you for using Personal Mini-Toolkit. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice! Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()
