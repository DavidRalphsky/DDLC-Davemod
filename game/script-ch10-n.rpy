image ghost3 = Image("natsuki/ghost3.png")

label ch10_n:
    $ delete_all_saves()
    $ persistent.deleted_saves = True
    $ config.window_hide_transition = None
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2
 
    s "Heeeeeeeyyy!!"
    "I see an annoying girl running toward me from the distance, waving her arms in the air like she's totally oblivious to any attention she might draw to herself."
    "That girl is Sayori, my neighbor and good friend since we were children."
    "You know, the kind of friend you'd never see yourself making today, but it just kind of works out because you've known each other for so long?"
    "We used to walk to school together on days like this, but starting around high school she would oversleep more and more frequently, and I would get tired of waiting up."
    "But if she's going to chase after me like this, I almost feel better off running away."
    "However, I just sigh and idle in front of the crosswalk and let Sayori catch up to me."
    $ s_name = "Sayori"
    show sayori 4p zorder 2 at t11
    s 4p "Haaahhh...haaahhh..."
    s "I overslept again!"
    s "But I caught you this time!"
    mc "Maybe, but only because I decided to stop and wait for you."
    show sayori at s11
    s 5c "Eeehhhhh, you say that like you were thinking about ignoring me!"
    s "That's mean, [player]!"
    mc "Well, if people stare at you for acting weird then I don't want them to think we're a couple or something."
    show sayori zorder 2 at t11
    s 1a "Fine, fine."
    s "But you did wait for me, after all."
    s "I guess you don't have it in you to be mean even if you want to~"
    mc "Whatever you say, Sayori..."
    s 1q "Ehehe~"
    show sayori zorder 1 at thide
    hide sayori
    "We cross the street together and make our way to school."
    "As we draw near, the streets become increasingly speckled with other students making their daily commute."
    show sayori 3a zorder 2 at t11
    s "By the way, [player]..."
    s "Have you decided on a club to join yet?"
    mc "A club?"
    mc "I told you already, I'm really not interested in joining any clubs."
    mc "I haven't been looking, either."
    show sayori at s11
    s 4h "Eh? That's not true!"
    s "You told me you would join a club this year!"
    mc "Did I...?"
    "I'm sure it's possible that I did, in one of our many conversations where I dismissively go along with whatever she's going on about."
    "Sayori likes to worry a little too much about me, when I'm perfectly content just getting by on the average while spending my free time on games and anime."
    s 4j "Uh-huh!"
    s "I was talking about how I'm worried that you won't learn how to socialize or have any skills before college."
    s "Your happiness is really important to me, you know!"
    s "And I know you're happy now, but I'd die at the thought of you becoming a NEET in a few years because you're not used to the real world!"
    s 4g "You trust me, right?"
    s "Don't make me keep worrying about you..."
    mc "Alright, alright..."
    mc "I'll look at a few clubs if it makes you happy."
    mc "No promises, though."
    s 1h "Will you at least promise me you'll try a little?"
    mc "Yeah, I guess I'll promise you that."
    show sayori zorder 2 at t11
    s 4r "Yaay~!"
    "Why do I let myself get lectured by such a carefree girl?"
    "More than that, I'm surprised I even let myself relent to her."
    "I guess seeing her worry so much about me makes me want to ease her mind at least a little bit - even if she does exaggerate everything inside of her head."
 
    scene bg class_day
    with wipeleft_scene
 
    "The school day is as ordinary as ever, and it's over before I know it."
    "After I pack up my things, I stare blankly at the wall, looking for an ounce of motivation."
    mc "Clubs..."
    "Sayori wants me to check out some clubs."
    "I guess I have no choice but to start with the anime club..."
 
    s "Hellooo?"
    show sayori 1b zorder 2 at t11
    mc "Sayori...?"
    "Sayori must have come into the classroom while I was spacing out."
    "I look around and realize that I'm the only one left in the classroom."
    s 1a "I thought I'd catch you coming out of the classroom, but I saw you just sitting here and spacing out, so I came in."
    s "Honestly, you're even worse than me sometimes... I'm impressed!"
    mc "You don't need to wait up for me if it's going to make you late to your own club."
    s 1y "Well, I thought you might need some encouragement, so I thought, you know..."
    mc "Know what?"
    s 1a "Well, that you could come to my club!"
    mc "Sayori..."
    s 4r "Yeah??"
    mc "...There is no way I'm going to your club."
    show sayori at s11
    s 5d "Eeeehhhhh?! Meanie!"
    "Sayori is vice president of the Literature Club."
    "Not that I was ever aware that she had any interest in literature."
    "In fact, I'm 99%% sure she only did it because she thought it would be fun to help start a new club."
    "Since she was the first one to show interest after the one who proposed the club, she inherited the title \"Vice President\"."
    "That said, my interest in literature is guaranteed to be even less."
    mc "Yeah. I'm going to the anime club."
    show sayori zorder 2 at t11
    s 1g "C'mon, please?"
    mc "Why do you care so much, anyway?"
    s 5b "Well..."
    s "I kind of told the club yesterday I would bring in a new member..."
    $ gtext = glitchtext(7)
    s "{cps=30}And [gtext] made [gtext][gtext]{/cps}{nw}"
    stop music
    scene black with None
    pause 3
    scene bg corridor with None
    $ gtext = glitchtext(7)
    $ style.say_dialogue = style.normal
    "And thus, today marks the day I sold my soul for a [gtext]"
    "I dejectedly follow Sayori across the school and upstairs - a section of the school I rarely visit, being generally used for third-year classes and activities."
    "Sayori, full of energy, swings open the classroom door."
    call ch10_n2
    return

label ch10_n2:
    scene bg club_day
    with wipeleft
    play music t3
    show sayori 4 at l41
    s "Everyone! The new member is here~!"
    mc "I told you, don't call me a 'new member--'"
    show sayori at lhide
    hide sayori
    "Eh? I glance around the room."
    show yuri 1a zorder 2 at t11
    y "Welcome to the Literature Club. It's a pleasure meeting you."
    y "Sayori always says nice things about you."
    show yuri zorder 2 at t22
    show natsuki glitch1 zorder 2 at t21
    $ gtext = glitchtext(20)
    $ n_name = glitchtext(7)
    n "{cps=30}[gtext]{/cps}{nw}" 
    $ currentpos = get_pos()
    play music "<from " + str(currentpos) + " loop 10.893>bgm/3.ogg"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.1
    play music "<from " + str(currentpos) + " loop 10.893>bgm/3.ogg"
    pause 0.1
    play music "<from " + str(currentpos) + " loop 10.893>bgm/3.ogg"
    pause 0.1
    play music "<from " + str(currentpos) + " loop 10.893>bgm/3.ogg"
    pause 0.1
    play music "<from " + str(currentpos) + " loop 10.893>bgm/3.ogg"
    pause 0.1
    hide natsuki glitch1
    hide screen tear
    $ audio.t6g = "<loop 10.893>bgm/6g.ogg"
    play music t6g
    show monika 1k zorder 2 at t21
    $ m_name = 'Girl 2'
    m "Ah, [player]! What a nice surprise!"
    m "Welcome to the club!"
    show monika 1a
    mc "..."
    "All words escape me in this situation."
    "This club..."
    "{i}...is full of incredibly cute girls!!{/i}"
 
    show monika zorder 1 at thide
    show yuri zorder 1 at thide
    hide monika
    hide yuri
 
    s "This is Yuri, the smartest in the club!"
    $ y_name = 'Yuri'
    show sayori zorder 2 at t21
    show yuri zorder 3 at f22
    y 4b "D-Don't say things like that..."
    "Yuri, who appears decently mature and timid, seems to have a hard time keeping up with people like Sayori."
    show yuri zorder 2 at t22
    mc "Ah... Well, it's nice to meet you."
    show yuri zorder 1 at thide
    hide yuri
    show sayori zorder 3 at f21
    s 1a "And it sounds like you already know Monika, is that right?"
    $ m_name = 'Monika'
    show sayori zorder 2 at t21
    show monika 2a zorder 3 at f22
    m "That's right."
    m "It's great to see you again, [player]."
    show monika 5a at hop
    "Monika smiles sweetly."
    "We do know each other - well, we rarely talked, but we were in the same class last year."
    "Monika was probably the most popular girl in class - smart, beautiful, athletic."
    "Basically, completely out of my league."
    "So, having her smile at me so genuinely feels a little..."
    mc "Y-You too, Monika."
    show monika zorder 1 at thide
    hide monika
    show sayori zorder 3 at f21
    s 4x "Come sit down, [player]! We made room for you at the table, so you can sit next to me or Monika."
    $ gtext = glitchtext(20)
    s "I'll get the cupc{fast}[gtext] [gtext]{nw}"
    $ currentpos = get_pos()
    stop music
    show screen tear(20, 0.5, 0.5, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    show ghost3 at t11 with None
        
    pause 0.5
    hide screen tear
    scene black with None
    hide ghost3 onlayer front    
    pause 5
    
    scene bg club_day with None
    play music "<from " + str(currentpos) + " loop 10.893>bgm/6.ogg"
    
    show monika zorder 2 at t11
    m 3b "Okay, everyone!"
    m "I think with that, we can officially end today's meeting on a good note."
    m "Everyone remember tonight's assignment:"
    m "Write a poem to bring to the next meeting, so we can all share!"
    "Monika looks over at me once more."
    m 1a "[player], I look forward to seeing how you express yourself."
    show monika 5 at hop
    m "Ehehe~"
    mc "Y-Yeah..."
    show monika zorder 1 at thide
    hide monika
    "Can I really impress the class star Monika with my mediocre writing skills?"
    "I already feel the anxiety welling up inside me."
    $ gtext = glitchtext(7)
    "Meanwhile, the girls continue to chit-chat as Yuri and [gtext] clean up their food."
    show sayori 1a zorder 2 at t11
    s "Hey, [player], since we're already here, do you want to walk home together?"
    "That's right - Sayori and I never walk home together anymore because she always stayed after school for clubs."
    mc "Sure, might as well."
    s 4q "Yaay~"
 
    scene bg residential_day
    with wipeleft_scene
 
    "With that, the two of us depart the clubroom and make our way home."
    "The whole way, my mind wanders back and forth between the three girls:"
    show sayori 1 zorder 2 at t31
    "Sayori,"
    show yuri 1 zorder 2 at t32
    "Yuri,"
    show monika 1 zorder 2 at t33
    "and, of course, Monika."
    "Will I really be happy spending every day after school in a literature club?"
    "Perhaps I'll have the chance to grow closer to one of these girls..."
    hide sayori
    hide yuri
    hide monika
    with wipeleft
    "Alright!"
    "I'll just need to make the most of my circumstances, and I'm sure good fortune will find me."
    "And I guess that starts with writing a poem tonight..."
    
    return
    