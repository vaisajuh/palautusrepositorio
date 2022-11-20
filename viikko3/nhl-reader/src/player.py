class Player:
    def __init__(self, player):
        self.name = player["name"]
        self.nationality = player["nationality"]
        self.assists = player["assists"]
        self.goals = player["penalties"]
        self.penalties = player["team"]
        self.team = player["team"]

    def __str__(self):
        return f'{self.name} team {self.team} goals {self.goals} assists {self.assists}'
