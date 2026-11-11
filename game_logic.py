import random
from user_interface import get_round, get_name ,display_game_results , display_statistics ,display_game_history ,show_new_game , show_menu
from data_management import load_game_history, save_game


def roll_dice():
    return random.randint(1,6)

def play_round():
    player_num = roll_dice()
    computer_num = roll_dice()
    winner = calculate_winner(player_num,computer_num)
    return {"round": None, "player_dice": player_num,"computer_dice": computer_num, "winner": winner}

def calculate_winner(player,computer):
    if player > computer:
        return "player"
    elif computer > player:
        return "computer"
    return "draw"

def show_round(result:dict,name):
    print(f'''
---------- ROUND {result["round"]} ----------

{name}:  🎲 {result["player_dice"]}
computer: 🎲 {result["computer_dice"]}''')
    if result["winner"] != "draw":
        print(f"{result["winner"]} wins this round!")
    else:
        print("darw!!")

def calculate_score(results:list):
    player_score = 0
    compter_score = 0
    for result in results:
        if result["winner"] == "draw":
            continue
        elif result["winner"] == "computer":
            compter_score += 1
        else:
            player_score += 1
    return player_score,compter_score

def start_game():
    player = get_name()
    rounds = get_round()
    count = 0
    show_new_game(player,rounds)
    results = []
    while rounds != count:
        count += 1
        roll = play_round()
        roll["round"] = count
        if roll["winner"] == "player":
            roll["winner"] = player
        results.append(roll)
        show_round(roll,player)
    player_score , computer_score = calculate_score(results)
    winner = calculate_winner(player_score,computer_score)
    if winner == "player":
        winner = player
    game = {"player_name": player, "rounds": count,"player_score": player_score,"computer_score": computer_score, "winner": winner,"results":results}
    display_game_results(game)
    data = load_game_history()
    data.append(game)
    save = save_game(data)
    if save:
        print("Game saved successfully!")

def run():
    user_choice = None
    while user_choice != "4":
        show_menu()
        user_choice = input("Choose an option:\n")
        match user_choice:
            case "1":
                start_game()
            case "2":
                data = load_game_history()
                if data:
                    display_game_history(data)
                else:
                    print("There is no game history yet.")
            case "3":
                data = load_game_history()
                if data:
                    display_statistics(data)
                else:
                    print("There is no game history yet.")
            case _:
                    print("invalid choice enetr num (1-4)")

