""" Implementation of the extended Euclidean algorithm that prints out all steps in the form of a matrix.

https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm:
'In arithmetic and computer programming, the extended Euclidean algorithm is an extension to the Euclidean
algorithm, and computes, in addition to the greatest common divisor of integers a and b, also the coefficients
of Bézout's identity, which are integers x and y such that [a*s+b*t=gcd(a,b)].'
"""

__author__ = "Zacharuk, Markus"
__email__ = "markus.zacharuk@stud.uni-frankfurt.de"


def create_string(table, space_between_columns=2):
    """ This creates a formatted string with variable column widths.

    Printing with "\t" didn't format well when big numbers were given, so this is a workaround.
    """
    result = ""
    column_widths = [0, 0, 0, 0, 0]
    for i in range(len(table)):
        for j in range(1, 5):
            if column_widths[j] < len(str(table[i][j-1])) + space_between_columns:
                column_widths[j] = len(str(table[i][j-1])) + space_between_columns
    column_widths[0] = len(str(i)) + 2
    for x in column_widths:
        x += 1
    for i in range(len(table)):
        # Print the list we created.
        if i == 0:
            result += "j".ljust(column_widths[0])
        else:
            result += str(i).ljust(column_widths[0])
        for j in range(len(table[i])):
            result += str(table[i][j]).ljust(column_widths[j+1])
        result += "\n"
    return result


def extended_euclidean_algorithm(a, b):
    """ Clculates the biggest common divisor with bézout-coefficients.

    Prints out a matrix that shows each step of the algorithm.
    a and b can be any integers.
    """

    r = 0
    s = 0
    t = 0
    q = 0

    if b > a:
        # Make sure the numbers are given in the right order to the algorithm
        c = a
        a = b
        b = c
    # The list (matrix) representing each step as sublist. the first element (and row) is the header, specifying the columns.
    table = [['q', 'r', 's', 't'], [0, a, 1, 0], [a//b, b, 0, 1]]

    while True:
        # The algorithm-loop
        r = table[-2][1] - table[-1][0] * table[-1][1]
        if r == 0:
            break
        s = table[-2][2] - table[-1][0] * table[-1][2]
        t = table[-2][3] - table[-1][0] * table[-1][3]
        q = table[-1][1] // r
        table.append([q, r, s, t])

    print()
    print(create_string(table))

    print("gcd(", a, ",", b, ") = ", table[-1][1], sep="")
    print(s, "*", a, "+", t, "*", b, "=", s*a + t*b, end="\n\n")


def parse_input():
    """ Get two integers from the user as input and return them"""
    input_str = input("First number: ")
    if "exit" in input_str:
        return 0, 0
    if not input_str.isdigit():
        print("Only integers allowed! Aborting program!")
    a = int(input_str)
    input_str = input("Second number: ")
    if "exit" in input_str:
        return 0, 0
    if not input_str.isdigit():
        print("Only integers allowed! Aborting program!")
    b = int(input_str)
    return a, b


def main():
    """ Handle the controll flow of the program: Get the numbers and run the algorithm on them."""
    print("Implementation of the extended Euclidean algorithm that prints out all steps in the form of a matrix.\nType exit to end the program.")
    while True:
        a, b = parse_input()
        if a == 0 and b == 0:
            break
        extended_euclidean_algorithm(a, b)
    print("Program exited.")


if __name__ == "__main__":
    main()
