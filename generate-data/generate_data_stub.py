from generate_location_data import *
from generate_temp_data import *
from generate_device_data import *


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

    print(device_numbers_list)

#####################################################
# Run the Job:
if __name__ == "__main__":
    generate_data_stub(1, 1)