def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2
    
def divide(num1, num2):
    if num2 == 0:
        print("Cannot divide by zero. Please choose another operation.")
        return None
    return num1 / num2

def calculator_game():
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter the number of your choice (1/2/3/4): ")

    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice. Please choose 1, 2, 3, or 4.")
        return

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == '1':
        result = add(num1, num2)
        operation = '+'
    elif choice == '2':
        result = subtract(num1, num2)
        operation = '-'
    elif choice == '3':
        result = multiply(num1, num2)
        operation = '*'
    elif choice == '4':
        result = divide(num1, num2)
        if result is None:
            return
        operation = '/'

    print(f"Calculate: {num1} {operation} {num2}")
    user_input = print(f"Answer: {result}")


# Main loop for the game
while True:
    calculator_game()
    play_again = input("Do you want to play again? (yes/no): ").lower()

    if play_again != 'yes':
        print("Thanks for playing. Goodbye!")
        break
