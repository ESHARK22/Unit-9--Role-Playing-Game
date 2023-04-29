from PySide6.QtGui import QImage, QPixmap, QColor, QPainter
from PySide6 import QtCore, QtWidgets, QtGui
# Load the PNG file into a QImage object


class Player:
    name = "Albert"
    character = "monster2animCharSprites\Albert.png"
    def __init__(self):
        self.name = "Albert"
        self.state = "forwards_idle"
        self.step_parity = 0

    def get_character_image(self, state:str):
        image = QImage(self.character)
        
        chars = self.extract_characters()
        if self.state == "forwards_idle":
            return chars[0]
        elif self.state == "forwards_walk":
            if self.step_parity == 0:
                self.step_parity = 1
                return chars[4]
            else:
                self.step_parity = 0
                return chars[5]
            
        # elif self.state == "backwards_idle":
        #     return chars[2]
        # elif self.state == "backwards_walk":




        return chars[5]

    def extract_characters(self):
        # Load the PNG file into a QImage object
        image = QImage(self.character)

        characters = []
        for i in range(20):
            # Calculate the row and column of the character
            column = i % 4
            row = i // 4

            # Crop the section of the image containing the character
            x = column * 16
            y = row * 16
            width = 16
            height = 16

            # Create a new QImage object for the character and copy the pixels from the original image
            character_image = QImage(width, height, QImage.Format_RGBA8888)
            for i in range(width):
                for j in range(height):
                    pixel = image.pixel(x + i, y + j)
                    character_image.setPixelColor(i, j, QColor(pixel))

            # Optionally, apply additional image processing steps here, such as removing a background color or adding a border
            character_image = self.remove_bg(character_image)
            character_image = self.add_border(character_image)

            # Convert the QImage to a QPixmap and add it to the list of characters
            character_pixmap = QPixmap.fromImage(character_image)
            characters.append(character_pixmap)

        return characters



    def remove_bg(self, image: QImage, colour_to_remove: QtGui.QColor=QtGui.QColor(255, 0, 255, 255)):
        # Replace all pixels of that color with transparent pixels
        for x in range(image.width()):
            for y in range(image.height()):
                if image.pixelColor(x, y) == colour_to_remove:
                    image.setPixelColor(x, y, QColor(0, 0, 0, 0))

        # # Create an alpha mask for the image
        # alpha_mask = image.createAlphaMask()
        # image.setAlphaChannel(alpha_mask)

        return image
    
    def add_border(self, image):

        # Define the size of the border (in pixels)
        border_size = 5

        # Create a new QImage with a larger size
        bordered_image = QImage(image.width() + 2 * border_size, image.height() + 2 * border_size, QImage.Format_RGBA8888)

        # Fill the new image with a transparent color
        bordered_image.fill(QColor(0, 0, 0, 0))

        # Paint the original image onto the new image with a black border
        painter = QPainter(bordered_image)
        painter.drawImage(border_size, border_size, image)
        painter.setPen(QColor(0, 0, 0))
        painter.drawRect(0, 0, bordered_image.width() - 1, bordered_image.height() - 1)
        painter.end()

        return bordered_image