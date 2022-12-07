from statistics import stdev,variance
from numpy import sqrt,square
dataSet=[19,36,8,4,45,18,14,8,9,5,37,46]
v=variance(dataSet)
sd=stdev(dataSet)
print('Correlation Standard Deviation-Variance '.center(50,'-'),'\nData: ',dataSet)
print('Standard Deviation: ',sd)
print('Variance: ',v)
print(sqrt(v), square(sd))
