class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict["nationality"]
        self.assists = dict["assists"]
        self.goals = dict["goals"]
        self.points = self.assists + self.goals
        self.team = dict["team"]
        self.games = dict["games"]

    
    def __str__(self):
        return f"{self.name}"
