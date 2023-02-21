import math
import csv
import BasicStatistics as stats


with open('ComputerSales.csv', newline='') as csv_file:
    reader = csv.reader(csv_file)
    salesData = list(reader)


def getStringData(index):
    dataList = [0]*40
    dataDict = {}

    for i in range(1, len(salesData)):
        dataList[i] = salesData[i][index]

    print(salesData[i][index])
    print(dataList)
    del dataList[0]
    dataSet = set(dataList)
    uniqueList = list(dataSet)

    for i in range(0, len(uniqueList)):
        numItems = dataList.count(uniqueList)
        dataDict[uniqueList[i]] = numItems

    return dataDict


if __name__ == '__main__':
    print(getStringData(2))
