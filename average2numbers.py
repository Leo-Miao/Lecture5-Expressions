"""
File: average2numbers.py
------------------------
This program asks the user for two numbers
and prints their average.
"""

def main():
    print("This program averages two numbers.")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    total = (num1 + num2) / 2
    print("The average is", total)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
