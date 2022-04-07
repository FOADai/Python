import csv
# For the average
from statistics import mean 
from collections import OrderedDict
import operator
import itertools
averages = OrderedDict()

def calculate_averages(input_file_name, output_file_name):
    with open(input_file_name) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            scores = []
            for i in row[1:]:
                scores.append(float(i))
            avg = mean(scores)
            averages [row[0]] = avg
    with open(output_file_name, 'w') as out:
        count = 0
        for person in averages:
            count += 1
            if count == 1:
                out.write(person + ',' + str(averages[person]))
            else:
                out.write('\n' + person + ',' + str(averages[person]))
    


def calculate_sorted_averages(input_file_name, output_file_name):
    nerakar = OrderedDict()
    with open(input_file_name) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            scores = []
            for i in row[1:]:
                scores.append(float(i))
            avg = mean(scores)
            nerakar [row[0]] = avg
        averages = OrderedDict(sorted(nerakar.items(), key=lambda t: t[1]))
        result = []
        for k,v in itertools.groupby(averages, lambda item: item[1]):
            result.extend(sorted(v))
    with open(output_file_name, 'w') as out:
        count = 0
        for person in averages:
            count += 1
            if count == 1:
                out.write(person + ',' + str(averages[person]))
            else:
                out.write('\n'+ person + ',' + str(averages[person]))
    


def calculate_three_best(input_file_name, output_file_name):
    nerakar = OrderedDict()
    with open(input_file_name) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            scores = []
            for i in row[1:]:
                scores.append(float(i))
            avg = mean(scores)
            nerakar [row[0]] = avg
        averages = OrderedDict(sorted(nerakar.items(), key=lambda t: t[1]))
        golakar = OrderedDict( sorted(averages.items(), key=operator.itemgetter(1),reverse=True))
        
    with open(output_file_name, 'w') as out:
        count = 0
        for person in golakar:
            count += 1
            if count == 1:
                out.write(person + ',' + str(golakar[person]))
            elif count <= 3:
                out.write('\n' + person + ',' + str(golakar[person]))
def calculate_three_worst(input_file_name, output_file_name):
    nerakar = OrderedDict()
    with open(input_file_name) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            scores = []
            for i in row[1:]:
                scores.append(float(i))
            avg = mean(scores)
            nerakar [row[0]] = avg
        averages = OrderedDict(sorted(nerakar.items(), key=lambda t: t[1]))
    with open(output_file_name, 'w') as out:
        count = 0
        for person in averages:
            count += 1
            if count == 1:
                out.write(str(averages[person]))
            elif count <= 3:
                out.write('\n' + str(averages[person]))

def calculate_average_of_averages(input_file_name, output_file_name):
    with open(input_file_name) as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            scores = []
            for i in row[1:]:
                scores.append(float(i))
            avg = mean(scores)
            averages [row[0]] = avg
        ave_s = list()
        for row in averages:
            ave_s.append(averages[row])
                
    with open(output_file_name, 'w') as out:
        out.write(str(mean(ave_s)))