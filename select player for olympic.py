time = input()
players = input()
players = players.split()
players = list(map(int, players))
lst = []

for i in players:
    if i <= 2:
        lst.append(i)
                
print(int(len(lst)/3))

