# use_string is {x} uses y on {z}
# eg {Player 1} throws a rock at {Player 2}
# Defeat string is {x} defeats {y} with {z}
# {Player 2} is knocked out by {Player 1} with a rock
# Fail string is {x} fails to use {y}  on {z}
# {player 2} dodges {player 1}'s rock

class Item:
    def __init__(self, name, use_string, defeat_string, fail_string):
        self.name = name
        self.use_string = use_string
        self.defeat_string = defeat_string
        self.fail_string = fail_string


# History:

# Textbook on World History

# Use_string: {Student 1} uses the textbook on World History as a shield to defend against boring lectures.
# Defeat_string: {Student 2} defeats {Student 1} in a historical trivia contest using the textbook on World History as their secret weapon.
# Fail_string: {Student 1} fails to use the textbook on World History to impress their crush with historical facts, stumbling over their words.
# Timeline of Important Events

# Defeat_string is when the student defeats the teacher
# Fail_string is when the student is defeated by the teacher

History_textbook = Item(
    "History Textbook", 
    "{} uses the textbook on World History as a shield to defend against boring lectures.",
    "{} defeats {} in a historical trivia contest using the textbook on World History.",
    "{} fails to use the textbook on World History, and ends up stumbling over their words"
)

Timeline_of_important_events = Item(
    "Timeline of Important Events",
    "{} uses the timeline of important events as a makeshift cape and dramatically reenacts historical moments.",
    "{} defeats {} in a debate about historical accuracy by referencing the timeline of important events as evidence.",
    "{} fails to use the timeline of important events to answer a student's question and resorts to making up a wild story."
)

Historical_maps = Item(
    "Historical Maps",
    "{} uses the historical map to navigate through the school corridors, pretending to be on a grand expedition.",
    "{} defeats {} in a treasure hunt game by cleverly altering the historical map and leading them to the wrong location.",
    "{} fails to use the historical map to find their way out of a maze-like hallway, spinning around in circles instead."
)

calculator = Item(
    "Calculator",
    "{} uses the calculator to create a rhythmic beat by pressing the buttons in a musical sequence during a math class.",
    "{} defeats {} in a mental calculation challenge, outperforming them even when the student uses the calculator.",
    "{} fails to use the calculator correctly and accidentally types in a math equation that causes the calculator to display an error."
)

graphing_paper = Item(
    "Graphing Paper",
    "{} uses the graphing paper as a canvas to create a masterpiece by meticulously drawing geometric shapes and patterns.",
    "{} defeats {} in a drawing competition by utilizing the graphing paper to create a stunningly accurate graph representation of a famous painting.",
    "{} fails to use the graphing paper to draw a straight line and ends up with a squiggly and distorted artwork."
)

geometry_set = Item(
    "Geometry Set",
    "{} uses the geometry set to construct a mini fort on their desk during a particularly dull geometry lesson.",
    "{} defeats {} in a geometry challenge, showcasing incredible precision and accuracy while using the same geometry set.",
    "{} fails to use the compass properly and pokes their finger instead of drawing a circle."
)   


# Use_string: {Teacher} uses the timeline of important events as a makeshift cape and dramatically reenacts historical moments.
# Defeat_string: {Student} defeats {Teacher} in a debate about historical accuracy by referencing the timeline of important events as evidence.
# Fail_string: {Teacher} fails to use the timeline of important events to answer a student's question and resorts to making up a wild story.
# Historical Maps

# Use_string: {Explorer} uses the historical map to navigate through the school corridors, pretending to be on a grand expedition.
# Defeat_string: {Custodian} defeats {Explorer} in a treasure hunt game by cleverly altering the historical map and leading them to the wrong location.
# Fail_string: {Explorer} fails to use the historical map to find their way out of a maze-like hallway, spinning around in circles instead.
# Maths:

# Calculator

# Use_string: {Student} uses the calculator to create a rhythmic beat by pressing the buttons in a musical sequence during a math class.
# Defeat_string: {Math Whiz} defeats {Student} in a mental calculation challenge, outperforming them even when the student uses the calculator.
# Fail_string: {Student} fails to use the calculator correctly and accidentally types in a math equation that causes the calculator to display an error.
# Graphing Paper

# Use_string: {Artist} uses the graphing paper as a canvas to create a masterpiece by meticulously drawing geometric shapes and patterns.
# Defeat_string: {Teacher} defeats {Artist} in a drawing competition by utilizing the graphing paper to create a stunningly accurate graph representation of a famous painting.
# Fail_string: {Artist} fails to use the graphing paper to draw a straight line and ends up with a squiggly and distorted artwork.
# Geometry Set (compass, protractor, ruler)

# Use_string: {Student} uses the geometry set to construct a mini fort on their desk during a particularly dull geometry lesson.
# Defeat_string: {Mathlete} defeats {Student} in a geometry challenge, showcasing incredible precision and accuracy while using the same geometry set.
# Fail_string: {Student} fails to use the compass properly and pokes their finger instead of drawing a circle.
# English:

# Classic Literature Novels

# Use_string: {Student} uses the classic literature novel as a makeshift pillow during an especially long and boring English class.
# Defeat_string: {Bookworm} defeats {Student} in a literary quiz by extracting detailed information from the classic literature novel.
# Fail_string: {Student} fails to use the classic literature novel as a conversation starter, awkwardly mispronouncing the author's name.
# Thesaurus

# Use_string: {Writer} uses the thesaurus to replace every word in their essay with grandiose synonyms, resulting in an unintentionally hilarious piece of writing.
# Defeat_string: {Grammar Enthusiast} defeats {Writer} in a language debate by pointing out the absurdity