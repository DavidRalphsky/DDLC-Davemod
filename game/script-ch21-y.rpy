label ch21_main_y:
    scene bg club_day2
    with dissolve_scene_half
    play music t2g3
    show monika 5 zorder 2 at t11
    m "Hi again, [player]!"
    m "Glad to see you didn't run away on us. Hahaha!"
    mc "Nah, don't worry."
    mc "This might be a little strange for me, but I at least keep my word."
    show monika zorder 1 at thide
    hide monika
    "Well, I'm back at the Literature Club."
    "I was the last to come in, so everyone else is already hanging out."
    show natsuki zorder 2 at i22
    n "Oh, come on! Like he deserves any slack."
    n 4e "You already had to be dragged here by Monika."
    n "I don't know if you plan to just come here and hang out, or what..."
    n "But if you don't take us seriously, then you won't see the end of it."
    show monika 2b onlayer front at l21
    m "Natsuki, you certainly have a big mouth for someone who keeps her manga collection in the clubroom."
    n 4o "M-M-M...!!"
    show monika onlayer front at lhide
    hide monika onlayer front
    "Natsuki finds herself stuck between saying \"Monika\" and \"Manga\"."
    show natsuki at h22
    n 1v "Manga is literature!!"
    show natsuki zorder 1 at thide
    hide natsuki
    "Swiftly defeated, Natsuki plops back into her seat."
    show layer master


    "Now that everyone's settled in, I expected Monika to kick off some scheduled activities for the club."
    "But that doesn't seem to be the case."
    "Sayori and Monika are having a cheery conversation in the corner."
    "I notice that Natsuki is rummaging around in the closet."


    $ nextscene = poemwinner[0] + "_exclusive_" + str(eval(poemwinner[0][0] + "_appeal"))
    call expression nextscene
    
    show monika 1 zorder 2 at t21
    hide sayori
    hide natsuki
    m "By the way, did you remember to write a poem last night?"
    mc "Y-Yeah..."
    "My relaxation ends."
    "I can't believe I agreed to do something so embarrassing."
    "I couldn't really find much inspiration, since I've never really done this before."
    m "Well, now that everyone's ready, why don't you find someone to share with?"
    show sayori 4q zorder 2 at t22
    s "I can't wait~!"
    show sayori zorder 1 at thide
    show monika zorder 1 at thide
    hide sayori
    hide monika
    "Sayori and Monika enthusiastically pull out their poems."
    "Sayori's is on a wrinkled sheet of loose leaf torn from a spiral notebook."
    "On the other hand, Monika wrote hers in a composition notebook."
    "I can already see Monika's pristine handwriting from where I sit."
    "Natsuki reluctantly complies as well, reaching into her bags."
    "I do the same, myself."

    return

label ch21_end_y:
    stop music fadeout 1.0
    scene bg club_day
    with wipeleft_scene
    play music t3
    mc "Phew..."
    "I guess that's everyone."
    "I glance around the room."
    "That was a little more stressful than I anticipated."
    "It's as if everyone is judging me for my mediocre writing abilities..."
    "Even if they're just being nice, there's no way my poems can stand up to theirs."
    "This is a literature club, after all."
    "I sigh."
    "I guess that's what I ended up getting myself into."
    
    scene bg club_day
    show monika 4b zorder 2 at t11
    with wipeleft_scene
    m "Okay, everyone!"
    m "It's just about time for us to leave."
    m "How did you all feel about sharing poems?"
    show monika 4a
    show sayori 4x zorder 2 at t31
    s "It was a lot of fun!"
    show sayori behind natsuki at thide
    hide sayori
    show natsuki 4q zorder 2 at t31
    n "It was alright."
    show natsuki zorder 1 at thide
    hide natsuki
    m 1a "[player], how about you?"
    mc "...Yeah, I'd say the same."
    mc "It was a neat thing to talk about with everyone."
    m 1j "Awesome!"
    m 1a "In that case, we'll do the same thing tomorrow."
    m "And maybe you learned something from your friends, too."
    m 3b "So your poems will turn out even better!"
    mc "..."
    show monika zorder 1 at thide
    hide monika
    "I think to myself."
    "I did learn a little more about the kinds of poems everyone likes."
    "With any luck, that means I can at least do a better job impressing those I want to impress."
    "I nod to myself with newfound determination."
    show sayori 1x zorder 2 at t11
    s "[player]!"
    s "Ready to walk home?"
    mc "Sure, let's go."
    s 4q "Ehehe~"
    "Sayori beams at me."
    "It truly has been a while since Sayori and I have spent this much time together."
    "I can't really say I'm not enjoying it, either."
    scene bg residential_day
    show sayori 1a zorder 2 at t11
    with wipeleft_scene
    s "You know, [player]..."
    s "It's nice that I get to spend time with you in the club."
    s "But I think seeing you get along with everyone is what makes me the happiest."
    s 1x "And I think everyone really likes you, too!"
    mc "That's--!"
    s 4q "Ehehe~"
    s "Every day is going to be so much fun~"
    mc "Sigh..."
    "It looks like Sayori still hasn't caught onto the kind of situation I'm in."
    "Sure, being friends with everyone is nice, but..."
    "...Does it really need to stop there?"
    mc "We'll just have to see what the future holds, Sayori."
    "I pat Sayori on the shoulder."
    "I said that more to myself than to her, but it's easy to use Sayori as an internal monologue sometimes."
    show sayori at h11
    s 1x "Okay~!"
    "Yeah..."
    "Let's do this!"
    return
    