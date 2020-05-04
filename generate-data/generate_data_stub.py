from generate_location_data import *
from generate_temp_data import *
from generate_device_data import *

import json


def get_configs_dir_location():
    # Current Dir:
    current_dir = os.path.dirname(__file__)
    # Config files location:
    return os.path.join(current_dir, 'configs')


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

    # print(device_numbers_list)
    # print(device_numbers_list.__len__())

    filename = '/Users/philip.carrington/Documents/personal/github-repos/position-tracker/data/' \
               'generated-data/out.json'

    f = open(filename, "w")

    for device in device_numbers_list:

        device_data_dict[device] = {}

        # Get the devices location:
        device_data_dict[device]["location_data"] = get_location_data(no_of_points_per_device,0)

        # Get device temps:
        device_data_dict[device]["temp_data"] = get_temperature(no_of_points_per_device)

        json_data = (json.dumps(device_data_dict))

        f.write(json_data + '\n')

    f.close()


#####################################################
# Run the Job:
if __name__ == "__main__":
    generate_data_stub(3, 10)