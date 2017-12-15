label yuri_exclusive3:
    scene bg residential_day with wipeleft    
    "It's the day of the festival, and I'm running really late."
    "I was wrapped up thinking about Yuri and forgot to set my alarm."
    "Thankfully my natural clock meant I woke up around the same time."
    "Despite being late, I can't help but be smiling."
    "I can't wait to see Yuri again."
    "The festival should be a big boost in her confidence. This banner is going to draw some eyes."
    "I wonder if I should try to get people to compliment her? That could help a lot."
    "I decide I should probably send her a text to see how she is. It'll be nice for her to know someone cares."
    "Huh, I have a bunch of texts. How come my phone didn't buzz?"
    "I must have set it to silent, or just didn't feel it buzzing."
    "I unlock my phone and check who's been texting."
    stop music
    "It's Yuri."
    "{i}[player], I can hear them again.{/i}"
    "{i}The walls are closing in...{/i}"
    "{i}[player]?{/i}"
    "{i}[player]!{/i}"
    "{i}[player]...please!{/i}"
    "Oh God."
    "I quickly text her back, trying to simultaneously comfort her and explain why I didn't respond."
    "No response, but it's only been a few seconds. I start running."
    
    scene bg corridor with wipeleft
    "I run down the hall on the way to the Literature Club. I can already tell something's wrong."
    "Monika is standing in front of the door. She looks distraught."
    "I realize I'm still carrying the stupid banner and drop it, running up to Monika."
    mc "What happened?"
    show monika 1d zorder 2 at t11
    m "[player], don't go in there. Go get a teacher."
    mc "What? What's wrong?"
    m 1q "It's Yuri, she..."
    mc "What happened, Monika?!"
    m "Just...go get a teacher, [player]."
    "I grab the door handle. I need to find out if Yuri."
    "If she hurt herself again..."
    m 1d "[player], don't..."
    "I don't care. I open the door."
    scene bg club_day with wipeleft_scene
    "I run in, scanning the room."
    "{cps=30}There's something on the floo--{/cps}{nw}"
    
    window hide(None)
    window auto
    $ persistent.yuri_dead = 1
    
    if persistent.playthrough == 0:
        $ persistent.playthrough = 2
    elif persistent.playthrough == 2:
        $ persistent.playthrough = 3
    else:
        $ persistent.playthrough = 4
        
    $ in_character_death = True
    $ delete_character("yuri")

    show y_kill
    play music td
    pause 1
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 1
    hide screen tear
    pause 3.75
    
    "No...Oh my God...no..."
    "How could I let this happen?"
    "This is all my fault..."
    "There's a piece of paper on the ground next to her."
    "It's somehow untouched by all the blood."
    "I pick it up..."
    call showpoem (poem_yuri, music=False)
    "What the fuck..."
    "I did this...."
    "I wanted to help her..."
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
