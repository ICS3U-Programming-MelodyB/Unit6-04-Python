#!/usr/bin/env python3

# Created by: Melody Berhane
# Created on: Feb 2, 2022
# This program uses a nested for loops to generate and
# print random numbers in a 2d array. It then calculates
# and displays the average of the numbers.

import constants
import random


# function calculates the average of the all the numbers
def calc_average(passed_list):
    # initializing sum and counters
    sum = 0

    # calculating sum
    for row_value in passed_list:
        for single_element in row_value:
            sum += single_element

    # calculating average
    average = sum / (len(passed_list) * len(row_value))

    # copies average to the main function
    return average


# collects user input, checks for invalid data
# displays results
def main():
    # declaring variable
    a_2_list = []

    # display opening message to console
    print("This program will ask the user for the number"
          " of rows and columns to")
    print("create a 2D array. It will then "
          "populate it with random numbers and")
    print("calculate the average of the numbers.")
    print("")

    # gets input from user
    rows = input("Enter the number of rows: ")

    try:
        # converts input to int
        rows_int = int(rows)

        # checks if input is a positive integer
        if rows_int > 0:

            # gets input from user
            columns = input("Enter the number of columns: ")

            try:
                # converts
                columns_int = int(columns)

                # checks if input is a positive integer
                if columns_int > 0:
                    print("")

                    # generate random numbers in 2d array
                    for counter_rows in range(0, rows_int):
                        column_array = []
                        for counter_columns in range(0, columns_int):
                            ranNum = random.randint(constants.MIN_NUM,
                                                    constants.MAX_NUM)
                            column_array.append(ranNum)
                            print("{0} " .format(ranNum), end="")
                        a_2_list.append(column_array)
                        print("")

                    # assigns variable to function call
                    average_user = calc_average(a_2_list)
                    # displays results to user
                    print("")
                    print("The average is: {:,.2f}" .format(average_user))
                else:
                    print("Please enter a number greater than 0!")
            except Exception:
                print("{} is not a valid number" .format(columns))
        else:
            print("Please enter a number greater than 0!")
    except Exception:
        print("{} is not a valid number" .format(rows))


if __name__ == "__main__":
    main()
