label ch21_main_n:
    scene bg club_day
    with dissolve_scene_half
    play music t2
    show monika 5 zorder 2 at t11

    m "Hi again, [player]!"
    m "Glad to see you didn't run away on us. Hahaha!"
    mc "Nah, don't worry."
    mc "This might be a little strange for me, but I at least keep my word."
    show monika zorder 1 at thide
    hide monika
    "Well, I'm back at the Literature Club."
    "I was the last to come in, so everyone else is already hanging out."
    show yuri 1a zorder 2 at t32
    y "Thanks for keeping your promise, [player]."
    y "I hope this isn't too overwhelming of a commitment for you."
    y 1u "Making you dive headfirst into literature when you're not accustomed to it..."
    show yuri zorder 2 at t22
    show sayori 2x zorder 3 at f21
    s "Don't worry, guys~"
    s "[player] always gives it his best as long as he's having fun."
    s "He helps me with busywork without me even asking."
    s "Like cooking, cleaning my room..."
    show sayori 2a zorder 2 at t21
    show yuri zorder 3 at f22
    y 2m "How dependable..."
    show yuri zorder 2 at t22
    mc "Sayori, that's because your room is so messy it's distracting."
    mc "And you almost set your house on fire once."
    show sayori at s21
    s 5 "Is that so... Ehehe..."
    show yuri zorder 3 at f22
    y 1s "You two are really good friends, aren't you?"
    y "I might be a little jealous..."
    show yuri zorder 2 at t22
    show sayori zorder 3 at f21
    s 1 "How come? You and [player] can become good friends too!"
    show sayori zorder 2 at t21
    show yuri zorder 3 at f22
    y 4b "U-Um..."
    show yuri zorder 2 at t22
    mc "S-Sayori--"
    show sayori zorder 3 at f21
    s "Hmm?"
    show sayori zorder 2 at t21
    mc "..."
    "As usual, Sayori seems oblivious to the weird situation she just put me into."
    show sayori zorder 3 at f21
    s 4x "Oh, oh! Yuri even brought you something today, you know~"
    show sayori zorder 2 at t21
    show yuri zorder 3 at f22
    y 3n "W-Wait! Sayori..."
    show yuri zorder 2 at t22
    mc "Eh? Me?"
    show yuri zorder 3 at f22
    y 3o "Um... Not really..."
    show yuri zorder 2 at t22
    show sayori zorder 3 at f21
    s 4r "Don't be shy~"
    show sayori zorder 2 at t21
    show yuri zorder 3 at f22
    y "It's really nothing..."
    show yuri zorder 2 at t22
    mc "What is it?"
    show yuri zorder 3 at f22
    y 4c "N-Never mind!"
    y "Sayori made it sound like a big deal when it's really not..."
    y "Uuuuh, what do I do..."
    show yuri zorder 2 at t22
    show sayori zorder 3 at f21
    s 1g "Eh? I'm sorry, Yuri, I wasn't thinking..."
    show sayori zorder 1 at thide
    hide sayori
    show yuri zorder 2 at t11
    "I guess that means it's up to me to rescue this situation..."
    mc "Hey, don't worry about it."
    mc "First of all, I wasn't expecting anything in the first place."
    mc "So any nice gesture from you is a pleasant surprise."
    mc "It'll make me happy no matter what."
    y 3v "I-Is that so..."
    mc "Yeah. I won't make it a big deal if you don't want it to be."
    y "Alright..."
    y 1a "Well, here."
    "Yuri reaches into her bag and pulls out a book."
    y "I didn't want you to feel left out..."
    y "So I picked out a book that I thought you might enjoy."
    y "It's a short read, so it should keep your attention, even if you don't usually read."
    y "And we could, you know..."
    show yuri at sink
    y 4b "Discuss it...if you wanted..."
    "Th-This is..."
    "How is this girl accidentally being so cute?"
    "She even picked out a book she thinks I'll like, despite me not reading much..."
    mc "Yuri, thank you! I'll definitely read this!"
    "I enthusiastically take the book."
    show yuri 2m zorder 2 at t11
    y "Phew..."
    y 2a "Well, you can read it at your own pace."
    y "I look forward to hearing what you think."
    show yuri zorder 1 at thide
    hide yuri


    "Now that everyone's settled in, I expected Monika to kick off some scheduled activities for the club."
    "But that doesn't seem to be the case."
    "Sayori and Monika are having a cheery conversation in the corner."
    "Yuri's face is already buried in a book."
    "I can't help but notice her intense expression, like she was waiting for this chance."


    $ nextscene = poemwinner[0] + "_exclusive_" + str(eval(poemwinner[0][0] + "_appeal"))
    call expression nextscene


    show monika 1 zorder 2 at t21
    hide sayori
    hide yuri
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
    "Yuri reluctantly complies as well, reaching into her bags."
    "I do the same, myself."
    return

label ch21_end_n:
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
    
    show monika 4b zorder 2 at t11
    with wipeleft_scene
    m "Okay, everyone!"
    m "It's just about time for us to leave."
    m "How did you all feel about sharing poems?"
    show monika 4a
    show sayori 4x zorder 2 at t31
    s "It was a lot of fun!"
    show sayori behind yuri at thide
    show yuri 1i zorder 2 at t31
    hide sayori
    y "Well, I'd say it was worth it."
    show yuri at thide
    hide yuri
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
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
