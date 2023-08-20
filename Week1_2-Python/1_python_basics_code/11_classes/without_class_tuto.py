import datetime
virat = {
    'first_name': 'virat',
    'last_name': 'kohli',
    'birth_year': 1988,
    'scores': []
}


virat['scores'].append(80)
virat['scores'].append(100)
virat['scores'].append(0)


def get_average_score(player):
    return sum(player['scores'])/len(player['scores'])


def get_age(player):
    now = datetime.datetime.now()
    return now.year - player['birth_year']


print(get_average_score(virat))
print(get_age(virat))

david = {
    'first_name': 'david',
    'last_name': 'warner',
    'birth_year': 1986,
    'scores': []
}

david['scores'].append(35)
david['scores'].append(120)
david['scores'].append(12)

print(get_average_score(david))
print(get_age(david))


