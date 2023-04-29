# Basic game where the character in ./RPGMCharacter_V1.0.png moves around the screen, with animations.

import pygame
import sys
import os
import time
import random
from pygame.locals import *


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
        # Check if attacking and if state is < 3 then go back to idle
        if self.frame == 3 and (self.state == "up_attack" or self.state == "down_attack" or self.state == "left_attack" or self.state == "right_attack"):
            self.frame = 0
            self.state = self.before_attack_state
            self.idle()
            return self.load_sprite_map()[0]

        print(self.state, self.frame)
        # if self.state == "up_idle": 
        
        if self.frame == 0:
            # return the first sprite in the sprite map
            self.frame += 1
            return self.load_sprite_map()[0]
        
        elif self.frame == 1:
            # return the second sprite in the sprite map
            self.frame += 1
            return self.load_sprite_map()[1]
        elif self.frame == 2:
            # return the third sprite in the sprite map
            self.frame = 0
            return self.load_sprite_map()[2]
        
        # elif self.state == "up_walk":


    
    def get_animation_sprite_map(self):
        """Returns the sprite map for the current animation state."""
        file_name = f"./assets/RPGMCharacter_V1.0/pngs/{self.state}.png"
        return pygame.image.load(file_name)
    
    
    def load_sprite_map(self):
        """Splits the sprite map into individual sprites and returns them in a list."""
        sprite_map = self.get_animation_sprite_map()
        sprite_list = []
        for i in range(4):
            for j in range(3):
                sprite = sprite_map.subsurface((j*16, i*16, 16, 16))
                sprite_list.append(sprite)
        return sprite_list
    


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

    # Show the player sprite
    player_sprite = player.get_animation_sprite()
    player_sprite = pygame.transform.scale(player_sprite, (128, 128))
    player_sprite_rect = player_sprite.get_rect()
    player_sprite_rect.center = (window_width/2, window_height/2)
    print(player.load_sprite_map())

    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        # Handle key presses
        keys = pygame.key.get_pressed()
        if keys[K_UP] or keys[K_w]:
            player.walk()
            player_sprite_rect.y -= 1
        elif keys[K_DOWN] or keys[K_s]:
            player.walk()
            player_sprite_rect.y += 1
        elif keys[K_LEFT] or keys[K_a]:
            player.walk()
            player_sprite_rect.x -= 1
        elif keys[K_RIGHT] or keys[K_d]:
            player.walk()
            player_sprite_rect.x += 1
        elif keys[K_SPACE]:
            player.attack()
        else:
            player.idle()

        # Draw the background
        window.fill((0, 0, 0))

        # Draw the player
        window.blit(player.get_animation_sprite(), player_sprite_rect)

        # Update the display
        pygame.display.update()
        clock.tick(60)


main()