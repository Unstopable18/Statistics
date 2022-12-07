from scipy.stats import mode

dataSet=[19,36,8,4,45,18,14,8,9,5,37,46]

print(' Mode '.center(50,'-'),'\nData: ',dataSet,'\nMode Value: ',mode(dataSet).mode,'\nMode Frequency: ',mode(dataSet).count)