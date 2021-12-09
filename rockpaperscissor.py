import random

options = ["snake","weasel","tiger"]
pc = random.choice(options)

print('Raghav Soni A2305218217 7CSE-4X')
while True:
    user = input("\nPick either Snake, Weasel or Tiger: ")

    print('PC chose: ', pc)
    print('User chose: ', user)

    if user == 'snake':
        if pc == 'snake':
            print('Tie Game')
        elif pc == 'weasel':
            print('PC Wins')
        else:
            print ('User Wins')

    if user == 'weasel':
        if pc == 'snake':
            print ('User Wins')
        elif pc == 'weasel':
            print ('Tie Game')
        else:
            print ('PC Wins')

    if user == 'tiger':
        if pc == 'snake':
            print ('PC Wins')
        elif pc == 'weasel':
            print ('User Wins')
        else:
            print ('Tie Game')

    if input('\nDo You Want To Continue? ') not in ['y','Y']:
        break
