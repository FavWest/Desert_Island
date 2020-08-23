hours=0
net=False

while hours<12:
    action=input("Gather or fish? ")
    if action=='gather':
        print("gathered")
        hours+=1
    if action=='fish':
        if not net:
            choice=input("No net. Make net? y/n ")
            if choice=='y':
                print("Made net. Ready to fish!")
                net=True
            else:
                print("No net.")
        if net:
            print('fished')
            hours+=1
