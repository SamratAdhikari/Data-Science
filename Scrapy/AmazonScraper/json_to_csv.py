import json
import csv


with open('data.json') as json_file:
    jsonData = json.load(json_file)


data_file = open('data.csv', 'w', newline='')
csv_writer = csv.writer(data_file)


datas = jsonData[0].replace("'", '"')

column = True
# print(jsonData)
for data in datas:
    if column:
        header = data.keys()
        csv_writer.writerow(header)
        column = False

    csv_writer.writerow(data.values())


data_file.close()
