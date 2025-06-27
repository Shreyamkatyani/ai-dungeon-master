class Player:
    def __init__(self, name):
        self.name = name
        self.stats = {'strength': 10, 'intelligence': 10, 'charisma': 10}
        self.inventory = ['sword', 'healing potion']

    def status(self):
        return f"{self.name} | Stats: {self.stats} | Inventory: {self.inventory}"
