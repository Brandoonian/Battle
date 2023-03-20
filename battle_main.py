from time import sleep
from random import choice, randint
from monsters.monster_one import Monster_ONE
from monsters.monster_two import Monster_TWO
from monsters.monster_three import Monster_THREE

active_effects = []
active_fortify = []
turns_poisoned = []

def simulate_battle():
    battle_active = True
    while battle_active == True:
        print(user_monster.HP)
        print(cpu_monster.HP)
        print("\nChoose your attack by entering the corresponding number:")
        get_user_attack()
        if cpu_monster.check_hp() != True:
            break

        check_effect()
        set_duration()
        apply_duration()
        apply_paralyze()
        apply_freeze()
        check_fortify()

        sleep(2)

        print(user_monster.HP)
        print(cpu_monster.HP)

        print("\nNow it's your opponent's turn....")
        sleep(2)

        possible_attacks = (
        cpu_monster.attack_1_name, cpu_monster.attack_2_name, cpu_monster.attack_3_name, cpu_monster.attack_4_name)
        cpu_attack = choice(possible_attacks)
        apply_confusion()

        if cpu_attack == cpu_monster.attack_1_name:
            print(f"\nYour opponent used it's {cpu_monster.attack_1_name} attack!")
            for fortify in active_fortify:
                if fortify['name'] == "defense rose":
                    user_monster.HP = (float(cpu_monster.attack_1()) * (float(apply_fortify()) ** len(active_fortify))) + float(user_monster.HP)
                elif apply_confusion() == True and fortify['name'] == "confused":
                    damage_self = randint(1, 2)
                    if damage_self == 1:
                        print(f"{cpu_monster.name} hurt itself in it's confusion!")
                        cpu_monster.HP = float(cpu_monster.attack_1()) + float(cpu_monster.HP)
                else:
                    user_monster.HP = float(cpu_monster.attack_1()) + float(user_monster.HP)
            if user_monster.check_hp() != True:
                break

        if cpu_attack == cpu_monster.attack_2_name:
            print(f"\nYour opponent used it's {cpu_monster.attack_2_name} attack!")
            for fortify in active_fortify:
                if fortify['name'] == "defense rose":
                    user_monster.HP = (float(cpu_monster.attack_2()) * (
                                float(apply_fortify()) ** len(active_fortify))) + float(user_monster.HP)
                elif apply_confusion() == True and fortify['name'] == "confused":
                    damage_self = randint(1, 2)
                    if damage_self == 1:
                        print(f"{cpu_monster.name} hurt itself in it's confusion!")
                        cpu_monster.HP = float(cpu_monster.attack_2()) + float(cpu_monster.HP)
                else:
                    user_monster.HP = float(cpu_monster.attack_2()) + float(user_monster.HP)
            if user_monster.check_hp() != True:
                break

        if cpu_attack == cpu_monster.attack_3_name:
            print(f"\nYour opponent used it's {cpu_monster.attack_3_name} attack!")
            for fortify in active_fortify:
                if fortify['name'] == "defense rose":
                    user_monster.HP = (float(cpu_monster.attack_3()) * (
                                float(apply_fortify()) ** len(active_fortify))) + float(user_monster.HP)
                elif apply_confusion() == True and fortify['name'] == "confused":
                    damage_self = randint(1, 2)
                    if damage_self == 1:
                        print(f"{cpu_monster.name} hurt itself in it's confusion!")
                        cpu_monster.HP = float(cpu_monster.attack_3()) + float(cpu_monster.HP)
                else:
                    user_monster.HP = float(cpu_monster.attack_3()) + float(user_monster.HP)
            if user_monster.check_hp() != True:
                break

        if cpu_attack == cpu_monster.attack_4_name:
            print(f"\nYour opponent used it's {cpu_monster.attack_4_name} attack!")
            for fortify in active_fortify:
                if fortify['name'] == "defense rose":
                    user_monster.HP = (float(cpu_monster.attack_4()) * (
                                float(apply_fortify()) ** len(active_fortify))) + float(user_monster.HP)
                elif apply_confusion() == True and fortify['name'] == "confused":
                    damage_self = randint(1, 2)
                    if damage_self == 1:
                        print(f"{cpu_monster.name} hurt itself in it's confusion!")
                        cpu_monster.HP = float(cpu_monster.attack_4()) + float(cpu_monster.HP)
                else:
                    user_monster.HP = float(cpu_monster.attack_4()) + float(user_monster.HP)
            if user_monster.check_hp() != True:
                break

        apply_poison()
    sleep(2)

def get_user_attack():
    user_attack = input(f"1.{user_monster.attack_1_name} {user_monster.display_PP_1()}"
                        f"     2.{user_monster.attack_2_name} {user_monster.display_PP_2()}"
                        f"\n3.{user_monster.attack_3_name} {user_monster.display_PP_3()}"
                        f"     4.{user_monster.attack_4_name} {user_monster.display_PP_4()}: ")

    if user_attack == '1':
        print(f"\nYour monster used it's {user_monster.attack_1_name} attack!!")
        cpu_monster.HP = user_monster.attack_1() + cpu_monster.HP
        

    if user_attack == '2':
        print(f"\nYour monster used it's {user_monster.attack_2_name} attack!!")
        cpu_monster.HP = user_monster.attack_2() + cpu_monster.HP
        if user_monster.attack_2_effect() != None:
            if active_effects:
                for effects in active_fortify:
                    print(f"{cpu_monster.name} is already {effects['name']}!")
            else:
                active_fortify.append(user_monster.attack_2_effect())


    if user_attack == '3':
        print(f"\nYour monster used it's {user_monster.attack_3_name} attack!!")
        cpu_monster.HP = user_monster.attack_3() + cpu_monster.HP
        if user_monster.attack_3_effect() != None:
            if active_effects:
                for effects in active_effects:
                    print(f"{cpu_monster.name} is already {effects['name']}!")
            else:
                active_effects.append(user_monster.attack_3_effect())


        print(active_effects)
        # Check for effects
        # See if effects activate
        # get duration of effects
        # Get damage from effects
        # Allow or disable opponent attacks

    if user_attack == '4':
        print(f"\nYour monster used it's {user_monster.attack_4_name} attack!!")
        cpu_monster.HP = user_monster.attack_4() + cpu_monster.HP
        if user_monster.attack_4_effect() != None:
            active_fortify.append(user_monster.attack_4_effect())

    sleep(3)

def check_effect():
    for effects in active_effects:
        odds = randint(1, 20)
        if effects['name'] == "poisoned" and odds <= effects['odds'] and effects['active'] == False:
            print(f"{cpu_monster.name} has been poisoned!")
            effects['active'] = True
        if effects['name'] == "paralyzed" and odds <= effects['odds'] and effects['active'] == False:
            print(f"{cpu_monster.name} has been paralyzed!")
            effects['active'] = True
        if effects['name'] == "frozen" and odds <= effects['odds'] and effects['active'] == False:
            print(f"{cpu_monster.name} has been frozen!")
            effects['active'] = True
    for effects in active_fortify:
        odds = randint(1, 20)
        if effects['name'] == "confused" and odds <= effects['odds'] and effects['active'] == False:
            print(f"{cpu_monster.name} has become confused!")
            effects['active'] = True

def check_fortify():
    for fortify in active_fortify:
        if fortify['name'] == "defense rose" and fortify['active'] == False:
            print(f"{user_monster.name}'s {fortify['name']}!")
            fortify['active'] = True

def apply_fortify():
    for fortify in active_fortify:
        if fortify['name'] == "defense rose" and fortify['active'] == True:
           return fortify['defense']

def set_duration():
    for effects in active_effects:
        if effects['active'] == True and effects['duration_set'] == False:
            effects['duration_set'] = True
    for effects in active_fortify:
        if effects['active'] == True and effects['duration_set'] == False:
            effects['duration_set'] = True

def apply_duration():
    for effects in active_effects:
        if effects['duration_set'] == True:
            duration = effects['duration']
            return duration
    for effects in active_fortify:
        if effects['duration_set'] == True:
            duration = effects['duration']
            return duration


def apply_poison():
    for effects in active_effects:
        if effects['duration_set'] == True and effects['name'] == "poisoned":
            duration = apply_duration()
            print(f"duration: {duration}")
            if duration > len(turns_poisoned):
                turns_poisoned.append(1)
                print(f"Turns poisoned: {turns_poisoned}")
                for effects in active_effects:
                    cpu_monster.HP = cpu_monster.HP + effects["damage"]
                    print(user_monster.HP)
                    print(cpu_monster.HP)
            elif duration <= len(turns_poisoned):
                print(f"{cpu_monster.name} is no longer poisoned.")
                active_effects.clear()
                turns_poisoned.clear()
                for effects in active_effects:
                    effects['active'] = False
                    effects['set_duration'] = False

def apply_paralyze():
    for effects in active_effects:
        if effects['duration_set'] == True and effects['name'] == "paralyzed":
            duration = apply_duration()
            print(f"duration: {duration}")
            if duration > len(turns_poisoned):
                while duration > len(turns_poisoned):
                    turns_poisoned.append(1)
                    print(f"Turns paralyzed: {turns_poisoned}")
                    print(f"{cpu_monster.name} is paralyzed and cannot attack!")
                    get_user_attack()
                    print(user_monster.HP)
                    print(cpu_monster.HP)
                print(f"{cpu_monster.name} is no longer paralyzed.")
            elif duration <= len(turns_poisoned):
                active_effects.clear()
                turns_poisoned.clear()
                for effects in active_effects:
                    effects['active'] = False
                    effects['set_duration'] = False

def apply_freeze():
    for effects in active_effects:
        if effects['duration_set'] == True and effects['name'] == "frozen":
            duration = apply_duration()
            print(f"duration: {duration}")
            if duration > len(turns_poisoned):
                while duration > len(turns_poisoned):
                    turns_poisoned.append(1)
                    print(f"Turns frozen: {turns_poisoned}")
                    print(f"{cpu_monster.name} is frozen and cannot attack!")
                    get_user_attack()
                    cpu_monster.HP = cpu_monster.HP + effects["damage"]
                    print(user_monster.HP)
                    print(cpu_monster.HP)
                print(f"{cpu_monster.name} is no longer frozen.")
            elif duration <= len(turns_poisoned):
                active_effects.clear()
                turns_poisoned.clear()
                for effects in active_effects:
                    effects['active'] = False
                    effects['set_duration'] = False

def apply_confusion():
    for effects in active_fortify:
        if effects['duration_set'] == True and effects['name'] == "confused":
            duration = apply_duration()
            print(f"duration: {duration}")
            print(f"{cpu_monster.name} is confused...")
            if duration > len(turns_poisoned):
                turns_poisoned.append(1)
                print(f"Turns poisoned: {turns_poisoned}")
                return True
            elif duration <= len(turns_poisoned):
                print(f"{cpu_monster.name} is no longer poisoned.")
                active_effects.clear()
                turns_poisoned.clear()
                for effects in active_fortify:
                    effects['active'] = False
                    effects['set_duration'] = False

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







