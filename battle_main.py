from time import sleep
from random import choice, randint
from monsters.monster_one import Monster_ONE
from monsters.monster_two import Monster_TWO
from monsters.monster_three import Monster_THREE

active_poison = []
active_paralyze = []
active_freeze = []
active_defense = []
active_confuse = []
active_blind = []
turns_effected = []

def simulate_battle():
    battle_active = True
    while battle_active == True:
        print(user_monster.HP)
        print(cpu_monster.HP)
        print("\nChoose your attack by entering the corresponding number:")
        get_user_attack()
        if cpu_monster.check_hp() != True:
            break

        check_poison()
        check_paralyze()
        check_freeze()
        check_confuse()
        set_duration()
        apply_duration()
        apply_paralyze()
        apply_freeze()
        apply_confuse()
        sleep(2)

        print(user_monster.HP)
        print(cpu_monster.HP)

        print("\nNow it's your opponent's turn....")
        sleep(2)
        get_cpu_attack()

        if user_monster.check_hp() != True:
            break
        elif cpu_monster.check_hp() == False:
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
        hit = randint(1, 100)
        print(hit)
        if hit <= user_monster.accuracy:
            cpu_monster.HP = user_monster.attack_1() + cpu_monster.HP
            if user_monster.attack_1_effect() != None:
                if active_poison or active_paralyze or active_freeze or active_confuse:
                    for effects in active_poison:
                        print(f"{cpu_monster.name} took damage but is already {effects['name']}!")
                    for effects in active_paralyze:
                        print(f"{cpu_monster.name} is already {effects['name']}!")
                    for effects in active_freeze:
                        print(f"{cpu_monster.name} took damage but is already {effects['name']}!")
                    for effects in active_confuse:
                        print(f"{cpu_monster.name} took damage but is already {effects['name']}!")
                elif user_monster.attack_1_effect()['name'] == "defense rose":
                    active_defense.append(user_monster.attack_1_effect())
                elif user_monster.attack_1_effect()['name'] == "blinded":
                    active_blind.append(user_monster.attack_1_effect())
                    cpu_monster.accuracy = cpu_monster.accuracy * apply_blinding()
                    print(f"{cpu_monster.name}'s accuracy fell!")
                    print(cpu_monster.accuracy)
                else:
                    if user_monster.attack_1_effect()['name'] == "poisoned":
                        active_poison.append(user_monster.attack_1_effect())
                    elif user_monster.attack_1_effect()['name'] == "paralyzed":
                        active_paralyze.append(user_monster.attack_1_effect())
                    elif user_monster.attack_1_effect()['name'] == "frozen":
                        active_freeze.append(user_monster.attack_1_effect())
                    elif user_monster.attack_1_effect()['name'] == "confused":
                        active_confuse.append(user_monster.attack_1_effect())
        else:
            print("The attack missed!")

    if user_attack == '2':
        print(f"\nYour monster used it's {user_monster.attack_2_name} attack!!")
        hit = randint(1, 100)
        print(hit)
        if hit <= user_monster.accuracy:
            cpu_monster.HP = user_monster.attack_2() + cpu_monster.HP
            if user_monster.attack_2_effect() != None:
                if active_poison or active_paralyze or active_freeze or active_confuse:
                    for effects in active_poison:
                        print(f"{cpu_monster.name} took damage but is already {effects['name']}!")
                    for effects in active_paralyze:
                        print(f"{cpu_monster.name} is already {effects['name']}!")
                    for effects in active_freeze:
                        print(f"{cpu_monster.name} took damage but is already {effects['name']}!")
                    for effects in active_confuse:
                        print(f"{cpu_monster.name} took damage but is already {effects['name']}!")
                elif user_monster.attack_2_effect()['name'] == "defense rose":
                    active_defense.append(user_monster.attack_2_effect())
                elif user_monster.attack_2_effect()['name'] == "blinded":
                    active_blind.append(user_monster.attack_2_effect())
                    cpu_monster.accuracy = cpu_monster.accuracy * apply_blinding()
                    print(f"{cpu_monster.name}'s accuracy fell!")
                    print(cpu_monster.accuracy)
                else:
                    if user_monster.attack_2_effect()['name'] == "poisoned":
                        active_poison.append(user_monster.attack_2_effect())
                    elif user_monster.attack_2_effect()['name'] == "paralyzed":
                        active_paralyze.append(user_monster.attack_2_effect())
                    elif user_monster.attack_2_effect()['name'] == "frozen":
                        active_freeze.append(user_monster.attack_2_effect())
                    elif user_monster.attack_2_effect()['name'] == "confused":
                        active_confuse.append(user_monster.attack_2_effect())
        else:
            print("The attack missed!")

        print(active_confuse)
    if user_attack == '3':
        print(f"\nYour monster used it's {user_monster.attack_3_name} attack!!")
        hit = randint(1, 100)
        print(hit)
        if hit <= user_monster.accuracy:
            cpu_monster.HP = user_monster.attack_3() + cpu_monster.HP
            if user_monster.attack_3_effect() != None:
                if active_poison or active_paralyze or active_freeze or active_confuse:
                    for effects in active_poison:
                        print(f"{cpu_monster.name} took damage but is already {effects['name']}!")
                    for effects in active_paralyze:
                        print(f"{cpu_monster.name} is already {effects['name']}!")
                    for effects in active_freeze:
                        print(f"{cpu_monster.name} took damage but is already {effects['name']}!")
                    for effects in active_confuse:
                        print(f"{cpu_monster.name} took damage but is already {effects['name']}!")
                elif user_monster.attack_3_effect()['name'] == "defense rose":
                    active_defense.append(user_monster.attack_3_effect())
                elif user_monster.attack_3_effect()['name'] == "blinded":
                    active_blind.append(user_monster.attack_3_effect())
                    cpu_monster.accuracy = cpu_monster.accuracy * apply_blinding()
                    print(f"{cpu_monster.name}'s accuracy fell!")
                    print(cpu_monster.accuracy)
                else:
                    if user_monster.attack_3_effect()['name'] == "poisoned":
                        active_poison.append(user_monster.attack_3_effect())
                    elif user_monster.attack_3_effect()['name'] == "paralyzed":
                        active_paralyze.append(user_monster.attack_3_effect())
                    elif user_monster.attack_3_effect()['name'] == "frozen":
                        active_freeze.append(user_monster.attack_3_effect())
                    elif user_monster.attack_3_effect()['name'] == "confused":
                        active_confuse.append(user_monster.attack_3_effect())
        else:
            print("The attack missed!")

    if user_attack == '4':
        print(f"\nYour monster used it's {user_monster.attack_4_name} attack!!")
        hit = randint(1, 100)
        print(hit)
        if hit <= user_monster.accuracy:
            cpu_monster.HP = user_monster.attack_4() + cpu_monster.HP
            if user_monster.attack_4_effect() != None:
                if active_poison or active_paralyze or active_freeze or active_confuse:
                    for effects in active_poison:
                        print(f"{cpu_monster.name} took damage but is already {effects['name']}!")
                    for effects in active_paralyze:
                        print(f"{cpu_monster.name} is already {effects['name']}!")
                    for effects in active_freeze:
                        print(f"{cpu_monster.name} took damage but is already {effects['name']}!")
                    for effects in active_confuse:
                        print(f"{cpu_monster.name} took damage but is already {effects['name']}!")
                elif user_monster.attack_4_effect()['name'] == "defense rose":
                    active_defense.append(user_monster.attack_4_effect())
                elif user_monster.attack_4_effect()['name'] == "blinded":
                    active_blind.append(user_monster.attack_4_effect())
                    cpu_monster.accuracy = cpu_monster.accuracy * apply_blinding()
                    print(f"{cpu_monster.name}'s accuracy fell!")
                    print(cpu_monster.accuracy)
                else:
                    if user_monster.attack_4_effect()['name'] == "poisoned":
                        active_poison.append(user_monster.attack_4_effect())
                    elif user_monster.attack_4_effect()['name'] == "paralyzed":
                        active_paralyze.append(user_monster.attack_4_effect())
                    elif user_monster.attack_4_effect()['name'] == "frozen":
                        active_freeze.append(user_monster.attack_4_effect())
                    elif user_monster.attack_4_effect()['name'] == "confused":
                        active_confuse.append(user_monster.attack_4_effect())
        else:
            print("The attack missed!")

    sleep(3)

def get_cpu_attack():
    possible_attacks = (
        cpu_monster.attack_1_name, cpu_monster.attack_2_name,
        cpu_monster.attack_3_name, cpu_monster.attack_4_name
                        )
    cpu_attack = choice(possible_attacks)

    if cpu_attack == cpu_monster.attack_1_name:
        hit = randint(1, 100)
        if hit <= cpu_monster.accuracy:
            if active_defense:
                print(f"\nYour opponent used it's {cpu_monster.attack_1_name} attack!")
                user_monster.HP = (float(cpu_monster.attack_1()) * apply_defense()) + float(user_monster.HP)
            elif active_confuse and hurt_self() == True:
                print(f"{cpu_monster.name} hurt itself in confusion!")
                cpu_monster.HP = float(cpu_monster.attack_1()) + float(cpu_monster.HP)
            else:
                print(f"\nYour opponent used it's {cpu_monster.attack_1_name} attack!")
                user_monster.HP = float(cpu_monster.attack_1()) + float(user_monster.HP)
        else:
            print("The attack missed!")

    if cpu_attack == cpu_monster.attack_2_name:
        hit = randint(1, 100)
        if hit <= cpu_monster.accuracy:
            if active_defense:
                print(f"\nYour opponent used it's {cpu_monster.attack_2_name} attack!")
                user_monster.HP = (float(cpu_monster.attack_2()) * apply_defense()) + float(user_monster.HP)
            elif active_confuse and hurt_self() == True:
                print(f"{cpu_monster.name} hurt itself in confusion!")
                cpu_monster.HP = float(cpu_monster.attack_2()) + float(cpu_monster.HP)
            else:
                print(f"\nYour opponent used it's {cpu_monster.attack_2_name} attack!")
                user_monster.HP = float(cpu_monster.attack_2()) + float(user_monster.HP)
        else:
            print("The attack missed!")

    if cpu_attack == cpu_monster.attack_3_name:
        hit = randint(1, 100)
        if hit <= cpu_monster.accuracy:
            if active_defense:
                print(f"\nYour opponent used it's {cpu_monster.attack_3_name} attack!")
                user_monster.HP = (float(cpu_monster.attack_3()) * apply_defense()) + float(user_monster.HP)
            elif active_confuse and hurt_self() == True:
                print(f"{cpu_monster.name} hurt itself in confusion!")
                cpu_monster.HP = float(cpu_monster.attack_3()) + float(cpu_monster.HP)
            else:
                print(f"\nYour opponent used it's {cpu_monster.attack_3_name} attack!")
                user_monster.HP = float(cpu_monster.attack_3()) + float(user_monster.HP)
        else:
            print("The attack missed!")

    if cpu_attack == cpu_monster.attack_4_name:
        hit = randint(1, 100)
        if hit <= cpu_monster.accuracy:
            if active_defense:
                print(f"\nYour opponent used it's {cpu_monster.attack_4_name} attack!")
                user_monster.HP = (float(cpu_monster.attack_4()) * apply_defense()) + float(user_monster.HP)
            elif active_confuse and hurt_self() == True:
                print(f"{cpu_monster.name} hurt itself in confusion!")
                cpu_monster.HP = float(cpu_monster.attack_4()) + float(cpu_monster.HP)
            else:
                print(f"\nYour opponent used it's {cpu_monster.attack_4_name} attack!")
                user_monster.HP = float(cpu_monster.attack_4()) + float(user_monster.HP)
        else:
            print("The attack missed!")

def check_poison():
    for effects in active_poison:
        odds = randint(1, 20)
        if effects['name'] == "poisoned" and odds <= effects['odds'] and effects['active'] == False:
            print(f"{cpu_monster.name} has been poisoned!")
            effects['active'] = True

def check_paralyze():
    for effects in active_paralyze:
        odds = randint(1, 20)
        if effects['name'] == "paralyzed" and odds <= effects['odds'] and effects['active'] == False:
            print(f"{cpu_monster.name} has been paralyzed!")
            effects['active'] = True

def check_freeze():
    for effects in active_freeze:
        odds = randint(1, 20)
        if effects['name'] == "frozen" and odds <= effects['odds'] and effects['active'] == False:
            print(f"{cpu_monster.name} has been frozen!")
            effects['active'] = True

def check_confuse():
    for effects in active_confuse:
        odds = randint(1, 20)
        if effects['name'] == "confused" and odds <= effects['odds'] and effects['active'] == False:
            print(f"{cpu_monster.name} has become confused!")
            effects['active'] = True

def set_duration():
    for effects in active_poison:
        if effects['active'] == True and effects['duration_set'] == False:
            effects['duration_set'] = True
            print('Duration set!')

    for effects in active_paralyze:
        if effects['active'] == True and effects['duration_set'] == False:
            effects['duration_set'] = True
            print('Duration set!')

    for effects in active_freeze:
        if effects['active'] == True and effects['duration_set'] == False:
            effects['duration_set'] = True
            print('Duration set!')

    for effects in active_confuse:
        if effects['active'] == True and effects['duration_set'] == False:
            effects['duration_set'] = True
            print('Duration set!')


def apply_duration():

    for effects in active_poison:
        if effects['duration_set'] == True:
            duration = effects['duration']
            return duration

    for effects in active_paralyze:
        if effects['duration_set'] == True:
            duration = effects['duration']
            return duration

    for effects in active_freeze:
        if effects['duration_set'] == True:
            duration = effects['duration']
            return duration

    for effects in active_confuse:
        if effects['duration_set'] == True:
            duration = effects['duration']
            return duration

def apply_poison():
    for effects in active_poison:
        if effects['duration_set'] == True and effects['name'] == "poisoned":
            duration = apply_duration()
            print(f"duration: {duration}")
            if duration > len(turns_effected):
                turns_effected.append(1)
                print(f"Turns poisoned: {turns_effected}")
                for effects in active_poison:
                    cpu_monster.HP = cpu_monster.HP + effects["damage"]
                    print(user_monster.HP)
                    print(cpu_monster.HP)
            elif duration <= len(turns_effected):
                print(f"{cpu_monster.name} is no longer poisoned.")
                active_poison.clear()
                turns_effected.clear()
                for effects in active_poison:
                    effects['active'] = False
                    effects['set_duration'] = False

def apply_paralyze():
    for effects in active_paralyze:
        if effects['duration_set'] == True and effects['name'] == "paralyzed":
            duration = apply_duration()
            print(f"duration: {duration}")
            if duration > len(turns_effected):
                while duration > len(turns_effected):
                    turns_effected.append(1)
                    print(f"Turns paralyzed: {turns_effected}")
                    print(f"{cpu_monster.name} is paralyzed and cannot attack!")
                    get_user_attack()
                    print(user_monster.HP)
                    print(cpu_monster.HP)
                print(f"{cpu_monster.name} is no longer paralyzed.")
            elif duration <= len(turns_effected):
                active_paralyze.clear()
                turns_effected.clear()
                for effects in active_paralyze:
                    effects['active'] = False
                    effects['set_duration'] = False

def apply_freeze():
    for effects in active_freeze:
        if effects['duration_set'] == True and effects['name'] == "frozen":
            duration = apply_duration()
            print(f"duration: {duration}")
            if duration > len(turns_effected) and cpu_monster.HP > 0.0:
                while duration > len(turns_effected):
                    turns_effected.append(1)
                    print(f"Turns frozen: {turns_effected}")
                    print(f"{cpu_monster.name} is frozen and cannot attack!")
                    get_user_attack()
                    cpu_monster.HP = cpu_monster.HP + effects["damage"]
                    print(user_monster.HP)
                    print(cpu_monster.HP)
                print(f"{cpu_monster.name} is no longer frozen.")
                active_freeze.clear()
                turns_effected.clear()
                for effects in active_freeze:
                    effects['active'] = False
                    effects['set_duration'] = False
            else:
                cpu_monster.check_hp()

def apply_confuse():
    for effects in active_confuse:
        if effects['duration_set'] == True and effects['name'] == "confused":
            duration = apply_duration()
            print(f"duration: {duration}")
            if duration > len(turns_effected):
                turns_effected.append(1)
                print(f"Turns confused: {turns_effected}")
                print(user_monster.HP)
                print(cpu_monster.HP)
            elif duration <= len(turns_effected):
                print(f"{cpu_monster.name} is no longer confused.")
                active_confuse.clear()
                turns_effected.clear()
                for effects in active_confuse:
                    effects['active'] = False
                    effects['set_duration'] = False

def hurt_self():
    for effect in active_confuse:
        if effect['active'] == True:
            odds = randint(1, 2)
            if odds == 1:
                return True
            else:
                return False

def apply_defense():
    for defense in active_defense:
        dam_resist = defense['defense'] ** len(active_defense)
        return dam_resist

def apply_blinding():
    for effect in active_blind:
        acc_damage = effect['blinding'] ** len(active_blind)
        return acc_damage

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
        monster_one.chosen()
        user_monster = monsters_available.pop(0)
        sleep(2)
        break
    if user_pick == '2':
        monster_two.chosen()
        user_monster = monsters_available.pop(1)
        sleep(2)
        break
    if user_pick == '3':
        monster_three.chosen()
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







