import json
import timeit

with open("large-file.json", "r", encoding="utf-8") as json_file: #Used Copilot for encoding part
    data = json.load(json_file)

def sizec(data):
    for datas in data:
        datas['size'] = 35
start = timeit.default_timer()
sizec(data)
stop = timeit.default_timer()

time_taken = timeit.timeit(#Used Copilot
    stmt=lambda: sizec(data),
    number=10
)
    
with open("output.2.3.json", "w") as file:
    json.dump(data[::-1], file, indent=2)

print("Time to change size: ", stop-start)
print("Average time for 10 runs: ", time_taken / 10)