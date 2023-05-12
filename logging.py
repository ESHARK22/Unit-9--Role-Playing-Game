debug_mode = True
info_mode = True
warning_mode = True
error_mode = True

class colours:
    # Normal colours
    red = "31m"
    green = "32m"
    yellow = "33m"
    blue = "34m"

    # Bold colours
    bold = "1;"

    # Reset colour
    reset = "0m"

    # Colour dictionary
    colour_dict = {
        "start": "\033[",
        "red": red,
        "green": green,
        "yellow": yellow,
        "blue": blue,
        "bold_red": bold + red,
        "bold_green": bold + green,
        "bold_yellow": bold + yellow,
        "bold_blue": bold + blue,
        "reset": reset
    }


def print_colour(text: str, colour: str):
    """ Prints text in the specified colour """

    # Print the text in the specified colour
    print(colours.colour_dict["start"] + colours.colour_dict[colour] + text + colours.colour_dict["start"] + colours.colour_dict["reset"])


def center_word(word: str) -> str:
    """ Returns a centered word, which is padded with spaces. The length must be minimum 20 characters"""

    # Get the length of the word
    word_length = len(word)



    # Calculate the number of spaces to add to the word
    spaces = (20 - word_length) // 2

    # Add the spaces to the word
    centered_word = " " * spaces + word + " " * spaces

    # Return the centered word
    return centered_word

def info(process_name:str, message:str) -> None:
    """ Prints an info message """

    # Print the message
    print_colour(center_word(process_name) + " | " + message, "bold_blue") if info_mode else None

def debug(process_name:str, message:str) -> None:
    """ Prints a debug message """

    # Print the message
    print_colour(center_word(process_name) + " | " + message, "bold_green") if debug_mode else None

def warning(process_name:str, message:str) -> None:
    """ Prints a warning message """

    # Print the message
    print_colour(center_word(process_name) + " | " + message, "bold_yellow") if warning_mode else None

def error(process_name:str, message:str) -> None:
    """ Prints an error message """

    # Print the message
    print_colour(center_word(process_name) + " | " + message, "bold_red") if error_mode else None


