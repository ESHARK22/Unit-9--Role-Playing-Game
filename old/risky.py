# Import all the packages needed for the game
import pygame
import random
import time
import sys

# Creates an FPS System for pygame and creates a speed variable used later for character movement
FPS=60
clock=pygame.time.Clock()
vel = 1.3

# Initialises features for pygame, and creates a pygame window with a caption/title
pygame.init()
Resolution = (1080,720)
WIN = pygame.display.set_mode(Resolution)
Caption = pygame.display.set_caption("RPG Game V1.0")

# Variables for the health system
health = 5
old_health_time = 0
curr_health_time = 0


# Stores the width and height of the pygame window in variables
Screen_Width = WIN.get_width()
Screen_Height = WIN.get_height()

#Define some colours
class colours:
    white = (255,255,255)
    black = (0,0,0)
    red = (255,0,0)
    green = (0,255,0)
    grey = (128,128,128)
    blue = (0,0,255)
    yellow = (255,255,0)
    cyan = (0,255,255)
    magenta = (255,0,255)
    orange = (255,165,0)
    

# def draw_button(button_x: int, button_y: int):
#     """Draws a button with a grey background and a black border"""
#     pygame.draw.rect(WIN, colours.grey, (button_x, button_y, 350, 100)) # Draws a grey rectangle with the size of 350x100
#     pygame.draw.rect(WIN, colours.black, (button_x, button_y, 350, 100), 5) # Draws a black rectangle with the size of 350x100 with a border of 5 pixels


# Loads all the images needed for the game, and changes the size of them to fit the game   

background_image = pygame.image.load("Assets/Main_Menu/background_image.png")

Plus = pygame.image.load("Assets/Main_Menu/PLUS.png")
Plus = pygame.transform.scale(Plus, (80,80))

Minus = pygame.image.load("Assets/Main_Menu/MINUS.png")
Minus = pygame.transform.scale(Minus, (80,80))

# Button Images
Play_Button = pygame.image.load("Assets/Main_Menu/Play_Button.png")
Play_Button = pygame.transform.scale(Play_Button, (350,100))

Options_Button = pygame.image.load("Assets/Main_Menu/Options_Button.png")
Options_Button = pygame.transform.scale(Options_Button, (350,100))

Quit_Button = pygame.image.load("Assets/Main_Menu/Play_Button.png")
Quit_Button = pygame.transform.scale(Quit_Button, (350,100))

Controls_Button = pygame.image.load("Assets/Main_Menu/Play_Button.png")
Controls_Button = pygame.transform.scale(Controls_Button, (400,100))

Back_Button = pygame.image.load("Assets/Main_Menu/Play_Button.png")
Back_Button = pygame.transform.scale(Back_Button, (350,100))

Resume_Button = pygame.image.load("Assets/Main_Menu/Play_Button.png")
Resume_Button = pygame.transform.scale(Resume_Button, (350,100))

Audio_Button = pygame.image.load("Assets/Main_Menu/Play_Button.png")
Audio_Button = pygame.transform.scale(Audio_Button, (350,100))

Volume_UP_Button = pygame.image.load("Assets/Main_Menu/Play_Button.png")
Volume_UP_Button = pygame.transform.scale(Volume_UP_Button, (90,90))

Volume_DOWN_Button = pygame.image.load("Assets/Main_Menu/Play_Button.png")
Volume_DOWN_Button = pygame.transform.scale(Volume_DOWN_Button, (90,90))

#Health Bar Images
Full_Health = pygame.image.load("Assets/Health-Bar/Full-Bar.png")
Full_Health = pygame.transform.scale(Full_Health, (350,50))

Four_Health = pygame.image.load("Assets/Health-Bar/4-5.png")
Four_Health = pygame.transform.scale(Four_Health, (350,50))

Three_Health = pygame.image.load("Assets/Health-Bar/3-5.png")
Three_Health = pygame.transform.scale(Three_Health, (350,50))

Two_Health = pygame.image.load("Assets/Health-Bar/2-5.png")
Two_Health = pygame.transform.scale(Two_Health, (350,50))

One_Health = pygame.image.load("Assets/Health-Bar/1-5.png")
One_Health = pygame.transform.scale(One_Health, (350,50))

Zero_Health = pygame.image.load("Assets/Health-Bar/0-5.png")
Zero_Health = pygame.transform.scale(Zero_Health, (350,50))

Heart = pygame.image.load("Assets/Health-Bar/Heart.png")
Heart = pygame.transform.scale(Heart, (45,45))


# Draw text on the buttons by creating a font then creating a function to draw the text on the buttons
text_font = pygame.font.SysFont("arialblack", 60)
def draw_text(text,text_col,x,y):
        img=text_font.render(text,True,text_col)
        WIN.blit(img,(x,y))


#Define some coordinates used for object locations
class coordinates:
    c_x = 100
    c_y = 100

#Method used for handling all drawing features
def home_screen_drawing():
    WIN.fill(colours.orange)
    WIN.blit(background_image, (0,0))
    WIN.blit(Play_Button, (365,105))
    #draw_button(365, 105)
    WIN.blit(Options_Button, (365,310))
    WIN.blit(Quit_Button, (365,515))
    draw_text("PLAY", (0,0,0), 450, 110)
    draw_text("OPTIONS", (0,0,0), 390 , 310)
    draw_text("QUIT", (0,0,0), 450, 515)

def options_drawing():
    WIN.blit(background_image, (0,0))
    WIN.blit(Audio_Button, (365,105))
    WIN.blit(Controls_Button, (340,310))
    WIN.blit(Back_Button, (365,515))
    draw_text("AUDIO", (0,0,0), 430, 110)
    draw_text("CONTROLS", (0,0,0), 355 , 313)
    draw_text("BACK", (0,0,0), 445, 515)

def PAUSE_drawing():
    WIN.blit(background_image, (0,0))
    WIN.blit(Resume_Button, (365,105))
    WIN.blit(Options_Button, (365,310))
    WIN.blit(Quit_Button, (365,515))
    draw_text("RESUME", (0,0,0), 400, 110)
    draw_text("OPTIONS", (0,0,0), 390 , 310)
    draw_text("QUIT", (0,0,0), 450, 515)

def main_game_drawing():
    WIN.fill(colours.orange)
    pygame.draw.rect(WIN, colours.black, (coordinates.c_x, coordinates.c_y, 50, 50))
    WIN.blit(Full_Health, (60,15))
    WIN.blit(Heart, (7,17))
    
def audio_drawing():
    WIN.blit(background_image, (0,0))
    WIN.blit(Back_Button, (365,515))
    WIN.blit(Volume_UP_Button, (700,240))
    WIN.blit(Volume_DOWN_Button, (300,240))
    WIN.blit(Plus, (705,244))
    WIN.blit(Minus, (305,244))
    draw_text("BACK", (0,0,0), 445, 515)
    draw_text("VOLUME", (0,0,0), 400, 240)
    mouse = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    if Volume_UP_Button.get_rect(topleft=(700,240)).collidepoint(mouse):
        increse_audio()
    if Volume_DOWN_Button.get_rect(topleft=(305,240)).collidepoint(mouse):
        decrese_audio()

def PAUSE_MENU():
    global WINDOW_STATE
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        print("Escape key pressed")
        WINDOW_STATE="Pause_screen"
        
    

class Drawings:
    """This class is used for drawing all the images and text on the screen"""
    def home_screen():
        """This method is used for drawing the home screen"""

        pass
    def options_screen():
        pass
    def play_screen():
        pass
    def audio_screen():
        pass
    def controls_screen():
        pass
    
        


        
#Adds movement to a character
def character_controller():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        coordinates.c_x -= vel
    if keys[pygame.K_RIGHT]:
        coordinates.c_x += vel
    if keys[pygame.K_UP]:
        coordinates.c_y -= vel
    if keys[pygame.K_DOWN]:
        coordinates.c_y += vel
    
my_sound = pygame.mixer.Sound("Assets/Main_Menu/Backing Clipped.mp3")
def audio():
    
    global my_sound
    my_sound.play()
    my_sound.set_volume(0.5)

# Increse audio
def increse_audio():
    audio_key = pygame.key.get_pressed()
    global my_sound
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            my_sound.set_volume(my_sound.get_volume()+0.05)
            print(my_sound.get_volume())
            print("Audio increse")
def decrese_audio():
    global my_sound
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            my_sound.set_volume(my_sound.get_volume()-0.05)
            print(my_sound.get_volume())
            print("Audio increse")
    


def Health_System():
    global health
    global old_health_time
    global curr_health_time
    curr_health_time = time.time()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_f]:
        if curr_health_time - old_health_time > 5:
            print("debug key f was pressed")
            old_health_time = time.time()
            health -= 1
    
    
WINDOW_STATE = "Home_screen"


def Has_mouse_clicked(Button: pygame.Surface, button_x: int, button_y: int):
    mouse_pos = pygame.mouse.get_pos()
    if Button.get_rect(topleft=(button_x,button_y)).collidepoint(mouse_pos):
        return True
    else:
        return False



#Creates an event handler
def main():
    global WINDOW_STATE
    clock.tick(FPS)
    run=True

    
    audio()
    
    
    while run: # Main game loop
        
        PAUSE_MENU()
        for event in pygame.event.get(): # Event loop

            if event.type == pygame.QUIT:
                # Has the user closed the window?
                run = False
                pygame.quit()
                sys.exit()

            
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                # -------------> Home Screen <-----------------
                
                if WINDOW_STATE == "Home_screen":
                    print("Current WINDOW_STATE is Home_screen")

                    if Has_mouse_clicked(Play_Button, 365, 105):
                        print("Play Button Clicked")
                        WINDOW_STATE="Play_screen"

                    elif Has_mouse_clicked(Options_Button, 365, 310):
                        print("Options Button Clicked")
                        WINDOW_STATE="Options_screen"

                    elif Has_mouse_clicked(Quit_Button, 365, 515):
                        print("Quit Button Clicked")
                        pygame.quit()
                        sys.exit()

                #-------------> Options Screen <-----------------

                elif WINDOW_STATE == "Options_screen":
                    print("Current WINDOW_STATE is Options_screen")

                    if Has_mouse_clicked(Audio_Button, 365, 105):
                        print("Audio Button Clicked")
                        WINDOW_STATE="Options_screen::Audio"

                    elif Has_mouse_clicked(Controls_Button, 365, 310):
                        print("Controls Button Clicked")
                        WINDOW_STATE="Options_screen::Controls"

                    elif Has_mouse_clicked(Back_Button, 365, 515):
                        print("Back Button Clicked")
                        WINDOW_STATE="Home_screen"

                elif WINDOW_STATE == "Options_screen::Audio":
                    print("Current WINDOW_STATE is Options_screen::Audio")

                    if Has_mouse_clicked(Back_Button, 365, 515):
                        print("Back Button Clicked")
                        WINDOW_STATE="Options_screen"

                elif WINDOW_STATE == "Options_screen::Controls":
                    print("Current WINDOW_STATE is Options_screen::Controls")

                    if Has_mouse_clicked(Back_Button, 365, 515):
                        print("Back Button Clicked")
                        WINDOW_STATE="Options_screen"

                # -------------> Play Screen <-----------------

                elif WINDOW_STATE == "Play_screen":
                    print("Current WINDOW_STATE is Play_screen")

                    if Has_mouse_clicked(Back_Button, 365, 515):
                        print("Back Button Clicked")
                        WINDOW_STATE="Home_screen"


                # -------------> Pause Screen <-----------------

                elif WINDOW_STATE == "Pause_screen":
                    print("Current WINDOW_STATE is Pause_screen")

                    if Has_mouse_clicked(Resume_Button, 365, 105):
                        print("Resume Button Clicked")
                        WINDOW_STATE="Play_screen"

                    elif Has_mouse_clicked(Options_Button, 365, 310):
                        print("Options Button Clicked")
                        WINDOW_STATE="Pause_screen::Options"

                    elif Has_mouse_clicked(Quit_Button, 365, 515):
                        print("Quit Button Clicked")
                        pygame.quit()
                        sys.exit()

                elif WINDOW_STATE == "Pause_screen::Options":
                    print("Current WINDOW_STATE is Pause_screen::Options")

                    if Has_mouse_clicked(Back_Button, 365, 515):
                        print("Back Button Clicked")
                        WINDOW_STATE="Pause_screen"

                elif WINDOW_STATE == "Pause_screen::Audio": 
                    print("Current WINDOW_STATE is Pause_screen::Audio")

                    if Has_mouse_clicked(Back_Button, 365, 515):
                        print("Back Button Clicked")
                        WINDOW_STATE="Pause_screen"

                elif WINDOW_STATE == "Pause_screen::Controls":
                    print("Current WINDOW_STATE is Pause_screen::Controls")

                    if Has_mouse_clicked(Back_Button, 365, 515):
                        print("Back Button Clicked")
                        WINDOW_STATE="Pause_screen"


                    

                
               

                
                
        
        if WINDOW_STATE=="Home_screen":
            # print("Home_screen")
            home_screen_drawing()
        
        
        elif WINDOW_STATE=="Options_screen":
            # print("Options_screen")
            options_drawing()

        elif WINDOW_STATE=="Play_screen":
            # print("Play_screen")
            main_game_drawing()

        elif WINDOW_STATE=="Pause_screen":
            
            PAUSE_drawing()
        elif WINDOW_STATE=="Options_screen::Audio" 
            audio_drawing()

        
            
            
           
        
        health = Health_System ()
        character_controller()
        pygame.display.update()
        WIN.fill((0,0,0))
    pygame.quit() 

if __name__ == "__main__":#calls the main function
    main()



# Credit:
# 
# Assets:
# https://github.com/baraltech/Menu-System-PyGame/tree/main/assets
#
# Game:
# ESHARK22 - 6 characters :D
