from player import Player
import requests

class PlayerReader:
    def __init__(self, season):
        self.season = season
        self.url = f"https://studies.cs.helsinki.fi/nhlstats/{self.season}/players"
        self.response = requests.get(self.url).json()
    
    def get_players(self):
        players = []
        for player_dict in self.response:
            player = Player(player_dict)
            players.append(player)
        return players


class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        self.nationality = nationality
        national_players = filter(lambda player: player.nationality == self.nationality, self.players)
        
        return sorted(national_players, key=lambda player: player.points, reverse = True)
           
   
    
        
        