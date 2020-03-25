# Basic List Operations
numbers = []
for i in range(5):
    number = int(input("Enter a number: "))
    numbers.append(number)

print("The smallest number is", min(numbers))
print("The largest number is", max(numbers))
print("The  sum of the numbers is", sum(numbers))
print("The average of the numbers is", sum(numbers) / len(numbers))

# Woefully inadequate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Enter your username: ")
if username in usernames:
    print("Access Granted")
else:
    print("Access Denied")
