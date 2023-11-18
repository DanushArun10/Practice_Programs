runs = [('dhoni',51),('kholi',62),('dhoni',15),('rohit',105),('kholi',100),('dhoni',45)]
d = {}
for player,run in runs:
    if player not in d.keys():
        d[player] = []
    d[player].append(run)
print(d)
print(max(d['dhoni']))

for player in d.keys():
    print(player,max(d[player]))
for player in d.keys():
    print(player,min(d[player]))
for player in d.keys():
    print(player,(d[player]))


d.update({'kholi':105}) #d['kholi'] = 100