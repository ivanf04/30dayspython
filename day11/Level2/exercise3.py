# day 11 level 2 exercise 3
import math

def mean(data):
    sum = 0
    for datum in data:
        sum += datum
    return sum/ len(data)

def median(data):
    index = len(data) // 2
    if len(data) % 2 == 0:
        return (data[index] + data[index + 1]) / 2
    else:
        return data[index + 1]
    
def mode(data):
    dataPoints = dict()
    maxfrequency = 0
    modes = []
    for datum in data:
        if datum in dataPoints:
            dataPoints[datum] += 1
        else:
            dataPoints[datum] = 1
        
        if dataPoints.get(datum) > maxfrequency:
            maxfrequency = dataPoints.get(datum)
            modes.clear()
            modes.append(dataPoints[datum])
        elif dataPoints.get(datum) == maxfrequency:
            modes.append(dataPoints[datum])
    return modes

def range(data):
    data.sort()
    return data[len(data) - 1] - data[0]


def variance(data): 
    mu = mean(data)
    summation = 0 
    for datum in data:
        summation += (datum - mu) ** 2
    return summation / len(data - 2)

def standardDeviation(data):
    return math.sqrt(variance(data))


