import csv
import numpy as np
import matplotlib.pyplot as plt

#Index 3 = US
#Index 4 = Germany
#Index 5 = India

amerGoodRates = []
amerBadRates = []
germGoodRates = []
germBadRates = []
indGoodRates = []
indBadRates = []

goodDict = {
    4: amerGoodRates,
    5: germGoodRates,
    6: indGoodRates
}

badDict = {
    4: amerBadRates,
    5: germBadRates,
    6: indBadRates
}

def save_to_lists(index, string):
    number = float(string)
    if number >= 4:
        goodDict[index].append(number)
    else:
        badDict[index].append(number)


with open('ratingStats.csv') as csvFile:
    reader = csv.reader(csvFile, delimiter=',')
    for row in reader:
        if row[3]:
            for i in range(4,7):
                string = row[i]
                if "-" in string:
                    string = '0'
                save_to_lists(i, string)
            

goodTotal = len(goodDict[4]) + len(goodDict[5]) + len(goodDict[6])
badTotal = len(badDict[4]) + len(badDict[5]) + len(badDict[6])



xLabel = ['Good Ratings', 'Bad Ratings']
amerRates = np.array([len(goodDict[4])/goodTotal * 100, len(badDict[4])/badTotal * 100])
germRates = np.array([len(goodDict[5])/goodTotal * 100, len(badDict[5])/badTotal * 100])
indRates = np.array([len(goodDict[6])/goodTotal * 100, len(badDict[6])/badTotal * 100])
ind = [x for x, _ in enumerate(xLabel)]

# Prints percentages
print(len(goodDict[4])/goodTotal * 100)
print(len(badDict[4])/badTotal * 100)
print(len(goodDict[5])/goodTotal * 100)
print(len(badDict[5])/badTotal * 100)
print(len(goodDict[6])/goodTotal * 100)
print(len(badDict[6])/badTotal * 100)

#Prints values
print(len(goodDict[4]))
print(len(badDict[4]))
print(len(goodDict[5]))
print(len(badDict[5]))
print(len(goodDict[6]))
print(len(badDict[6]))




plt.bar(ind, indRates, width=0.8, label='India', color='#AA650A', bottom=germRates+amerRates)
plt.bar(ind, germRates, width=0.8, label='Germany', color='#AA0A0A', bottom=amerRates)
plt.bar(ind, amerRates, width=0.8, label='America', color='#FF880A')

plt.xticks(ind, xLabel)
plt.ylabel("Percentage")
plt.xlabel("Type of Rating")
plt.legend(loc="upper right")
plt.title("Good and Bad Ratings by Country")

plt.savefig('plot', dpi=500)
