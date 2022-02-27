age = int (input('please enter your number: '))
max_age= age
second = 0

while age !=-1 :
    if max_age < age:
        second = max_age
        max_age = age
    else:
        if second < age:
            second = age
    age = int (input('please enter your number: '))

# If the number -1 is entered, the program ends    
print(max_age,second)
