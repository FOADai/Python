point = int(input('please number 1 or 3 or 0: '))
index = 1
succ= 0
sume = 0

while index <= 30:
    if point == 3:
        succ = succ + 1
    sume = sume + point    
    index = index + 1
    if index <= 30:
        point = int(input('please enter number 1 or 3 or 0: '))
    
print(sume,succ)

