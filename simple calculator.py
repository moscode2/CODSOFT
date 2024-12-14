# File: simple calculator.py

def display_menu():
    print("\nSimple Calculator")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

def perform_calculation(num1, num2, operation):
    if operation == "1":
        return num1 + num2
    elif operation == "2":
        return num1 - num2
    elif operation == "3":
        return num1 * num2
    elif operation == "4":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero."
    else:
        return "Invalid operation."

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "5":
            print("Exiting the calculator. Goodbye!")
            break
        
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        
        result = perform_calculation(num1, num2, choice)
        if isinstance(result, str):  # Handle errors like division by zero
            print(result)
        else:
            print(f"Result: {result}")

if __name__ == "__main__":
    main()
