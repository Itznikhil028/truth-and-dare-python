import os

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_points(self, points):
        self.score += points

    def deduct_points(self, points):
        self.score -= points


class TruthAndDareGame:
    def __init__(self):
        self.players = []
        self.original_truths = [
            "Who tells the most lies in this group?",
            "What is your biggest and most embarrassing secret?",
            "If you had to date someone in this room, who would it be?"
        ]
        self.original_dares = [
            "Stand up and mimic any of your teachers in front of the class!",
            "Open your last WhatsApp chat and read the messages out loud to everyone."
        ]
        self.truths = list(self.original_truths)
        self.dares = list(self.original_dares)

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    game = TruthAndDareGame()
    print("Step 1 Complete! The game engine and player blueprints are ready.")