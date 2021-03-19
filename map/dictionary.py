import csv

datafile = open('sales.csv', 'r')
reader = csv.reader(datafile)
sales = {}
for row in reader:
    sales[row[0]] = {'lat':row[1], 'lon':row[2], 'title':row[3], 'skills':row[4], 'phone': row[5], 'email':row[6], 'picture':row[7]}
    