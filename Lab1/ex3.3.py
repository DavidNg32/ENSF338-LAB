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

for i in range(0,1000):
        time_taken = timeit.timeit(#Used Copilot
            stmt=lambda: sizec(data, 1),
            number=1)
        b.append(time_taken)

plt.hist(b,color = 'blue')
plt.xlabel('Time Values')
plt.ylabel('Frequency')
plt.title('Histogram for Average time for 1000 runs for 1000 records')
plt.savefig('output.3.3.png')
print("Average time for 100 runs for 1000 records: ", b[0])
print("Average time for 100 runs for 2000 records: ", b[1])
print("Average time for 100 runs for 5000 records: ", b[2])
print("Average time for 100 runs for 10000 records: ", b[3])

