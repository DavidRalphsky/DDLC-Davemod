label natsuki_exclusive3:
    scene bg residential_day with wipeleft_scene
    $ persistent.natsuki_dead = 1
    
    if persistent.playthrough == 0:
        $ persistent.playthrough = 2
    elif persistent.playthrough == 2:
        $ persistent.playthrough = 3
    else:
        $ persistent.playthrough = 4
        
    $ in_character_death = True
    $ delete_character("natsuki")
    "I run home."
    "If something happened to Natsuki, she might have come to my house for refuge."
    "My mind is racing."
    "Unless..."
    "My pace slows a bit."
    "What if I'm overreacting?"
    "Maybe she really was late."
    "Or sick today?"
    "I should've have jumped to conclusions..."
    "I reach my house."
    scene bg house with wipeleft
    "I walk up to my door, but something's wrong."
    "It's hanging open."
    "There's blood on the handle."
    "I quickly run inside. Oh God, oh God."
    scene black with wipeleft
    "I follow a trail of blood into my kitchen."
    mc "Hello?"
    "There's a body in the corner."
    "It has pink hair."
    mc "N-...Natsuki?"
    window hide(None)
    window auto
    show n_kill
    play music td    
    pause 1
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 1
    hide screen tear
    pause 3.75
    "Her body is curled up on the floor."
    "She's covered in bruises."
    "She's not moving."
    mc "Natsuki...no..."
    mc "Natsuki! Talk to me!"
    "She's not breathing."
    "I'm panicking..."
    "Should I perform CPR?"
    "How do you even do CPR?"
    "Would pressing on her chest make it worse?"
    "I grab my head and fall back from her body."
    "It doesn't matter..."
    "It's too late..."
    "I hear someone sobbing..."
    "It takes me a while to realize it's me."
    "She told me about her father..."
    if natsuki_choice == 1:
        "And I told her to stand up to him..."
        "Good God, I'm so stupid!"
        "I told her to stand up to him!"
        "I did this..."
        "I killed her..."
    else:
        "And I told her to go to an adult..."
        "Good God, I'm so stupid!"
        "He must have found out."
        "I did this..."
        "I killed her..."
    "I wanted to help..."
    "But I still couldn't do what she needed from me."
    "And now..."
    "I can never take it back."
    "Never."
    "Never."
    "Never."
    "Never."
    "Never..."
    $ in_character_death = False
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
