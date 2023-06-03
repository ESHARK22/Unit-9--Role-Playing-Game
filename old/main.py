import pygame
from logging import info, debug, warning, error

# All the reigion tags are for the code folding extension in vscode. (It makes it easier to navigate the code)


#region ------> Pygame initialization <------ 
# This could be just one line, but I wanted to add some logging to it for debugging purposes

(init_success, init_failed) = pygame.init()
if init_failed != 0:
    error("Pygame:Init", f"Pygame failed to initialize with {init_failed} errors")
    exit()
else:
    info("Pygame:Init", f"Pygame succesfully initialized {init_success} modules")
#endregion


#region ------> Pygame window creation <------ 

# Create the window
window = pygame.display.set_mode((800, 600))

# Set the window title
pygame.display.set_caption("Eshark's rpg!")

# TODO: Add an icon (pygame.display.set_icon) 


#endregion


#region ------> Input handling <------

def input_handler():
    """ Handles input """
    global running


    for keys in pygame.event.get():
        if keys.type == pygame.QUIT:
            running = False
            debug("InputHandler", "User closed the window")

        if keys.type == pygame.KEYDOWN:
            if keys.key == pygame.K_ESCAPE:
                running = False
                debug("InputHandler", "User pressed escape")

            if keys.key == pygame.K_w:
                debug("InputHandler", "User pressed W")

            if keys.key == pygame.K_a:
                debug("InputHandler", "User pressed A")

            if keys.key == pygame.K_s:
                debug("InputHandler", "User pressed S")

            if keys.key == pygame.K_d:
                debug("InputHandler", "User pressed D")

        elif keys.type == pygame.KEYUP:
            if keys.key == pygame.K_w:
                debug("InputHandler", "User released W")

            if keys.key == pygame.K_a:
                debug("InputHandler", "User released A")

            if keys.key == pygame.K_s:
                debug("InputHandler", "User released S")

            if keys.key == pygame.K_d:
                debug("InputHandler", "User released D")




#endregion


#region ------> General functions <------
def clear_screen():
    """ Clears the screen. This is usually called at the start of the game loop to remove the previous
        frame.                                                                                       """
    window.fill((0, 0, 0))

def update_screen():
    """ Updates the screen. This is usually called at the end of the game loop to update the screen  
        with the new frame. This is the opposite of clear_screen()                                  """
    pygame.display.update()

#endregion


#region ------> Pygame game loop <------

# Game loop variables
running = True

# Game loop
while running:
    clear_screen() # Clear the screen

    input_handler() # Handle input

    


    update_screen() # Update the screen



#endregion



