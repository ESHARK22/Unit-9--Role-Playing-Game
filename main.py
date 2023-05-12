import os
import random
import sys
import time

import pygame
import random
import time




def load_animation(direction, state):
    """
        Loads the animation for the given direction and state
    """
    animation_file = "./assets/RPGMCharacter_v1.0/pngs/{DIRECTION}_{STATE}.png"

    return pygame.image.load(animation_file.format(STATE=state, DIRECTION=direction))

current_animation_state = "idle"
current_animation_direction = "right"
last_animation_time = 0
last_animation_state = "idle"
last_animation_direction = "up"


def split_png(png_file):
    """Splits a png into multiple sections. Used for spirte sheets"""


    # Load the image
    image = pygame.image.load(png_file)

    # Get the width and height of the image
    image_width = image.get_width()
    image_height = image.get_height()

    # Get the number of rows and columns
    rows = image_height // 32
    columns = image_width // 32

    # Create a list to store the images
    images = []

    # Loop through the rows and columns
    for row in range(rows):
        for column in range(columns):
            # Create a new image
            new_image = pygame.Surface((32, 32))

            # Copy the sprite from the sheet onto the new image
            new_image.blit(image, (0, 0), (column * 32, row * 32, 32, 32))

            # Add the image to the list
            images.append(new_image)

    return images


    


def play_animation():
    """
        Draws the character on the screen
    """
    global current_animation_state
    global current_animation_direction
    global current_time

    global last_animation_time
    global last_animation_state
    global last_animation_direction


    possible_states = ["idle", "walk", "attack"]
    possible_directions = ["left", "right", "up", "down"]

    # if last_animation_time

    if current_time - last_animation_time > 1000: # 1 second
        # Move to the next state
        current_animation_state = possible_states.index(last_animation_state) + 1 # find out what index the last state was in the list amd move to the next one
        current_animation_state = possible_states[current_animation_state % len(possible_states)] # make sure the index is in range

        # Move to the next direction
        current_animation_direction = possible_directions.index(last_animation_direction) + 1 # find out what index the last direction was in the list amd move to the next one
        current_animation_direction = possible_directions[current_animation_direction % len(possible_directions)] # make sure the index is in range

        # Move the current states to the last states a new animation will be played
        last_animation_time = current_time
        last_animation_state = current_animation_state
        last_animation_direction = current_animation_direction

    image = load_animation(current_animation_direction, current_animation_state)

    # make the image bigger
    image = pygame.transform.scale(image, (image.get_width() * 4, image.get_height() * 4))



    game_display.blit(image, (0, 0))






# Set up the display
display_width = 800
display_height = 600
game_display = pygame.display.set_mode((display_width, display_height))

# Load the image
image = load_animation(current_animation_direction, current_animation_state)

# Set up the clock
clock = pygame.time.Clock()

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


    print("STATE: {STATE}, DIRECTION: {DIRECTION}".format(STATE=current_animation_state, DIRECTION=current_animation_direction))

    current_time = pygame.time.get_ticks()
    

    # Clear the screen
    game_display.fill((255, 255, 255))

    play_animation()


    # Update the display
    pygame.display.update()

    # Set the frame rate
    clock.tick(60)