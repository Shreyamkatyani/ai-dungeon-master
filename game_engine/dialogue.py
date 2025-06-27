def handle_dialogue(user_input, world, player):
    npc_name = user_input.replace("talk to", "").strip().title()
    return f"You approach {npc_name}. They say: 'Greetings, {player.name}. Beware the {world.current_location}!' "

