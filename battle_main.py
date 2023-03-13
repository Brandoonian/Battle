from time import sleep
from random import choice
from monster_one import Monster_ONE
from monster_two import Monster_TWO
from monster_three import Monster_THREE

def simulate_battle():
    battle_active = True
    while battle_active == True:
        print(user_monster.HP)
        print(cpu_monster.HP)
        print("\nChoose your attack by entering the corresponding number:")
        user_attack = input(f"1.{user_monster.attack_1_name} {user_monster.display_PP_1()}"
                            f"     2.{user_monster.attack_2_name} {user_monster.display_PP_2()}"
                            f"\n3.{user_monster.attack_3_name} {user_monster.display_PP_3()}"
                            f"     4.{user_monster.attack_4_name} {user_monster.display_PP_4()}: ")

        if user_attack == '1':
            print(f"\nYour monster used it's {user_monster.attack_1_name} attack!!")
            cpu_monster.HP = user_monster.attack_1() + cpu_monster.HP
            if cpu_monster.check_hp() != True:
                break
        if user_attack == '2':
            print(f"\nYour monster used it's {user_monster.attack_2_name} attack!!")
            cpu_monster.HP = user_monster.attack_2() + cpu_monster.HP
            if cpu_monster.check_hp() != True:
                break
        if user_attack == '3':
            print(f"\nYour monster used it's {user_monster.attack_3_name} attack!!")
            cpu_monster.HP = user_monster.attack_3() + cpu_monster.HP
            if cpu_monster.check_hp() != True:
                break
        if user_attack == '4':
            print(f"\nYour monster used it's {user_monster.attack_4_name} attack!!")
            cpu_monster.HP = user_monster.attack_4() + cpu_monster.HP
            if cpu_monster.check_hp() != True:
                break

        sleep(3)
        print(user_monster.HP)
        print(cpu_monster.HP)

        print("\nNow it's your opponent's turn....")
        sleep(2)

        possible_attacks = (cpu_monster.attack_1_name, cpu_monster.attack_2_name, cpu_monster.attack_3_name, cpu_monster.attack_4_name)
        cpu_attack = choice(possible_attacks)

        if cpu_attack == cpu_monster.attack_1_name:
            print(f"\nYour opponent used it's {cpu_monster.attack_1_name} attack!")
            user_monster.HP = cpu_monster.attack_1() + user_monster.HP
            if user_monster.check_hp() != True:
                break

        if cpu_attack == cpu_monster.attack_2_name:
            print(f"\nYour opponent used it's {cpu_monster.attack_2_name} attack!")
            user_monster.HP = cpu_monster.attack_2() + user_monster.HP
            if user_monster.check_hp() != True:
                break

        if cpu_attack == cpu_monster.attack_3_name:
            print(f"\nYour opponent used it's {cpu_monster.attack_3_name} attack!")
            user_monster.HP = cpu_monster.attack_3() + user_monster.HP
            if user_monster.check_hp() != True:
                break

        if cpu_attack == cpu_monster.attack_4_name:
            print(f"\nYour opponent used it's {cpu_monster.attack_4_name} attack!")
            user_monster.HP = cpu_monster.attack_4() + user_monster.HP
            if user_monster.check_hp() != True:
                break

        sleep(2)
    sleep(2)

monster_one = Monster_ONE()
monster_two = Monster_TWO()
monster_three = Monster_THREE()

print("Welcome to Battle Monsters!")
print("To begin, choose your monster!")
print(monster_one.attack_1)
print(f"\nType '1' for {monster_one.name}")
print(f"Type '2' for {monster_two.name}")
print(f"Type '3' for {monster_three.name}")

monsters_available = [monster_one, monster_two, monster_three]
user_monster = []
while True:
    user_pick = input("Enter number: ")
    if user_pick == '1':
        monster_one.chosen_1()
        user_monster = monsters_available.pop(0)
        sleep(2)
        break
    if user_pick == '2':
        monster_two.chosen_2()
        user_monster = monsters_available.pop(1)
        sleep(2)
        break
    if user_pick == '3':
        monster_three.chosen_3()
        user_monster = monsters_available.pop(2)
        sleep(2)
        break
    else:
        print("Please type a valid number and hit enter.")
        sleep(2)
    sleep(2)

cpu_monster = choice(monsters_available)
if cpu_monster == monster_one:
    print(f"\nYou will be battling against {monster_one.name}!")
elif cpu_monster == monster_two:
    print(f"\nYou will be battling against {monster_two.name}!")
elif cpu_monster == monster_three:
    print(f"\nYou will be battling against {monster_three.name}!")
sleep(2)

print("\nLet the battle begin!")
sleep(2)
print("First is your move.")

simulate_battle()

print(user_monster.HP)
print(cpu_monster.HP)
if user_monster.HP <= 0:
    print("YOU LOSE.")
else:
    print("YOU WIN!")






