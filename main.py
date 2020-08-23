#Create a text-based game about resource gathering and management

#start with one character

import resources as re
import random

resource_list=[]
tools={'net':False}
palms=re.Resource('Cluster of Palm Trees', 10000, 2000, 100)
cove=re.Resource('Nearby Cove', 500, 100, 500)
bananas=re.Resource('Banana Tree', 200, 200, 20)

main=re.Person()

print("You are the sole survivor of a plane crash.")
print("You swam to shore and found yourself on an uninhabited, tropical island.")
print("Waves crash on the white sand of the beach. Seagulls cry.")
print("The sun is hot, but there is shade in the trees beyond the beach.")

action=''
skip=False

while action!='explore':
    action=input("Type 'explore' to go up to the trees and look around.\n")
    if action=='skip':
        skip=True
        break

action=''

print('''You walk up to the shady trees. The air smells of salt and warm vegetation.
Exploring further, you are able to find a spring of fresh water that seems
safe to drink.
You gather some branches and vines, and use them to build yourself a
shelter a little inland from the beach. The island seems to be several miles
wide, but you are too tired to explore it all today. You drink some more water,
lie down, and soon fall asleep.''')

if not skip:
    any_key=input('\nPress enter to continue\n')

print('''DAY 1:
You wake up intensely hungry. You must find food soon.''')
day=1
if not skip:
    action=input('''Type 'explore' to search for food. It is 6:00 AM.
    Exploring will take 2 hours.\n''')

    while action!='explore':
        action=input("Type 'explore' to search for food.")

print('''You explore the nearby beach and trees. You find two places that
look promising. There is a cluster of palm trees with coconuts, and there
is little cove where you might be able to catch some fish. It would be easy
to get the coconuts-- all you need to do is pick up a large stick and knock
them down. To catch fish, you would need to make yourself a net. The net would
take about 4 hours to make, but you could probably reuse it many times.''')

resource_list.append(palms)
resource_list.append(cove)

if not skip:
    action=input("Type 'list' to see your options\n")

    if action=='list':
        print('''Cluster of Palm Trees (coconuts):
    Food: 10,000   Gather rate: 2,000/hr
    Replenish rate: Unknown, but probably slow- you have to wait for more to grow
    Type 'gather' to collect coconuts.

    Nearby Cove (fish):
    Food: 500   Gather rate: unknown
    Replenish rate: Unknown, but probably fast- connected to the sea
    Type 'fish' to start weaving a net. NOTE: THIS WILL TAKE 4 hours.
    ''')

    print('It is now 8:00 AM.')

    action=input("Type 'main' to see information about yourself.\n")

    if action=='main':
          print('Supplies', main.supplies, 'Hunger', main.hunger)

hours=0

action=input("What would you like to do? Type 'gather' or 'fish'. ")

if action=='gather' or action=='gather coconuts' or action=='coconuts':
    print('''You spend an hour gathering coconuts from the trees.
You have enough food for today. You could pick more for tomorrow,
but you're not sure how well it will keep.
+2,000 food
It is 9:00 AM.
''')
    main.supplies+=2000
    palms.food-=2000
    hours=1

if action=='fish':
    print('''You gather vines and tie them together, creating a net.
At about noon, the net is finished, and you cast it into the cove.
You are able to catch some fish, but they are small.
+100 food
It is 1:00 PM''')
    main.supplies+=100
    hours=5
    tools['net']=True

action=''
days=0

while True:
    days+=1
    if days!=1:
        print('')
        print('DAY', days)
    while hours < 12:
        #Display available actions
        if len(resource_list) < 3:
            action=input("Pick an action. Fish, gather, explore, list, main, done\n")
        else:
            add=''
            if bananas in resource_list:
                add+='bananas,'
            action=input('Pick an action. Fish, gather, explore, '+ add + ' list, main, done. ')
        #Resolve hunger penalties
        if main.hunger > 6000  and action != 'list' and action!= 'main' and action!='done':
            if main.hunger < 10000:
                print("You are hungry and it slows you down.")
                hours+=1
            if main.hunger >= 10000:
                print("You are very hungry and it slows you down a lot.")
                hours+=2
            print((12-hours), 'hours remaining in the day')
        #Resolve chosen action
        if action=='fish':
            if not tools['net']:
                choice=input("You need to make a net first. It will take 4 hours. Proceed? y/n ")
                if choice=='y':
                    print("You gather vines and tie them together, creating a net.")
                    hours+=4
                    tools['net']==True
            temp=main.supplies
            cove.gather(main)
            catch=main.supplies-temp
            hours+=1
            print("You went fishing in the nearby cove. +" + str(catch), 'food')
            if main.hunger>0:
                need='2,200'
            else:
                need='2,000'
            print("You have", main.supplies, "food. You will need about", need, "today.")
            print((12-hours), 'hours remaining in the day')
        elif action=='gather' or action=='gather coconuts' or action=='coconuts':
            temp=main.supplies
            palms.gather(main)
            harvest=main.supplies-temp
            hours+=1
            print("You gathered coconuts from the cluster of palm trees. +" + str(harvest), 'food')
            if main.hunger>0:
                need='2,200'
            else:
                need='2,000'
            print("You have", main.supplies, "food. You will need about", need, "today.")
            print((12-hours), 'hours remaining in the day')
        elif action=='gather bananas' or action=='bananas':
            if bananas in resource_list:
                temp=main.supplies
                bananas.gather(main)
                harvest=main.supplies-temp
                hours+=1
                print("You picked all the ripe bananas. +" +str(harvest), 'food')
                if main.hunger>0:
                    need='2,200'
                else:
                    need='2,000'
                print("You have", main.supplies, "food. You will need about", need, "today.")
                print((12-hours), 'hours remaining in the day')
            else:
                print("You haven't found any bananas yet.")
        elif action=='explore':
            luck=random.randint(1,3)
            if luck==3 and bananas not in resource_list:
                print("You found a banana tree!")
                print("Type 'bananas' or 'gather bananas' to pick bananas.")
                resource_list.append(bananas)
            else:
                print("You explore the island, but don't find any more food.")
            hours+=1
            print((12-hours), 'hours remaining in the day')
        elif action=='list':
            re.list(resource_list)
        elif action=='main':
            print('Supplies', main.supplies, 'Hunger', main.hunger)
        elif action=='done':
            break

    print("Nightfall. Time to rest.")
    re.end_Day(main)
    re.replenish(resource_list)
    any_key=input('\nPress enter to continue\n')
    print("You wake up the next morning.")
    if main.hunger >= 48000:
        print("Warning: You must eat something tomorrow!")
    if main.hunger > 50000:
        print("Game over.")
        break
    elif main.hunger > 0:
        print("You feel hungry ("+str(main.hunger)+"/50000).")
    else:
        print("You have a good breakfast and feel satisfied.")
    if main.supplies >0:
        print("You have", main.supplies, "supplies.")
    hours=0
