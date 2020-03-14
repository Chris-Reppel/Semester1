MINIMUM_LENGTH = 4


def main():
    """Get password from user"""
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)


def get_password(minimum_length):
    """Make sure password is minimum length"""
    password = input("Please enter a password that is at least {} characters: ".format(minimum_length))
    while len(password) < minimum_length:
        print("Your password is too short")
        password = input("Please enter a password that is at least {} characters: ".format(minimum_length))
    return password


def print_asterisks(sequence):
    """Print the same number of asterisks as there are characters in the password"""
    print('*' * len(sequence))


main()
