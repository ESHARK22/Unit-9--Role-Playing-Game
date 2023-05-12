import pygame
import os
import random
import sys

class Player:
    def __init__(self, name, health):
        
        self.name = name
        self.health = health


        # Set the player's animation state to idle and direction to right

        self.current_animation_frame = 0   
        self.current_animation_state = "idle"   
        self.current_animation_direction = "up"  
    
        self.last_animation_time = 0
        self.last_animation_state = "idle"
        self.last_animation_direction = "up"
        





class Animations:
    def __init__(self) -> None:
        pass

    def split_image(image_path :str, x_pixels_split :int = 64, y_pixels_split :int = 64) -> list:
        """ Takes an image and splits it into a list of smaller images based on the x and y pixels 
        split. For example, a 256x128 image split into 64x64 images would return a list of 8 images """


        full_image = pygame.image.load(image_path).convert_alpha()

        # Get the width and height of the full image
        full_image_width = full_image.get_width()
        full_image_height = full_image.get_height()

        # Get the number of rows and columns
        rows = full_image_height // y_pixels_split
        columns = full_image_width // x_pixels_split

        # Create a list to store the images
        split_images = []

        # Loop through the rows and columns
        for row in range(rows):
            for column in range(columns):

                # Create a new image
                new_image = pygame.Surface((x_pixels_split, y_pixels_split))

                # Replace the background color with a transparent color
                new_image.fill((255, 255, 255))
                new_image.set_colorkey((255, 255, 255))

                # Copy the sprite from the sheet onto the new image
                new_image.blit(full_image, (0, 0), (column * x_pixels_split, row * y_pixels_split, x_pixels_split, y_pixels_split))

                # Add the image to the list
                split_images.append(new_image)

        return split_images
    
    def get_animation_frame(self, animation_state :str, animation_direction :str, animation_frames :list, animation_speed :int = 100) -> pygame.Surface:
        """ Returns the next animation frame based on the animation state, direction, and speed """

        # Get the current time
        current_time = pygame.time.get_ticks()

        # Check if the animation state or direction has changed
        if animation_state != self.last_animation_state or animation_direction != self.last_animation_direction:

            # Reset the animation frame
            self.current_animation_frame = 0

            # Update the last animation state and direction
            self.last_animation_state = animation_state
            self.last_animation_direction = animation_direction

        # Check if enough time has passed to update the animation frame
        elif current_time - self.last_animation_time > animation_speed:

            # Update the animation frame
            self.current_animation_frame += 1

            # Reset the animation frame if the animation has reached the end
            if self.current_animation_frame >= len(animation_frames):
                self.current_animation_frame = 0

            # Update the last animation time
            self.last_animation_time = current_time

        # Return the current animation frame
        return animation_frames[self.current_animation_frame]
    
    