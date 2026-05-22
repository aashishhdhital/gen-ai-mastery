"""
🧮 SIMPLE CALCULATOR - Phase 1 Project

This is a beginner-friendly calculator that demonstrates:
- Functions and parameters
- User input handling
- Error handling (try-except)
- Control flow (if-else)

Author: Gen AI Mastery
Date: 2025
"""

# Import the calculator functions
from calculator import add, subtract, multiply, divide


def display_menu():
    """Display the calculator menu"""
    print("\n" + "="*40)
    print("     SIMPLE CALCULATOR")
    print("="*40)
    print("\nChoose an operation:")
    print("  1. Add (+)")
    print("  2. Subtract (-)")
    print("  3. Multiply (*)")
    print("  4. Divide (/)")
    print("  5. Exit")
    print("="*40)


def get_number(prompt):
    """
    Get a valid number from the user
    
    Parameters:
        prompt (str): The message to display
    
    Returns:
        float: The valid number entered by user
    """
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            # If user enters non-numeric input
            print("❌ Invalid input! Please enter a valid number.")


def perform_operation(operation, num1, num2):
    """
    Perform the selected operation
    
    Parameters:
        operation (str): The operation to perform
        num1 (float): First number
        num2 (float): Second number
    
    Returns:
        float: The result of the operation
    """
    # Match operation to function
    if operation == "1":
        return add(num1, num2), "+"
    elif operation == "2":
        return subtract(num1, num2), "-"
    elif operation == "3":
        return multiply(num1, num2), "*"
    elif operation == "4":
        # Division needs special error handling
        try:
            return divide(num1, num2), "/"
        except ZeroDivisionError:
            print("❌ Error: Cannot divide by zero!")
            return None, "/"
    else:
        print("❌ Invalid operation! Please choose 1-5.")
        return None, None


def main():
    """
    Main calculator loop - keeps running until user exits
    """
    print("\n🎉 Welcome to Simple Calculator!")
    print("This calculator will help you learn Python fundamentals.\n")
    
    while True:
        # Display menu
        display_menu()
        
        # Get user's choice
        choice = input("\nEnter your choice (1-5): ").strip()
        
        # Exit condition
        if choice == "5":
            print("\n👋 Thank you for using the calculator! Goodbye!\n")
            break
        
        # Get numbers from user
        if choice in ["1", "2", "3", "4"]:
            try:
                num1 = get_number("\nEnter first number: ")
                num2 = get_number("Enter second number: ")
                
                # Perform operation
                result, operator = perform_operation(choice, num1, num2)
                
                # Display result
                if result is not None:
                    print(f"\n✅ Result: {num1} {operator} {num2} = {result}")
                
            except Exception as e:
                print(f"\n❌ An error occurred: {e}")
        else:
            print("❌ Invalid choice! Please enter 1-5.")


if __name__ == "__main__":
    # This line ensures main() only runs when the script is executed directly
    # (not when imported as a module in another script)
    main()
