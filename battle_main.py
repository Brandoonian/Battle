from time import sleep
from random import choice
from monster_one import Monster_ONE
from monster_two import Monster_TWO

monster_one = Monster_ONE()
monster_two = Monster_TWO()

print("Welcome to Battle Monsters!")
print("To begin, choose your monster!")

print("\nType '1' for monster1")
print("Type '2' for monster2")
print("Type '3' for monster3")

monsters_available = [monster_one, monster_two]
user_monster = []
while True:
    user_pick = input("Enter number: ")
    if user_pick == '1':
        print("You have chosen monster1!")
        user_monster = monsters_available.pop(0)
        break
    if user_pick == '2':
        print("You have chosen monster2!")
        user_monster = monsters_available.pop(1)
        break
    if user_pick == '3':
        print("You have chosen monster3!")
        break
    else:
        print("Please type a valid number and hit enter.")
        sleep(2)

#sleep(3)
# CPU picks it's monster.
cpu_monster = choice(monsters_available)
if cpu_monster == monster_one:
    print("You will be battling monster1!")
elif cpu_monster == monster_two:
    print("You will be battling monster2!")

print("Let the battle begin!")
print("First is your move.")
user_hp = 100
cpu_hp = 100
while user_hp and cpu_hp > 0:
    print("Choose your attack:")
    user_attack = input("Type '1' for POWER FIST or '2' for SUPER KICK: ")
    if user_attack == '1':
        print("Your monster used it's POWER FIST attack!!")
        cpu_hp -= 10
    if user_attack == '2':
        print("Your monster used it's SUPER KICK attack!!")
        cpu_hp -= 15

    print("Now it's your opponent's turn....")
    sleep(2)
    possible_attacks = ("POWER FIST", "HEADBUTT")
    cpu_attack = choice(possible_attacks)
    if cpu_attack == "POWER FIST":
        print("Your opponent used it's POWER FIST attack")
        user_hp -= 10
    if cpu_attack == "HEADBUTT":
        print("Your opponent used it's HEADBUTT attack")
        user_hp -= 20

if user_hp <= 0:
    print("You have been defeated.")

if cpu_hp <= 0:
    print("You have defeated your opponent!")






