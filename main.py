import csv

filename = "input1.csv"

word_freq = {}
try:
    reader = open(filename, 'r')
    csvFileReader = csv.reader(reader)
    for line in csvFileReader:
        for word in line:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
    reader.close()

    for word in word_freq:
        print(word, word_freq[word])
except FileNotFoundError as fe:
    print(f'Error: {filename} not found')

