# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Random")
define m = Character("Me")


# The game starts here.

label start:
    "narrator this is"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show random at right with moveinleft

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    m "Why?"

    e "Once you add a story, pictures, and music, you can release it to the world!"

    e "Cats or Dogs?"

    menu: 
        "I like dogs": 
            jump dogs
        "I like cats":
            e "YAY"
            jump cats

    # This ends the game.

    return
label dogs:
    scene bg anime
    e "WORDS WORDS"
label cats: 
    e "NO WORDS"
    return