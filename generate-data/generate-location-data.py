#!/usr/bin/env python

import csv
import string
import random
from json import loads, dumps
from collections import OrderedDict


def get_location_data(output_flie_path,
                      mobile_no,
                      no_of_points=10,
                      debug=0):

    # Choose a letter to read:
    choose_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    chosen_letter = random.choice(choose_letters)
    if debug == 1:
        print('The chosen letter is: {} and of type: {}'.format(chosen_letter, type(chosen_letter)))

    # Read the postcode file into a dictionary:
    input_file = csv.DictReader(open("/Users/philip.carrington/Documents/personal/github-repos/position-tracker/data/"
                                     "external-data/ukpostcodes.csv"))

    # Covert the ordered dict to dict:
    # postcodes = loads(dumps(input_file))
    # Get all the postcodes that have a postcode of the chosen_letter
    choosen_letter_postcodes = {}

    for row in input_file:
        postcode = (row["postcode"])
        if debug == 1:
            print('The postcode is: {} and the first letter: {} of type: {} and the chossen letter is: {}'.format(
                postcode, postcode[0], type(postcode[0]), chosen_letter))

        if postcode[0] in chosen_letter:
            choosen_letter_postcodes[row]
            if debug == 1:
                print(choosen_letter_postcodes)

    print(choosen_letter_postcodes)
    print(type(choosen_letter_postcodes))

    for choosen_letters_postcode_row in choosen_letter_postcodes:
        print(choosen_letters_postcode_row)

    # Reset the points counter
    returned_points = 0


#####################################################
# Run the Job:


if __name__ == "__main__":
    get_location_data(None, None, 11, 0)



