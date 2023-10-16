class Character:
    def __init__(self, name, race):
        self.name = name
        self.race = race
        self.gold = 0
        self.silver = 0
        self.copper = 0
        self.inv = Inventory([], 0, 0, 0)
    

    
class Chest: 
    def __init__(self, items, gold, silver, copper):
       self.inv =  Inventory(items, gold, silver, copper)

class Inventory:
    def __init__(self, items, gold, silver, copper):
        self.items = items
        self.set_currency(gold, silver, copper)


    def transfer(self, from_inv, to_inv):
        #add all the items from_inv to to_inv
        to_inv.items.extend(from_inv.items) 
        #delete all the items from from_inv
        from_inv.items = []

    
     #setter
    def set_currency(self, gold, silver, copper): 
        self.copper = gold * 1000 + silver * 100 + copper

    #getter
    def get_currency(self):
        gold = self.copper // 10000
        silver = (self.copper % 1000) // 100
        copper = self.copper % 100
        #return gold silver copper
        return gold, silver, copper
    