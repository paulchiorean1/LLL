import csv

filename = "input1.csv"

word_freq = {}

with open(filename, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        for word in row:
            word = word.lower()
            if word not in word_freq:
                word_freq[word] = 1
            else:
                word_freq[word] += 1

for word, freq in word_freq.items():
    print(word, freq)

print()
