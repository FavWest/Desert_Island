import resources as re

resource_list=[]
main=re.Person()

palms=re.Resource('Cluster of Palm Trees', 10000, 2000, 100)
resource_list.append(palms)
cove=re.Resource('Nearby Cove', 500, 100, 500)
resource_list.append(cove)

action=''
hours=0
days=0

while True:
    days+=1
    print('Day', days)
    while hours < 12:
        action=input("Pick an action. Fish, gather, list, main, done\n")
        if action=='fish':
            temp=main.supplies
            cove.gather(main)
            catch=main.supplies-temp
            hours+=1
            print("You went fishing in the nearby cove. +" + str(catch), 'food')
            print((12-hours), 'hours remaining in the day')
        elif action=='gather':
            temp=main.supplies
            palms.gather(main)
            harvest=main.supplies-temp
            hours+=1
            print("You gathered coconuts from the cluster of palm trees. +" + str(harvest), 'food')
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

