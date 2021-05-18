import sys
import csv
import numpy as np
import re


def main():
    # Verify the number of arguments passed in input
    if len(sys.argv) != 3:
        # Aguments is not enogth
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit()
    # Assing names to each argument
    database = sys.argv[1]
    sequence = sys.argv[2]

    # Lists to save the DB and DNA str count
    headers = []
    information = []
    dnastrcount = []

    # Open the database
    with open(database, 'r') as csvfile:
        reader = csv.reader(csvfile)
        line = 0
        for row in reader:
            if line == 0:
                headers = row
                line += 1
            else:
                information.append(row)

    print(headers)
    print(information)

    # Open the sequence and remove new line at the end
    with open(sequence, 'r') as txtfile:
        sq = txtfile.readline().rstrip("\n")

    # for loop to count each DNA str and save in a list
    for i in range(1, len(headers)):
        dnastrcount.append(counter(headers[i], sq))
    dnastrcount = np.array(dnastrcount)

    # for loop to compare DNA str count with sequences
    for i in range(len(information)):
        temp = np.array(information[i][1:])
        if (temp == dnastrcount).all():
            name = information[i][0]
            break
        else:
            name = "No match"
    print(name)


# Function to count each pattern in a sequence
def counter(c, s):
    p = rf'({c})\1*'
    pattern = re.compile(p)
    match = [match for match in pattern.finditer(s)]
    max = 0
    print(match)
    for i in range(len(match)):
        if match[i].group().count(c) > max:
            max = match[i].group().count(c)
    return str(max)


main()
