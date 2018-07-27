import csv
from tabulate import tabulate

fileName = raw_input("what file? ")

with open(fileName, 'rU') as csvfile:
    fileReader = csv.reader(csvfile)#, delimiter = ' ', quotechar = '|')
    contain = []
    for row in fileReader:
        des = []
        for i in row:
            temp = i.split(",")
            des = des + temp
        contain.append([des[0], des[4]])
    print tabulate(contain[1:6], contain[0], tablefmt = "fancy_grid")

print contain[:6]
