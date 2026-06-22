import random
import time
import os
import sys

# Terminal Colors for a Premium UI/UX
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

# Player Blueprint (OOPs Concept)
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_points(self, points):
        self.score += points

    def deduct_points(self, points):
        self.score -= points

# Main Game Engine (OOPs Concept)
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

    # Hardware audio trigger (\a triggers the motherboard beep speaker)
    def play_beep(self):
        sys.stdout.write('\a')
        sys.stdout.flush()

    # Big ASCII Header text at startup
    def show_ascii_art(self):
        art = f"""{Colors.CYAN}
  _____                _     _        ___    ____                    
 |_   _| __ _   _  _ _| |__  | |__    ( _ )  |  _ \\   __ _  _ __  ___ 
   | |  '__/ _` | | | | __| | '_ \\   / _ \\  | | | | / _` || '__|/ _ \\
   | | |  | (_| | |_| | |_  | | | | | (_) | | |_| || (_| || |  |  __/
   |_|___\\__,_|\\__,_|\\__| |_| |_|  \\___/  |____/  \\__,_||_|   \\___|
        {Colors.ENDC}"""
        print(art)

    # Task 2: Player Registration Logic
    def setup_players(self):
        self.clear_screen()
        self.show_ascii_art()
        
        while True:
            try:
                num = int(input(f"{Colors.BOLD}How many players are playing? (Min 2): {Colors.ENDC}"))
                if num >= 2:
                    break
                print(f"{Colors.FAIL}At least 2 players are required to play this game!{Colors.ENDC}")
            except ValueError:
                print(f"{Colors.FAIL}Invalid input! Please enter a valid number.{Colors.ENDC}")

        for i in range(num):
            while True:
                name = input(f"Enter name for Player {i+1}: ").strip()
                if name:
                    self.players.append(Player(name))
                    break
                print(f"{Colors.FAIL}Player name cannot be empty!{Colors.ENDC}")

        print(f"\n{Colors.GREEN}All {len(self.players)} players registered successfully!{Colors.ENDC}")
        input(f"\nPress {Colors.BOLD}Enter{Colors.ENDC} to continue...")

    # Suspense animation logic
    def spin_bottle(self):
        print(f"{Colors.BLUE}🍾 Spinning the bottle...{Colors.ENDC}")
        for _ in range(4):
            time.sleep(0.5)
            print(f"{Colors.BLUE}.{Colors.ENDC}", end="", flush=True)
            self.play_beep()
        print("\n")

    # Task 3: Main Game Loop
    def start_game_loop(self):
        while True:
            self.clear_screen()
            
            # Colored Scoreboard
            print(f"\n{Colors.BOLD}--- 📊 CURRENT SCOREBOARD ---{Colors.ENDC}")
            for p in self.players:
                print(f"👤 {p.name}: {Colors.WARNING}{p.score}{Colors.ENDC} Points")
            print("-----------------------------\n")

            self.spin_bottle()

            current_player = random.choice(self.players)
            self.play_beep()
            print(f"🎯 Target Locked! It is turn of: {Colors.BOLD}{Colors.FAIL}{current_player.name.upper()}{Colors.ENDC}!")

            choice = input(f"\nChoose {Colors.CYAN}(T)ruth{Colors.ENDC} or {Colors.FAIL}(D)are{Colors.ENDC}? [Or type 'quit' to exit]: ").lower().strip()

            if choice == 'quit':
                break
            
            elif choice in ['t', 'truth']:
                if not self.truths:
                    self.truths = list(self.original_truths)
                task = random.choice(self.truths)
                self.truths.remove(task)
                print(f"\n{Colors.CYAN}🤔 TRUTH FOR {current_player.name.upper()}:{Colors.ENDC}\n👉 {Colors.BOLD}{task}{Colors.ENDC}")
                
            elif choice in ['d', 'dare']:
                if not self.dares:
                    self.dares = list(self.original_dares)
                task = random.choice(self.dares)
                self.dares.remove(task)
                
                if "{}" in task:
                    others = [p.name for p in self.players if p.name != current_player.name]
                    target = random.choice(others) if others else "a friend"
                    task = task.format(target)
                print(f"\n{Colors.FAIL}⚡ DARE FOR {current_player.name.upper()}:{Colors.ENDC}\n👉 {Colors.BOLD}{Colors.WARNING}{task}{Colors.ENDC}")
                
            else:
                print(f"{Colors.WARNING}\nInvalid input! Round skipped.{Colors.ENDC}")
                time.sleep(1.5)
                continue

            print("\n---------------------------------------------")
            status = input("Did you complete the task? (Y)es / (N)o: ").lower().strip()
            
            if status in ['y', 'yes']:
                print(f"🎉 {Colors.GREEN}+10 Points!{Colors.ENDC}")
                current_player.add_points(10)
            else:
                print(f"👎 {Colors.FAIL}-5 Points! Sneaky!{Colors.ENDC}")
                current_player.deduct_points(5)

            input(f"\nPress {Colors.BOLD}Enter{Colors.ENDC} for the next round...")

        self.end_game()

    # End-game summary and winner calculation
    def end_game(self):
        self.clear_screen()
        print(f"{Colors.HEADER}============================================={Colors.ENDC}")
        print(f"{Colors.HEADER}               🎮 GAME OVER 🎮                {Colors.ENDC}")
        print(f"{Colors.HEADER}=============================================\n")
        
        winner = max(self.players, key=lambda p: p.score)
        print(f"🏆 The ultimate player is: {Colors.GREEN}{Colors.BOLD}{winner.name.upper()}{Colors.ENDC} ({winner.score} Points)!\n")
        print("Thanks for playing! Goodbye.")

if __name__ == "__main__":
    game = TruthAndDareGame()
    game.setup_players()
    game.start_game_loop()