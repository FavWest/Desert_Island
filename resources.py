class Resource:
    def __init__(self, name, food, rate, replenish, max_food=False):
        self.name=name
        self.food=food
        self.rate=rate
        self.replenish=replenish
        if not max_food:
            self.max_food=self.food
    def gather(self, main):
        if self.food>=self.rate:
            self.food-=self.rate
            main.supplies+=self.rate
        if self.food < self.rate:
            main.supplies+=self.food
            self.food=0

class Person:
    def __init__(self):
        self.supplies=0
        self.leftovers=0
        self.hunger=0
#TEST CODE
        
main=Person()

def end_Day(main):
    if main.supplies <2000:
        eaten=main.supplies
        main.hunger+=2000-main.supplies
        main.supplies=0
    else:
        eaten=2000
        main.supplies-=2000
    if main.hunger > 0:
        if main.supplies >= 200 and main.hunger >=200:
            eaten+=200
            main.supplies-=200
            main.hunger-=200
        elif main.supplies < 200 and main.hunger >= 200:
            eaten+=main.supplies
            main.hunger-=main.supplies
            main.supplies=0
        elif main.supplies > main.hunger:
            eaten+=main.hunger
            main.supplies-=main.hunger
            main.hunger=0
        else:
            eaten+=main.supplies
            main.hunger-=main.supplies
            main.supplies=0
    if main.leftovers > eaten:
        main.leftovers-=eaten
        main.supplies-=main.leftovers
        print(main.leftovers, 'food went bad.')
    main.leftovers=main.supplies

def replenish(resource_list):
    for resource in resource_list:
        resource.food+=resource.replenish
        if resource.food>resource.max_food:
            resource.food=resource.max_food

def list(resource_list):
    print('')
    for resource in resource_list:
        print(resource.name)
        print('Available food:', resource.food)
        print('Harvest rate:', resource.rate, 'per hour')
        print('Replenish rate:', resource.replenish, 'per day\n')

            
    
    
