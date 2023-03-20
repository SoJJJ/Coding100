import numpy as np

a = np.array([['-','_','_'],
             ['_','_','_'],
             ['_','_','_']])
a2 = a.flatten()

game_is_on = True

def change(player, number):
    a2[number] = player
    a3 = a2.reshape((3, 3))
    print(a3)


while game_is_on:
    player = input('Are you player 1 or 2: ')
    number = int(input('which to change: '))
    change(player, number)
    if (a2[0] == a2[1] == a2[2] and a2[0] !='_') or (a2[3] == a2[4] == a2[5] and a2[3] !='_') or (a2[6] == a2[7] == a2[8] and a2[6] !='_') or \
        (a2[0] == a2[3] == a2[6] and a2[0] !='_' ) or (a2[1] == a2[4] == a2[7] and a2[1] !='_') or (a2[2] == a2[5] == a2[8] and a2[2] !='_') or \
        (a2[0] == a2[4] == a2[8] and a2[0] !='_') or (a2[2] == a2[4] == a2[5] and a2[2] !='_'):
        print(f"You(player {player}) win!")
        break
    else:
        continue




