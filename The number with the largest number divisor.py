def larger_divisor(number):
    time_a = 1
    max_e = 0
    pre_num = 0
    while time_a <= 20:
        index = 1
        Divisor = 0
        while number>=index:
            if number%index==0:
                Divisor = Divisor + 1
            index = index + 1
            if max_e == Divisor:
                if pre_num < number:
                    pre_num = number
            if max_e<Divisor:
                max_e = Divisor
                pre_num = number
        time_a = time_a + 1
        if time_a > 20:
            print('larger number is',pre_num,'with divisor',max_e)
        if time_a <= 20:
            number = int (input('please enter your number: '))

number = int (input('please enter your number: '))
larger_divisor(number)

 
