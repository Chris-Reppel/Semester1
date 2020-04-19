import random

numbers_per_line = 6
minimum = 1
maximum = 45


def main():
    number_of_picks = int(input("How many picks?: "))
    while number_of_picks < 0:
        print("That won't work")
        number_of_picks = int(input("How many picks?: "))

    for i in range(number_of_picks):
        picks = []
        for j in range(numbers_per_line):
            number = random.randint(minimum, maximum)
            while number in picks:
                number = random.randint(minimum, maximum)
            picks.append(number)
        picks.sort()
        print(" ".join("{:2}".format(number) for number in picks))


main()

