time = input('enter Number of players:')
players = input('enter players with number play, Example:5 2 1 0 3, :')
players = players.split()
players = list(map(int, players))
lst = []

for i in players:
    if i <= 2:
        lst.append(i)
                
print(int(len(lst)/3))

