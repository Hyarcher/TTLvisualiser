import csv
import random
import time

#The variables initial values
packet_identifier = 0
ttl_value = random.randint(240, 255)

#Setting column names
fieldnames = ['packet_identifier', 'ttl_value']

#The creation of the CSV
with open('data2.csv', 'w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()

#When the file is opened is fills it with data
while True:
    with open('data2.csv', 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {'packet_identifier': packet_identifier, 'ttl_value': ttl_value}

        #Writes a new singular entry
        csv_writer.writerow(info)

        packet_identifier += 1

        #Random TTl values are assigned to the packets with less of a range to produce high ttl packet loads
        ttl_value = random.randint(240, 255)

    time.sleep(0.2)