#!/usr/bin/env python

import csv
import string
import random

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
    input_file = csv.DictReader(open("/Users/philip.carrington/Documents/personal/github-repos/position-tracker/data/external-data/ukpostcodes.csv"))

    # print(type(input_file))
    # print(input_file)

    # Reset the points counter
    returned_points = 0

    for row in input_file:
        postcode = (row["postcode"])
        # print('The postcode is: {} and the first letter: {} of type: {}'.format(postcode, postcode[0], type(postcode[0])))
        while returned_points <= no_of_points:
            if postcode[0] == chosen_letter:
                print('+++++++ Row chosen +++++')
                print(row)
            returned_points = returned_points + 1

#####################################################
# Run the Job:


if __name__ == "__main__":
    get_location_data(None, None, 11, 1)



