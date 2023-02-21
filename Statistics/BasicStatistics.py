# Basic Statistics
import math


# ------------------------ Mean --------------------
# Average Value
# Sum of frequencies/ no of frequencies
# u(miu): mean of population
# x bar: mean of sample
# Outliers Effect result

def mean(*args):
    numerator = sum(args)
    denominator = len(args)

    return numerator / denominator


# ------------------------ Median -----------------
# Number at the center of data set
# If the total number of data is odd, the no at the center is median
# Elif the total number of data is even, take the average of two middle numbers

def median(*args):
    if len(args) % 2 != 0:
        index = math.floor(len(args) / 2)

        return sorted(args)[index]
    else:
        i = round((len(args) + 1) / 2)
        j = i - 1
        print(i, j)

        return (args[i] + args[j]) / 2


# ------------------------- Mode ----------------------
# most occuring item

def mode(*args):
    itemDict = {i: args.count(i) for i in sorted(args)}
    modeList = [key for key, value in itemDict.items() if value ==
                max(itemDict.values())]
    return modeList


# ------------------------ Variance -----------------
def variance(*args):
    meanVal = mean(*args)
    
    numerator = 0
    for item in args:
        numerator += (item - meanVal)**2
    denominator = len(args) - 1
    
    return numerator / denominator


# ----------------------- Standard Deviation -----------------
def standardDeviation(*args):
    varianceVal = variance(*args)
    
    return math.sqrt(varianceVal)


# --------------------- Coefficient of Variance --------------------
def coeffVariance(*args):
    stdDeviationVal = standardDeviation(*args)
    meanVal = mean(*args)
    
    return stdDeviationVal / meanVal


# ------------------ Covariance------------------------
def CoV(*args):
    list1 = args[0][0]
    list2 = args[0][1]
    
    list1_mean = mean(*list1)
    list2_mean = mean(*list2)

    numerator = 0
    if len(list1) == len(list2):
        for index in range(len(list1)):
            numerator += (list1[index] - list1_mean) * (list2[index] - list2_mean)
            
        denominator = len(list1) - 1
        
        return numerator / denominator
    
    
# -------------- Correlation Coefficient ----------------
def rXY(*args):
    list1 = args[0][0]
    list2 = args[0][1]

    list1_sd = standardDeviation(*list1)
    list2_sd = standardDeviation(*list2)

    numerator = CoV(*args)
    denominator = list1_sd * list2_sd
    
    return numerator / denominator


if __name__ == '__main__':
    # print(f"Mean: {mean(1, 2, 3, 4, 5)}")
    # print(f"Median: {median(2, 4, 5, 3, 1, 6)}")
    # print(f"Mode: {mode(2, 4, 5, 3, 1, 6, 2, 3, 3, 4)}")
    # print(f"Variance: {variance(4, 3, 6, 5, 2)}")
    # print(f"Standard Deviation: {standardDeviation(4, 3, 6, 5, 2)}")
    # print(f"Coefficient of Variance: {coeffVariance(3, 4, 4.5, 3.5)}")
    inputList = [[1532, 1488, 1343, 928, 615], [58, 35, 75, 41, 17]]
    # print(f"Covariance: {CoV(inputList)}")
    print(f"Correlation Coefficient: {rXY(inputList)}")
