# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Louise")
define m = Character("...")

default floor4_seen = False
default floor_number = 5

transform fullscreen_background:
    xysize (config.screen_width, config.screen_height)

transform floor7_character_fit:
    xysize (config.screen_width, config.screen_height)
    yoffset 200

transform floor5_character_fit:
    zoom (0.95 * config.screen_height / renpy.image_size("images/floor 5 character.png")[1])
    xalign 0.5
    yalign 0.0
    yoffset 130


# The game starts here.

label start:

    play music "audio/iiif-service_mbrsrs_mbrsjukebox_dlc_victor_35324_02_c4470_01_dlc_victor_35324_02_c4470_01-full-full-0-full-default.mp3" loop if_changed

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    image starting room2:
        "images/starting room2.png"
        xysize (config.screen_width, config.screen_height)
    image distorted starting room2:
        "images/distorted starting room2.png"
        xysize (config.screen_width, config.screen_height)
    image stairs1 unblurred:
        "images/stairs1 unblurred.png"
        xysize (config.screen_width, config.screen_height)
    image hallway1:
            "images/hallway1.png"
            xysize (config.screen_width, config.screen_height)
    image hallway1 unblurred:
            "images/hallway1 unblurred.jpg"
            xysize (config.screen_width, config.screen_height)
    image hallway2:
            "images/hallway2.png"
            xysize (config.screen_width, config.screen_height)
    image hallway3:
            "images/hallway3.png"
            xysize (config.screen_width, config.screen_height)
    image distorted hallway1:
            "images/distorted hallway1.png"
            xysize (config.screen_width, config.screen_height)
    image distorted hallway2:
            "images/distorted hallway2.png"
            xysize (config.screen_width, config.screen_height)
    image distorted hallway3:
            "images/distorted hallway3.png"
            xysize (config.screen_width, config.screen_height)
    image black:
            "images/black.png"
            xysize (config.screen_width, config.screen_height)
    image hiding:
            "images/hiding.png"
            xysize (config.screen_width, config.screen_height)
    image chair:
            "images/chair.png"
            xysize (config.screen_width, config.screen_height)
    image distorted chair:
            "images/distorted chair.png"
            xysize (config.screen_width, config.screen_height)
    image eye cluster:
            "images/eye cluster.png"
            xysize (config.screen_width, config.screen_height)
    image chair unblurred:
            "images/chair unblurred.png"
            xysize (config.screen_width, config.screen_height)
    image unblurred hallway3:
            "images/hallway3 unblurred.jpg"
            xysize (config.screen_width, config.screen_height)
    image unblurred hallway2:
            "images/hallway2 unblurred.png"
            xysize (config.screen_width, config.screen_height)
    image floor 7 character:
            "images/floor 7 character.png"
            xysize (config.screen_width, config.screen_height)
    image floor 5 character:
            "images/floor 5 character.png"

    scene starting room2 at fullscreen_background
    with fade

    
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.
    show floor 5 character at floor5_character_fit
    m "A ringing comes from down the hallway."

    e "What was that!?"

    menu:
        "Go investigate the noise":
            e "I should go check it out..."
            e "The sound is coming from the downstairs."
            label stairs5:
                scene stairs1 unblurred at fullscreen_background
                e "Which way do I go...?"
                menu:
                    "Go downstairs":
                        e "I'll go downstairs to investigate."
                        if floor4_seen:
                            jump floor4v2
                        else:
                            jump floor4v1
                    "Go upstairs":
                        e "I'll go upstairs to investigate."
                        jump floor6
            
        "Ignore it":
            m "The ringing continues."
            menu:
                "Go investigate the noise":
                    e "The sound is coming from the downstairs."
                    jump stairs5
                "Ignore it":
                    e "The sound is getting louder..."
                    e "I need to leave."
                    m "There are stairs at the end of the hallway."
                    jump stairs5


    label floor4v1:
        $ floor4_seen = True
        scene black at fullscreen_background
        m "You are on floor 4."
        scene hallway1 at fullscreen_background

        e "There's a light in the distance."
        e "Someone's coming this way..."
        menu:
            "Hide in the laundry cart":
                scene black at fullscreen_background
                e "I should be safe here..."
                m "The figure passes by and doesn't spot anything."
                scene hallway1 at fullscreen_background
                $ floor_number = 4
                $ floor_image = "hallway1"
                jump floor_choices

                
            "Hide in the the cell":
                scene black at fullscreen_background
                e "I'll hide in the cell over there."

                scene hiding at fullscreen_background
                menu:
                    "You've been found. Restart.":
                        jump start

label floor1:
    $ floor_number = 1

    scene expression Transform("images/exit.png", xysize=(config.screen_width, config.screen_height)) at fullscreen_background
    show floor 5 character at floor5_character_fit
    with fade

    m "You reached the exit."
    m "You escaped."

    return


label floor2:
    scene unblurred hallway3 at fullscreen_background
    m "memory"
    $ floor_number = 2
    $ floor2_image = renpy.random.choice(["hallway3", "distorted hallway3"])
    $ floor_image = floor2_image

    scene expression floor_image at fullscreen_background
    with fade
    m "You are on floor 2."

    jump floor_choices


label floor3:
    scene unblurred hallway2 at fullscreen_background
    m "memory"
    $ floor_number = 3
    $ floor3_image = renpy.random.choice(["hallway2", "distorted hallway2"])
    $ floor_image = floor3_image

    scene expression floor_image at fullscreen_background
    with fade
    m "You are on floor 3."

    jump floor_choices


label floor4:
label floor4v2:
    scene hallway1 unblurred at fullscreen_background
    m "memory"
    $ floor_number = 4
    $ floor4_image = renpy.random.choice(["hallway1", "distorted hallway1"])
    $ floor_image = floor4_image

    scene expression floor_image at fullscreen_background
    with fade
    m "You are on floor 4."
    e "Did this room always look like this...?"
    e "Am i seeing things again...?"
    m "Loud ringing resumes continues to sound."
    e "The sound is coming from upstairs again..."
    e "I need to make it to the exit on level 1."

    jump floor_choices


label floor5:
    $ floor_number = 5
    $ floor5_image = renpy.random.choice(["starting room2", "distorted starting room2"])
    $ floor_image = floor5_image

    scene expression floor_image at fullscreen_background
    with fade
    m "You are back on floor 5."
    e "Did this room always look like this...?"
    e "I think something is wrong."
    e "I need to make it to the exit downstairs."


    jump floor_choices


label floor6:
    scene chair unblurred at fullscreen_background
    m "memory"
    $ floor_number = 6
    $ floor6_image = renpy.random.choice(["chair", "distorted chair"])

    $ floor_image = floor6_image

    scene expression floor_image at fullscreen_background
    with fade
    m "You are on floor 6."
    e "Did this room always look like this...?"
    e "Something feels wrong."
    e "I'm seeing things again...I think...?"
    e "I need to make it to the exit downstairs."

    jump floor_choices


label floor7:
    $ floor_number = 7
    $ floor7_image = "eye cluster"
    $ floor_image = floor7_image
    scene black at fullscreen_background
    e "Where am I...?"
    e "I can't see anything..."
    e "I..."
    scene eye cluster at fullscreen_background
    show floor 7 character at floor7_character_fit
    m "You reached the top floor. You died."

    menu:
        "Restart":
            $ floor4_seen = False
            $ floor_number = 5
            jump start

        "Return to main menu":
            return


label floor_choices:
    menu:
        "Go upstairs":
            $ floor_step = 1
        "Go downstairs":
            $ floor_step = -1

    if floor_image.startswith("distorted"):
        $ floor_step = -floor_step

    $ next_floor = floor_number + floor_step

    if next_floor < 1:
        m "There are no floors below floor 1."
        jump floor_choices
    elif next_floor > 7:
        m "There are no floors above floor 7."
        jump floor_choices

    if next_floor == 4:
        if not floor4_seen:
            jump floor4v1
        jump floor4v2

    jump expression "floor" + str(next_floor)
