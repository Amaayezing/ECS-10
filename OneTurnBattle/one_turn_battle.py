#Maayez Imam 10/14/17
#One Turn Battle Program

import random
import math

seed = int(input("Enter the seed to run the fight with: "))
hp_attacker = int(input("Enter the attacker's hp: "))
strength_attacker = int(input("Enter the attacker's strength: "))
accuracy_attacker = int(input("Enter the attacker's accuracy: "))
crit_chance_attacker = int(input("Enter the attacker's crit chance: "))
#determine if critical hit, if so then definitely hit and +1 on attack strength
dodge_rate_attacker = int(input("Enter the attacker's dodge rate: "))
hp_defender = int(input("Enter the defender's hp: "))
strength_defender = int(input("Enter the defender's strength: "))
accuracy_defender = int(input("Enter the defender's accuracy: "))
crit_chance_defender = int(input("Enter the defender's crit chance: "))
dodge_rate_defender = int(input("Enter the defender's dodge rate: "))
guarding = str(input("Is the defender guarding? Y for yes, n for no: "))

random.seed(seed)
crit_chance = random.randint(0, 100)
if crit_chance <= crit_chance_attacker:
    #hit
    strength_attacker = strength_attacker + 1
    hp_defender = hp_defender - strength_attacker
    print("attacker crit defender for %d points of damage" % strength_attacker)
elif crit_chance > crit_chance_attacker:
    #random.seed(seed)
    accuracy = random.randint(0, 100)
    if accuracy <= accuracy_attacker:
        #random.seed(seed)
        dodgerate = random.randint(0, 100)
        if dodgerate <= dodge_rate_defender:
            #miss
            hp_defender = hp_defender
            print("defender dodged attacker's attack")
        else:
            #hit
            #random.seed(seed)
            strength = random.randint(math.floor(strength_attacker // 2), strength_attacker)
            hp_defender = hp_defender - strength
            print("attacker hit defender for %d points of damage" % strength)
    else:
        #miss
        hp_defender = hp_defender
        print("attacker missed defender")
#else:
    #exit(0)

if hp_defender > 0:
    #random.seed(seed)
    crit_chance_2 = random.randint(0, 100)
    if crit_chance_2 <= crit_chance_defender:
        #hit
        strength_defender = strength_defender + 1
        hp_attacker = hp_attacker - strength_defender
        print("defender crit attacker for %d points of damage" % strength_defender)
    elif crit_chance_2 > crit_chance_defender:
        #random.seed(seed)
        accuracy_2 = random.randint(0, 100)
        if accuracy_2 <= accuracy_defender:
            #random.seed(seed)
            dodgerate_2 = random.randint(0, 100)
            if dodgerate_2 <= dodge_rate_attacker:
                #miss
                hp_attacker = hp_attacker
                print("attacker dodged defender's attack")
            else:
                #hit
                strength_2 = random.randint(math.floor(strength_defender // 2), strength_defender)
                hp_attacker = hp_attacker - strength_2
                print("defender hit attacker for %d points of damage" % strength_2)
        else:
            #miss
            hp_attacker = hp_attacker
            print("defender missed attacker")

if hp_attacker < 0:
    hp_attacker = 0

if hp_defender < 0:
    hp_defender = 0

print("After fighting the attacker has %d hp left and the defender has %d hp left" % (hp_attacker, hp_defender))
