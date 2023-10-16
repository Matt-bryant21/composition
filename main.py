import rpg

aragorn = rpg.Character('aragorn', 'human', )
galadriel = rpg.Character('galadriel', 'elf')
frodo = rpg.Character('frodo', 'Hobbit')

frodo.set_currency(10 ,5 , 0)

chest = rpg.Chest(['longsword', 'iron helm'], 2, 25, 50)

print(chest.inv.__dict__)                      
# print(aragorn.__dict__)
# print(galadriel.__dict__)
# print(frodo.__dict__)
                        
print(frodo.get_currency()[0])                  


