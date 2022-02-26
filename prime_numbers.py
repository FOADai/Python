numberk = input('Enter your number: ')
numberk = int (numberk)
counter = 0
index = 1
while index <= numberk:
    if numberk % index == 0:
        counter = counter + 1
    index = index + 1    
    
    
if counter == 2:
    print('prime')
else:
    print('not prime')
        


