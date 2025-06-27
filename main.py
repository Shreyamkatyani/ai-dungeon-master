from game_engine.story_generator import generate_story_response
from game_engine.character import Player
from game_engine.world_state import GameWorld
from game_engine.dialogue import handle_dialogue
from game_engine.events import resolve_event
import json
import os
import random

def save_game(player, world):
    with open("savegame.json", "w") as f:
        json.dump({
            "player": {
                "name": player.name,
                "stats": player.stats,
                "inventory": player.inventory
            },
            "world": {
                "current_location": world.current_location
            }
        }, f)
        print("Game saved successfully.")

def load_game():
    if os.path.exists("savegame.json"):
        with open("savegame.json", "r") as f:
            data = json.load(f)
            player = Player(data['player']['name'])
            player.stats = data['player']['stats']
            player.inventory = data['player']['inventory']
            world = GameWorld()
            world.current_location = data['world']['current_location']
            print("Game loaded successfully.")
            return player, world
    return None, None

def generate_procedural_quest():
    quest_giver = random.choice(["a mysterious traveler", "a village elder", "a talking cat"])
    objective = random.choice(["retrieve the lost artifact", "slay the beast in the woods", "deliver a message to the castle"])
    reward = random.choice(["a bag of gold", "a magic sword", "ancient knowledge"])
    return f"You meet {quest_giver} who asks you to {objective}. If you succeed, you will earn {reward}."

def main():
    print("Welcome to AI Dungeon Master! Type 'exit' to quit.")
    print("Type 'save' to save, 'load' to load your game, 'quest' for a random quest.")

    player, world = load_game()
    if not player or not world:
        player = Player(name="Hero")
        world = GameWorld()

    while True:
        user_input = input("\n> Your action: ")
        if user_input.lower() == 'exit':
            print("Thanks for playing!")
            break
        elif user_input.lower() == 'save':
            save_game(player, world)
            continue
        elif user_input.lower() == 'load':
            player, world = load_game()
            continue
        elif user_input.lower() == 'quest':
            print(f"\n{generate_procedural_quest()}")
            continue

        if user_input.startswith("talk to"):
            response = handle_dialogue(user_input, world, player)
        elif user_input.startswith("fight") or user_input.startswith("explore"):
            response = resolve_event(user_input, world, player)
        else:
            response = generate_story_response(user_input, world, player)

        print(f"\n{response}")

if __name__ == "__main__":
    main()
