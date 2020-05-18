# Import pandas as pd
import pandas as pd
import os
import random
from random import randrange
import datetime
import json


def get_dir_location():
    # Current Dir:
    return os.path.dirname(os.path.realpath(__file__))


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


# Generate a random Temp:
def get_temperature():
    return random.uniform(int(30), int(40))


# Get the data from the file for the postcode and flourish:
def get_location_data(mobile_no, location_ids, postcodes_data_frame):
    # Create a dataframe to hold the chosen data before flourishing:
    chosen_data_mod = pd.DataFrame(columns=('id', 'postcode', 'latitude', 'longitude',
                                            'temperature', 'reading_time'))
    # Create a dataframe to hold the chosen data:
    chosen_data = pd.DataFrame(columns=('id', 'postcode', 'latitude', 'longitude',
                                        'temperature', 'reading_time', 'mobile_no'))
    # Create the var for the time:
    current = datetime.datetime(2020, 9, 20, 13, 00)

    for find_id in location_ids:
        chosen_data_mod = chosen_data_mod.append(postcodes_data_frame.loc[postcodes_data_frame['id'] == find_id],
                                                 ignore_index=True)
        # Add some changing things to the data:
        # Add a Temp to the line:
        chosen_data_mod['temperature'] = get_temperature()
        # Generate at time:
        current = current + datetime.timedelta(minutes=randrange(10))
        chosen_data_mod['reading_time'] = current

        # Add to the actual data
        chosen_data = chosen_data.append(chosen_data_mod, ignore_index=True)

    # Add the same mobile phone number to all the data:
    chosen_data['mobile_no'] = mobile_no

    # Remove the redundant columns:
    del chosen_data['postcode_first_letter']

    chosen_data_list = chosen_data.to_dict(orient='records')

    return chosen_data_list


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


def generate_device_data(
        no_of_devices,
        no_of_data_points,
        out_file_name
):
    # Get the current filepath:
    current_file_path = get_dir_location()

    # Create the data paths:
    data_path = '{}/{}'.format(current_file_path, 'data')
    external_data_path = '{}/{}'.format(data_path, 'external')
    processed_data_path = '{}/{}'.format(data_path, 'processed')
    generated_data_path = '{}/{}'.format(data_path, 'generated')

    # Create the file paths:
    postcodes_file = '{}/{}'.format(external_data_path, 'ukpostcodes.csv')
    processed_postcodes = '{}/{}'.format(processed_data_path, 'ukpostcodes.json')
    iot_data = '{}/{}'.format(generated_data_path, out_file_name)

    # Import the Postcodes file:
    postcodes_df = pd.read_csv(postcodes_file)

    # Create a column of the first letter:
    postcodes_df['postcode_first_letter'] = postcodes_df['postcode'].str[0]

    # Print out postcodes
    # print(postcodes_df)

    # Get the Min and Max IDs for the
    min_pcode_id_sr = postcodes_df.groupby('postcode_first_letter', sort=True)['id'].min()
    max_pcode_id_sr = postcodes_df.groupby('postcode_first_letter', sort=True)['id'].max()

    # Generate a device numbers list:
    device_numbers = get_device_numbers(no_of_devices)

    # Generate the data to go with it:
    no_of_mobile_nos = 1
    for mobile_no in device_numbers:
        # Generate the post code letter:
        chosen_letter = get_postcode_letter(0)
        # print(chosen_letter)

        # Get the ids to find from the file:
        min_postcode_id = min_pcode_id_sr.get(key=chosen_letter)
        max_postcode_id = max_pcode_id_sr.get(key=chosen_letter)

        location_ids = get_location_data_ids(min_postcode_id, max_postcode_id, no_of_data_points)

        # Get the location ids:
        location_data = get_location_data(mobile_no, location_ids, postcodes_df)

        # Write the data to the file
        write_locations_data_to_file(iot_data, location_data, no_of_mobile_nos)
        no_of_mobile_nos = no_of_mobile_nos + 1


#####################################################
# Run the Job:
if __name__ == "__main__":
    generate_device_data(1, 10, 'outkey.txt')