import csv

filename = input()

word_freq = {}

with open(filename, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for line in csvFileReader:
        for word in line:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
    reader.close()

for word, freq in word_freq.items():
    print(word, freq)


print()
