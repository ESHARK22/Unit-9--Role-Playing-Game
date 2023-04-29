# Basic game where the character in ./RPGMCharacter_V1.0.png moves around the screen, with animations.

import pygame
import sys
import os
import time
import random
from pygame.locals import *
debug = True

all_debug_tags = [
    "[open_sprite_map]",
    "[split_sprite_map]",
    "[get_animation_sprite]",
    "[Main loop - Key Handler]"
]
enabled_debug_tags = [

]
def debug(message):
    """Prints a message to the console if the debug variable is set to True."""

    # Debug messages go like [sommething] message or [something][something2] message
    # The first part is the debug tag, the second part is the message

    msg = message.split("]")[-1:][0] # IDk why this works but it does
    tag = message.split("]")[:-1][0] + "]" # HELP MEEEEEEEEEEEEEEEEEEEEEEEEE

    if tag in enabled_debug_tags:
        print(message)
    elif tag not in all_debug_tags:
        raise Exception(f"Debug tag {tag} not found in all_debug_tags")


class player_animation:
    def __init__(self) -> None:
        self.state = "up_idle"
        self.available_states = [
            "up_idle", "up_walk", "up_attack", 
            "down_idle", "down_walk", "down_attack",
            "left_idle", "left_walk", "left_attack",
            "right_idle", "right_walk", "right_attack"
            ]
        self.frame = 0

        sprite_map = {}

        # to use the sprite map, use sprite_map[state][frame]

        # Load the sprite map for each state
        for state in self.available_states:
            sprite_map[state] = self.open_sprite_map(state)

        # Split the sprite map into a list of sprites
        for state in self.available_states:
            sprite_map[state] = self.split_sprite_map(sprite_map[state])

        self.sprite_map = sprite_map

        self.before_attack_state = None



    def open_sprite_map(self, state):
        path = f"./assets/RPGMCharacter_v1.0/pngs/{state}.png"
        debug(f"[open_sprite_map] Opening sprite map at {path}")
        sprite_map = pygame.image.load(path)
        return sprite_map

    def split_sprite_map(self, sprite_map):
        """Takes a sprite map and splits it into a list of sprites. 
        It should autodetect the number of sprites in the sprite map as there should be no fully transparent sprites."""
        
        sprite_map = self.open_sprite_map(self.state)

        # Get the width and height of the sprite map
        sprite_map_width = sprite_map.get_width()
        sprite_map_height = sprite_map.get_height()

        debug(f"[split_sprite_map] Sprite map width: {sprite_map_width}")
        debug(f"[split_sprite_map] Sprite map height: {sprite_map_height}")

        # Get the width and height of each sprite
        sprite_width = 64#int(sprite_map_width / 2)
        sprite_height = 64#int(sprite_map_height / 4)

        debug(f"[split_sprite_map] Sprite width: {sprite_width}")
        debug(f"[split_sprite_map] Sprite height: {sprite_height}")



        # Create a list of sprites
        sprites = []

        # Split the sprite map into a list of sprites
        for y in range(0, sprite_map_height, sprite_height):
            for x in range(0, sprite_map_width, sprite_width):
                debug(f"[split_sprite_map] x: {x}, y: {y}")
                sprites.append(sprite_map.subsurface(x, y, sprite_width, sprite_height))

        # Remove any fully transparent sprites
        # This is done by checking if the sprite is fully transparent by checking if the sprite is black
        # If the sprite is black, then it is fully transparent 
        for sprite in sprites:
            if sprite.get_at((0, 0)) == (0, 0, 0, 255):
                debug(f"[split_sprite_map] Removing sprite {sprite}")
                sprites.remove(sprite) 

        # Scale the sprites to 64x64
        for sprite in sprites:
            sprite = pygame.transform.scale(sprite, (128, 128))



        return sprites
    

    def change_state(self, new_state):
        """Changes the state of the player animation."""
        if new_state in self.available_states: # Checks if the new state is valid
            self.state = new_state
        else:
            raise ("Invalid state") # If the new state is invalid, raise an error
        
    def get_state(self):
        """Returns the current state of the player animation."""
        return self.state
    
    def walk(self):
        """Changes the state of the player animation to a walking state."""
        if self.state == "up_idle":
            self.state = "up_walk"
        elif self.state == "down_idle":
            self.state = "down_walk"
        elif self.state == "left_idle":
            self.state = "left_walk"
        elif self.state == "right_idle":
            self.state = "right_walk"

    def idle(self):
        """Changes the state of the player animation to an idle state."""

        if self.state == "up_walk":
            self.state = "up_idle"
        elif self.state == "down_walk":
            self.state = "down_idle"
        elif self.state == "left_walk":
            self.state = "left_idle"
        elif self.state == "right_walk":
            self.state = "right_idle"

    def attack(self):
        """Changes the state of the player animation to an attack state."""

        if self.state == "up_idle":
            self.before_attack_state = "up_idle"
            self.state = "up_attack"
        elif self.state == "down_idle":
            self.before_attack_state = "down_idle"
            self.state = "down_attack"
        elif self.state == "left_idle":
            self.before_attack_state = "left_idle"
            self.state = "left_attack"
        elif self.state == "right_idle":
            self.before_attack_state = "right_idle"
            self.state = "right_attack"

    def get_animation_sprite(self):
        """takes the sprite map and returns the sprite for the current animation state."""
        # The player animation is 3 frames long, so the frame number is the current frame modulo 3
        # Idle animations are 5 frames long, so the frame number is the current frame modulo 5
        # Walking animations are 4 frames long, so the frame number is the current frame modulo 4
        
        # If the player is attacking, and the frame number is > 3, then the player is done attacking
        # and the player should return to the state they were in before attacking
        
        # animations should update every 5 pygame ticks

        if pygame.time.get_ticks() % 3 == 0:
            self.frame += 1


        debug("[get_animation_sprite][state] " + self.state)

        if self.state == "up_attack" and self.frame > 3:
            self.state = self.before_attack_state
            self.frame = 0

        elif self.state == "down_attack" and self.frame > 3:
            self.state = self.before_attack_state
            self.frame = 0

        elif self.state == "left_attack" and self.frame > 3:
            self.state = self.before_attack_state
            self.frame = 0

        elif self.state == "right_attack" and self.frame > 3:
            self.state = self.before_attack_state
            self.frame = 0

        # If the player is walking, and the frame number is > 4, then the player is done walking
        # and the player should return to the idle state
        elif self.state == "up_walk" and self.frame > 4:
            self.state = "up_idle"
            self.frame = 0

        elif self.state == "down_walk" and self.frame > 4:
            self.state = "down_idle"
            self.frame = 0

        elif self.state == "left_walk" and self.frame > 4:
            self.state = "left_idle"
            self.frame = 0

        elif self.state == "right_walk" and self.frame > 4:
            self.state = "right_idle"
            self.frame = 0

        # If the player is idle, and the frame number is > 5, then the player is done idling
        # and the player should return to the idle state
        elif self.state == "up_idle" and self.frame > 5:
            self.state = "up_idle"
            self.frame = 0

        elif self.state == "down_idle" and self.frame > 5:
            self.state = "down_idle"
            self.frame = 0

        elif self.state == "left_idle" and self.frame > 5:
            self.state = "left_idle"
            self.frame = 0

        elif self.state == "right_idle" and self.frame > 5:
            self.state = "right_idle"
            self.frame = 0

        # If the player is attacking, then the frame number is the current frame modulo 3
        if self.state == "up_attack":
            frame_number = self.frame % 3
        elif self.state == "down_attack":
            frame_number = self.frame % 3
        elif self.state == "left_attack":
            frame_number = self.frame % 3
        elif self.state == "right_attack":
            frame_number = self.frame % 3

        # If the player is walking, then the frame number is the current frame modulo 4
        elif self.state == "up_walk":
            frame_number = self.frame % 4
        elif self.state == "down_walk":
            frame_number = self.frame % 4
        elif self.state == "left_walk":
            frame_number = self.frame % 4
        elif self.state == "right_walk":
            frame_number = self.frame % 4

        # If the player is idle, then the frame number is the current frame modulo 5
        elif self.state == "up_idle":
            frame_number = self.frame % 5
        elif self.state == "down_idle":
            frame_number = self.frame % 5
        elif self.state == "left_idle":
            frame_number = self.frame % 5
        elif self.state == "right_idle":
            frame_number = self.frame % 5

        # Get the sprite from the sprite map
        sprite = self.sprite_map[self.state][frame_number]

        # Return the sprite
        return sprite
    



def main():
    # Just show the player sprite 
    pygame.init()

    # Set up the window
    window_width = 800
    window_height = 600
    window = pygame.display.set_mode((window_width, window_height))

    # Set up the clock
    clock = pygame.time.Clock()

    # Set up the player
    player = player_animation()

    # Fill the window with white
    window.fill((255, 255, 255))
    # Get the sprite
    sprite = player.get_animation_sprite()

    player_rect = sprite.get_rect()
    player_rect.center = (window_width // 2, window_height // 2)
    # Draw the sprite
    window.blit(sprite, player_rect)


    # Main loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        sprite = player.get_animation_sprite()



        # Handle key presses
        keys = pygame.key.get_pressed()
        # debug(f"keys: {keys}")
        if keys[pygame.K_UP]:
            debug("[Main loop - Key Handler] Player is moving up")
            player.state = "up_idle"
            player.walk()
            player_rect.move_ip(0, -5)
             
        elif keys[pygame.K_DOWN]:
            debug("[Main loop - Key Handler] Player is moving down")
            player.state = "down_idle"
            player.walk()
            player_rect.move_ip(0, 5)

        elif keys[pygame.K_LEFT]:
            debug("[Main loop - Key Handler] Player is moving left")
            player.state = "left_idle"
            player.walk()
            player_rect.move_ip(-5, 0)

        elif keys[pygame.K_RIGHT]:
            debug("[Main loop - Key Handler] Player is moving right")
            player.state = "right_idle"
            player.walk()
            player_rect.move_ip(5, 0)




        # Delete the old sprite
        # We cannot use window.fill((255, 255, 255)) because that would delete the entire windo
        # Instead, we will draw a white rectangle over the old sprite
        pygame.draw.rect(window, (255, 255, 255), player_rect)


        # Draw the sprite
        window.blit(sprite, player_rect)

        # Update the display
        pygame.display.update()

        # Tick the clock
        clock.tick(60)

main()