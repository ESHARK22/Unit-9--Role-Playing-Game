# Create a basic rpg game taht allows the user to move around.
# This shoudl use PySide6 
import random
import time
import sys
import os
import PySide6
import character
from PySide6 import QtCore, QtWidgets, QtGui



# Create a class for the main window 
class MainWindow(QtWidgets.QMainWindow):
    # Create a constructor for the main window
    def __init__(self):
        # Call the constructor of the parent class
        super().__init__()
        # Set the title for the main window
        self.setWindowTitle("RPG 2023")
        # Set the size of the main window
        self.resize(800, 600)

        # Create a label for the main window
        self.label = QtWidgets.QLabel("RPG 2023", self)
        # Set the font for the label
        self.label.setFont(QtGui.QFont("Arial", 20))
        # Set the position of the label
        self.label.move(300, 50)

        # Create a button for the main window
        self.button = QtWidgets.QPushButton("Start", self)
        # Set the position of the button
        self.button.move(350, 100)
        # Connect the button to a function
        self.button.clicked.connect(self.start_game)

        # Create a button for the main window
        self.button = QtWidgets.QPushButton("Exit", self)
        # Set the position of the button
        self.button.move(350, 150)
        # Connect the button to a function
        self.button.clicked.connect(self.exit_game)


    # Create a function to start the game
    def start_game(self):
        # Create a new window for the game
        self.game = GameWindow()
        # Show the new window
        self.game.show()
        # Hide the main window
        self.hide()

    
    # Create a function to exit the game
    def exit_game(self):
        # Close the main window
        self.close()

class GameWindow(QtWidgets.QMainWindow):
    # this should just show the character 

    # Create a constructor for the game window
    def __init__(self):
        # Call the constructor of the parent class
        super().__init__()

        # Set the title for the game window
        self.setWindowTitle("RPG 2023")

        # Set the size of the game window
        self.resize(800, 600)

        # Create the character label
        self.character = QtWidgets.QLabel(self)
        # Set the position of the character label
        self.character.move(300, 300)
        # Set the size of the character label
        self.character.resize(100, 100)
        # Set the image for the character label
        self.character.setPixmap(character.Player().get_character_image("idle").scaled(100, 100))

        # Create a button for the game window
        self.button = QtWidgets.QPushButton("Exit", self)
        # Set the position of the button
        self.button.move(350, 150)
        # Connect the button to a function
        self.button.clicked.connect(self.exit_game)

    # Create a function to start the game



    def keyPressEvent(self, event):
        print(event.key())
        try:
            self.parity = self.parity + 1
        except:
            self.parity = 0

        if self.parity % 5 == 0:
            print("forwards_idle")
            self.character.setPixmap(character.Player().get_character_image("idle").scaled(100, 100))
        else:
            print("forwards_walk")
            self.character.setPixmap(character.Player().get_character_image("walk").scaled(100, 100))

        self.parity = self.parity + 1

        # for x in range(50):
        #     # step the character for 5 seconds then idle for 5
        #     self.character.setPixmap(character.Player().get_character_image("forwards_idle").scaled(100, 100))
        #     time.sleep(0.5)
        #     self.character.setPixmap(character.Player().get_character_image("forwards_walk").scaled(100, 100))
        #     time.sleep(0.5)


    # Create a function to exit the game
    def exit_game(self):
        # Close the game window
        self.close()

def main():
    # Create an instance of the QApplication
    app = QtWidgets.QApplication([])

    # Create an instance of the main window
    window = MainWindow()
    # Show the main window
    window.show()

    # Run the application
    sys.exit(app.exec())

# Create a class for the game window


# Call the main function
main()


# End of file
