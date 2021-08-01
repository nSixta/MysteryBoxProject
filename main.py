import random


def pickWeapon(box, weapon_summary):
    primary_weapon = "M1911"
    secondary_weapon = ""
    tactical_granade = ""
    number = input("Enter number here: ")
    if number == "1":
        weapon = random.choice(box)
        print(weapon[0:-2])
        secondary_weapon = weapon[0:-2]
        print("\nPrimary Weapon: " + primary_weapon)
        print("Secondary Weapon: " + secondary_weapon)
        print("Tactical Weapon: " + tactical_granade)
    keep_going = True
    while keep_going:
        decision = input("Enter 1 for another weapon or press 0 to stop: ")
        if decision == "1":
            weapon = random.choice(box)
            print(weapon[0:-2])
            if weapon[-1] == "1":
                switchWeapon = input("Enter 5 to switch primary weapons, 6 for secondary weapon, 7 to not switch: ")
                if switchWeapon == "5":
                    primary_weapon = weapon[0:-2]
                if switchWeapon == "6":
                    secondary_weapon = weapon[0:-2]
                if switchWeapon == "7":
                    continue
            elif weapon[-1] == "2":
                if tactical_granade == "":
                    tactical_granade = weapon[0:-2]
                else:
                    switchTactical = input("Enter 8 to switch Tactical Grenade, 9 to not switch: ")
                    if switchTactical == "8":
                        tactical_granade = weapon[0:-2]
                    if tactical_granade == "9":
                        continue
            weapon_summary.append(weapon[0:-2])
            print("\nPrimary Weapon: " + primary_weapon)
            print("Secondary Weapon: " + secondary_weapon)
            print("Tactical Weapon: " + tactical_granade)
        elif decision == "0":
            print("Thanks for Playing")
            keep_going = False
        else:
            print("Only enter 1 or 0")
    print("\nWeapons Pulled")
    print(*weapon_summary, sep=", ")


def startUp(box, weapon_summary):
    print("Welcome to Mystery Box")
    print("Enter 1 for random weapon from the mystery box")
    pickWeapon(box, weapon_summary)


def main():
    box = ["31-79 JGb215-1", "AUG-1", "Ballistic Knife-1", "China Lake-1", "Commando-1", "Crossbow-1", "CZ75-1", "CZ75 Dual Wield-1",
           "Dragunov-1", "Famas-1", "FN FAL-1", "G11-1", "Galil-1", "Gersh Device-2", "HS-10-1", "HK21-1", "L96A1-1", "M72 Law-1",
           "Matryoshka Doll-2", "Monkey Bomb-2", "Python-1", "Quantum Entanglement Device-2", "Ray Gun-1", "RPK-1", "Scavenger-1",
           "SPAS-12-1", "Thundergun-1", "V-R11-1", "Winter's Howl-1", "Wave Gun-1", "Wunderwaffe DG-2-1"]
    weapon_summary = []
    startUp(box, weapon_summary)


if __name__ == '__main__':
    main()
