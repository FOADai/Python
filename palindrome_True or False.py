word = input()
word = word.lower()
vice_versa = word[::-1]

if word == vice_versa:
    print('palindrome')
else:
    print('not palindrome')