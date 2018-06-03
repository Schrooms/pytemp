import csv
import datetime


def write(temp):
    t = datetime.datetime.now()
    with open('data.csv', 'a') as csvfile:

        fieldnames = ['date', 'temp']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'date': t.strftime('%Y-%m-%d %H:%M:%S'), 'temp': temp})
