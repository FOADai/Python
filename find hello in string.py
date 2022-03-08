firststring = input()
to_find = 'hello'

def check_string(firststring, to_find):
    c = 0
    for i in firststring:
        if i == to_find[c]:
            c += 1
        if c == len(to_find):
            return "YES"
    return "NO"

print(check_string(firststring, to_find))