"""
Lottery balls

Program asks the user to enter the total number of lottery balls then the
amount of balls that are drawn. Program checks that the user input is correct:
Both amounts, total and drawn balls, are positive numbers and that the amount
of total balls is greater than the amount of drawn balls. Program counts the
probability for the player to guess all the drawn balls correctly.

Writer of the program: EILeh
"""


def factorial(input_number):
    """
    Counts the factorial of input number.
    :param input_number: The number from which the factorial is calculated.
    :return: The factorial of the number.
    """

    factorial = 1

    # Goes through the variable n_balls till the variable i value is 1. Every
    # loop the i decreases by one.
    for i in range(input_number, 1, -1):
        factorial = factorial * i

    # Factorial of zero is 1_ 0! = 1
    if input_number == 0:
        factorial = 1
        print(factorial)

    return factorial


def main():

    n_balls = int(input("Enter the total number of lottery balls: "))

    p_balls = int(input("Enter the number of the drawn balls: "))

    # If number of total balls or number of drawn balls is not a positive number
    # an error will be printed when program is trying to count the probability.
    if p_balls < 0:
        print("The number of balls must be a positive number.")

    if n_balls < 0:
        print("The number of balls must be a positive number.")

    # If drawn balls is greater than the total balls, an error is printed
    # because it is not possible to draw more balls than there are balls to
    # draw.
    elif n_balls < p_balls:
        print("At most the total number of balls can be drawn.")
        
    else:

        # Stores the information of factorial of all balls.
        factorial_n = factorial(n_balls)

        # Stores the information of difference of total balls minus
        # drawn balls.
        difference = int((n_balls - p_balls))

        # Stores the information of the difference's factorial.
        factorial_difference = factorial(difference)

        # Stores the information of the factorial of drawn balls.
        factorial_p = factorial(p_balls)

        # Counts the probability.
        probability = (factorial_n)//(factorial_difference * factorial_p)

        print(f"The probability of guessing all {p_balls} balls correctly is"
              f" {1}/{probability}")


if __name__ == "__main__":
    main()