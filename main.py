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


#region ------> Pygame game loop <------

# Game loop variables
running = True

# Game loop
while running:
    # Event loop
    for event in pygame.event.get():
        # Check if the user wants to quit
        if event.type == pygame.QUIT:
            # Set running to false to break the game loop
            running = False

#endregion



