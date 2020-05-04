from generate_location_data import *
from generate_temp_data import *
from generate_device_data import *
from generate_time_data import *

import json
import os
import datetime


def get_data_dir_location():
    # Current Dir:
    current_dir = os.path.dirname(__file__)
    # Config files location:
    return os.path.join(current_dir, 'generated_data')


def generate_data_stub(no_of_devices, no_of_points_per_device):
    # Generate the devices:
    # Create counter:
    device_counter = 0

    # generate numbers:
    device_numbers_list = []
    while device_counter < no_of_devices:
        device_numbers_list.append(get_mobile_no())

        # Inc the counter:
        device_counter = device_counter + 1

    # Create device dictionary:
    device_data_dict = {}
    device_count_no = 0

    filename = '/Users/philip.carrington/Documents/personal/github-repos/position-tracker/data/' \
               'generated-data/out.json'

    f = open(filename, "w")

    for device in device_numbers_list:
        # Get the location list:
        location_list = get_location_data(no_of_points_per_device, 0)
        # Get the device temps:
        temps_list = get_temperature(no_of_points_per_device)
        # Get the times list:
        start_date = datetime.datetime(2020, 9, 20, 13, 00)
        times_list = list(get_random_datetime(start_date, no_of_points_per_device))

        for time, location, temp in zip(times_list, location_list, temps_list):
            device_data_dict['mobile_no'] = device
            device_data_dict['reading_time'] = time
            device_data_dict['postcode'] = location[0]
            device_data_dict['lat'] = location[1]
            device_data_dict['long'] = location[2]
            device_data_dict['temperature'] = temp

            json_data = (json.dumps(device_data_dict, sort_keys=True, default=str))

            f.write(json_data + '\n')

    f.close()


#####################################################
# Run the Job:
if __name__ == "__main__":
    generate_data_stub(3, 20)