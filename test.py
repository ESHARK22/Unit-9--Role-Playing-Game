import pygame
from logging import info, debug, warning, error



# ------> Pygame initialization <------ # 

# This could be just one line, but I wanted to add some logging to it for debugging purposes

init_success, init_failed = pygame.init()
if init_failed != 0:
    error("Pygame:Init", f"Pygame failed to initialize with {init_failed} errors")
    exit()
else:
    info("Pygame:Init", f"Pygame succesfully initialized {init_success} modules")


