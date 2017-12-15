


label start:


    $ anticheat = persistent.anticheat


    $ chapter = 0


    $ _dismiss_pause = config.developer


    $ s_name = "???"
    $ m_name = "Girl 3"
    $ n_name = "Girl 2"
    $ y_name = "Girl 1"

    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ in_character_death = None
    $ allow_skipping = True
    $ config.allow_skipping = True


    if persistent.playthrough == 0:

        $ chapter = 0
        call ch0_main


        call poem


        $ chapter = 1
        call ch1_main
        call poemresponse_start
        call ch1_end


        call poem


        $ chapter = 2
        call ch2_main
        call poemresponse_start
        call ch2_end


        call poem


        $ chapter = 3
        call ch3_main
        call poemresponse_start
        call ch3_end

        $ chapter = 4
        call ch4_main
        
        $ chapter = 5
        call ch5_main

        call endgame

    elif persistent.playthrough == 2: # Act 2
        $ chapter = 0
        if persistent.natsuki_dead == 1:
            call ch10_n
        elif persistent.yuri_dead == 1:
            call ch10_y
        else:
            call ch10_s
        call poem
        $ chapter = 1
        if persistent.natsuki_dead == 1:    # Natsuki dies first
            call ch21_main_n
            call poemresponse_start
            call ch21_end_n
            call poem (False)
            $ chapter = 3
            call ch23_main_n
            call poemresponse_start
            call ch23_end_n
            $ chapter = 4
            call ch24_main
            $ chapter = 5                    
            call ch25_main
            call endgame
            
        elif persistent.yuri_dead == 1: # Yuri dies first
            call ch21_main_y
            call poemresponse_start
            call ch21_end_y
            call poem (False)
            $ chapter = 3
            call ch23_main_y
            call poemresponse_start
            call ch23_end_y
            $ chapter = 4
            call ch24_main
            $ chapter = 5                    
            call ch25_main
            call endgame
            
        else:                              # Sayori dies first
            call ch21_main_s
            call poemresponse_start
            call ch21_end_s
            call poem (False)
            $ chapter = 3
            call ch23_main_s
            call poemresponse_start
            call ch23_end_s
            $ chapter = 4
            call ch24_main
            $ chapter = 5                    
            call ch25_main
            call endgame
            
    elif persistent.playthrough == 3: # Act 3
        if persistent.natsuki_dead == 1:       
            if persistent.yuri_dead == 1:     
                call ch30_main_s
                call sayori_exclusive4
                call sayori_exclusive3
            else:                                     
                call ch30_main_y
                call ch4_exclusive_yuri
                call yuri_exclusive3
        elif persistent.yuri_dead == 1:      
            if persistent.natsuki_dead == 1:  
                call ch30_main_s
                call sayori_exclusive4
                call sayori_exclusive3
            else:                                       
                call ch30_main_n
                call ch4_exclusive_natsuki
                call natsuki_exclusive3
        else:                                           
            if persistent.natsuki_dead == 1:  
                call ch30_main_y   
                call ch4_exclusive_yuri
                call yuri_exclusive3
            else:                                       
                call ch30_main_n
                call ch4_exclusive_natsuki
                call natsuki_exclusive3
                

    elif persistent.playthrough == 4:           # Everyone's dead

        $ chapter = 0
        call ch40_main
        jump credits

label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
