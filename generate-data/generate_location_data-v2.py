import csv
import random
import json


def get_postcode_letter(debug):
    # Choose a letter to read:
    choose_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    chosen_letter = random.choice(choose_letter)

    if debug == 1:
        print('The chosen letter is: {} and of type: {}'.format(chosen_letter, type(chosen_letter)))

    return chosen_letter


def read_input_file_to_dict(input_file, output_file, debug):
    # Start the dict:
    location_data = {}

    # Read the
    with open(input_file, 'r') as fin:
        reader = csv.reader(fin, skipinitialspace=True, quotechar="'")
        with open(output_file, 'w') as writer:
            for row in reader:
                if row[0] not in 'id':
                    location_data['id'] = row[0]
                    location_data['postcode'] = row[1]
                    location_data['latitude'] = row[2]
                    location_data['longitude'] = row[3]

                    json_data = (json.dumps(location_data, sort_keys=True, default=str))

                    writer.write(json_data + '\n')
            writer.close()


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
               'external-data/ukpostcodes.csv'
    out_filename = '/Users/philip.carrington/Documents/personal/github-repos/position-tracker/data/generated-data' \
                   '/locations-processed.json'

    # Choose a letter to read:
    chosen_letter = get_postcode_letter(debug)

    # Read the postcode file into a dictionary and a file for process debug:
    read_input_file_to_dict(filename, out_filename, debug)

    # Read in the locations file:
    with open(out_filename, 'r') as processed_locations:
        processed_location_line = processed_locations.readline()
        while processed_location_line:
            print(type(processed_location_line))




#####################################################
# Run the Job:
if __name__ == "__main__":
    get_location_data(11, 1)



