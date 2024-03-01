import json
import timeit
import numpy as np
import matplotlib.pyplot as plt

with open("large-file.json", "r", encoding="utf-8") as json_file: #Used Copilot for encoding part
    data = json.load(json_file)

def sizec(data, n):
    count = 0
    start = timeit.default_timer()
    for datas in data:
        datas['size'] = 35
        count += 1
        if count == 1000* n:
            stop = timeit.default_timer()
    return stop-start

b = []

def forl(data, b):
    k = [1,2,5,10]
    for i in k:
        time_taken = timeit.timeit(#Used Copilot
            stmt=lambda: sizec(data, i),
            number=100)
        b.append(time_taken/100)
    return b

forl(data,b)
print("Average time for 100 runs for 1000 records: ", b[0])
print("Average time for 100 runs for 2000 records: ", b[1])
print("Average time for 100 runs for 5000 records: ", b[2])
print("Average time for 100 runs for 10000 records: ", b[3])

avgtimes = [b[0],b[1],b[2],b[3]]
listlengths = [1000,2000,5000,10000]
slope, intercept = np.polyfit(listlengths, avgtimes, 1)
plt.scatter(listlengths, avgtimes)
linevalues = [slope * x + intercept for x in listlengths]
plt.plot(listlengths, linevalues, 'r')
plt.savefig('output.3.2.png')