import datetime

class CricketPlayer:
    def __init__(self, fname, lname, birth, team):
        self.first_name = fname
        self.last_name = lname
        self.birth_year = birth
        self.team = team
        self.score = []

    def get_age(self):
        now = datetime.datetime.now()
        return now.year - self.birth_year

    def add_score(self, score):
        self.score.append(score)

    def get_average_score(self):
        return sum(self.score) / len(self.score)

    def __lt__(self, other):
        my_score = self.get_average_score()
        other_score = other.get_average_score()
        return my_score < other_score

    def __str__(self):
        return f'{self.first_name} {self.last_name}, the cricket player from {self.team} '

virat = CricketPlayer('Virat', 'Kohli', 1988, 'India')
virat.add_score(80)
virat.add_score(100)
virat.add_score(0)

print(virat.get_average_score())

david = CricketPlayer('David', 'Warner', 1986, 'Australia')
david.add_score(37)
david.add_score(23)
david.add_score(85)

print(david.get_average_score())

print(virat < david)

print(virat)
print(david)
