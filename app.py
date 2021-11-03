# Create three inputs, two numbers and an operator and store them in variables
# Make the number inputs integers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = input("Enter operator: ")

# Use if statement to check if op is addition and print addition of num1 and num2
if op == '+':
    print("The addition is:", num1 + num2)
# Use elif statement to check if op is subtraction and print the difference of num1 and num2
elif op == '-':
    print("The subtraction is:", num1 - num2)
# Use elif statement to check if op is multiplication and print the product of num1 and num2
elif op == '*':
    print("The multiplication is:", num1 * num2)
