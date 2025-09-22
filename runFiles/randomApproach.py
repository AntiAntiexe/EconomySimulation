import random
'''
exclude = []
for i in range(10):
    household = random.choice([j for j in range(0,10 - 1) if j not in exclude])
    exclude.append(household)
    print(household)
    


'''

nhouseholdsList = list(range(0,10-1))

for i in range(10):
    randHouse = random.choice(nhouseholdsList)
    print(randHouse)
    nhouseholdsList.remove(randHouse)
    print('---')
    
def randomHousehold(nhouseholds, exclude):
    
    