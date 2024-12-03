define Narrator = Character('Narrator', color="#5fad5f")
define Akane = Character('Akane', color="#ffb5c0")
define Kotarou = Character('Kotarou', color= "#b8e3e9")
define Aira = Character('Aira', color="#f0e68c")
define Daichi = Character('Daichi', color="#c03f3f")

label start:

    scene school front
    with fade

    Narrator "The new school year begins, bringing fresh classroom assignments. 
    Kotarou Azumi, a shy literature enthusiast aspiring to be a great writer, 
    meets Akane Mizuno, a talented track star who excels in both sports and academics."

    with Dissolve (0.5)
    pause 0.5

    scene school corridor 1

    show akane smile 1
    Akane "Breathe in, breathe out. Stay calm, you will be okay."
    with fade

    show akane sad
    Akane "I am feeling nervous about this new school year of mine. But this will be okay, I got this!"

    with Dissolve (0.5)
    pause 0.5

    scene school corridor 1
    Narrator "But despite her capabilities to conquer and excel in everything, she cannot contain her emotions most especially her nervousness."

    Narrator "However,  with encouragement and determination in her soul, Akane then proceeded to enter their classroom premises to attend her first class on her first day of being a third year student."

    with dissolve

    scene classroom 1
    image  kotaro normal:
        "kotaro normal.png"
        zoom .9
    show kotaro normal
    Kotarou "Even in middle school, there is inequality—upper class and middle class, smart and average, and cool clubs and lame ones."
    
    with Dissolve (0.5)
    pause 0.5

    scene classroom 1 
    Narrator "On  the other hand, there is a boy filled with wisdom and perception in his mind. A boy full of knowledge with words only wise knows. He has the capabilities to sort his emotions up through writing a literary piece."

    with Dissolve (0.5)
    pause 0.5
    
    scene classroom 1
    image  akane normal:
        "akane normal.png"
        zoom .6
    show akane normal at right

    image  kotaro normal:
        "kotaro normal.png"
        zoom .6
    show kotaro normal at left
    Kotarou "She seems unfamiliar, I haven't seen her last year, she must be new."

    with Dissolve (0.5)
    pause 0.5

    scene classroom 1

label choice:
    image  kotaro laugh and sweat:
        "kotaro laugh and sweat.png"
        zoom .6
    show kotaro laugh and sweat
    $ approach = False
    Kotarou "SHOULD I APPROACH HER OR NOT?"

menu:
    "Yes":
        jump choice_yes
    "No":
        jump choice_no

label choice_yes:
    image  kotaro smirk:
        "kotaro smirk.png"
        zoom .6
    show kotaro smirk
    Kotarou "Okay let's do it!"
    $ approach = True
    jump choice_scene1

label choice_no:
    Kotarou "Maybe next time. "
    jump choice_scene2

label choice_scene1: 

label flags:
    if approach:
        image  akane normal:
            "akane normal.png"
            zoom .6
        show akane normal at right
        image  kotaro laugh and sweat:
            "kotaro laugh and sweat.png"
            zoom .6
        show kotaro laugh and sweat at left
        Kotarou "H-hi… are you okay? You seem so pale, are you feeling well?"

        Akane "Ahhh…. Yes… I'm all right, I was just nervous… you know first day of school things"

        image  kotaro normal:
            "kotaro normal.png"
            zoom .6
        show kotaro normal at left
        Kotarou "Ohh, is that so. Do you need some water?"

        Akane "No, no. But thank you!"

        image  kotaro laugh and sweat:
            "kotaro laugh and sweat.png"
            zoom .6
        show kotaro laugh and sweat at left
        Kotarou "All right!"

        with Dissolve (0.5)
        pause 0.5

        scene classroom 1
        image  kotaro laugh and sweat:
            "kotaro laugh and sweat.png"
            zoom .6
        show kotaro laugh and sweat
        Kotarou "Phew! Why was that so awkward and kind of tense"
        jump scene_2

    else:
        show kotaro normal
        Kotarou "null"
        jump scene_2

label choice_scene2:

label flags_2: 
    scene school corridor 1
    image  aira delighted:
            "aira delighted.png"
            zoom 1.3
    show aira delighted at right
    image  akane normal:
            "akane normal.png"
            zoom .6
    show akane normal at left
    Aira "Akane! Here it’s Aira, remember me?"

    Narrator "Akane was then called by her friends to come over to their desks."

    image  aira laugh:
            "aira laugh.png"
            zoom 1.3
    show aira laugh at right
    Aira "We were in the same third grade class. I'm so glad we're in the same class again!"

    image  akane smile 1:
            "akane smile 1.png"
            zoom .6
    show akane smile 1 at left   
    Akane "Oh, Aira! I remember you! I'm glad to see you again too!"


    Aira "You're in the track and field club, aren't you?"

    Akane "Yes, I am."

    with Dissolve (0.5)
    scene school corridor 1
    Daichi "Do you know her? You have been staring at her since the time she walked in this classroom."

    Kotarou "Oh, no, I don't know her. I was just thinking about something."

    scene school corridor 1
    image chill guy:
        "chill guy.png"
        zoom 3.0
    show chill guy
    Narrator "For the first time, the two are placed in the same class. 
    Although they notice each other, their interactions are limited to fleeting glances, as they belong to different social circles."
    jump scene_2

return