def stateDataCompile(csvfile):

	stateData = open(csvfile, 'r')
	readAll = stateData.read()

	row_list = readAll.split('\n')

	ozone = []
	date = []

	for row in row_list:
		data_point = row.split(',')
		ozone.append(data_point[0])
		date.append(data_point[len(data_point)-1])

	ozone_sum = float(ozone[0])
	sums_list = []
	for day in range(1,len(date)-1):
		if date[day] != date[day-1]:
			sums_list.append(ozone_sum)
			ozone_sum = float(ozone[day])
		else:
			ozone_sum += float(ozone[day])

	return sums_list

print stateDataCompile('Texas_reordered.csv')