import hashlib
import csv
from collections import OrderedDict
foad = OrderedDict()
hero = OrderedDict()
def hash_password_hack(input_file_name, output_file_name):
    for i in range(1000, 10000):
        hashed_string = hashlib.sha256(str(i).encode('utf-8')).hexdigest()
        foad[hashed_string] = i

    with open(input_file_name) as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            for i in foad:
                if row[1] == i:
                    hero[row[0]] = str(foad[i])
    with open(output_file_name, 'w') as out:
       count = 0
       for i in hero:
            count += 1
            if count == 1:
                out.write(i + ',' + hero[i])
            if count > 1:
                out.write('\n' + i + ',' + hero[i])
             


    