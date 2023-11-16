#!/usr/bin/env python3

# Created by: Lily Carroll
# Created on: Nov/16/2023
# This program will display all the possible color combinations for RBG using nested loops.


def main():
    # Initializing my color variables.
    red = 0
    blue = 0
    green = 0

    # Explaining my program to the user.
    print("My program will display all the RGB color combinations.")

    # Using nested for loops to display all the possible color combinations.
    # First loop for red values.
    for red in range(0, 256, 1):
        # Second loop for green values.
        for green in range(0, 256, 1):
            # Third loop for blue values.
            for blue in range(0, 256, 1):
                # Displaying the RGB color code.
                print(
                    "\033[38;2;{};{};{}mRGB({}, {}, {})\033[0m".format(red, green, blue)
                )


if __name__ == "__main__":
    main()
