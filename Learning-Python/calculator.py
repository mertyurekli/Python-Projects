num1 = int(input("\nEnter first number: "))
num2 = int(input("Enter second number: "))

print("\n1. Opearion Add")
print("2. Opearion Substract")
print("3. Opearion Multiply")
print("4. Opearion Divide\n")

operation = input("Enter the operation number: ")

if operation == '1':
    print(num1 + num2)
elif operation == '2':
    print(num1 - num2)
elif operation == '3':
    print(num1 * num2)
elif operation == '4':
    print(num1 / num2)
else:
    print("\nOperation number is not valid!\n")
