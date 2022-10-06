# import csv
#
#
# with open("weather_data.csv", "r") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         temperatures.append(row[1])
#     temperatures.remove("temp")

import pandas

data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()
# print(data_dict)

# average = data["temp"].mean()
# print(average)
# print(data[data.temp == max(data.temp)])

monday = data[data.day == "Monday"]
print(int(monday.temp) * 1.8 + 32)