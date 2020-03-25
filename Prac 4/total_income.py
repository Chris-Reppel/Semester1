"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    income = []
    month = int(input("How many months? "))

    for month in range(1, month + 1):
        income = float(input("Enter income for month {}: ".format(month)))
        income.append(income)

    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, month + 1):
        income = income[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()

