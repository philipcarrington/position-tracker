import random


def get_temperature(no_of_temps):
    temps_counter = 0
    temp_list = []

    while temps_counter < no_of_temps:
        temp_list.append(random.uniform(int(30), int(40)))

        # In the counter:
        temps_counter = temps_counter + 1

    return temp_list