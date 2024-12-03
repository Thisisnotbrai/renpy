# Define Characters
define Akane = Character('Akane', color="#ffb5c0")
define Narrator = Character('Narrator', color="#008000")
define Ayane = Character('Ayane', color="#eb8bb8")  # Akane's Sister

# Define Images
image akane smile 1 = "akane smile 1.png"
image akane sad = "akane sad.png"
image akane normal = "akane normal.png"
image kotaro normal = "kotaro normal.png"
image kotaro awkward = "kotaro laugh and sweat.png" 

image dummy = "dummy.png"

# The backgrounds and expression must be change.

label scene_2:

    scene school front
    with fade

    Narrator "Days have passed for the two of them. As the school prepares for its sports festival, Akane focuses on her training while Kotarou spends his time immersed in books, observing the world from the sidelines."    
    with dissolve
    pause 0.5

    scene house akane
    with fade

    # Akane's happy expression
    show akane smile 1 at left:
        zoom .6
    Akane "Good evening! It has been such a long day for me."

    # Show dummy character (sister Ayane)
    show dummy at right:
        zoom .6
    Akane "Hello, sis, apparently we are having our dinner outside."
    
    # Akane's happy response
    Akane "Really!? That’s nice! Let me change my clothes first."
    with dissolve
    pause 0.5

    # Change to restaurant at night
    scene restaurant 
    Narrator "It was just a typical and usual dinner night for the family. They all ordered the dishes they pleased and indulged in every piece of it."
    Narrator "Not until Akane had a glimpse of someone familiar—a boy sitting two tables beside them, also eating with his family tonight."

    # Akane's anxious expression
    show akane sad at left:
        zoom .6
    Akane "He is in the same class as me. This feels so uncomfortable."
    with dissolve
    pause 0.5

    Narrator "Akane feels anxious by Kotarou’s presence in the restaurant they are in. What a coincidence, right?"

    # Akane's sister advises her
    show akane sad at left
    show dummy at right
    Ayane "You have a game, right? You should be eating lots of healthy food."

    # Akane's shy expression
    show akane smile 1 at left
    Narrator "Akane, being shy in the first place, has a blush on her cheeks."

    # Akane feels uncomfortable
    show akane sad at left
    Akane "Stop… I feel uncomfortable with this. Excuse me, I will just head to the beverage area to get some drinks."
    with dissolve
    pause 0.5

    # Change to beverage area scene
    scene beverage
    with fade

    # Show Kotaro in the beverage area
    show kotaro normal at left:
        zoom .6
    Narrator "Akane held her sanity and went to the beverage area, where Kotarou also happens to get a drink."
    pause 0.5
    
    # Show Akane in the beverage area
    show akane normal at right:
        zoom .6
    Narrator "It is like they were destined to intertwine with each other these past days."

    show kotaro surprised at left:
        zoom .6
    show akane smile 1 at right:
        zoom .6

    # Final moment with both characters shown
    Narrator "They’ve had a glimpse of each other while getting their drink."

    label choice:
    image  kotaro laugh and sweat:
        "kotaro laugh and sweat.png"
        zoom .6
    show kotaro laugh and sweat
    $ approach = False
    Kotarou "Should I speak to her and greet her? That’ll be reasonable since we both are in the same class."

    menu:
    "Yes":
        jump choice_yes
    "No":
        jump choice_no


    label choice_yes:
    show kotaro awkward
        zoom .6
    Kotarou "Okay, I guess I'll greet her "
    $ approach = True
    jump yes_scene


    label choice_no:
    Narrator "Kotarou was done getting himself and his family their drinks. He then proceeded to their table to give it to them, leaving Akane staring at the beverage machine. He did not even glimpse her way."
    jump main_scene



    label yes_scene: 

    label flags:
        if approach:
            show kotaro normal at left
            zoom .6
            show akane normal at right
            zoom .6
            pause 0.5 

            show kotaro awkward at left
            zoom .6
            Kotarou "Hello! I remember you from our class, I guess you are my classmate, am I right? Nice to see you here!"
            
            show akane smile 1 at center
            zoom .6

            show dummy at right
            zoom .6
            Kotarou "H-Hi, yes, we are in the same class. Have a good night!"
            show kotaro smile at left
            zoom .6
            Narrator "They both felt shy, Kotarou nodded at Akane and bowed at Akane’s sister that was currently heading their way."
            Kotarou "Bye for now, I have to bring this to my parents, they might already be thirsty."
            Akane "O-Okay…"
            

        else:
            show kotaro normal
            Kotarou "null"
            jump main_scene


    label main_scene:



    return
