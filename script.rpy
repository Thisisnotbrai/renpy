define Narator = Character('Narator', color="#008000")
define Akane = Character('Akane', color="#ffb5c0")
define Kotarou = Character('Kotarou', color= "#b8e3e9")

label start:

    scene school front
    with fade

    Narator "The new school year begins, bringing fresh classroom assignments. 
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
    Narator "But despite her capabilities to conquer and excel in everything, she cannot contain her emotions most especially her nervousness. 
    However,  with encouragement and determination in her soul, Akane then proceeded to enter their classroom premises to attend her first class on her first day of being a third year student."

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
    Narator "On  the other hand, there is a boy filled with wisdom and perception in his mind. A boy full of knowledge with words only wise knows. He has the capabilities to sort his emotions up through writing a literary piece."

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
    Kotarou "She seems unfamiliar, I haven’t seen her last year, she must be new."

    with Dissolve (0.5)
    pause 0.5

    scene classroom 1

label choice:
    $ approach = False
    Kotarou "SHOULD I APPROACH HER OR NOT?"

menu:
    "Yes":
        jump choice_yes
    "No":
        jump choice_no

label choice_yes:
    Kotarou "Okay let's do it!"
    $ approach = True
    jump choice_scene1

label choice_no:
    Kotarou "Maybe next time. "
    jump choice_scene1

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

        Akane "Ahhh…. Yes… I’m all right, I was just nervous… you know first day of school things"

        Kotarou "Ohh, is that so. Do you need some water?"

        Akane "No, no. But thank you!"

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

label scene_2:
    scene school front
    show akane sad
    Kotarou "null ulit"

return