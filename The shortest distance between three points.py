number = input()
number = number.split()
number = list(map(int, number))
number.sort()
num1 = number[2] - number[1]
num2 = number[1] - number[0]
print(num1+num2)