
#SETUP
yes_no = ['yes', 'no']
directions = ['left', 'right', 'forward', 'backward']

#INTRO
name = input("What is your adventurer's name?\n")
print('Greetings, ' + name + '. Its adventure time!' )
print("You are a doctor and you suddenly you wake up in the hospital")
print("after you stretch and stuff u recognized there is blood on the wall")
print("you hear a loud scream of somebody dying in the back of the hall")
print("you need a way to escape the building")
print("CAn YoU FiNd A wAy OuT?!")

#START
answer = ""
while answer not in yes_no:
    answer = input('would you like to escape?\nyes/no\n')
    if answer == 'yes':
        print('you start walking out of your room')
    elif answer == 'no':
        print('cool your dead!')
        quit()
    else:
        print("i don't understand that")

#BEGINNING OF THE GAME
answer = ""
while answer not in directions:
    print('To your left, you see the killer with red eyes ready to chase you')
    print('To your right you see another path to your doom ')
    print('There is a big broken window infront of you')
    print('Behind you is the room you woke up in')
    answer = input('What direction do you move? \nLeft/right/forward/backwards\n')
    if answer == 'left':
        print('he grabs you by your throat and slices your stomach and your organs falls on the ground.\nGameOver\n')
        quit()
    elif answer == 'right':
        print('you walk towards the next hall and u see more trails comming your way')
    elif answer == 'backward':
        print('You go back to sleep and you accepted your fate\nGameover\n')
        quit()
    elif answer == 'forward':
        print('you look outside of the window and you decide to jump of the window \nGameOver\n')
        quit()

#PART TWO OF THE GAME
answer = ""
while answer not in directions:
    print('to your left, you see a giant red door in flames')
    print('to your right, you see a long dark hallway')
    print('there is a big chest infront of you.')
    print('behind you is the killer.')
    answer = input('What direction do you move? \nLeft/right/forward/backwards\n')
    if answer == 'left':
        print('you walk towards the door and grab the doorknob, you open the door and you see everything is on fire, you decided to join and burn with it.\nGameOver\n')
        quit()
    elif answer == 'right':
        print('You run towards the dark hallway further away from the killer.')
    elif answer == 'backward':
        print('you walk towards the killer just to die in his hands\nGameOver\n')
        quit()
    elif answer == 'forward':
        print('u walk towards the chest and decided to open it, you open the chest and it ended up to be a boobytrap!\nGameOver\n')
        quit()

#PART THREE OF THE GAME
answer = ""
while answer not in directions:
    print("to your left, you see a bear who hasen't eaten in 10 years in your path")
    print('to your right, you see couple of scared nurses who need help')
    print('infront of you is a shining door')
    print('behind you is the killer but u found a gun laying around')
    answer = input('What direction do you move? \nLeft/right/forward/backwards\n')
    if answer == 'left':
        print("you walk past the bear's corpse and continue you're escape in hell")
    elif answer == 'right':
        print('you walk towards the scared nurses but it ended up to be the henchmen of the killer\nGameOver\n')
        quit()
    elif answer == 'backward':
        print("u grab the gun and shoot the killer, the killer didn't finch and ended up slicing your throat\nGameOver\n")
        quit()
    elif answer == 'forward':
        print('you walk towards the door and ended up falling in a put full of needles\nGameOver\n')
        quit()
    
#PART FOUR OF THE GAME
answer = ""
while answer not in directions:
    print('to your left is a simple door...')
    print('to your right is another human being crying for help')
    print('infront of you is a open window')
    print('behind you is the bloodthirsty killer')
    answer = input('What direction do you move? \nLeft/right/forward/backwards\n')
    if answer == 'left':
        print ("you walk towards the door and look in the little peep hole while opening the door, the gun in the other side pull the trigger and shot your brains out\nGameOver\n")
        quit()
    elif answer == 'right':
        print ("The crazy doctor start laughing while looking at you, he grabs you and put you in his electric chair, he start laughing more and raise the electricity to the max ending up killing you\nGameOver\n")
        quit()
    elif answer == 'backward':
        print('you accepted your fate and let the killer end your life\nGameOver\n')
        quit()
    elif answer == 'forward':
        print ('you jump out of the window and landed on a a glass surface, u broke your leg but you ae determined to move forward and escape')

#FINAL PART OF THE GAME
answer = ""
while answer not in directions:
    print('to your left you see the big exit gate of the hospital')
    print('to your right you see another exit gate but a bit smaller')
    print("infront of you is a gun w a note saying 'this is an shotgun to kill the killer but! if u kill him u got everything backwards'")
    print('behind you is the angry killer licking the blood of his machete')
    answer = input('What direction do you move? \nLeft/right/forward/backwards\n')
    if answer == 'left':
        print('you finally escaped the hospital!\nyou stepped into your car and drove out of the hospital\n \nYou Win\n')
    elif answer == 'right':
        print("you walk to the wat smaller exit gate, you open the door and the cardboard exit gate drop in your head, the killer is behind you and he finish you off")
        quit()
    elif answer == 'backward':
        print('you are in so much pain and just stopped walking cus of your broken leg\nGameOver\n')
        quit()
    elif answer == 'forward':
        print('you grab the gun and aim it to the killer, u shoot the gun but the barrel was aimed toward you instead of the killer, killing u at the end\nGameOver\n')
        quit()

#Game made by jahny and yu-lin
    
    





