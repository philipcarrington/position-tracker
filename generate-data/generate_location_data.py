import csv
import random


def get_postcode_letter(debug):
    # Choose a letter to read:
    choose_letters = 'A' #BCDEFGHIJKLMNOPQRSTUVWXYZ'
    chosen_letter = random.choice(choose_letters)

    if debug == 1:
        print('The chosen letter is: {} and of type: {}'.format(chosen_letter, type(chosen_letter)))

    return chosen_letter


def read_input_file_to_dict(input_file, debug):
    # Start the dict:
    location_data = {}

    # Read the
    with open(input_file) as fin:
        reader = csv.reader(fin, skipinitialspace=True, quotechar="'")
        for row in reader:
            location_data[row[0]] = row[1:]

    return location_data


def get_chosen_lowest_id(find_data):
    return list(find_data.keys())[0]


def get_chosen_highest_id(find_data):
    return list(find_data.keys())[-1]


def get_location_data(
                      no_of_points=10,
                      debug=0
):

    # TODO: Pass the properly with relative file name etc:
    filename = '/Users/philip.carrington/Documents/personal/github-repos/position-tracker/data/' \
               'external-data/ukpostcodes-head.csv'

    # Choose a letter to read:
    chosen_letter = get_postcode_letter(debug)

    # Read the postcode file into a dictionary:
    location_data_from_file = read_input_file_to_dict(filename, debug)

    # Look into the returned dict:

    # Instantiate the the chosen postcode dict:
    chosen_postcodes = {}

    for location_data_row, location_data_value in location_data_from_file.items():
        # See if this a postcode we want:
        # Get the first letter of the postcode:
        postcode_first_letter = location_data_value[0][0]

        # If it does match add to the chosen dict:
        if chosen_letter == postcode_first_letter:
            # Merge the two dicts:
            chosen_postcodes[location_data_row] = location_data_value

    # Reset the points counter
    returned_points = 0

    # Create the list:
    keys_to_fetch = []

    # Get the range to pass to random:
    lowest_random_value = get_chosen_lowest_id(chosen_postcodes)
    highest_random_value = get_chosen_highest_id(chosen_postcodes)

    while returned_points < no_of_points:
        # Generate random value:
        random_key_value = int(random.uniform(int(lowest_random_value), int(highest_random_value)))

        # Add to the list:
        keys_to_fetch.append(random_key_value)

        # Inc the counter:
        returned_points = returned_points + 1

    # Get the points:
    # Create the return dict:
    location_tracking_data = {}
    return_data_list = []

    # Loop through the list to get the random postcodes:
    for key_point in keys_to_fetch:
        for unique_id, unique_id_data in chosen_postcodes.items():
            if int(unique_id) == key_point:
                return_data_list_items = [unique_id_data[0], float(unique_id_data[1]), float(unique_id_data[2])]

                return_data_list.append(return_data_list_items)

    return return_data_list


#####################################################
# Run the Job:
# if __name__ == "__main__":
#    get_location_data(11, 0)



