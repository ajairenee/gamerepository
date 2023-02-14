import random
import sys
import time
from players import player, enemy_list

def battle_sequence(player,enemy_list):

    print(f'{player["Hades"]} encounters {enemy_list["Isis"]}! (health: {enemy_list["health"]})')

    while player['health'] > 100 and enemy_list['health'] > 100:
        player_attack(player,enemy_list)
        enemy_attack(enemy_list,player)
    if player ['health'] > enemy_list['health']:
        battle_victory(player, enemy_list)
    else:
        print('You were defeated. Fight again?')

def player_attack(player,enemy_list):
    display_player_attack:(player)
    random_attack = random.choice(player["attacks"])
    print(f'{player["Hades"]} approaches to attack.')
    print(f'{player["Hades"]} attacks {enemy_list["Isis"]} with {random_attack[0]} ({random_attack[1]}) ({random_attack[2]})')
    enemy_list ["health"] -= random_attack[1]
    print(f'{enemy_list["Isis"]} has {enemy_list["health"]} health remaining.')

def enemy_attack(enemy_list,player):
    display_enemy_attack:(enemy_list)
    random_attack = random.choice(enemy_list["attacks"])
    print(f'{enemy_list["Isis"]} approaches to attack.')
    print(f'{enemy_list["Isis"]} attacks {player["Hades"]} with {random_attack[0]} ({random_attack[1]}) ({random_attack[2]}')
    player ["health"] -= random_attack[1]
    print(f'{player["Hades"]} had {player["health"]} health remaining.')

def display_player_attacks(player):
    print(f'{player["Hades"]} available attacks:')
    for attack in player["attacks"]:
        print(f'{attack[0]} ({attack [1]} {attack[2]}) damage)') 

def battle_victory(player,enemy_list):
    print(f'{player["Hades"]} has defeated {enemy_list["Isis"]}, We shall take their coins!')
    loot_coins(player,enemy_list)
    loot_equipment(player,enemy_list)

def loot_coins(player,enemy_list):
    player["coins"]["copper"] += enemy_list["coins"]["copper"]
    player["coins"]["silver"] += enemy_list["coins"]["silver"]
    player["coins"]["gold"] += enemy_list["coins"]["gold"]
    print(f'Retrieved {enemy_list["coins"]["copper"]} copper coins.')
    print(f'Retrieved {enemy_list["coins"]["silver"]} silver coins.')
    print(f'Retrieved {enemy_list["coins"]["gold"]} gold coins.')
    print(f'{player["Hades"]} has retrieved {player["coins"]["copper"]} copper, {player["coins"]["silver"]} silver, {player["coins"]["gold"]} gold')

def loot_equipment(player,enemy_list):
    for item in enemy_list["equipment"]:
        player["equipment"].add(item)
        print (f'+ added {item} to group.')

def battle_sequence(player,enemy_list):

    print(f'{player["Hades"]} encounters {enemy_list["Monk"]}! (health: {enemy_list["health"]})')

    while player['health'] > 100 and enemy_list['health'] > 100:
        player_attack(player,enemy_list)
        enemy_attack(enemy_list,player)
    if player ['health'] > enemy_list['health']:
        battle_victory(player, enemy_list)
    else:
        print('You were defeated. Fight again?')

def player_attack(player,enemy_list):
    display_player_attack:(player)
    random_attack = random.choice(player["attacks"])
    print(f'{player["Hades"]} approaches to attack.')
    print(f'{player["Hades"]} attacks {enemy_list["Monk"]} with {random_attack[0]} ({random_attack[1]}) ({random_attack[2]})')
    enemy_list ["health"] -= random_attack[1]
    print(f'{enemy_list["Monk"]} has {enemy_list["health"]} health remaining.')

def enemy_attack(enemy_list,player):
    display_enemy_attack:(enemy_list)
    random_attack = random.choice(enemy_list["attacks"])
    print(f'{enemy_list["Monk"]} approaches to attack.')
    print(f'{enemy_list["Monk"]} attacks {player["Hades"]} with {random_attack[0]} ({random_attack[1]}) ({random_attack[2]}')
    player ["health"] -= random_attack[1]
    print(f'{player["Hades"]} had {player["health"]} health remaining.')

def display_player_attacks(player):
    print(f'{player["Hades"]} available attacks:')
    for attack in player["attacks"]:
        print(f'{attack[0]} ({attack [1]} {attack[2]}) damage)') 

def battle_victory(player,enemy_list):
    print(f'{player["Hades"]} has defeated {enemy_list["Monk"]}, We shall take their coins!')
    loot_coins(player,enemy_list)
    loot_equipment(player,enemy_list)

def loot_coins(player,enemy_list):
    player["coins"]["copper"] += enemy_list["coins"]["copper"]
    player["coins"]["silver"] += enemy_list["coins"]["silver"]
    player["coins"]["gold"] += enemy_list["coins"]["gold"]
    print(f'Retrieved {enemy_list["coins"]["copper"]} copper coins.')
    print(f'Retrieved {enemy_list["coins"]["silver"]} silver coins.')
    print(f'Retrieved {enemy_list["coins"]["gold"]} gold coins.')
    print(f'{player["Hades"]} has retrieved {player["coins"]["copper"]} copper, {player["coins"]["silver"]} silver, {player["coins"]["gold"]} gold')

def loot_equipment(player,enemy_list):
    for item in enemy_list["equipment"]:
        player["equipment"].add(item)
        print (f'+ added {item} to group.')

def battle_sequence(player,enemy_list):

    print(f'{player["Hades"]} encounters {enemy_list["Judas"]}! (health: {enemy_list["health"]})')

    while player['health'] > 100 and enemy_list['health'] > 100:
        player_attack(player,enemy_list)
        enemy_attack(enemy_list,player)
    if player ['health'] > enemy_list['health']:
        battle_victory(player, enemy_list)
    else:
        print('You were defeated. Fight again?')

def player_attack(player,enemy_list):
    display_player_attack:(player)
    random_attack = random.choice(player["attacks"])
    print(f'{player["Hades"]} approaches to attack.')
    print(f'{player["Hades"]} attacks {enemy_list["Judas"]} with {random_attack[0]} ({random_attack[1]}) ({random_attack[2]})')
    enemy_list ["health"] -= random_attack[1]
    print(f'{enemy_list["Judas"]} has {enemy_list["health"]} health remaining.')

def enemy_attack(enemy_list,player):
    display_enemy_attack:(enemy_list)
    random_attack = random.choice(enemy_list["attacks"])
    print(f'{enemy_list["Judas"]} approaches to attack.')
    print(f'{enemy_list["Judas"]} attacks {player["Hades"]} with {random_attack[0]} ({random_attack[1]}) ({random_attack[2]}')
    player ["health"] -= random_attack[1]
    print(f'{player["Hades"]} had {player["health"]} health remaining.')

def display_player_attacks(player):
    print(f'{player["Hades"]} available attacks:')
    for attack in player["attacks"]:
        print(f'{attack[0]} ({attack [1]} {attack[2]}) damage)')

def battle_victory(player,enemy_list):
    print(f'{player["Hades"]} has defeated {enemy_list["Judas"]}, We shall take their coins!')
    loot_coins(player,enemy_list)
    loot_equipment(player,enemy_list)

def loot_coins(player,enemy_list):
    player["coins"]["copper"] += enemy_list["coins"]["copper"]
    player["coins"]["silver"] += enemy_list["coins"]["silver"]
    player["coins"]["gold"] += enemy_list["coins"]["gold"]
    print(f'Retrieved {enemy_list["coins"]["copper"]} copper coins.')
    print(f'Retrieved {enemy_list["coins"]["silver"]} silver coins.')
    print(f'Retrieved {enemy_list["coins"]["gold"]} gold coins.')
    print(f'{player["Hades"]} has retrieved {player["coins"]["copper"]} copper, {player["coins"]["silver"]} silver, {player["coins"]["gold"]} gold')

def loot_equipment(player,enemy_list):
    for item in enemy_list["equipment"]:
        player["equipment"].add(item)
        print (f'+ added {item} to group.')

def run_game(player,enemy_list):
    print('You are now entering to the showdown of the Gods!')
    battle_sequence (player,enemy_list)
    print('You have defeated all the Gods and are truly worthy!')

run_game(player,enemy_list) 







