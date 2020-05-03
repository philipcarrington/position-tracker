import csv

filename = '/Users/philip.carrington/Documents/personal/github-repos/position-tracker/data/' \
           'external-data/ukpostcodes.csv'

data={}
with open(filename) as fin:
    reader=csv.reader(fin, skipinitialspace=True, quotechar="'")
    for row in reader:
        data[row[0]]=row[1:]

print(data)
