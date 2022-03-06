import random
guess = random.randint (1, 99)
guess = int(guess)
print (guess)
Answer = input ('your idea? ')
a = 1
c = 99 
#your answer 'True', ' large' , ' Small'
while Answer != 'True':
    if Answer == 'large':
        c = guess
    elif Answer == 'Small':
        a = guess    
    import random
    guess = random.randint(a, c)
    guess = int(guess)
    print (guess)
    Answer = input ('your idea? ')
    
        
print ('I am a smart computer!!!!!!')



