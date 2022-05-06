import random


def get_number():
    """Get number from user.
    Try until user give proper number."""
    while True:
        try:
            result = int(input("Chose the number: "))
            break
        except ValueError:
            print("It's not a number")

    return result


def get_numbers():
    """Get 6 different numbers between 1 and 49."""
    result = []
    while len(result) < 6:
        number = get_number()
        if number not in result and 0 < number <= 49:
            result.append(number)
        else:
            print("Number must be between 1 and 49, or number is duplicate!")
    return result


def print_numbers(numbers):
    """Print given numbers with ascending order."""
    print(", ".join(str(number) for number in sorted(numbers)))


def drawing_numbers():
    """Chose 6 random numbers."""
    numbers = list(range(1, 50))
    random.shuffle(numbers)
    return numbers[:6]


def lotto():
    """Main function with our program."""
    user_numbers = get_numbers()
    print("Your numbers:")
    print(user_numbers)

    random_numbers = drawing_numbers()
    print("Lotto numbers:")
    print(random_numbers)

    hits = 0
    for number in user_numbers:
        if number in random_numbers:
            hits += 1

    print(f"You hit {hits} {'number' if hits == 1 else 'numbers'}!")


if __name__ == '__main__':
    lotto()
