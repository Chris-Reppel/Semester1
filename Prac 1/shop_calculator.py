total = 0
num_items = int(input("Enter number of items: "))
while num_items <= 0:
    print("Invalid number of items")
    num_items = int(input("enter number of items: "))
for i in range(num_items):
    cost = float(input("Cost of item: "))
    total += cost
if total > 100:
    total *= 0.9
print("Total cost for {} items is ${:.2f}".format(num_items, total))
