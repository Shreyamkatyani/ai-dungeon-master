from game_engine.story_generator import generate_story_response
from game_engine.character import Player
from game_engine.world_state import GameWorld
from game_engine.dialogue import handle_dialogue
from game_engine.events import resolve_event


def main():
    print("Welcome to AI Dungeon Master! Type 'exit' to quit.")
    player = Player(name="Hero")
    world = GameWorld()

    while True:
        user_input = input("\n> Your action: ")
        if user_input.lower() == 'exit':
            print("Thanks for playing!")
            break

        if user_input.startswith("talk to"):
            response = handle_dialogue(user_input, world, player)
        elif user_input.startswith("fight") or user_input.startswith("explore"):
            response = resolve_event(user_input, world, player)
        else:
            response = generate_story_response(user_input, world, player)

        print(f"\n{response}")


if __name__ == "__main__":
    main()
