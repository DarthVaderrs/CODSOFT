# Function to perform arithmetic operations.
# Input from the user
# Perform the calculation


# Display the result


def perform_calculation(num1, num2, operator):
    if operator == '+':
      return num1 + num2
    elif operator == '-':
        return num1 - num2
   elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")

result = perform_calculation(num1, num2, operator)


print(f"Result: {result}")
