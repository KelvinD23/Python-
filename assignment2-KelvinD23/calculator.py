# Author: <Kelvin Delarosa>
# Assignment #2 - Calculator
# Date due: 2020-10-09
# I pledge that I have completed this assignment without
# collaborating with anyone else, in conformance with the
# NYU School of Engineering Policies and Procedures on
# Academic Misconduct.


def print_menu():
    #prints the general instructions for the user to understand which operation each
    #number references
    print()
    print("1) Perform addition")
    print("2) Perform subtraction")
    print("3) Perform multiplication")
    print("4) Perform division")

def do_multiplication():
    """Informs user that multiplication was chosen, multiplies two
    numbers input by the user, and outputs the result.

    :return: None
    """


    print()
    print("You have chosen the multiplication operation.")
    num_one = float(input("Enter first number: "))
    num_two = float(input("Enter second number: "))
    product = str(num_one * num_two)
    result_product = "The product is " + product + "."
    print(result_product)

def do_division():
    """Informs user that division was chosen, divides two
    numbers input by the user, and outputs the result.

    :return: None
    """
    print()
    print("You have chosen the division operation.")
    num_one = float(input("Enter first number: "))
    num_two = float(input("Enter second number: "))
    divided_num = str(num_one / num_two)
    result_division = "The result of the division of the two numbers is " + divided_num + "."
    print(result_division)

def do_addition():
     """Informs user that addition was chosen, sums two
    numbers input by the user, and outputs the result.

    :return: None
    """
     print()
     print("You have chosen the addition operation.")
     num_one = float(input("Enter first number: "))
     num_two = float(input("Enter second number: "))
     total_sum = str(num_one + num_two)
     result_total_sum = "The sum is " + total_sum + "."
     print(result_total_sum)

def do_subtraction():
    """Informs user that subtraction was chosen, calculates
    the difference between two numbers input by the user, and
    outputs the result.

    :return: None
    """
    print()
    print("You have chosen the subtraction operation.")
    num_one = float(input("Enter first number: "))
    num_two = float(input("Enter second number: "))
    difference = str(num_one - num_two)
    result_difference = "The difference is " + difference + "."
    print(result_difference)

def do_calculation():

   """Prompts user for calculation choice and calls
    function to perform calculation

    :return: the character entered by user
    """
   operation_choice= input("Please enter an option (1-4) or 'q' to quit: ")

   if (operation_choice) == "1":
       do_addition()
   elif (operation_choice) == "2":
       do_subtraction()
   elif (operation_choice) == "3":
       do_multiplication()
   elif (operation_choice) == "4":
       do_division()
   elif (operation_choice) == "q":
       print("\nGoodbye.")
   else:
       print("\nThat was not a valid choice. Try again.")

   return operation_choice


def run_calculator():
    #runs the calculator and performs the proper operation when user enters any
    #number 1-4. The calculator stops running if the user enters "q". If character entered
    #is not 1-4 or 'q' the calculator tells user that input is invalid and to try again.
    print("Welcome to the CS 1114 Calculator!")
    option = None
    while option != "q":
        print_menu()
        option = do_calculation()






def main():

    """Runs a program for performing basic arithmetic
    operations between two numbers
    """
    run_calculator()


####### DO NOT REMOVE IF STATEMENT BELOW ########

if __name__ == '__main__':
    # Remove comments for next 4 lines to run doctests
    # print("Running doctests...")
    # import doctest
    # doctest.testmod(verbose=True)

    # print("\nRunning program...\n")

    main()
