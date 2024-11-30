class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.score_player_1 = 0
        self.score_player_2 = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.score_player_1 += 1
        else:
            self.score_player_2 += 1

    def same_points(self):
        return self.score_player_1 == self.score_player_2
    
    def different_points(self):
        return self.score_player_1 >= 4 or self.score_player_2 >= 4

    def score_when_same_points(self):
        score_names = {0: "Love-All", 1: "Fifteen-All", 2: "Thirty-All"}
        return score_names.get(self.score_player_1, "Deuce")

    def score_when_different_points(self):
        minus_result = self.score_player_1 - self.score_player_2
        if minus_result == 1:
            return "Advantage player1"
        elif minus_result == -1:
            return "Advantage player2"
        elif minus_result >= 2:
            return "Win for player1"
        else:
            return "Win for player2"

    def score_name(self, score):
        score_names = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}
        return score_names.get(score, "")

    def score_during_normal_play(self):
        return f"{self.score_name(self.score_player_1)}-{self.score_name(self.score_player_2)}"

    def get_score(self):
        if self.same_points():
            return self.score_when_same_points()
        elif self.different_points():
            return self.score_when_different_points()
        else:
            return self.score_during_normal_play()
