numbera = int ( input ('please enter three number? ') )
number_3 = ( numbera % 10 ) * 100
number_2 = ( ( numbera // 10)  % 10 ) * 10
number_1 = ( numbera // 100)
print ( (number_3 + number_2 + number_1 ) * 2 )
