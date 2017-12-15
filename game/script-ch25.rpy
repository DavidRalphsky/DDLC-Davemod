label ch25_main:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full

    "It's the day of the festival."
    if ch24_scene == "sayori":
        "I've been helping Sayori with the project online."
        "She had some great designs ready, and we discussed them for what felt like hours."
        "I don't know why. I didn't really have any contributions to make to the discussion."
        "She just wanted to talk I guess."
        "Anyways, now I've got to carry these pamphlets to school."
        "Sayori slept in again."
        "I can't really worry about that though. Monika will kill me if I show up late. These pamphlets are the most important part."
    elif ch24_scene == "natsuki":
        "I couldn't wait to see how everyone reacted to our cupcakes."
        "Natsuki hasn't responded to any of my texts, but I figured she had her hands full with the trays."
        "She had volunteered to bring them herself."
    else:
        "The banner Yuri and I painted is dry, and I gently rolled it up to take with me."
        "She sent me a pleasant text reminding me not to forget anything, and I reassured her."
    "I'm more excited for the festival to be over so I can spend time with [ch4_name] at the festival."
    "But knowing Monika, I'm sure the event will be great, too."
    
    if ch24_scene == "yuri":
        call yuri_exclusive3 
        return
    
    scene bg club_day with wipeleft_scene
    show monika 5 zorder 2 at t11
    m "[player]!"    
    m "You're the first one here."
    m "Thanks for being early!"
    mc "That's funny, I thought at least Yuri would be here by now."
    "Monika is placing little booklets on each of the desks in the classroom."
    "They must be the ones she prepared that has all the poems we're performing."
    "In the end, I found a random poem online that I thought Monika would like, and submitted it."
    "So, that's the one I'll be performing."
    m 1d "I'm surprised you didn't bring Sayori with you."
    mc "Yeah, she overslept again..."
    mc "That dummy."
    mc "You'd think that on days this important, she'd try a little harder..."
    if sayori_hearttoheart == True:
        "I say that, but I suddenly remember what Sayori told me yesterday..."
        "And I suddenly feel awful, knowing it's not nearly that simple for her."
        "I only said it because it's the way I'm used to thinking."
        "But..."
        "Maybe I should have gone to wake her up after all?"
        m 1k "Ahaha."
        m 4b "You should take a little responsibility for her, [player]!"
        m "I mean, especially after your exchange with her yesterday..."
        m "You kind of left her hanging this morning, you know?"
        show monika 4a
        mc "Exchange...?"
        mc "Monika-- You know about that??"
        m 2a "Of course I do."
        m "I'm the club president, after all."
        mc "But--!"
        "I stammer, embarrassed."
        "Did Sayori really tell her about it that quickly?"
        if sayori_confess:
            "That we're...a couple now?"
            "I didn't really plan on bringing it up with anyone yet..."
        else:
            "About how I basically turned down her confession?"
            "That makes me really seem like the bad guy here..."
            "But I'm the one who knows what's best for her, right?"
        mc "Jeez..."
        mc "You don't know understand...it's complicated..."
        m 2j "Don't worry."
        m "I probably know a lot more than you think."
        "What does that mean?"
        "Monika looks at me kind of expectantly."
        mc "Oh! The pamphlets. Here."
        "I show her the pamphlets. I notice Sayori's is an entire block of text."
        hide monika
        call showpoem (poem_sayori, music=False)
        mc "Ah--"
        "What is this...?"
        "Reading the poem, I get a pit in my stomach."
        show monika 1d zorder 2 at t11
        m "[player]?"
        m "What's wrong?"
        mc "Oh God."
        "What the hell is wrong with me?!"
        "How could I not realize what was wrong?"
        mc "I have to go!"
        m "What?"
        m "What's wrong?"
        "I sprint out of the room without answering."
        call sayori_exclusive3 
    else:
        mc "Hey, where's Natsuki?"
        m "I don't know. She's just not here."
        mc "What? Did she text you?"
        m "No. What's wrong?"
        if persistent.yuri_dead == 0:
            show yuri 1 zorder 2 at t33
            y "Hey everyone. Are we ready for the festival?"
            mc "Wait a minute, did either of you hear from Natsuki?"
            show sayori 1 zorder 2 at t31
        elif persistent.sayori_dead == 0:
            s "Sorry I'm late!"
            m "That's alright, we were just getting started."
            mc "GUYS! Where is Natsuki?!"
        else:
            mc "Oh God."
        m "[player], calm down. She's probably just late."
        "Oh God, oh God. What if something happened to Natsuki?"
        mc "I-I've got to go!"
        m "[player]!"
        "I sprint out of the room without answering."
        call natsuki_exclusive3
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

