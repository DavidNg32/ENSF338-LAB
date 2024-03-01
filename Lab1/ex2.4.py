import string
import timeit

consonants = set(string.ascii_lowercase) - set('aeiouy')

files = open("pg2701.txt", encoding="utf8")#Used Copilot for encoding
text = files.read()

def timeforcalc(text):
    startline = "CHAPTER 1. Loomings."
    startindex = text.find(startline)
    text = text[startindex:]

    text = text.translate(str.maketrans('', '', string.punctuation)) #Used Copilot
    words = text.split()

    consonant_counts = [sum(1 for char in word.lower() if char in consonants) for word in words] #Used Copilot

    average_consonants = sum(consonant_counts) / len(words) #Used Copilot
    return average_consonants

time_taken = timeit.timeit(#Used Copilot
    stmt=lambda: timeforcalc(text),
    number=100
)

average_time = time_taken / 100

start = timeit.default_timer()
a = timeforcalc(text)
stop = timeit.default_timer()
print("Average Consants: ", a)
print("Time for 1 run: ", stop-start)
print("Average time for 100 runs: ", average_time)
