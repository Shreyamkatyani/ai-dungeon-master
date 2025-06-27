import random

def resolve_event(user_input, world, player):
    if "fight" in user_input:
        outcome = random.choice(["win", "lose"])
        return f"You engage in battle and you {outcome} the fight!"
    elif "explore" in user_input:
        discovered = random.choice(["a hidden chest", "a secret passage", "an old scroll"])
        return f"You explore the {world.current_location} and find {discovered}."
    return "Nothing happens."
