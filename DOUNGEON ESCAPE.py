import time
from textfx import typeeffect
import os
import platform
inventory = []
userpocket = ["bread","rock"]
userChoice=0
findKey=False
findTourch=False
firsttimer1 = True
firsttimer2 = True
firsttimer3 = True
firsttimer4 = True
firsttimer5 = True
findnote = False
def clear_screen():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        # For Linux/Mac - check if TERM exists
        if os.environ.get('TERM'):
            os.system('clear')
        else:
            # Fallback: just print newlines
            print('\n' * 100)


def play_again():
    clear_screen()
    typeeffect("\n========================================", delay=0.05)
    typeeffect("\n         GAME OVER", delay=0.05)
    typeeffect("\n========================================\n", delay=0.05)
    typeeffect("Do you want to play again?\n\n", delay=0.05)
    typeeffect("1. Yes, restart\n", delay=0.05)
    typeeffect("2. No, quit\n\n", delay=0.05)

    choice = input("Your choice: ")

    match choice:
        case "1" | "yes" | "y":
            # Reset all global variables
            global inventory, userpocket, findKey, findTourch
            global firsttimer1, firsttimer2, firsttimer3, firsttimer4, firsttimer5
            global findnote

            inventory = []
            userpocket = ["bread", "rock"]
            findKey = False
            findTourch = False
            findnote = False
            firsttimer1 = True
            firsttimer2 = True
            firsttimer3 = True
            firsttimer4 = True
            firsttimer5 = True

            clear_screen()
            typeeffect("Restarting game...\n", delay=0.05)
            time.sleep(1)
            return 1 # Signal to restart

        case "2" | "no" | "n" | "quit":
            clear_screen()
            typeeffect("\nThanks for playing!\n", delay=0.05)
            typeeffect("Goodbye! 👋\n", delay=0.05)
            time.sleep(1)
            return False  # Signal to quit

        case _:
            typeeffect("\nInvalid choice. Exiting...\n", delay=0.05)
            time.sleep(1)
            return False
def room1():
    clear_screen()
    global firsttimer1
    if firsttimer1==True:
        options = "Options:\n1. Try the wooden door\n2. Go left into the dark corridor\n3. Look under the grate\n4. Search your pockets"
        typeeffect(
            "You wake up on cold stone floor. Your head throbs.\nTorches flicker on damp walls, casting dancing shadows\n\nA heavy wooden door with an iron lock stands before you.\nA dark corridor disappears to your left.\nA small grate in the floor catches your eye.\n\nWhat do you do?\n\n",
            delay=0.1)
        typeeffect(options, delay=0.1)
        firsttimer1=False
    else :
        print("Options:\n1. Try the wooden door\n2. Go left into the dark corridor\n3. Look under the grate\n4. Search your pockets")

    room1Choice = int(input())
    match (room1Choice):
        case 1:
            clear_screen()
            typeeffect("You walk toward the wooden door and try the handle.\nIt's locked, but you feel it might open with the right key.\nYou step back and examine the door more closely.",delay=0.1)
            time.sleep(2)
            return 2

        case 2:
            clear_screen()
            typeeffect("You step into the darkness...\nThe torchlight from behind fades as you move forward.\nSoon, you're surrounded by shadows.",delay=0.1)
            time.sleep(2)
            return 3
        case 3:
            clear_screen()
            typeeffect("You grab the edge of the rusty grate and pull.\nIt creaks loudly but lifts open.\nBelow is a dark hole with a small ladder.\nYou climb down...",delay=0.1)
            time.sleep(2)
            return 5
        case 4:
            clear_screen()
            if len(userpocket) == 0:
                typeeffect("Your pockets are empty.\nNothing else to find here.",delay=0.1)
                time.sleep(2)
                return 1
            else:
                typeeffect("You pat down your pockets.\nNothing useful... wait, what's that?\nYou find a small ROCK and a piece of BREAD.\nNot much, but better than nothing.",delay=0.1)
                time.sleep(2)
                for item in userpocket:
                    inventory.append(item)
                userpocket.clear()
                time.sleep(2)
                return 1




def room2():
    global findKey,firsttimer2
    clear_screen()
    if firsttimer2==True:
        typeeffect(
            "You stand before the weathered door.\nThe iron lock looks old but sturdy.\nThrough the cracks, you see a faint light.\n\nWhat do you do?\n\n",
            delay=0.1)
        options = "Options:\n1. Try to open the door\n2. Inspect the lock closely\n3. Listen at the door\n4. Go back to entrance\n"
        typeeffect(options)
        firsttimer2=False
    else:
        print("Options:\n1. Try to open the door\n2. Inspect the lock closely\n3. Listen at the door\n4. Go back to entrance\n")

    room2Choice =int(input())
    match(room2Choice):
        case 1:
            clear_screen()
            if findKey==True:
                typeeffect("You pull out the rusty key and insert it into the lock.\nIt fits perfectly!\nCLICK! The lock opens.\nThe door swings open. SUNLIGHT pours in!\nYou step outside and feel the warm air on your face.\n\n🎉 CONGRATULATIONS! YOU ESCAPED! 🎉",delay=0.1)
                if not play_again():
                    quit()
                else:
                    return 1  # Restart from room1
            else:
                typeeffect("The door is locked tight. Won't budge.", delay=0.1)
                time.sleep(2)
                return 2

        case 2:
            clear_screen()
            typeeffect("It's a simple old lock. A rusty key would fit perfectly.",delay=0.1)
            time.sleep(2)
            return 2
        case 3:
            clear_screen()
            typeeffect("You hear wind... maybe outside? Or is that a monster breathing?",delay=0.1)
            time.sleep(2)
            return 2
        case 4:
            clear_screen()
            typeeffect("You step away from the door and walk back.\nThe entrance flickers with torchlight ahead.\nYou're back where you started.",delay=0.1) #go back to room 1
            time.sleep(2)
            return 1



def room3():
    global findKey, findTourch,firsttimer3
    clear_screen()
    if firsttimer3==True:
        typeeffect(
            "The corridor stretches into darkness.\nYou can't see more than 2 steps ahead.\nWater drips somewhere. The air is cold and damp.\n\nWhat do you do?\n\n",
            delay=0.1)
        typeeffect(
            "Options:\n1. Feel along the wall\n2. Return to entrance\n3. Call out into darkness\n4. Light a torch\n",
            delay=0.1)
        firsttimer3=False
    else:
        print("Options:\n1. Feel along the wall\n2. Return to entrance\n3. Call out into darkness\n4. Light a torch\n")

    room3Choice= int(input())
    match(room3Choice):
        case 1:
            clear_screen()
            typeeffect("You press your hands against the cold stone wall.\nYour fingers trace rough bricks and wet slime.\nYou feel nothing useful... just more wall.\nA spider crawls over your hand. You shake it off.\nAfter minutes of searching, you find nothing.\nYou decide to stop before you get lost.",delay=0.1)
            time.sleep(2)
            return 3
        case 2:
            clear_screen()
            typeeffect("You've had enough of this dark corridor.\nYou turn around and walk back the way you came.\nThe entrance torchlight grows brighter as you approach.\nSoon, you're back where you started.",delay=0.1) # go baack to room 1
            time.sleep(2)
            return 1
        case 3:
            clear_screen()
            typeeffect("You take a deep breath and shout:\n\"HELLO?! IS ANYONE THERE?!\"\n\nYour voice echoes through the corridor...\n\"hello... hello... hello...\"\n\nThen... silence.\nNo response. Just the dripping water.\nYou feel stupid for shouting.",delay=0.1)
            time.sleep(2)
            return 3
        case 4:
            clear_screen()
            #if player has tourch
            if findTourch==False:
                typeeffect("You reach for a torch but remember...\nYou don't have one.\nNothing to light. Nothing to see with.\nYou stay in the darkness.")
                time.sleep(2)
                return 3
            else:
                typeeffect("You reach into your pocket and pull out your torch.\nYour hands tremble as you strike a spark...\nFOOM! The torch ignites!\n\nOrange flame dances, casting flickering shadows.\nThe corridor comes to life!\nYou can now see a GLINT of something at the far end.\n\nThe torch feels warm in your hands. You're not alone in the darkness anymore.",delay=0.1)
                time.sleep(2)
                clear_screen()
                typeeffect("Your torch blazes brightly, pushing back the darkness.\nFlames dance and crackle, illuminating every corner.\nAt the far end of the corridor, something GLINTS!\nA small metallic object lies on the floor.",delay=0.1)
                typeeffect("\nWhat do you do?\n\n1. Investigate the glint\n2. Walk deeper into the corridor\n3. Return to entrance\n",delay=0.1)
                tourchlitChoice = int(input())
                tourchlitfst=True
                match (tourchlitChoice):
                    case 1:
                        clear_screen()
                        if tourchlitfst == True:
                            typeeffect("You walk toward the glint, torch held high.\nAs you get closer, you see it...\nA RUSTY KEY lying on the cold stone floor!\nYou grab it and slip it into your pocket.",delay=0.1)
                            findKey=True
                            tourchlitfst=False
                            inventory.append("key")
                            time.sleep(2)
                            return 3
                        else:
                            typeeffect("You walk to where the key was.\nNothing there now. Just empty floor.",delay=0.1)
                            time.sleep(2)
                            return 3

                    case 2:
                        clear_screen()
                        typeeffect("You decide to go further.\nThe corridor narrows. The air gets colder.\nA foul smell wafts toward you.\nYou hear deep breathing ahead...\nA cavern opens up before you.")
                        time.sleep(2)
                        return 4
                    case 3:
                        clear_screen()
                        typeeffect("You've seen enough of this corridor.\nYou turn back the way you came, torch lighting your path.\nThe entrance torchlight grows brighter as you approach.\nSoon, you're back where you started.")
                        time.sleep(2)
                        return 1
                        #go back to room 1



def room4():
    global firsttimer4
    clear_screen()
    if firsttimer4 == True:
        typeeffect(
            "You enter a large cavern.\nA GIANT TROLL sleeps in the corner.\nIt's ugly. Huge. Smelly.\nNext to it, you see an EXIT DOOR!\n\nWhat do you do?\n\n",
            delay=0.1)
        typeeffect(
            "Options:\n1. Sneak past the troll\n2. Fight the troll\n3. Throw something to distract it\n4. Run back to corridor\n",
            delay=0.1)
        firsttimer4=False
    else :
        print("Options:\n1. Sneak past the troll\n2. Fight the troll\n3. Throw something to distract it\n4. Run back to corridor\n")

    room4Choice = int(input())
    match (room4Choice):
        case 1:
            clear_screen()
            typeeffect("You take one step... two steps...\nCRACK! You stepped on a bone!\nThe troll wakes up. ROOOAAAR!\nIt sees you. GAME OVER! 💀",delay=0.1)
            time.sleep(2)
            play_again()
        case 2:
            clear_screen()
            typeeffect("You punch the troll. It's like punching a wall.\nThe troll laughs. Then eats you.\nGAME OVER! 💀",delay=0.1)
            time.sleep(2)
            play_again()
        case 3:
            clear_screen()
            if len(userpocket)==0:
                typeeffect(  "You throw your [ITEM].\nThe troll turns toward the noise!\nNow's your chance!\n\nWhat do you do?\n1. Run for the exit door\n2. Try to grab treasure nearby",delay=0.1)
                throwChoice = int(input())
                match (throwChoice):
                    case 1:
                        clear_screen()
                        typeeffect("You sprint past the distracted troll!\nYou reach the door, throw it open, and ESCAPE!\n\n🎉 YOU SURVIVED! 🎉", delay=0.1)
                        time.sleep(2)
                        if not play_again():
                            quit()
                        else:
                            return 1  # Restart from room1
                    case 2:
                        clear_screen()
                        typeeffect("You reach for the shiny object...\nBut you're too slow! The troll turns back!\nGAME OVER! 💀",delay=0.1)
                        time.sleep(2)
                        play_again()
            else:
                clear_screen()
                typeeffect("You reach into your pockets...\nNothing.\nYou have nothing to throw.\nThe troll sleeps on, undisturbed.\nWhat now?")
                time.sleep(2)
                return 4

            #if player has something to throw

        case 4:
            return 3
def secretroom():
    global firsttimer5,findnote
    global findTourch
    clear_screen()
    if firsttimer5==True:
        typeeffect(
            "You pry open the rusty grate.\nBelow is a small hidden chamber.\nA SKELETON sits against the wall.\nIn its bony hand: a GLOWING TORCH!\n\nWhat do you do?\n\n",
            delay=0.1)
        typeeffect("Options:\n1. Take the glowing torch\n2. Search the skeleton\n3. Climb back up\n", delay=0.1)
        firsttimer5=False
    else:
        print("Options:\n1. Take the glowing torch\n2. Search the skeleton\n3. Climb back up\n")
    secretroomChoice = int(input())
    match (secretroomChoice):
        case 1:
            clear_screen()
            if findTourch==False:
                typeeffect("You got a GLOWING TORCH! (Add to inventory)\nIt never goes out! Magic!", delay=0.1)
                inventory.append("torch")
                findTourch = True
                time.sleep(2)
                return 5
            else:
                typeeffect("Its hand is empty now. Nothing left to take.",delay=0.1)
                time.sleep(2)
                return 5

        case 2:
            clear_screen()
            if findnote==False:
                typeeffect("You find a NOTE:\n\"The key is in the darkness. Light reveals truth.\"", delay=0.1)
                findnote=True
                inventory.append("note")
                time.sleep(2)
                return 5
            else:
                typeeffect("You search the skeleton again.\nJust bones and dust.\nNothing new.",delay=0.1)
                time.sleep(2)
                return 5

        case 3:
            clear_screen()
            return 1
userChoice = room1()
while True:
    match(userChoice):
        case 1:
            userChoice =room1()
        case 2:
            userChoice=room2()
        case 3:
            userChoice=room3()
        case 4:
            userChoice=room4()
        case 5:
            userChoice=secretroom()
