numbers = int (input('enter your number: '))
count = 0
total = 0
average = 0
while (numbers != -1):
    count = count + 1
    total = total + numbers
    average = total / count 
    numbers = int (input('enter your number: '))

print(average)
    
    



