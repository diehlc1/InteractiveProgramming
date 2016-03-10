def stateDataCompile(csvfile, sliderposition, screenMax):

	stateData = open(csvfile, 'r')
	readAll = stateData.read()

	row_list = readAll.split('\n')
	del row_list[len(row_list)-1], row_list[len(row_list)-1]

	ozone = []
	date = []

	for row in row_list:
		data_point = row.split(',')
		if row == row_list[0]:
			statename = data_point[14]
		ozone.append(data_point[3])
		date.append(data_point[0])

	ozone_sum = float(ozone[0])
	sums_list = []
	list_of_dates = [date[0]]
	for day in range(1,len(date)-1):
		if date[day] != date[day-1]:
			sums_list.append(ozone_sum)
			ozone_sum = float(ozone[day])
			list_of_dates.append(date[day])
		else:
			ozone_sum += float(ozone[day])

	percentTotal = float(sliderposition) / float(screenMax)
	datePos = int(percentTotal * (len(sums_list)-1))
	data4date = sums_list[datePos]
	the_date = list_of_dates[datePos]

	return statename, data4date, the_date


# print stateDataCompile('ad_viz_plotval_data.csv')
# for number in range(1, 51):
# 	csvName = 'ad_viz_plotval_data(%s).csv' % number
# 	print stateDataCompile(csvName)

print stateDataCompile('ad_viz_plotval_data.csv', 50, 1000)