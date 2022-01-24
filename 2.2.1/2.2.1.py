class FootballTeam:
    def __init__(self, won, draw, lost, goals_scored, missed_goals):  # конструктор
        self.won = won
        self.draw = draw
        self.lost = lost
        self.goals_scored = goals_scored
        self.missed_goals = missed_goals

    def match_result(self):
        print(self.goals_scored, "-", self.missed_goals)

    def club_result(self):
        print(self.won, "-", self.lost)

    def match_difference(self):
        i = self.goals_scored - self.missed_goals
        print(i)

class FootballTeam2(FootballTeam):

    def __init__(self, won, draw, lost, goals_scored, missed_goals):
        super().__init__(won, draw, lost, goals_scored, missed_goals)
        self.won = won
        self.draw = draw
        self.lost = lost
        self.goals_scored = goals_scored
        self.missed_goals = missed_goals

    def total(self):
        print(self.won + self.lost + self.draw)


if __name__ == '__main__':
    navi = FootballTeam2(15, 6, 3, 25, 17)
    navi.match_result()
    navi.club_result()
    navi.match_difference()
    navi.total()

