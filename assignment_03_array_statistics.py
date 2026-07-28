# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def get_sum(numbers):
    """Return the sum of the numbers using a loop."""
    total = 0
    for value in numbers:
        total += value
    return total


def get_average(numbers):
    """Return the average of the numbers."""
    if len(numbers) == 0:
        return 0
    return get_sum(numbers) / len(numbers)


def get_maximum(numbers):
    """Return the maximum value from the list using a loop."""
    if len(numbers) == 0:
        return None
    maximum = numbers[0]
    for value in numbers[1:]:
        if value > maximum:
            maximum = value
    return maximum


def get_minimum(numbers):
    """Return the minimum value from the list using a loop."""
    if len(numbers) == 0:
        return None
    minimum = numbers[0]
    for value in numbers[1:]:
        if value < minimum:
            minimum = value
    return minimum


def read_numbers(count):
    """Read a list of numbers from the user."""
    numbers = []
    for i in range(1, count + 1):
        while True:
            try:
                value = float(input(f"Enter number {i}: "))
                numbers.append(value)
                break
            except ValueError:
                print("Error: Please enter a valid number.")
    return numbers


def main():
    """Main program for the array statistics calculator."""
    try:
        count = int(input("How many numbers? "))
    except ValueError:
        print("Error: Please enter a valid integer.")
        return

    if count <= 0:
        print("Error: Number of values must be a positive integer.")
        return

    numbers = read_numbers(count)
    total = get_sum(numbers)
    average = get_average(numbers)
    maximum = get_maximum(numbers)
    minimum = get_minimum(numbers)

    print("\nResults:")
    print(f"Sum:     {total}")
    print(f"Average: {average}")
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")


if __name__ == "__main__":
    main()

