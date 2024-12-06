import random

def LEFT(s, length):
    return str(s[:length])

#HP variables.
#I could add ticks to make the healing more interesting

#Attacking Variables
#random attack value
#crit strike chance

#Combat Properties
P1Style = ["STAB","SLASH","BLOCK","HEAL"]
BossStyle = ["The dragon pounces!","The dragon attempts to stomp","The dragon lets out a mighty roar!"]
#special attacks

def main():
    try:
        input("A huge dragon lies sleeping before you...(Press 'ENTER' to continue...)")

        FightChoice = "initialized here"
        while FightChoice not in ["Y","N"]:

            FightChoice = LEFT(input("Do you wish to fight it? Y/N\n"),1).upper()

            if(FightChoice not in ["Y","N"]):
                print("The elders do not understand your command...")
            elif(FightChoice == "N"):
                print("You carefully back out of the cave, being careful not to awake the dragon.")
            else:
                print("You take a step forward. The dragon accepts your challenge and lets out a roar!")
                #Main battle starts here. This will be awesome with objects, but for now it's line by line.
                BossHP = 200
                P1HP = 100
                PotionCount = 4
                Heal = 10

                while BossHP > 0 and P1HP > 0:
                    P1Choice = "initialized here"
                    print("Your HP:",P1HP)
                    print("Boss HP:",BossHP)
                    while P1Choice not in P1Style:
                        print("Select an attack!")
                        P1Choice = input("'Stab','Slash','Block','Heal'\n").upper()
                        if P1Choice not in P1Style:
                             print("The elders do not understand your command...")
                        else:
                             BossChoice = random.choice(BossStyle)
                             print(BossChoice)
                    #Combat Choices
                    if(P1Choice == "HEAL"):
                        print("You dodge the dragons attack!")
                        if(P1HP == 100):
                              input("You drink the potion...(Press ENTER to continue...)")
                              print("and it does nothing!!!")
                        elif(PotionCount == 0):
                             input("You drink the potion...(Press ENTER to continue...)")
                             print("Wait a sec, the vial is empty! The dragon raises a scaly eyebrow at you.")
                             print("The embarrassment hurts you a little!")
                             P1HP = P1HP - 10
                        else:
                            input("You drink the potion...(Press ENTER to continue...)")
                            print("you feel rejuvinated")
                            P1HP = P1HP+Heal
                            PotionCount = PotionCount-1
                    
                    #Slash properties
                    elif(P1Choice == "SLASH"):
                         if(BossChoice == "The dragon pounces!"):
                              print("You swing your sword to retaliate! You both take damage!")
                              P1HP = P1HP - 10
                              BossHP = BossHP - 20
                         elif(BossChoice =="The dragon attempts to stomp"):
                              print("You slash the dragons leg, inflicting heavy damage!")
                              BossHP = BossHP - 40
                         elif(BossChoice =="The dragon lets out a mighty roar!"):
                              print("Rocks from the roof of the cave fall onto your head!")
                              P1HP = P1HP - 20

                    #Stab Properties
                    elif(P1Choice == "STAB"):
                         if(BossChoice == "The dragon attempts to stomp"):
                              print("You stab the dragon in the leg as it crushes you! You both take damage!")
                              P1HP = P1HP - 10
                              BossHP = BossHP - 20
                         elif(BossChoice =="The dragon pounces!"):
                              print("You thrust your sword into the pouncing dragon, inflicting heavy damage!")
                              BossHP = BossHP - 40
                         elif(BossChoice =="The dragon lets out a mighty roar!"):
                              print("Rocks from the roof of the cave fall onto your head!")
                              P1HP = P1HP - 20
                    
                    #Block Properties
                    else:
                         if(BossChoice == "The dragon pounces!"):
                              print("You desperately fight the dragons leg off of your shield! You become exhausted!")
                              P1HP = P1HP - 10
                              BossHP = BossHP - 20
                         elif(BossChoice =="The dragon lets out a mighty roar!"):
                              print("Rocks fall from the roof of the cave, but you block them with your shield!")
                              print("The dragon hurt itself in it's confusion! ;)")
                              BossHP = BossHP - 40
                         elif(BossChoice =="The dragon attempts to stomp"):
                              print("The dragon crushes you between a wall and your shield!!")
                              P1HP = P1HP - 20
                if(BossHP <= 0 and P1HP > 0):
                     print("You vanquish the horrible monster, and take the crystal you need to free yourself from the vision.")
                elif(P1HP <= 0 and BossHP > 0):
                     print("You crumble to ashes before the dragon, as it claims your soul!")
                elif(BossHP <= 0 and P1HP <= 0):
                     print("You both simultaneously crumble to ashes, locked in battle for eternity!")
                else:
                    print("--------------------------------------------------------------------")

        print("The vision fades, the warlocks drag you out of the scrying pool...")
    except:
        print("You become overwhelmed by horrific visions, the warlocks drag you out of the scrying pool...")
main()