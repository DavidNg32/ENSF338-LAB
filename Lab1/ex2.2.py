import string

consonants = set(string.ascii_lowercase) - set('aeiouy')

files = open("pg2701.txt", encoding="utf8")#Used Copilot for encoding
text = files.read()

startline = "CHAPTER 1. Loomings."
startindex = text.find(startline)
text = text[startindex:]

text = text.translate(str.maketrans('', '', string.punctuation)) #Used Copilot
words = text.split()

consonant_counts = [sum(1 for char in word.lower() if char in consonants) for word in words] #Used Copilot

average_consonants = sum(consonant_counts) / len(words) #Used Copilot

print(average_consonants)