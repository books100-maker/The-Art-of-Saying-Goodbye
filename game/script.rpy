# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Jerymaya")
define m = Character("Me")
define q = Character("???")


# The game starts here.

label start:
    $ renpy.movie_cutscene("Cutscene1.webm")
    scene bg room
    #play music "main_theme.webm
    "I finally got in without getting caught. . ."

    "I guess I can look around and look for clues of- why"

    "You look around the apartment briefly, hautend by the memories which hold the past you once adored and knew all too well"

    "you make your way to his bedroom, looking at all of his belongings, which are still there. Nothing has changed since the incident"

    "His bed that he slept in every night and you both watched movies in, the door to the bathroom, his art desk in which he loved to draw. You still keep his drawings… and his closet, which seemed to be creaked open as if it wanted to be open, you can see that some sort of box was in there."

    "you stare around, starting to feel a bit sick and lightheaded, till your sight lands on the bedside table, in which you see a framed photo, a framed photo that seems to hold a picture of you and him"

    "this silence seems to stop time, and not even the wind is making a sound. His smile seems to make everything loud, yet so quiet."

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show 2 at right with moveinleft
    show old photo at left with moveinright

    # These display lines of dialogue.

    e "I'm sad"

    m "Why?"
    hide old photo
    call screen talk

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
screen talk():
    imagebutton:
        idle "old photo.png"
        hover "Picture_hover.png"
        xpos 0
        ypos 100
        action Jump("Picture")
label Picture:
    scene bg room
    show old photo at center
    "…..for a while you feel sick, too sick to be able to keep looking at it. You drop the framed photo. Horrified at your actions, you run to the bathroom; you feel like you're drowning from all the memories of him, and seeing him again so alive seems to makes those emotions—of when you found out what happened to him, flood back"

    "as you stare at the bathroom mirror, you seem to be hyperventilating, but you don’t really think about that because the only thing that’s in your mind is him, Ithen"

    e "It’s fine. You’re fine. It’s all fine. Don’t cry, don’t you dare"
    
    show 2 at right
    "you suddenly find yourself on your hands and knees, staring at the floor. Through tears, you can barely make out something shining below the vanity"
screen talk_key():
    imagebutton:
        idle "key1.png"
        hover "key1_hover.png"
        xpos 0
        ypos 100
        action Jump("key")
label key:
    scene bg room
    show key1 at center
    "you have acquired a key"

    e "I wonder where this goes. I think I saw a chest back out in the bedroom—maybe it works there?"
    show q at left
    hide q with moveoutright
    e "who was that?"

    scene bg room
    show 3 at right with moveinleft

    e "I wonder where this goes. I think I saw a chest back out in the bedroom—maybe it works there?"

    "you walk back to the bedroom, just a little more numb than before."

    "turning to the closet, you find a chest. It’s not quite large, but not quite small, either. You wonder what’s inside."

    "You insert the key into the lock, the only thing that keeps you from the secrets inside. Nothing happens."

    "I wonder what could be in there? Either way, if this key doesn’t fit…oh—it has to go somewhere..."

    "You look around once more, realizing that the art desk had been locked. One lock for each drawer."

    "It wasn’t like that before."

    "You quickly make your way to the art desk—and, swiftly shoving the key into the lock, open the desk. Inside, you find one singular piece of art."

    e "huh?"
screen talk_key2():
    imagebutton: 
        idle "key2.png"
        hover "key2_hover.png"
        xpos 0
        ypos 100
        action Jump ("idk")
label key2:
    scene bg room
    show 1 at right
    call screen talk_key2
label idk:
    scene bg room
    show key2 at center
    e "Another one?"

    
label random:
    scene bg room
    show 2 at right
    
    "art piece 1 acquired"

    "there are 3 more locks"
    menu: 
        "where do you want to search?"

        "Closet":
            e "words"
            jump random

        "Bed":
            jump random
        "Kitchen":
            jump random 
label closet:
    scene bg room
    show 1 at right

    "You take a few steps into a small hallway, lined with Ithen’s paintings. You hurry through, making it to the kitchen."

    "The kitchen, while not decrepit, feels as if all the color has been drained from it. You can’t help hoping to see Ithen’s face in every corner."

    "You push past your memories. It’s hard but must be done, if you ever want to find out what happened"

    "Your mind does not clear, and your resolve waivers, but you can faintly see something glinting inside the oven."

    “Ithen, he feels so close here.” 

*You have acquired the second key*

*You walk back to the bedroom, a little more numb than before.*

*Placing the key into the lock, it opens. Revealing yet another painting.* 

*You have acquired another art peice.*


