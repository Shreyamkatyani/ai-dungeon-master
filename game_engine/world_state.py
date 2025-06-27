import json

class GameWorld:
    def __init__(self):
        self.locations = {
            'village': "A peaceful village with cobblestone streets.",
            'forest': "A dark forest full of whispers.",
            'castle': "An ancient, haunted castle."
        }
        self.current_location = 'village'

    def summary(self):
        return f"Location: {self.current_location} - {self.locations[self.current_location]}"
