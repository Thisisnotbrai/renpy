# Define Characters
define Akane = Character('Akane', color="#ffb5c0")
define Narrator = Character('Narrator', color="#008000")
define Ayane = Character('Ayane', color="#eb8bb8")  # Akane's Sister
define MomK  = Character("Kotarou's Mom", color="#eb8bb8")  # Akane's Mother
define MomA  = Character("Akane's Mom", color="#eb8bb8")  # Akane's Mother

# Define Images
image akane smile 1 = "akane smile 1.png"
image akane sad = "akane sad.png"
image akane normal = "akane normal.png"
image kotaro normal = "kotaro normal.png"
image kotaro awkward = "kotaro laugh and sweat.png" 
image MomK = "motherkotarou.png" 
image Mom Akane = "motherakane.png" 
image akane smug = "akane smug.png"
image akane annoyed = "akane annoyed.png"


image dummy = "dummy.png"

transform shake:
    xoffset -5
    linear 0.05 xoffset 5
    linear 0.05 xoffset -5
    linear 0.05 xoffset 5
    linear 0.05 xoffset 0 

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
        zoom .9
    Akane "Good evening! It has been such a long day for me."

    # Show dummy character (sister Ayane)
    show dummy at right:
        zoom .9
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
    show akane smile 1 at left:
        zoom .9 
    Narrator "Akane, being shy in the first place, has a blush on her cheeks."

    # Akane feels uncomfortable
    show akane sad at left:
        zoom .6
    Akane "Stop… I feel uncomfortable with this. Excuse me, I will just head to the beverage area to get some drinks."
    
    with dissolve
    pause 0.5

    # Change to beverage area scene
    scene beverage
    with fade

    # Show Kotaro in the beverage area
    show kotaro normal at left:
        zoom .9
    Narrator "Akane held her sanity and went to the beverage area, where Kotarou also happens to get a drink."
    pause 0.5
    
    # Show Akane in the beverage area
    show akane normal at right:
        zoom .9
    Narrator "It is like they were destined to intertwine with each other these past days."

    show kotaro surprised at left:
        zoom .6
    show akane smile 1 at right:
        zoom .9

    # Final moment with both characters shown
    Narrator "They’ve had a glimpse of each other while getting their drink."

    label ask:
    show kotaro laugh and sweat at left:
        zoom .9
    $ approach = False
    Kotarou "Should I speak to her and greet her? That’ll be reasonable since we both are in the same class."

menu:
    "Yes":
        jump speak
    "No":
        jump notspeak

label speak:
    show kotaro awkward:
        zoom .6
    Kotarou "Okay, I guess I'll greet her."
    $ approach = True
    jump yes_scene

label notspeak:
    Narrator "Kotarou was done getting himself and his family their drinks. He then proceeded to their table to give it to them, leaving Akane staring at the beverage machine. He did not even glimpse her way."
    jump main_scene




    label yes_scene: 
        if approach:
            show kotaro normal at left:
                zoom .9
            show akane normal at right:
                zoom .9
            pause 0.5 

            show kotaro awkward at left:
                zoom .6
            Kotarou "Hello! I remember you from our class, I guess you are my classmate, am I right? Nice to see you here!"
            
            show akane smile 1 at center:
                zoom .9

            show dummy at right:
                zoom .9
            Kotarou "H-Hi, yes, we are in the same class. Have a good night!"
            show kotaro normal at left:
                zoom .9
            Narrator "They both felt shy, Kotarou nodded at Akane and bowed at Akane’s sister that was currently heading their way."
            Kotarou "Bye for now, I have to bring this to my parents, they might already be thirsty."
            Akane "O-Okay…"

            with Dissolve (0.5)
            pause 0.5
            

        else:
            jump main_scene


    label main_scene:

        scene restaurant 
        with fade

        show dummy at right:
            zoom .9
        show akane normal at left:
            zoom .9

        Ayane "What’s up, sis? Can you carry all of that, here let me help you."
        show akane smile 1 at left:
            zoom .9
        Akane "Just get some of this and I will manage."
        Ayane "Do you know that guy? You seem so invested with him—you keep looking his way."
        Akane "He is in the same class as mine."

        Narrator "Ayane’s older sister then proceeded to give her parents their drinks."

        with dissolve
        pause 0.5

    # Change to beverage area scene
        scene beverage
        with fade

        show akane normal at left:
            zoom .9

        show Mom Akane at right
            

        "*Akane whispering something to her mother*"

        show Mom Akane at right, shake:
            zoom .9
        MomA  "Is that so!? Really!!? We should proceed by greeting them!"

        with Dissolve (0.5)
        pause 0.5

        scene restaurant
        with fade 

        show MomK at right:
            zoom 2
            
        show Mom Akane at left:
            zoom 2

        Narrator "As Akane headed back to their table, she was flabbergasted by what she saw; she almost dropped a glass full of juice on the ground."
        
        MomA "Yeah, yeah. Nice to meet you, our children are in the same class. Akane, my daughter is your son’s classmate."

      

        MomK "Oh… is that so? Kotarou did not mention any of this. What a coincidence! I hope they’d be good friends with each other. Nice to meet you too!"

        Narrator "Both Akane and Kotarou felt awkwardness and chagrin with the situation. It was clearly unplanned for their parents to talk and to greet each other knowing that even them, themselves haven’t properly introduced themselves to each other, they just got a minimal interaction."

        Narrator "The dinner went on, both families munch on their foods to satisfy their appetite. Afterwards, they went ahead and paid their bills."

        with Dissolve (0.5)
        pause 0.5

        scene restaurant

        show akane sad at left:
            zoom .6
      
        show kotaro normal at right:
            zoom .9
        
        pause 0.5

        Akane " I feel so nervous, but I feel like I need to do this."

        Narrator "Kotarou standing beside the wall while waiting for his family was then approached by Akane."

        Akane "Hey, I know it felt awkward a while ago—when our parents casually greeted each other, we hadn't introduced ourselves properly yet our parents already did to themselves. My name is Akane…."

        Narrator "Akane was bowing down her head out of embarrassment. Kotarou was a bit confused by Akane's sudden move—when she approached Kotarou just to introduce herself."
        
        Kotarou "Don’t mind it, it’s just fine."

        Akane "Hmm, I have a kind of a favor to ask, don’t tell anyone at school about today."

        Narrator "Akane then left Kotarou after saying that. Kotarou was a bit puzzled and dumbfounded by Akane’s words, he never had felt and said such a thing."
        jump scene_3



















    return
