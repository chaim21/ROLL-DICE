def get_name():
    valid_name = False
    while not valid_name:
        user_input = input("enter your name:\n")
        if user_input.strip():
            return user_input
        else:
            print("cannot execept empty name")

def get_round():
    valid_num = False
    while not valid_num:
        try:
            user_input = int(input("enter number of rotations (1-10):\n"))
            if user_input > 10 or user_input < 1:
                print("please enter num between (1-10)!")
                continue
            return user_input
        except ValueError:
            print("please enter num between (1-10)!")

def display_game_results(game:dict):
    print(f'''
================================
          GAME OVER
================================
{game["player_name"]}: {game["player_score"]} points
Computer: {game["computer_score"]} points

WINNER: {game["winner"]}
''')

def display_statistics(history:list):
    games = len(history)
    player_win = len([game["winner"] for game in history if game["winner"] not in ["computer","draw"]])
    computer_win = len([game["winner"] for game in history if game["winner"] == "computer"])
    draw = len([game["winner"] for game in history if game["winner"] == "draw"])
    percent = player_win / games * 100
    print(F"GAMES: {games} ")
    print(F"PLAYERS WIN: {player_win}")
    print(F"COMPUTER WIN: {computer_win}")
    print(f"DRAWS: {draw}")
    print(f"Players' Win Percentage: {percent}")

def display_game_history(history:list):
    print('''
================================
          GAME HISTORY
================================''')
    for i,game in enumerate(history,start=1):
        print(f'''
      ------ game {i} ------
      name: {game["player_name"]} | rounds {game["rounds"]}
player score: {game["player_score"]} | computer score: {game["computer_score"]}
      -- winner: {game["winner"]} --''')

def show_new_game(player,rounds):
    print(f'''
================================
            NEW GAME
================================
    
player name: {player}
Number of rounds: {rounds}''')
    
def show_menu():
    print('''
================================
          ROLL DICE
================================

1. Start New Game
2. View Game History
3. View Statistics
4. Exit''')