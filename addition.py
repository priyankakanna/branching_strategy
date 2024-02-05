# Python program to add two numbers

# Function to add two numbers
def add_numbers(num1, num2):
    return num1 + num2

# Main function
def main():
    # Get input from user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Calculate the sum
    sum = add_numbers(num1, num2)

    # Display the result
    print("The sum of", num1, "and", num2, "is:", sum)

# Entry point of the program
if __name__ == "__main__":
    main()
# Make changes to addition.py