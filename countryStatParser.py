import csv
import matplotlib.pyplot as plt; plt.rcdefaults();
import numpy as np
import matplotlib.pyplot as plt

def graphData(num, x_list, y_list):
    y_pos = np.arange(len(x_list))
    plt.figure(num, figsize=(22,14))
    plt.barh(y_pos, y_list, align='center', alpha=0.5)
    plt.yticks(y_pos, x_list)
    plt.xlabel('# of Installs')
    plt.title('Installs by Country, Version ' + str(num))

    plt.savefig('plot' + str(num), dpi=500)


#Lists that holds all the raw data
countryList = []
installList = []

with open('countryInstallChart.tsv') as tsvfile:
    reader = csv.reader(tsvfile, delimiter='\t')
    for row in reader:
        if row[1].isdigit():
            installList.append(int(row[1]))
        countryList.append(row[0])


countryData1, countryData2, countryData3, countryData4 = np.array_split(countryList, 4)
installData1, installData2, installData3, installData4 = np.array_split(installList, 4)

graphData(1, countryData1, installData1)
graphData(2, countryData2, installData2)
graphData(3, countryData3, installData3)
graphData(4, countryData4, installData4)
