# with open("weather.csv") as csv:
#     data =  csv.readlines()
#     print(data)

# import csv
# with open("weather.csv") as cs:
#     data =  csv.reader(cs)
#     for row in data:
#         if(row[1]!='temp'):
#             row[1] = int(row[1])
#         print(row)

import pandas as pd
cs = pd.read_csv("weather.csv")
max_temp = cs["temp  "].max()
print(cs[cs.temp==max_temp])

# data={"Name":["Rohit", "Rohan", "Hasranga"], "Age": [20,21,23],"Salary": ["5L", "6L", "8L"]}
#
# data = pd.DataFrame(data)
# print(data)
# data.to_csv("data.csv")
# data.to_numpy()
# print(data)