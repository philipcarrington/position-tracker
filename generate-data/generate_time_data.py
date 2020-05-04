from random import randrange
import datetime


def get_random_datetime(start,l):
    current = start
    while l >= 0:
        current = current + datetime.timedelta(minutes=randrange(10))
        yield current
        l-=1

#####################################################
# Run the Job:
# if __name__ == "__main__":
    # startDate = datetime.datetime(2013, 9, 20, 13, 00)

    # for x in list(random_date(startDate, 10)):
        # print(x.strftime("%d/%m/%yT%H:%M"))