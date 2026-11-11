import json

def load_game_history():
    try:
        with open("game_history.json", "r") as file:
            content = json.load(file)
            return content
    except Exception:
        return []

def save_game(game):
    try:
        with open("game_history.json", "w", encoding="utf-8") as file:
            json.dump(game, file, indent=2, ensure_ascii=False)
            return True
    except Exception as e:
        print(f"error: {e}")
        return False

