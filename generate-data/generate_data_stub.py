import csv
import random
from random import randrange
import ast
import datetime
import json
import os


def get_data_dir_location():
    # Current Dir:
    current_dir = os.path.dirname(__file__)
    # Config files location:
    return os.path.join(current_dir)


# Takes the input file and crates a processed file:
def read_input_file_to_dict(input_file, output_file, debug):
    # Start the dict:
    location_data = {}

    # Read the
    with open(input_file, 'r') as fin:
        reader = csv.reader(fin, skipinitialspace=True, quotechar="'")
        with open(output_file, 'w') as writer:
            for row in reader:
                if row[0] not in 'id':
                    location_data['id'] = int(row[0])
                    location_data['postcode'] = row[1]
                    location_data['latitude'] = row[2]
                    location_data['longitude'] = row[3]

                    json_data = (json.dumps(location_data, sort_keys=True, default=str))

                    writer.write(json_data + '\n')
            writer.close()


# Function to get the min ID of the postcode from the file:
def get_min_postcode_letter_id(data_file, postcode_letter):
    min_id = 99999
    with open(data_file, 'r') as processed_locations:
        for processed_location_line in processed_locations:
            dict_location_line = ast.literal_eval(processed_location_line)
            if dict_location_line['postcode'][0] in postcode_letter:
                if int(dict_location_line['id']) < min_id:
                    min_id = int(dict_location_line['id'])

    processed_locations.close()
    return min_id


# Function to get the min ID of the postcode from the file:
def get_max_postcode_letter_id(data_file, postcode_letter):
    max_id = 0
    with open(data_file, 'r') as processed_locations:
        for processed_location_line in processed_locations:
            dict_location_line = ast.literal_eval(processed_location_line)
            if dict_location_line['postcode'][0] in postcode_letter:
                if int(dict_location_line['id']) > max_id:
                    max_id = int(dict_location_line['id'])

    processed_locations.close()
    return max_id


# Function for working out the min and max of each letter:
def get_postcodes_min_max_id(data_file):
    # Create a list for the letters:
    postcode_letters = {}

    # Process the data:
    with open(data_file, 'r') as processed_locations:
        for processed_location_line in processed_locations:
            # Turn the file line into an actual dict in mem:
            dict_location_line = ast.literal_eval(processed_location_line)
            # Postcode letter:
            postcode_letter = dict_location_line['postcode'][0]
            if postcode_letter not in postcode_letters:
                postcode_letters[postcode_letter] = {}
                postcode_letters[postcode_letter]['min'] = get_min_postcode_letter_id(data_file, postcode_letter)
                postcode_letters[postcode_letter]['max'] = get_max_postcode_letter_id(data_file, postcode_letter)

    processed_locations.close()
    return postcode_letters


# Generate a number of devices as specified by the input:
def get_device_number():
    return int(random.uniform(int(1), int(9)))


def get_mobile_no():
    mobile_no = '07'

    # Generate the other part of the No.:
    # Create the counter:
    device_number_counter = 1
    while device_number_counter <= 9:
        mobile_no = mobile_no + str(get_device_number())

        # Inc the counter
        device_number_counter = device_number_counter + 1

    return mobile_no


def get_device_numbers(no_of_devices):
    # Generate the devices:
    device_numbers_list = []
    device_counter = 1
    while device_counter <= no_of_devices:
        mobile_no = get_mobile_no()

        if mobile_no not in device_numbers_list:
            # Add the device:
            device_numbers_list.append(mobile_no)
            # Inc the counter:
            device_counter = device_counter + 1

    return device_numbers_list


# Choose a letter:
def get_postcode_letter(debug):
    # Choose a letter to read:
    choose_letter = 'A' # BCDEFGHIJKLMNOPQRSTUVWXYZ'
    chosen_letter = random.choice(choose_letter)

    if debug == 1:
        print('The chosen letter is: {} and of type: {}'.format(chosen_letter, type(chosen_letter)))

    return chosen_letter


# Generate a random Temp:
def get_temperature():
    return random.uniform(int(30), int(40))


# Get the random data location postcodes for the device:
def get_location_data_ids(min_id, max_id, no_of_points):
    # Start the counter:
    points_counter = 1
    # Start the list:
    ids_to_find = []
    while points_counter <= no_of_points:
        new_id = int(random.uniform(int(min_id), int(max_id)))
        if new_id not in ids_to_find:
            ids_to_find.append(new_id)
            points_counter = points_counter + 1

    return ids_to_find


# Get the data from the file for the postcode and flourish:
def get_location_data(mobile_no, location_ids, data_file):
    # Create the list:
    chosen_locations = []
    # Create a dict to hold the chosen data:
    chosen_data = {}
    # Create the var for the time:
    current = datetime.datetime(2020, 9, 20, 13, 00)

    with open(data_file, 'r') as processed_locations:
        for processed_location_line in processed_locations:
            # Turn the file line into an actual dict in mem:
            dict_location_line = ast.literal_eval(processed_location_line)
            if int(dict_location_line['id']) in location_ids:
                # Move the data to a new dict:
                chosen_data = dict_location_line
                # Add the mobile phone no:
                chosen_data['mobile_no'] = mobile_no
                # Add a Temp to the line:
                chosen_data['temp'] = get_temperature()
                # Generate at time:
                current = current + datetime.timedelta(minutes=randrange(10))
                chosen_data['reading_time'] = current.strftime("%Y-%m-%dT%H:%M")

                # Add the new data to the returned list:
                chosen_locations.append(chosen_data)

            if len(location_ids) == len(chosen_locations):
                break

    processed_locations.close()
    return chosen_locations


# Write the data to the file:
def write_locations_data_to_file(out_filename, location_data, no_of_mobile_nos):
    # If it is the first write, then set overwrite flag:
    if no_of_mobile_nos == 1:
        write_setting = 'w'
    else:
        write_setting = 'a'

    # Write the data to the file:
    out_file = open(out_filename, write_setting)

    for location_data_row in location_data:
        jsoned_data = (json.dumps(location_data_row, sort_keys=True, default=str))
        out_file.write(jsoned_data + '\n')

    out_file.close()


def generate_data_stub(
        no_of_devices,
        no_of_data_points
):
    # Get the current filepath:
    current_file_path = get_data_dir_location()
    print(current_file_path)


    # TODO: Pass the properly with relative file name etc:
    filename = '/Users/philip.carrington/Documents/personal/github-repos/position-tracker/data/' \
               'external-data/ukpostcodes.csv'
    processed_filename = '/Users/philip.carrington/Documents/personal/github-repos/position-tracker/data/generated-data' \
                         '/locations-processed.json'
    out_filename = '/Users/philip.carrington/Documents/personal/github-repos/position-tracker/data/generated-data/' \
                   'locations-out.json'

    # Read the postcode file into a dictionary and a file for process debug:
    read_input_file_to_dict(filename, processed_filename, 0)

    # Get the min and max ids of the postcodes from the file
    postcodes_min_max_ids = get_postcodes_min_max_id(processed_filename)

    # Generate a device numbers list:
    device_numbers = get_device_numbers(no_of_devices)

    # Generate the data to go with it:
    no_of_mobile_nos = 1
    for mobile_no in device_numbers:
        # Generate the post code letter:
        chosen_letter = get_postcode_letter(0)

        # Get the ids to find from the file:
        min_postcode_id = postcodes_min_max_ids[chosen_letter]['min']
        max_postcode_id = postcodes_min_max_ids[chosen_letter]['max']
        location_ids = get_location_data_ids(min_postcode_id, max_postcode_id, no_of_data_points)

        # Get the location ids:
        location_data = get_location_data(mobile_no, location_ids, processed_filename)

        # Write the data to the file
        write_locations_data_to_file(out_filename, location_data, no_of_mobile_nos)
        no_of_mobile_nos = no_of_mobile_nos + 1
#####################################################
# Run the Job:
if __name__ == "__main__":
    generate_data_stub(1, 100)
