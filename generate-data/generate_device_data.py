import random


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
