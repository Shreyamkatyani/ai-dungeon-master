# AI Dungeon Master

An interactive text-based RPG powered by GPT acting as a Dungeon Master.

## Features
- Dynamic story generation
- Character tracking
- World state awareness
- Dialogue and event resolution
- ✅ Save and load your game progress
- ✅ Procedural quest generation!

## Setup
1. Clone the repo
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up `.env` file:
   ```bash
   echo "OPENAI_API_KEY=your_api_key_here" > .env
   ```
4. Run the game:
   ```bash
   python main.py
   ```

## Sample Interaction
```
> Your action: Go to the forest
>> You arrive at a dark forest full of whispers and the rustling of leaves...

> Your action: Talk to old man
>> You approach Old Man. They say: 'Greetings, Hero. Beware the forest!'

> Your action: save
>> Game saved successfully.

> Your action: load
>> Game loaded successfully.

> Your action: quest
>> You meet a talking cat who asks you to deliver a message to the castle. If you succeed, you will earn a magic sword.
```