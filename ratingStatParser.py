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
            

xLabel = ['Good Ratings', 'Bad Ratings']
amerRates = np.array([len(amerGoodRates), len(amerBadRates)])
germRates = np.array([len(germGoodRates), len(germBadRates)])
indRates = np.array([len(indGoodRates), len(indBadRates)])
ind = [x for x, _ in enumerate(xLabel)]

plt.bar(ind, indRates, width=0.8, label='India', color='gold', bottom=germRates+amerRates)
plt.bar(ind, germRates, width=0.8, label='Germany', color='silver', bottom=amerRates)
plt.bar(ind, amerRates, width=0.8, label='America', color='#CD853F')

plt.xticks(ind, xLabel)
plt.ylabel("# of Ratings")
plt.xlabel("Type of Rating")
plt.legend(loc="upper right")
plt.title("Ratings by Country")


plt.show()
