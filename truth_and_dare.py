import random
import time
import os
import sys

# Terminal Colors
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

# Player Blueprint
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_points(self, points):
        self.score += points

    def deduct_points(self, points):
        self.score -= points

# Main Game Engine
class TruthAndDareGame:
    def __init__(self):
        self.players = []
        self.original_truths = [
            "Who tells the most lies in this group?",
            "What is your biggest and most embarrassing secret?",
            "If you had to date someone in this room, who would it be?",
            "When was the last time you lied, and what was it about?",
            "Have you ever cheated in school or college? Did you get caught?"
        ]
        self.original_dares = [
            "Stand up and mimic any of your teachers in front of the class!",
            "Open your last WhatsApp chat and read the messages out loud to everyone.",
            "Look at {} and sing a romantic song!",
            "For the next 2 rounds, you must say 'Moo' at the end of every sentence.",
            "Touch the feet of {} and say 'You are my savior'!"
        ]
        self.truths = list(self.original_truths)
        self.dares = list(self.original_dares)

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def play_beep(self):
        sys.stdout.write('\a')
        sys.stdout.flush()

    def setup_players(self):
        self.clear_screen()
        print("=============================================")
        print("         🎯 PLAYER REGISTRATION 🎯           ")
        print("=============================================\n")
        
        while True:
            try:
                num = int(input("How many players are playing? (Min 2): "))
                if num >= 2:
                    break
                print("At least 2 players are required to play this game!")
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        for i in range(num):
            while True:
                name = input(f"Enter name for Player {i+1}: ").strip()
                if name:
                    self.players.append(Player(name))
                    break
                print("Player name cannot be empty!")

        print(f"\n All {len(self.players)} players registered successfully!")
        input("\nPress Enter to continue...")

    def start_game_loop(self):
        while True:
            self.clear_screen()
            
            print("\n=============================")
            print("--- 📊 CURRENT SCOREBOARD ---")
            for p in self.players:
                print(f"👤 {p.name}: {p.score} Points")
            print("=============================\n")

            current_player = random.choice(self.players)
            print(f"🎯 Target Locked! It is turn of: {current_player.name.upper()}!")

            choice = input("\nChoose (T)ruth or (D)are? [Or type 'quit' to exit]: ").lower().strip()

            if choice == 'quit':
                print("\nExiting the game loop...")
                break
            
            elif choice in ['t', 'truth']:
                if not self.truths:
                    self.truths = list(self.original_truths)
                task = random.choice(self.truths)
                self.truths.remove(task)
                print(f"\n🤔 TRUTH FOR {current_player.name.upper()}:\n👉 {task}")
                
            elif choice in ['d', 'dare']:
                if not self.dares:
                    self.dares = list(self.original_dares)
                task = random.choice(self.dares)
                self.dares.remove(task)
                
                if "{}" in task:
                    others = [p.name for p in self.players if p.name != current_player.name]
                    target = random.choice(others) if others else "a friend"
                    task = task.format(target)
                print(f"\n⚡ DARE FOR {current_player.name.upper()}:\n👉 {task}")
                
            else:
                print("\nInvalid input! Round skipped.")
                time.sleep(1.5)
                continue

            print("\n---------------------------------------------")
            status = input("Did you complete the task? (Y)es / (N)o: ").lower().strip()
            
            if status in ['y', 'yes']:
                print(f"🎉 Great job! +10 Points!")
                current_player.add_points(10)
            else:
                print(f"👎 Sneaky or scared! -5 Points!")
                current_player.deduct_points(5)

            input("\nPress Enter for the next round...")


if __name__ == "__main__":
    game = TruthAndDareGame()
    game.setup_players()
    game.start_game_loop()