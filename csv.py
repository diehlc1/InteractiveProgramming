import csv

ozone = []
date = []

with open('Texas_reordered.csv', 'rb') as csvfile:
	datareader = csv.reader(csvfile, delimiter=',')
	for row in datareader:
		ozone.append(row[0])
		date.append(row[2])

print ozone
print date