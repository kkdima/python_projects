# import csv

# with open("day_25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("day_25/weather_data.csv")
data_squirrel = pandas.read_csv("day_25/TheSquirrelCensusDataAnalysis/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# average_temp = data["temp"].mean()
# max_temp = data["temp"].max()

# print(f"Average temperature: {
#       round(average_temp, 1)}\nMax temperature: {max_temp}")

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# convert celcius to fahrenheit

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp.iloc[0])

# monday_temp_f = monday_temp * 9/5 + 32

# print(data[data.temp == data.temp.max()])

fur_color_counts = data["Primary Fur Color"].value_counts()