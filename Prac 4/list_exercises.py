numbers = []
for i in range(5):
    number = int(input("Enter a number: "))
    numbers.append(number)

print("The smallest number is", min(numbers))
print("The largest number is", max(numbers))
print("The  sum of the numbers is", sum(numbers))
print("The average of the numbers is", sum(numbers) / len(numbers))
