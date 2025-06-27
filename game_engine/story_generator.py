import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_story_response(user_input, world, player):
    prompt = f"""
    You are the Dungeon Master of a fantasy RPG.
    World: {world.summary()}
    Player: {player.status()}
    Action: {user_input}
    Continue the story:
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a Dungeon Master in a medieval fantasy RPG."},
            {"role": "user", "content": prompt},
        ]
    )
    return response.choices[0].message['content'].strip()
