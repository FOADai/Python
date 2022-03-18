

vote = int(input())
lst = []
for i in range(0, vote):
    names = input()
    lst.append(names)

counter = dict()
for letter in lst:
    if letter in counter:
        counter[letter] += 1
    else:
        counter[letter] = 1

for this_one in sorted(counter):
    print(this_one,counter[this_one])

 



