def leader():
    board.append(player_go)
    return board
  
def bubble(): 
    swap=True
    while swap==True:
        swap=False
        for i in range(len(board)-1): 
            if board[i] > board[i+1]:  
                temp = board[i]  
                board[i]=board[i+1]  
                board[i+1]=temp  
                swap=True 
    board.reverse() 
    return board 

def player_attack():
    print("you",P_atk_method, "your",player_stats[6][0])
    P_heat_dam=randint(player_stats[6][1]-2,player_stats[6][1])+P_atk_bonus[0] +P_atk_method_bonus[0]
    P_electricity_dam=randint(player_stats[6][2]-2,player_stats[6][2])+P_atk_bonus[1]+P_atk_method_bonus[1]
    P_poison_dam=randint(player_stats[6][3]-2,player_stats[6][3])+P_atk_bonus[2]+P_atk_method_bonus[2]
    P_bludgeon_dam=randint(player_stats[6][4]-2,player_stats[6][4])+P_atk_bonus[3]+P_atk_method_bonus[3]
    P_cold_dam=randint(player_stats[6][5]-2,player_stats[6][5])+P_atk_bonus[4]+P_atk_method_bonus[4]
    P_attack_dam=[P_heat_dam,P_electricity_dam,P_poison_dam,P_bludgeon_dam,P_cold_dam]
    #for i in range(len(P_attack_dam)):
        #print(P_attack_dam[i])
    #print()
    return P_attack_dam

def boss_guard():
    E_heat_def=randint(boss_stuff[1]-2,boss_stuff[1])
    E_electricity_def=randint(boss_stuff[2]-2,boss_stuff[2])
    E_poison_def=randint(boss_stuff[3]-2,boss_stuff[3])
    E_bludgeon_def=randint(boss_stuff[4]-2,boss_stuff[4])
    E_cold_def=randint(boss_stuff[5]-2,boss_stuff[5]) #######################################on all of these add things for bonus effect of items and leveled up stats!!!!!!!!!!!!!!!!!!!!!!!!!!!
    E_guard_def=[E_heat_def,E_electricity_def,E_poison_def,E_bludgeon_def,E_cold_def]##################also need to add changes and luck variation for each attack
    #for i in range(len(E_guard_def)):
        #print(E_guard_def[i])
    #print()
    return E_guard_def



def boss_attack():
    print(boss_stuff[0],"retaliates as they",E_atk_method,"their",boss_stuff[6][0])
    E_heat_dam =randint(boss_stuff[6][1]-2,boss_stuff[6][1])
    E_electricity_dam =randint(boss_stuff[6][2]-2,boss_stuff[6][2])
    E_poison_dam =randint(boss_stuff[6][3]-2,boss_stuff[6][3])#for i in range these to make em shorter
    E_bludgeon_dam =randint(boss_stuff[6][4]-2,boss_stuff[6][4])
    E_cold_dam =randint(boss_stuff[6][5]-2-2,boss_stuff[6][5])
    E_attack_dam=[E_heat_dam,E_electricity_dam,E_poison_dam,E_bludgeon_dam,E_cold_dam]
    #for i in range(len(E_attack_dam)):
        #print(E_attack_dam[i])
    #print()
    return E_attack_dam


def player_guard():
    P_heat_def = randint(player_stats[1]-2,player_stats[1]) + player_stats[7][1]
    P_electricity_def = randint(player_stats[2]-2,player_stats[2]) + player_stats[7][2]
    P_poison_def = randint(player_stats[3]-2,player_stats[3] + player_stats[7][3])
    P_bludgeon_def = randint(player_stats[4]-2,player_stats[4] + player_stats[7][4])
    P_cold_def = randint(player_stats[5]-2,player_stats[5] + player_stats[7][5])
    P_guard_def=[P_heat_def,P_electricity_def,P_poison_def,P_bludgeon_def,P_cold_def]
    #for i in range(len(P_guard_def)):
        #print(P_guard_def[i])
    return P_guard_def


#boss_stuff[0]=Enemy_name
#boss_stuff[1]=E_heat_def
#boss_stuff[2]=E_electricity_def
#boss_stuff[3]=E_poison_def
#boss_stuff[4]=E_bludgeon_def
#boss_stuff[5]=E_cold_def
#boss_stuff[6]=E_weapon
#boss_stuff[7]=E_cheat
#boss_stuff[8]=E_active
#boss_stuff[9]=boss_number
#boss_stuff[10]=boss_room
#boss_stuff[11]=boss_department
#boss_stuff[12]=other rooms you can go to in department
#boss_stuff[13]=HP


    
    print()# COULD TURN INTO WHILE LOOP IN MAIN CODE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def title():
    print("\n")
    sleep(PAUSE)    
    print(" _____   _____          _____   _____             _____   _____      _____                    ____     _____            _____      ")
    sleep(PAUSE)
    print("|       |      |     | |     | |     | |         |     | |          |       |     |    /\    |    \   |     | |      | |            ")
    sleep(PAUSE)
    print("|       |      |     | |     | |     | |         |     | |          |       |     |   /  \   |     |  |     | |      | |         "        )
    sleep(PAUSE)
    print("|_____  |      |-----| |     | |     | |         |     | |____      |_____  |-----|  /___\  |     |  |     | |      | |____        ")
    sleep(PAUSE)
    print("      | |      |     | |     | |     | |         |     | |                | |     | |      | |     |  |     | \  /\  /       |    ")
    sleep(PAUSE)
    print("_____| |____ |     | |____| |_____| |____    |_____| |          ______| |     | |      | |____/   |_____|  \/  \/  ______|")
    sleep(PAUSE)
    print("\n")
    sleep(PAUSE)
    print("))--------------------------------------------------<THE OFTED MENACE>------------------------------------------------------((")   
    print("\n") #MUST ADD INTRO DETAILS FOR STORY LIKE STAR WARS OPENING SCROLE
    sleep(PAUSE)
    print("It is dark times at AGSB...")
    print("\n")
    sleep(PAUSE)
    print("The headmaster has been removed from power and now serves the tight grip of Ofted which now controls us all")
    print("\n")
    sleep(PAUSE)
    print("they enforced harsher restrictions through their puppets, the teachers")
    print("\n")
    sleep(PAUSE)
    print("no ball games")
    print("\n")
    sleep(PAUSE)
    print("no recreational time")
    print("\n")
    sleep(PAUSE)
    print("no talking...EVER!")
    print("\n")
    sleep(PAUSE)
    print("no nice food")
    print("\n")
    sleep(PAUSE)
    print("no leaving school at 3:25")
    print("\n")
    sleep(PAUSE)
    print("and as the student body rebelled, we were all crushed... placed in detention or worse")
    print("\n")
    sleep(PAUSE)
    print("for those of us that fought back hard enough against ofsted's tyranical rule, we were suspended")
    print("\n")
    sleep(PAUSE)
    print("but no longer ")
    print("\n")
    sleep(PAUSE)
    print("our suspension ends today")
    print("\n")
    sleep(PAUSE)
    print("ofsted ends today")
    print("\n")
    sleep(PAUSE)
    print("join us fellow student and together we shall free the school and return it to glory!")
    for i in range(70):
          print()
    print("you walk in through the main entrance as",random.choice(weather_list),"reception and llok around")
    sleep(PAUSE)
    print("on either side of you, the corridoor is bleak and lifeless exept for the faint echoes of teachers' footsteps")
    sleep(PAUSE)
    print("you walk over to reception and find it empty apart from a misplaced lanyard")
    sleep(PAUSE)
    print("a sacred thing that allows you to send teachers to detention once they have been defeated")
    sleep(PAUSE)
    print("you imediately set up a computer and create a card with your details...")
    sleep(PAUSE)

def credit():
    print()
    print("                    Thank you for playing...")
    print()
    print("              School of Shadows: The Ofsted Menace")
    print()
    sleep(PAUSE)
    print("                   An AGSB role playing game")
    print()
    sleep(PAUSE)
    print("                Original game by J.Timmins 2018")
    print()
    sleep(PAUSE)
    print("                    Updated by W.Carr 2023")
    print()
    sleep(PAUSE)
    print("                   Modified by E.Aloul 2023")
    print()
    sleep(PAUSE)
    print("                     Directed by E.Aloul")
    print()
    sleep(PAUSE)
    print("                     released by E.Aloul")
    print()
    sleep(PAUSE)
    print("                     Based on real events")
    print()
    sleep(PAUSE)
    print("               Inspired by all cool pop culture")
    print()
    sleep(PAUSE)
    print("                A story written by Edward Aloul")
    print()
    sleep(PAUSE)
    print("           Here at AGSB we are grateful for your time")
    print()
    sleep(PAUSE)
    print("  And we apologise that some features of the game are not complete")
    print()
    sleep(PAUSE)
    print("              After all this is a work in progress")
    print()
    sleep(PAUSE)
    print("                  Not the final game experience")
    print()
    sleep(PAUSE)
    print(" And the studio executives privided us with a limiting release date")
    print()
    sleep(PAUSE)
    print("    Especially with the ambition of our creative and coding teams")
    print()
    sleep(PAUSE)
#                                                                    FINAL VERSION!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!





def P_character():
    print("before you begin your quest to save the school,select a character background for  you to play as and evolve as you progress")
    print("your chosen class will supply you with a UNIFORM, WEAPON, and STARTING STATS that are unique to that class and a SCHOOL BAG INVENTORY to get you started")
    print("as you journey on, you can add to these STATS, change your WEAPON and UNIFORM and aquire more items to add to your SCHOOL BAG")
    sportsman=["SPORTSMAN",6,7,3,4,9,cricket_bat,Summer_PE,60,"(1)"]
    musician=["MUSICIAN",8,4,2,7,1,violin,norm_uniform,70,"(2)"]
    librarian=["LIBRARIAN",6,4,8,9,1,library_book,norm_uniform,40,"(3)"]
    prankster=["PRANKSTER",6,4,10,8,2,whoopee_cushion,norm_uniform,70,"(4)"]##################add outfits to these and items and 1 cheat code
    new=["NEW STUDENT",0,0,0,0,0,toilet_roll,lost_uniform,30,"(5)"]
    char_list=[sportsman, musician, librarian, prankster, new]
    stat_rep=["class      :","heat       :","electricity:","poison     :","bludgeon   :","cold       :","weapon     :","attire     :","HP         :","to select press:"]
    print("your options are:")
    print()

    for char in char_list:
        for i in range(len(stat_rep)):
            if i==6 or i==7:
                print(stat_rep[i],char[i][0])#########need for items 
            elif i==0 or i==9:
                print(stat_rep[i],char[i])
                sleep(PAUSE)  
            
            else:
                print(stat_rep[i],char[i])
               
        print()##################################add items first
    


    print("select a background(use the number)")
    P_class=input(">")
    if P_class == "2":
        P_stuff=musician
    elif P_class == "3":
        P_stuff=librarian
    elif P_class == "4":
        P_stuff=prankster
    elif P_class == "5":
        P_stuff=new
    else:
        P_stuff=sportsman
    print("you have chosen the",P_stuff[0])
    
    print()
    return P_stuff

def bag():
    print()
    print("SCHOOL BAG!:")
    print()
    for i in inventory:
        if i[0]  == "WEAPONS:":
            print("WEAPONS:")
            for s in i[1:]:
                print(">",s[0])
            print("\n")
        elif i[0]  == "ATTIRES AND ARMOURS:":
            print("ATTIRES AND ARMOURS:")
            for s in i[1:]:
                print(">",s[0])
            print("\n")

        elif i[0]  == "SPECIAL ITEMS:":
            print("SPECIAL ITEMS:")
            for s in i[1:]:
                print(">",s[0])
            print("\n")

        else:
            print("CHEAT CODES:")
            for s in i[1:]:
                print(">",s[0])
            print("\n")
    norm_menu()

def loadout():
    print("Change Weapon: (1)")
    print("DONE         : (2)")
    loadout_menu_choice=int(input(">"))
    if loadout_menu_choice== 1:
        
        for i in range(len(inventory[0])):
            print(i,i[0])
    else:
        norm_menu()


def maps():
    print()
    print("            [Music]")
    print("               |")
    print("               |")
    print("[Physics]-------------------[Technology]------[English]---------------------------------------[The Grammar]")
    print("               |                                  |                                                 |")
    print("               |                                  |                                                 |")
    print("               |                                  |                                                 |")
    print("               |                                  |   [Coleman Hall]                           [Economics] ")
    print("               |                                  |         |                                       |    ")
    print("               |            [Food Tech]           |         |                                       |    ")
    print("               |                 |                |         |                                       |    ")
    print("          [Chemistry]----------------------------------[Reception]---[Geograpy]---[Philosophy]---[Maths]  ")
    print("               |                 |                |                             |             ")
    print("           [Biology]           [Art]---------[Languages]                [Computer Science]   ")
    print()
    
def navigation():
    global times
    global rooms
    global boss_stuff
    
    #previous_location=boss_stuff
    boss_stuff=0
    maps()
    if len(rooms)>0:
        for i in range(len(rooms)):
            print(i,")",rooms[i][10])
    else:
        times=times+1
        if times==1:
            rooms.append(coleman)
        elif times==2:
            rooms.append(coleman_stage)
        else:
            print("YOU LIBERATED THE SCHOOL")
            win= True
            lives = 0
            
    
    while boss_stuff==0:
        global num1
        print("where do you wish to travel?(use the number)")
        next_location=int(input(">"))
        num1=next_location
        if next_location<=len(rooms) and next_location>=0:
            boss_stuff=rooms[next_location]
        else:
            boss_stuff=0
            print("try again")
    

        

# Starting location

    


    
        
        
    

def active():
    verdict=0
    store=0
    for i in range(len(defeated_bosses)):
        if boss_stuff[0]==defeated_bosses[i]:
            store=1
        else:
            verdict=0
    if store==1:
        verdict=0
    else:
        verdict=1
    return verdict
    
def action_menu():
    print()
    print("attacks:")
    print("standard:(1)")
    print("ranged  :(2)")
    print("heavy   :(3)")
    print()
    print("how will you proceed?")
    action=input(">")
    if action == "2":
        P_attack_description = player_stats[6][7]
    elif action == "3":
        P_attack_description = player_stats[6][8]
    elif action=="1":
        P_attack_description = player_stats[6][6]
    else:
        P_attack_description=action
    return P_attack_description

def atk_method_mod_calc():
    if P_atk_method==player_stats[6][7]:
        type_mod=[2,2,2,2,2]
    elif P_atk_method==player_stats[6][8]:
        type_mod=[4,4,0,2,0]
    elif P_atk_method==player_stats[6][8]:
        type_mod=[0,0,4,2,4]
    else:
        type_mod=[0,0,0,0,0]
    return type_mod
    

def norm_menu():
    print()
    print("level up        :(1)")
    print("open school bag :(2)")
    print("change loadout  :(3)")# add feature somewhere ehere they can view stats
    print("continue journey:(4)")
    print()
    print("how will you proceed?")
    norm_choice=input(">")
    if norm_choice=="1":
        level_up()
    elif norm_choice=="2":
        bag()
    elif norm_choice=="3":
        loadout()
    else:
        navigation()#this is like where next but sort it out some point

def level_up():
    global spend_points
    global level
    chosen_level=[]
    print("your current stats will affect the damage you deal and your defence")
    print("available points to spend:",spend_points)
    level=level+spend_points
    level_display=["heat       :","electricity:","poison     :","bludgeon   :","cold       :"]
    
    for i in range(len(level_display)):
        number0= i+1
        print(level_display[i],player_stats[i+1],"   ("+ str(number0)+")")
    print()
    while spend_points > 0:
        print("which stat do you want to increase?")
        stat_inc_choice=input(">")
        if stat_inc_choice=="2":
            chosen_level=["electricity",player_stats[2]]
            
        elif stat_inc_choice=="3":
            chosen_level=["poison",player_stats[3]]
            

        elif stat_inc_choice=="4":
            chosen_level=["bludgeon",player_stats[4]]
           
        elif stat_inc_choice=="5":
            chosen_level=["cold",player_stats[5]]
            
        else:
            chosen_level=["heat",player_stats[1]]
        stored_level=chosen_level[1]
        print("You have chosen to increase your",chosen_level[0],"stat")
        print("available points:",spend_points)
        print("How many levels do you want to spend on",chosen_level[0],"?")
        num_levels=int(input(">"))
        while num_levels > int(spend_points):
            print("you don't have enough points for that!")
            print("Please try again")
            num_levels=int(input(">"))
        chosen_level[1]=chosen_level[1]+num_levels
        spend_points=spend_points-num_levels
        print()
        print(chosen_level[0],":")
        print(stored_level,">",chosen_level[1])
        print()
        if stat_inc_choice=="2":
            player_stats[2]=chosen_level[1]
            
        elif stat_inc_choice=="3":
            player_stats[3]=chosen_level[1]
            

        elif stat_inc_choice=="4":
            player_stats[4]=chosen_level[1]
           
        elif stat_inc_choice=="5":
            player_stats[5]=chosen_level[1]
            
        else:
            player_stats[1]=chosen_level[1]
        for i in range(len(level_display)):
            print(level_display[i],player_stats[i+1],"   (",i+1,")")
        print()
        print("available points:",spend_points)
      
            
        
    norm_menu()

def P_atk_bonus_calc():
    for i in range(5):
        if player_stats[i+1] > 4:
            P_atk_bonus[i]=player_stats[i+1] - 5
        else:
            P_atk_bonus[i]=0                       



def P_dead_check():
    global lives
    global losses
    if player_stats[8]==0:
        lives=lives-1
        losses=losses+1
        if lives > 0:
            print()
            print("you have been defeated by",boss_stuff[0],"of",boss_stuff[10])
            boss_stuff[13]=normal_boss_HP
            
            print()
            print("lives:",lives)
            print()
            print("At that exact moment the large hadron collider in Cern, Switzerland MALFUNCTIONED, causing a TEMPORAL SHIFT which caused the space time continuum to SCEW into an alternate version of",year,"running 10 minutes behind the original in which you were never defeated by",boss_stuff[0],"and are still at your previous location")#add prvious location
            


def E_dead_check():
    if boss_stuff[13]<0:
        boss_stuff[13]=0
        


    

#def next(): CONTINUE

import datetime
# Used to generate random numbers
import random
# Role playing game  
# Original J.Timmins 2018  
# Updated W.Carr 2023  
#modified E.Aloul 2023  
#---------------------------Import modules--------------------------------------  
from random import randint
from time import sleep

spend_points=0
year = datetime.datetime.today().year
PAUSE = 0.75#########################
board = []
weather_list=["the sun shines brightly throgh the windows into","a bleak frost chills the room with an icy blue light from the raging blizzard outside of","lightning streams from the sky and the room shakes from the raging storm outside of","you hear the rain violently beat at the windows of","a forboding fog seeps in through the windows from the grey light cast off of the sky beyond"]
#----------------------ITEMS-------------------------------------
#----------------------CLOTHES-------------------------------------
Summer_PE=["INDOOR PE KIT",2,2,0,4,0,"(1)"]
norm_uniform=["SCHOOL UNIFORM",1,1,1,1,3,"(2)"]
lost_uniform=["UNIFORM FROM LOST PROPERTY",1,0,0,1,0,"(3)"]

#-----------------------WEAPON STATS--------------------------------------------------------------------------------------
van_der_graaf_generator=[
    "VAN DER GRAAF GENERATOR",
    5,
    10,
    4,
    2,
    7,
    "swing",
    "send forth a beam of electricity bolts from",
    "release of devastating small field of electricity from","(1)"
    ]#ENEMY  weapon ATTACK stats
cricket_bat=["CRICKET BAT",3,2,5,10,3,"swing","fire off a ball in a perfect line with","perform a flurry of powerful blows with","(2)"]#PLAYER Weapon ATTACK stats
trebuchet=["TREBUCHET",4,2,4,10,3,"release the throwing arm with force into the opponent","load up a metal projectile and fling it through the air at the enemy","swing the the pouch around you violently","(3)"]
whoopee_cushion=["WHOOPEE CUSHION",5,3,10,13,1,"slap the opponent with","release the toxic air straight towards the opponent by squeezing","push the opponent, causing them to fall onto","(5)"]
library_book=["LIBRARY BOOK",7,2,5,8,3,"sweep the air with","throw a sharp paper aeroplane through the air using pages from","violently slam the pages shut creating a larhe shockwave with","(6)"]
violin=["VIOLIN", 7,5,3,7,4,"thrust your bow through the air from","skillfully play the violin, sending waves of powerful melodies from","release a deafening screech across the room from","(7)"]
toilet_roll=["TOILET ROLL",0,0,0,12,0,"unspool a length of paper and swing it like a whip from","send long reaching streams of bog paper through the air","wrap up the opponent with many layer of roll and pull it tightly, temporarily squeezing them","(8)"]
bike=["BIKE",7,4,2,6,0,"ring the bell creating a deafening wave of sound","drive into the opponent with","perform a BMX spin, knocking over the opponent with","(9)"]
rock=["ROCK",3,4,10,14,2,"swing with","break off a small part and throw it through the air with","dazzle the opponent with shining crystals and proceed to smack them with","(10)"]
pencil=["QUANTUM PENCIL", 5,10, 0, 3, 0, "zap your enemies with a surge of electric current from", "unleash a devastating heat wave with", "strike with precision using"]
rubber=["NANOBOT ERASER", 0, 8, 2, 0, 5, "electrify your opponents as", "poison your foes with a corrosive discharge from", "freeze your adversaries with"]
chem_launcher=["CHEMICAL REACTION LAUNCHER", 7, 0, 3, 0, 4, "ignite explosive reactions as", "unleash a stream of noxious fumes from", "chill your enemies with"]
compass=["GEOMETRIC COMPASS OF DOOM", 3, 0, 0, 9, 5, "pierce through defenses like a deadly needle with", "deliver a powerful bludgeoning blow using", "engulf your opponents in an icy vortex with"]
maths_gun=["MATHEMATICAL EQUATION BLASTER", 4, 6, 0, 0, 7, "solve equations and shoot energy bolts as", "shock your foes with", "shatter your enemies with"]
ruler=["PHYSICS-DEFYING RULER", 8, 0, 0, 6, 2, "bend the laws of physics with", "deliver a crushing blow using", "send forth a devastating surge of cold energy from"]
mutator=["BIOLOGY MUTATION EMITTER", 0, 3, 10, 0, 6, "manipulate DNA to unleash a biological shockwave as", "inflict venomous bites with", "surround your foes with a toxic cloud using"]
laser=["LASER POINTER OF DISRUPTION", 9, 4, 0, 0, 3, "dazzle and disorient your opponents with", "release a barrage of electric bolts from", "engulf your enemies in a blazing beam of"]
pen=["INFINITE INK PEN", 6, 6, 0, 2, 2, "draw intricate symbols and release them as energy projectiles with", "shock your adversaries using", "unleash a bludgeoning assault with"]
robot=["ROBOTICS CLUB BATTLE BOT", 10, 0, 0, 10, 0, "command the robotic ally to attack alongside", "crush the opponent with the mechanical might of", "freeze your foes with the robot's powerful"]
sword=["LITERATURE SWORD OF KNOWLEDGE", 3, 0, 0, 8, 4, "slash through ignorance and darkness with", "deliver precise strikes using", "engulf your adversaries in a chilling mist with"]
time_machine=["HISTORY TIME MANIPULATOR", 0, 9, 0, 5, 5, "bend the fabric of time to electrify your opponents with", "send forth devastating blasts of electricity from", "plunge your enemies into an icy time warp with"]
brush=["ARTISTIC BRUSH OF ILLUSION", 0, 0, 6, 0, 10, "paint illusions that confuse and disorient your foes as", "unleash a toxic paint splatter with", "create a freezing blizzard using"]
amp=["MUSIC SONIC AMPLIFIER", 6, 3, 0, 0, 9, "shatter the eardrums of your enemies with", "release electrifying shockwaves from", "surround your foes with a chilling melody using"]
trapdoor=["DRAMA STAGE TRAPDOOR", 0, 0, 4, 6, 8, "unleash a hidden trapdoor to surprise your opponents as", "deliver a powerful bludgeoning blow using", "engulf your enemies in a freezing mist from"]
sport_launcher=["SPORTS EQUIPMENT LAUNCHER", 8, 0, 0, 10, 0, "hurl various sports equipment at high velocity with", "crush your enemies using", "freeze your foes with the icy impact of"]
compiler=["PROGRAMMING CODE COMPILER", 0, 10, 0, 0, 5, "compile and execute devastating code attacks as", "send forth a barrage of electric bolts from", "surround your adversaries in a chilling binary field with"]
langun=["LANGUAGE TRANSLATOR RAY GUN", 9, 5, 0, 0, 4, "translate your opponents' words into electric shocks with", "zap your foes using", "freeze your enemies with"]
orbiter=["GEOGRAPHY ATLAS ORBITER", 0, 0, 8, 3, 6, "launch spinning globes to strike your opponents from", "unleash a poisonous mist using", "engulf your adversaries in a freezing blizzard from"]
bank_hax=["ECONOMICS MONEY MANIPULATOR", 5, 0, 7, 0, 3, "hurl coins at your enemies, causing electric shocks with", "strike your adversaries using", "surround your foes in a chilling financial storm with"]
food_canon=["HOME ECONOMICS FOOD FIGHT CANNON", 7, 0, 0, 9, 2, "blast your opponents with an array of food projectiles from", "crush your foes using", "freeze your enemies with the icy impact of"]
mind=["PSYCHOLOGY MIND CONTROL HELMET", 0, 8, 5, 0, 7, "manipulate your enemies' minds with a powerful helmet as", "shock your adversaries with", "plunge your foes into a frozen state of confusion with"]
lang_bomb=["FOREIGN LANGUAGE CONFUSION GRENADE", 0, 6, 4, 0, 8, "confuse and disorient your opponents with a language grenade that", "electrify your foes with", "surround your enemies with a freezing mist created by"]
hacker=["COMPUTER LAB HACKING KEYBOARD", 10, 0, 0, 3, 7, "hack into the digital realm and electrocute your foes with", "send forth a barrage of electric bolts from", "freeze your adversaries with the power of"]
saw_gun=["WORKSHOP SAWBLADE SHOOTER", 9, 0, 0, 10, 2, "shoot deadly sawblades at your enemies with", "deliver a crushing blow using", "surround the opponent with blades, cutting themas they escape using"]
drums=["RHYTHM DRUMS", 0, 0, 0, 10, 6, "unleash a thunderous rhythm that disorients your opponents from", "crush your enemies using the power of", "freeze your foes with the deafening impact of"]
flute=["HARMONY FLUTE", 0, 5, 0, 0, 9, "entrance and mesmerize your enemies with melodic tunes from", "electrify your foes with the power of", "create a freezing whirlwind using"]
ball_gun=["FOOTBALL CANNON",8, 0, 0, 10, 3,"launch high-velocity footballs at your enemies from","crush your foes using","freeze your adversaries with the icy impact of"]
basket=["BASKETBALL SLAMMER",10, 0, 0, 8, 5,"slam powerful basketballs into your opponents as","deliver a devastating blow using","engulf your enemies in a freezing mist from"]
gene=["GENE MANIPULATOR",0, 7, 10, 0, 4,"manipulate genetic codes to unleash a biological shockwave as","inflict venomous bites with","surround your foes with a toxic cloud using"]
palette=["PALETTE BLADE",0, 0, 6, 10, 4,"paint illusions that confuse and disorient your foes as","unleash a toxic paint splatter with","create a freezing blizzard using"]
sodexo=["SODEXO CARD SLICER",5, 0, 0, 8, 3,"slash through your enemies with the sharp edge of the Sodexo card as","deliver a powerful bludgeoning blow using","engulf your foes in a freezing mist from"]
langsword=["LINGUISTIC BLADE", 6, 0, 0, 8, 4, "carve through your enemies' defenses with the precision of", "strike your adversaries using", "engulf your foes in a freezing mist from"]
lang_rapier=["TRANSLATION RAPIER", 0, 6, 4, 0, 8, "shock and disorient your enemies with the linguistic prowess of", "electrify your foes using", "surround your adversaries with a chilling mist created by"]
bow=["IDIOM BOW", 0, 5, 6, 0, 7, "shoot linguistic arrows of confusion at your enemies with the", "zap your foes using", "freeze your enemies with the power of"]
atlas=["ATLAS HAMMER", 0, 0, 8, 10, 5, "crush your enemies with the weight of", "deliver a powerful blow using", "create a freezing blizzard using"]
tornado=["TORNADO WHIP", 0, 8, 0, 10, 0, "whip up destructive tornadoes to strike your enemies with the force of", "electrify your foes using", "create a freezing blizzard using"]
atari=["ATARI BLASTER", 0, 10, 0, 6, 0, "unleash a barrage of retro gaming energy blasts from", "electrify your foes using", "engulf your adversaries in a freezing mist from"]
gun=["MILITARY PISTOL",8, 0, 0, 10, 0,"precisely strike your enemies with lethal accuracy from","deliver a powerful concussive blow using","unleash a blinding flashbang effect to disorient your foes from"]
ethic_sword=["LOGIC SWORD", 0, 6, 0, 8, 0, "wield the power of logical reasoning to strike your enemies with", "deliver a morally just blow using", "envelop your foes in a serene aura of wisdom using"]
ofsted=["OFSTED AUDITOR",0, 10, 0, 0, 8,"evaluate your enemies with meticulous scrutiny from","deliver a devastating report using","envelop your adversaries in a chilling atmosphere of accountability using"]
phone=["PHONE OF CONNECTIVITY",0,3,1,5,0,"swing at the air with","play a loud ring tone with","hand up, dealing imense emotional damege with"]
#weapon[0]=name
#weapon[1]=heat
#weapon[2]=electricity
#weapon[3]=poison
#weapon[4]=bludgeoning
#weapon[5]=cold
#weapon[6]=stanasrd
#weapon[7]=range
#weapon[8]=heavy


#-----------------------CHARACTER STATS-----------------------------------------------------------------------------------
#character="SPORTSMAN"
#P_heat_def=6
#P_electricity_def=7
#P_poison_def=3
#P_bludgeon_def=4
#P_cold_def=9
#P_weapon=ruler#cricket_bat
#Payer_HP=50
#player_stats=[character,P_heat_def,P_electricity_def,P_poison_def,P_bludgeon_def,P_cold_def,P_weapon,Payer_HP]#PLAYER DEFENCE stats


#-----------------------SPECIFIC BOSS------------------------------------------------------------------------------------------
PC1=["SPEEDY LEE",5,4,3,6,2,bike,"(Slowly!)",1,6,"PC1","the PHYSICS DEPARTMENT"," ",70,1]
PC2=["MR GIFFIN",5,4,3,6,2,rock,"(GIFFIN!!)",1,6,"PC2","the PHYSICS DEPARTMENT"," ",70,1]
physics_department=["MR REEDER",6,3,7,8,3,van_der_graaf_generator,"(TSilver!)",1,6,"the PHYSICS DEPARTMENT HALLWAY","the PHYSICS DEPARTMENT"," ",50,1]


english_department=["MISS CHAPMAN",4,6,2,4,3,sword," ",1,6,"the ENGLISH DEPARTMENT HALLWAY","the ENGLISH DEPARTMENT"," ",80,1]
E6=["MR KEANEY",5,2,8,4,1,pencil," ",1,6,"E6","the ENGLISH DEPARTMENT"," ",100,1]
library=["MISS MAHONY",8,2,4,7,3,pen," ",1,6,"the LIBRARY","the ENGLISH DEPARTMENT"," ",100,1]

maths_department=["MISS SHORT",2,3,1,5,7,rubber," ",1,6,"the MATHS DEPARTMENT HALLWAY","the MATHS DEPARTMENT"," ",80,1]#
S16=["MR AYEBARE",5,5,5,5,100,maths_gun," ",1,6,"S16","the MATHS DEPARTMENT"," ",100,1]#
S14=["MR GOOCH",1,1,2,3,5,compass," ",1,6,"S14","the MATHS DEPARTMENT"," ",90,1]#

music_department=["MR MONUMENT",1,1,1,1,1,amp," ",1,6,"the MUSIC DEPARTMENT HALLWAY","the MUSIC DEPARTMEN"," ",70,1]#
MU8=["MR SMITH 3",2,3,7,3,2,drums," ",1,6,"MU8","the MUSIC DEPARTMEN"," ",70,1]#
MU9=["MISS JARRAT",10,4,1,4,2,flute," ",1,6,"MU9","the MUSIC DEPARTMEN"," ",70,1]#

technology_department=["MR CUNDICK",8,4,4,7,0,saw_gun," ",1,6,"the TECHNOLOGY DEPARTMENT HALLWAY","the TECHNOLOGY DEPARTMENT"," ",100,1]#
T1=["MR SMITH 1",8,4,4,7,0,robot," ",1,6,"T1","the TECHNOLOGY DEPARTMENT"," ",70,1]#
T2=["MR BAKER",10,10,10,10,10,trebuchet," ",1,6,"T2","the TECHNOLOGY DEPARTMENT"," ",100,1]#

grammar=["MR MEAKIN",5,2,6,12,6,sport_launcher," ",1,6,"the GRAMMAR CANTEEN","the PE DEPARTMENT"," ",120,1]#
astro=["MR RAWSON",4,6,2,7,3,ball_gun," ",1,6,"the ASTROTURF","the PE DEPARTMENT"," ",130,1]#
peel_hall=["MR SOULSBY",100,2,4,1,6,basket," ",1,6,"the PEEL HALL","the PE DEPARTMENT"," ",140,1]#

chemistry_department=["DR MARSDEN",10,10,30,10,10,chem_launcher," ",1,6,"the CHEMISTRY DEPARTMENT HALLWAY","the CHEMISTRY DEPARTMENT"," ",100,1]#
N9=["MR FLANAGAN",5,3,10,3,8,laser," ",1,6,"N9","the CHEMISTRY DEPARTMENT"," ",120,1]#
N4=["MRS HILL",3,5,7,3,6,time_machine," ",1,6,"N4","the CHEMISTRY DEPARTMENT"," ",120,1]#

biology_department=["DR THOMAS",7,3,2,6,1,mutator," ",1,6,"the BIOLOGY DEPARTMENT HALLWAY","the BIOLOGY DEPARTMENT"," ",80,1]#
N13=["MS WELSBY",4,7,2,5,6,mind," ",1,6,"N13","the BIOLOGY DEPARTMENT"," ",90,1]#
N14=["MR KIDD",2,5,3,7,5,gene," ",1,6,"N14","the BIOLOGY DEPARTMENT"," ",90,1]#

food_department=["MRS GORDON",13,5,6,3,0,food_canon," ",1,6,"F1","the FOOD DEPARTMENT"," ",100,1]#
Stamford_hall=["SODEXO STAFF",20,10,50,20,10,sodexo," ",1,6,"the STAMFORD HALL","the FOOD DEPARTMENT"," ",100,1]#

art_department=["MISS COOK",5,4,7,3,2,brush," ",1,6,"the ART DEPARTMENT HALLWAY","the ART DEPARTMENT"," ",120,1]#
A1=["MRS LEE",7,4,5,6,3,ruler," ",1,6,"A1","the ART DEPARTMENT"," ",130,1]#
A2=["MISS UNDERWOOD",1,5,3,8,6,palette," ",1,6,"A2","the ART DEPARTMENT"," ",130,1]#

languages_department=["MRS WALLWORK",1,5,3,4,7,langun," ",1,6,"the LANGUAGES DEPARTMENT HALLWAY","the LANGUAGES DEPARTMENT"," ",90,1]#
C13=["MRS BLAKELEY",8,2,4,6,0,langsword," ",1,6,"C13","the LANGUAGES DEPARTMENT"," ",90,1]#
C16=["MRS BRENNAN",4,6,2,6,1,lang_rapier," ",1,6,"C16","the LANGUAGES DEPARTMENT"," ",90,1]#
C18=["MRS DING",8,3,4,7,5,bow," ",1,6,"C18","the LANGUAGES DEPARTMENT"," ",90,1]#

geography_department=["MRS WEIL",8,3,2,5,8,orbiter," ",1,6,"the GEOGRAPHY DEPARTMENT HALLWAY","the GEOGRAPHY DEPARTMENT"," ",70,1]#
S1=["MR BROMLEY",1,1,10,4,10,atlas," ",1,6,"S1","the GEOGRAPHY DEPARTMENT"," ",70,1]#
S2=["MR WILLIAMS",2,7,6,3,4,tornado," ",1,6,"S2","the GEOGRAPHY DEPARTMENT"," ",70,1]#

computer_department=["MR CARR",10,10,10,10,10,compiler," ",1,6,"the COMPUTER SCIENCE DEPARTMENT HALLWAY","the COMPUTER SCIENCE DEPARTMENT"," ",100,1]#
S9=["MR CUMMINS",4,10,4,6,3,hacker," ",1,6,"S9","the COMPUTER SCIENCE DEPARTMENT"," ",90,1]#
Engine_room=["lORD TIMMINS OF MOBBERLEY!!!",50,50,50,50,50,atari,"(NOT TODAY!)",1,6,"the ENGINE ROOM","the COMPUTER SCIENCE DEPARTMENT"," ",70,100]#

philosophy_department=["MR PERKINS",6,5,2,5,3,ethic_sword," ",1,6,"the PHILOSOPHY DEPARTMENT HALLWAY","the PHILOSOPHY DEPARTMENT"," ",90,1]#

economics_department=["MR SMITH 2",4,3,6,5,4,bank_hax," ",1,6,"the ECONOMICS DEPARTMENT HALLWAY","the ECONOMICS DEPARTMENT"," ",100,1]


reception= ["RECEPTIONIST",1,1,1,1,1,phone," ",1,6,"RECEPTION","the SCHOOL"," ",50,1]
coleman=["MR WRIGHT",15,15,15,15,15,gun," ",1,6,"the COLEMAN HALL ENTRANCE","the SCHOOL"," ",150,1]#
coleman_stage=["GREG THE OFTED INSPECTOR",17,17,17,17,17,ofsted," ",1,6,"the COLEMAN HALL STAGE","the SCHOOL"," ",200,1]

#boss_stuff[0]=Enemy_name
#boss_stuff[1]=E_heat_def
#boss_stuff[2]=E_electricity_def
#boss_stuff[3]=E_poison_def
#boss_stuff[4]=E_bludgeon_def
#boss_stuff[5]=E_cold_def
#boss_stuff[6]=E_weapon
#boss_stuff[7]=E_cheat
#boss_stuff[8]=E_active
#boss_stuff[9]=boss_number
#boss_stuff[10]=boss_room
#boss_stuff[11]=boss_department
#boss_stuff[12]=other rooms you can go to in department
#boss_stuff[13]=HP
#boss_stuff[14]=points gained
#boss_stuff[15]=
#boss_stuff[16]=
#boss_stuff[17]=
#boss_stuff[18]=


play = input(str("play?: (y)"))

while play != "n":
    rooms=[physics_department,PC1,PC2,english_department,E6,library,maths_department,S16,S14,music_department,MU8,MU9,technology_department,T1,T2,grammar,astro,peel_hall,chemistry_department,N9,N4,biology_department,N13,N14,food_department,Stamford_hall,art_department,A1,A2,languages_department,C13,C16,C18,geography_department,S1,S2,computer_department,S9,Engine_room,philosophy_department,economics_department,reception]
    level=0
    times=0
    win=False
    boss_stuff=reception
    losses=0
    spend_points = 0
    P_atk_bonus=[0,0,0,0,0]
    title()
    weapon_store=["WEAPONS:"]
    attire_store=["ATTIRES AND ARMOURS:"]
    items_store=["SPECIAL ITEMS:"]
    cheat_codes_store=["CHEAT CODES:"]
    inventory=[weapon_store,attire_store,items_store,cheat_codes_store]
    lives = 5#MODIFY BACK 
    score_board = []  
    name = input(str("enter your name: "))
    player_stats=P_character()
    normal_player_HP=player_stats[8]
    inventory[0].append(player_stats[6])
    inventory[1].append(player_stats[7])
    defeated_bosses=[]
    bag()
    
    #print(inventory)
    print()




                  
    #print(player_stats)#temporary for testinfg#
     
    # what does this next instruction do? What is it called? it is an iteration that goes on forever know as a while loop
    
    #while lives > 0:#switch it up so it respawns before fight, store previous location to set back to
    while lives > 0:
        
    #while player_stats[8] > 0:
   

        #room = physics_department[10]# SPECIFIC TO THIS SENARIO TO WORK WITH SPEEDY, TRY MAKE SOME MORE BOSSES AND TEST OUT INTERCHANGING THEM
        #boss_stuff = T2#physics_department

        boss_stuff[8]=active()
        player_stats[8] = normal_player_HP
        if boss_stuff[8]==1:#decides wwhether to spawn in
            normal_boss_HP=boss_stuff[13]
            normal_HP=player_stats[8]
            weather_senario=random.choice(weather_list)
            print("you enter as",weather_senario,boss_stuff[10],"and see",boss_stuff[0],"tower over you and prepare their",boss_stuff[6][0])
            print("you prepare your",player_stats[6][0],"for the fight of your life")


            while boss_stuff[13] > 0 and player_stats[8] > 0:

                P_atk_bonus_calc()

                P_atk_method=action_menu()
                if P_atk_method==boss_stuff[7]:
                    boss_stuff[13]=0
                elif P_atk_method!=boss_stuff[7] and P_atk_method!=player_stats[6][6] and P_atk_method!=player_stats[6][7] and P_atk_method!=player_stats[6][8]:
                    boss_stuff[13]=boss_stuff[13] + 10
                    
                    
                P_atk_method_bonus=atk_method_mod_calc()
                #if P_atk_method != "run":
                P_damage_out = player_attack()
                E_defence = boss_guard()
                #print("before, BOSS HP =",boss_stuff[13])
                OG_HP=boss_stuff[13]
                for i in range(len(P_damage_out)):
                    if P_damage_out[i] > E_defence[i]:
                        E_deduction=P_damage_out[i]-E_defence[i]
                        boss_stuff[13]=boss_stuff[13]-E_deduction
                E_dead_check()
                print(boss_stuff[0],"takes",OG_HP - boss_stuff[13],"damage from your",str(player_stats[6][0])+"!")
                print(str(boss_stuff[0])+"'s HP:",boss_stuff[13])
                
                if boss_stuff[13] > 0:
                    E_atk_choice=[boss_stuff[6][6],boss_stuff[6][7],boss_stuff[6][8]]
                    E_atk_method= random.choice(E_atk_choice)
                    E_damage_out=boss_attack()
                    P_defence=player_guard()
                    OG_P_HP=player_stats[8]
                    for i in range(len(E_damage_out)):
                        if E_damage_out[i] > P_defence[i]:
                            P_deduction=E_damage_out[i]-P_defence[i]
                            player_stats[8]=player_stats[8]-P_deduction
                    if player_stats[8]<0:
                        player_stats[8]=0             
                    print("You take",OG_P_HP - player_stats[8],"damage from",str(boss_stuff[0])+"'s",str(boss_stuff[6][0])+"!")
                    print("Your HP:",player_stats[8])
                    P_dead_check()
    
            
            if boss_stuff[13] <= 0 and player_stats[8] > 0:
                print("You have successfully defeated",boss_stuff[0],"of",boss_stuff[10])#########################loops for some reason
                player_stats[8]==normal_HP+5
                defeated_bosses.append(boss_stuff[0])
                global num1
                del rooms[num1]
                
                print()
                inventory[0].append(boss_stuff[6])
                print("You add the",boss_stuff[6][0],"to your SCHOOL BAG!")
                print()
                print("defeated enemies:","  number:",len(defeated_bosses),":",defeated_bosses)
                print()

                spend_points=spend_points + boss_stuff[14]
                print("current usable level points:",spend_points)
                inventory[0].append(boss_stuff[6])
                print("You now have passage through", boss_stuff[11],"to  continue your quest to liberate the school")
                print()
                print("BUT!")
                print()
                print("Be wary, dark creatures may still lurk in the darkest corners of the individual surrounding rooms within",boss_stuff[11],"for you to conquer!")
            #else:
                #boss_stuff=previous impliment when navigation is in
            
            


#boss_stuff[0]=Enemy_name
#boss_stuff[1]=E_heat_def
#boss_stuff[2]=E_electricity_def
#boss_stuff[3]=E_poison_def
#boss_stuff[4]=E_bludgeon_def
#boss_stuff[5]=E_cold_def
#boss_stuff[6]=E_weapon
#boss_stuff[7]=E_cheat
#boss_stuff[8]=E_active
#boss_stuff[9]=boss_number
#boss_stuff[10]=boss_room
#boss_stuff[11]=boss_department
#boss_stuff[12]=other rooms you can go to in department
#boss_stuff[13]=HP
#boss_stuff[14]=points gained

            
        else:
            print(boss_stuff[0],",the master of",boss_stuff[10],"was defeated and you have already conquered this part of the school")
            print("HAZAR!")
            print("BUT dark creatures may still lurk in the darkest corners of the individual surrounding rooms within",boss_stuff[11],"for you to conquer!")
            print("yet your quest to save the school continues...")

        norm_menu()

            

         
        
    print() 
    print("GAME OVER!")  
    print("player: ",name)  
    print("final score:",len(defeated_bosses))  #add teacher number  
    print()
    if win==True:
        ending="VICTOR!"
    else:
        ending="defeated in battle"
    player_go = ["VICTORIES:",len(defeated_bosses),"PLAYER:",name,"CLASS:",player_stats[0],"LEVEL:",level,"DEFEATS:",losses,"FATE:",ending] #add teacher number    add a dead teacher list variable
    leader() 
    bubble() 
    print("SCORE BOARD:") 
    order=0

    for i in range(len(board)): 
        order = order +1 
        print(order,board[i])

    credit()

    print() 
    play = input(str("play again?: (y)"))