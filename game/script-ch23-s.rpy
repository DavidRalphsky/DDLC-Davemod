image noface1:
    topleft
    xtile 10 ytile 10
    block:
        block:
            choice:
                "images/sayori/noface1.png"
            choice:
                "images/sayori/noface1b.png"
        block:
            choice:
                0.075
            choice:
                0.3
            choice:
                0.4
            choice:
                0.5
            choice:
                0.6
        repeat
image noface2:
    "images/sayori/noface2.png"
    xalign 0.95 yalign 0.47

label ch23_main_s:
    if renpy.random.randint(0,15) == 0 and not seen_eyes_this_chapter:
        $ quick_menu = False
        scene white
        show noface1
        show noface2
        with dissolve_scene_half
        play sound "sfx/gnid.ogg"
        pause 7
        $ quick_menu = True
        scene bg club_day2
        show yuri 2 zorder 2 at i11

    scene bg club_day
    with dissolve_scene_half
    play music t3
    show monika 1g at l31
    m "Aw, man..."
    m "I'm the last one here again!"
    mc "Don't worry, I just walked in too."
    show yuri 1f zorder 3 at f32
    y "Were you practicing piano again?"
    show yuri zorder 2 at t32
    show monika zorder 3 at f31
    m 1l "Yeah..."
    m "Ahaha..."
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 1m "You must have a lot of determination."
    y "Starting this club, and now picking up piano..."
    show yuri 1a zorder 2 at t32
    show monika zorder 3 at f31
    m 1a "Well, maybe not determination..."
    m "But I guess passion."
    show natsuki 1z zorder 3 at f33
    show monika zorder 2 at t31
    n "Aaah, I can't wait for the festival!"
    n "It's gonna be great!"
    show natsuki zorder 2 at t33
    m 1d "Huh?"
    m "Weren't you complaining about it just yesterday, Natsuki?"
    show monika zorder 2 at t31
    show natsuki 2a zorder 3 at f33
    n "Well, yeah."
    n "I'm not talking about {i}our{/i} part of the festival."
    n 4l "But it's a whole day of school where we get to play and eat all kinds of delicious food!"
    show natsuki zorder 3 at f33
    n 4a "Monika! Do they usually have fried squid?"
    show natsuki zorder 2 at t33
    show monika 2a zorder 3 at f31
    m "Squid...?"
    m "That's a pretty specific thing to look forward to..."
    show monika zorder 2 at t31
    show natsuki 2k zorder 3 at f33
    n "Oh, come on."
    n "Are you saying you don't like squid?"
    n "You, of all people?"
    show natsuki zorder 2 at t33
    show monika 1d zorder 3 at f31
    m "What? I didn't say I don't like it."
    m "Besides, what do you mean by 'you of all people'?"
    show monika zorder 2 at t31
    show natsuki 1d zorder 3 at f33
    n "Because!"
    n "It's right in your name!"
    n 4z "Mon-ika!"
    show natsuki zorder 2 at t33
    show monika 5b zorder 3 at f31
    m "What?"
    m "That's not how you say my name at all!"
    m "Also, that joke makes no sense in translation!"
    show monika zorder 2 at t31
    show natsuki zorder 3 at f33
    n 4m "Oh."
    show natsuki zorder 2 at t33
    show monika 4l zorder 3 at f31
    m "Ah...never mind!"
    m "Let's just focus on our own event for now, okay?"
    show monika zorder 2 at t31
    show natsuki 2a zorder 3 at f33
    n "Ehehe."
    n "Fine, fine."
    n "Your reactions aren't as fun as Yuri's anyway."
    show natsuki zorder 2 at t33
    show yuri 2h zorder 3 at f32
    y "Excuse me..."
    hide natsuki
    hide yuri
    show monika zorder 2 at t11
    m "Anyways! Let's pair up, shall we?"
    hide monika
    
    if n_appeal == 0 and y_appeal == 0:
        jump ch23_start_none_s
    elif n_appeal > 1:
        jump ch23_start_natsuki_s
    elif y_appeal > 1:
        jump ch23_start_yuri_s
    elif poemwinner[1] == "natsuki":
        jump ch23_start_natsuki_s
    elif poemwinner[1] == "yuri":
        jump ch23_start_yuri_s
    elif poemwinner[0] == "natsuki":
        jump ch23_start_natsuki_s
    elif poemwinner[0] == "yuri":
        jump ch23_start_yuri_s
    else:
        jump ch23_start_none_s
    return



label ch23_start_natsuki_s:
    play music t6 fadeout 1
    show natsuki 3c zorder 2 at t11
    n "Hey, you."
    mc "Huh?"
    "I look up to see Natsuki next to me."
    n "Are you just gonna sit there and keep staring at nothing?"
    n "There isn't that much time, so..."
    mc "Ah, sorry."
    mc "I didn't mean to make you worry or anything."
    n 1q "I-It's not like I'm worried!"
    n "I was just..."
    "Natsuki glances down at her side."
    "She's holding a volume of manga in her hand."
    mc "That's right..."
    mc "Something just came up for a minute, but we can get started now."
    mc "I won't make you wait any longer."
    n 5n "Jeez..."
    n "Now you're making me feel like a jerk."
    n "If something's bothering you, then you can just tell me to leave you alone, and I will."
    n 5u "I mean..."
    n "Assuming you didn't feel like talking about it or anything..."
    "She practically mumbles that last part."
    mc "Nah, let's get started."

    if not n_exclusivewatched and poemwinner[2] == "natsuki":
        call natsuki_exclusive_ch3
    else:
        jump ch23_start_none_s
    return

label ch23_start_yuri_s:
    "Why does it feel like I'm being watched...?"
    "I glance around the room."
    show yuri 2t zorder 2 at t11
    "Suddenly, I notice Yuri peering at me from over her book."
    show yuri 4b
    "But she looks away just as quickly with a flustered look on her face."
    "I realize that she won't get anywhere like this."
    "I've never really seen Yuri approach anyone or start a conversation on her own accord."
    "So, I have no choice but to approach her myself."
    "By now, it's a little easier for me to do that."
    "I stand up from my desk and sit in one next to her own."
    play music t6 fadeout 1
    y 2v "..."
    y "I...didn't mean to bother you or anything..."
    mc "Relax, you didn't even do anything."
    y "But..."
    y "I could tell that you wanted to be alone with your thoughts..."
    mc "Alone with my thoughts...?"
    mc "How were you even able to tell that I was thinking like that?"
    y 1t "Well..."
    y "It's something that I do a lot..."
    y "So it wasn't hard for me to spot based on your posture and expression."
    y 3o "N-Not that I was staring or anything...!"
    y "I didn't do anything creepy like that...!"
    mc "In any case, I guess you were right."
    mc "I'm sorry if I caused you any concern."
    y 1s "Don't apologize..."
    y "Your troubles are only the concern of those who willingly share in that concern."
    y "Of course, there are certainly those who find the most comfort in keeping to themselves..."
    y "But if you would prefer to share what's on your mind, then I would be glad to listen."
    mc "Ah, it's really not that big of a deal..."
    mc "Anyway, as long as we're here, why don't we do some reading?"
    y 2s "Well..."
    y "As long as you're okay with it."
    mc "Yeah."


    if not y_exclusivewatched and poemwinner[2] == "yuri":
        call yuri_exclusive_ch3
    else:
        jump ch23_start_none_s
    return

label ch23_start_none_s:
    if not renpy.music.get_playing(channel='music') == audio.t3:
        stop music fadeout 1.0
    scene bg club_day
    with wipeleft_scene
    "..."
    if not renpy.music.get_playing(channel='music') == audio.t3:
        play music t3
    show monika 4b zorder 2 at t11
    m "Okay, everyone!"
    "After some time passes, Monika calls out to the clubroom."
    m "Why don't we share our poems now?"
    show monika zorder 1 at thide
    hide monika
    "Before I know it, everything is back to normal."
    "Everyone goes to retrieve their poems, and I do the same."
    "I make eye contact with Monika, and she smiles at me."
    "For some reason, I feel uneasy."
    return


label ch23_end_s:
    stop music fadeout 1.0
    scene bg club_day
    show monika 4b zorder 2 at t32
    with wipeleft_scene
    play music t3
    m "...Okay, you three!"
    m "We're all done sharing poems, right?"
    m "Why don't we start figuring out--"
    show natsuki 3c zorder 3 at f31
    n "Hold on a second!"
    n "Is it just me, or did you say something strange just now?"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 4d "Eh...?"
    show monika zorder 2 at t32
    show yuri 1e zorder 3 at f33
    y "Something did sound a bit unusual..."
    y "That's right."
    y 1f "You deviated from your usual catchphrase when addressing the club."
    show yuri zorder 2 at t33
    show monika 1n zorder 3 at f32
    m "C-Catchphrase?"
    m "I don't have a catchphrase..."
    show monika zorder 2 at t32
    show natsuki 4q zorder 3 at f31
    n "Jeez..."
    n "Why is the mood so weird today?"
    n "Look, even Yuri isn't immune to it."
    show natsuki zorder 2 at t31
    show yuri 4b zorder 3 at f33
    y "Uhh..."
    y "Stagnating air is common foreshadowing that something terrible is about to happen..."
    show yuri zorder 2 at t33
    mc "In {i}your{/i} books, maybe!"
    show natuski zorder 2 at t31
    show monika zorder 3 at f32
    show yuri 1e at t33
    m 1a "Anyway, we need to figure out the rest of the festival preparations, so..."
    m "Let's decide what everyone will be doing this weekend."
    show monika zorder 2 at t32
    show natsuki 4l zorder 3 at f31
    n "I already know what {i}I'm{/i} doing!"
    show natsuki zorder 2 at t31
    show monika 2b zorder 3 at f32
    m "That's right."
    m "Natsuki will be making cupcakes."
    m "But we might need a lot of them, and different flavors..."
    m "Can you handle that all by yourself, Natsuki?"
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 4z "Challenge accepted!"
    show natsuki 4a zorder 2 at t31
    show monika zorder 3 at f32
    m 1a "And as for myself..."
    m "I'll be assembling all the poetry pamphlets."
    m "And as for Yuri..."
    m 1d "..."
    m 3n "Yuri, you can..."
    m "Ah... Um..."
    show monika zorder 2 at t32
    show natsuki 3c zorder 3 at f31
    n "...?"
    show natsuki zorder 2 at t31
    show monika 5 zorder 3 at f32
    m "Guys..."
    m "Can you help me come up with something for Yuri...?"
    show monika zorder 2 at t32
    show yuri 4c zorder 3 at f33
    y "I..."
    y "I'm useless..."
    show yuri zorder 2 at t33
    show monika 1g zorder 3 at f32
    m "N-No!"
    m "That's not it at all!"
    m "You're the most talented person here, you know!"
    show monika zorder 2 at t32
    show natsuki 5g zorder 3 at f31
    n "..."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1g "N-Now Natsuki's pouting, too??"
    show monika zorder 3 at f32
    m "Ah..."
    m "That may be the case..."
    m 1i "But if I can't also be a leader on my own, then I won't grow as a person."
    m 2i "So, Yuri...!"
    m 2a "You have beautiful handwriting, you know?"
    m "So you should make some banners and decorations to help set the atmosphere."
    show monika zorder 2 at t32
    show yuri 4a zorder 3 at f33
    y "Atmosphere...?"
    y "Um, about that..."
    y "I..."
    y 2r "I love atmosphere!"
    show yuri 2l
    "Yuri's expression suddenly changes as she stares at her desk in focus and starts nodding to herself."
    show yuri zorder 2 at t33
    mc "Your mind is already racing, I see..."
    show monika 2b zorder 3 at f32
    m "That's great!"
    m "You'll be a wonderful help, Yuri."
    m 2a "But anyway..."
    m "That just leaves you, [player]."
    show monika zorder 2 at t32
    mc "The one who is truly useless."
    show monika 1k zorder 3 at f32
    m "Ahaha! Don't say that."
    m 1b "In fact..."
    m "Both Natsuki and Yuri have some pretty heavy tasks to handle."
    m "It would probably go a long way to give one of them a hand."
    m 1m "You could always help me out, as well..."
    m 1a "I would be really appreciative of that."
    show monika zorder 2 at t32
    mc "Ah--"
    mc "That's..."
    "Is Monika suggesting I spend the weekend with one of my club members?"
    "How on Earth are they going to respond to a suggestion like that...?"
    show yuri 1u zorder 3 at f33
    y "Ah..."
    y "I...suppose I wouldn't mind a bit of help..."
    show yuri zorder 2 at t33
    show natsuki 3c zorder 3 at f31
    n "Well, even if you don't know how to bake, there's always some dirty work I could give to you."
    n 3q "It's not like Monika's going to give me a choice, and you shouldn't be sitting on your butt anyway..."
    "Natsuki tries to mumble a bunch of excuses like that."
    show natsuki zorder 2 at t31
    show yuri 2k zorder 3 at f33
    y "Um..."
    y "If I recall, Natsuki..."
    y 2f "You mentioned that you would like to handle the baking on your own."
    y "[player] may not like to be around if you only make him out to be a nuisance..."
    y 2i "So therefore..."
    y "He may be more suited to assisting with the decorations."
    show yuri zorder 2 at t33
    show natsuki 4e zorder 3 at f31
    n "Hold on! I never said that!"
    n 4h "How hard could it be to make a few decorations, anyway?"
    n "Sounds more like you're just making excuses for [player] to--"
    show natsuki zorder 2 at t31
    show yuri 3n zorder 3 at f33
    y "W-What are you saying?!"
    y "It will be extremely meticulous work..."
    show yuri zorder 2 at t33
    show natsuki 5w zorder 3 at f31
    n "And baking isn't?"
    n "Just what do you think--"
    show natsuki zorder 2 at t31
    show monika 2g zorder 3 at f32
    m "Guys, guys!"
    m "Let's settle down for a moment..."
    m 2d "In the end, I think it's up to [player] to decide how he'd like to contribute."
    m "Besides..."
    m 5 "He hasn't really gotten the chance to spend any time with me yet, you know?"
    m "So I'm sure he's interested in--"
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 4f "You {i}literally{/i} just said--"
    show natsuki zorder 2 at t31
    show yuri 2h zorder 3 at f33
    y "I-I'm surprised as well!"
    show yuri zorder 2 at t33
    show monika 1l zorder 3 at f32
    m "Sorry, sorry!"
    m "I was just saying, though..."
    show monika zorder 2 at t32
    show natsuki 4x zorder 3 at f31
    n "Jeez..."
    n "Can we just settle this already?"
    show natsuki zorder 2 at t31
    show monika 1e zorder 3 at f32
    m "Yeah..."
    m "[player], you're okay with this, right?"
    m 1a "In the end, it's up to you."
    show monika zorder 2 at t32
    mc "Ah..."
    mc "Of course."
    show natsuki 5g zorder 3 at f31
    n "Hmph."
    show natsuki zorder 2 at t31
    show yuri 1f zorder 3 at f33
    y "Very well..."
    show yuri zorder 2 at t33
    show monika 1a zorder 3 at f32
    m "In that case..."
    show monika zorder 2 at t32
    "Everyone looks straight at me."
    menu:
        "But of course, I'm going to go with--"
        "Natsuki.":
            call ch23_end_natsuki_s
        "Yuri.":
            call ch23_end_yuri_s
        "Monika.":
            call ch23_end_monika_s
    scene bg residential_day
    with wipeleft_scene
    $ ch24_name = ch24_scene.capitalize()
    "I can't believe this!"
    "[ch4_name] is going to be coming to my house on Saturday...?"
    "My anxiety shoots through the roof."
    "Even though I've gotten pretty used to handling her at this point..."
    "There's no telling what might end up happening when we're outside of school."
    "More than that...she told me that she was looking forward to it."
    "Is this the chance I have to make something happen between us?"
    "...Or is it too early for that?"
    "Only time will tell..."
    "But until then, I won't be able to take my mind off it."
    "I seriously can't wait!"
    return
    
    
label ch23_end_monika_s:
    menu:
        "Natsuki.":
            call ch23_end_natsuki_s
        "Yuri.":
            call ch23_end_yuri_s
    return

label ch23_end_natsuki_s:
    $ ch24_scene = "natsuki"
    mc "Well, baking sounds like it could be fun..."
    mc "And you guys made it sound like a lot of work, so it could probably use two people."
    show natsuki 4l zorder 3 at f31
    n "Don't worry!"
    n "Baking is a ton of fun!"
    n "You'll definitely agree!"
    show natsuki zorder 2 at t31
    show monika 1d zorder 3 at f32
    m "Eh?"
    m "Just a minute ago you were saying that--"
    show monika zorder 2 at t32
    show natsuki 1q zorder 3 at f31
    n "Nevermind that!"
    show natsuki zorder 2 at t31
    show monika 2a zorder 3 at f32
    m "Well, anyway..."
    m "You'll be fine by yourself, right, Yuri?"
    show monika zorder 2 at t32
    show yuri 1j zorder 3 at f33
    y "Of course."
    y "I'm used to it, after all..."
    show yuri 1g zorder 2 at t33
    show monika 1e zorder 3 at f32
    m "Er..."
    show monika zorder 2 at t32
    "This is awkward."
    show monika zorder 3 at f32
    m 1n "That's...good..."
    "Even though Yuri is being melodramatic, it's a little hard to not feel bad..."
    show monika 1m zorder 2 at t32
    show natsuki 3a zorder 3 at f31
    n "So, that's everything, right?"
    n "Anything else we need to talk about?"
    show natsuki zorder 2 at t31
    show monika 1a zorder 3 at f32
    m "No, I think that's it..."
    m "Are you guys excited?"
    show monika zorder 2 at t32
    show natsuki 1z zorder 3 at f31
    n "Yes!"
    n "Everything except the performance is gonna be awesome!"
    show natsuki 1a zorder 2 at t31
    mc "I don't think that really counts..."
    show monika zorder 3 at f32
    m "What about you, [player]?"
    show monika zorder 2 at t32
    mc "Me?"
    mc "Ah, I guess you could say I'm interested to see how it'll turn out..."
    show monika 2b zorder 3 at f32
    m "That's good enough for me!"
    m "What about you, Yuri?"
    m 2d "...Yuri?"
    show monika zorder 2 at t32
    show natsuki 3c zorder 3 at f31
    n "She's still sulking."
    show natsuki zorder 2 at t31
    show yuri 4b zorder 3 at f33
    y "Hmph."
    show yuri zorder 2 at t33
    show natsuki 5n zorder 3 at f31
    "Natsuki starts pouting, too."
    n "It's not..."
    n 5m "I mean, it's not that big of a deal or anything..."
    show natsuki zorder 2 at t31
    mc "Well, it might not be just that..."
    show natsuki zorder 3 at f31
    n "What?"
    show natsuki zorder 2 at t31
    mc "I think that Yuri might just be feeling a little underappreciated in general."
    mc "Having to come up with something for her to do, and then nobody offering to help."
    show natsuki zorder 3 at f31
    n 5q "That doesn't mean..."
    n 5r "Well..."
    show natsuki 5u
    "Natsuki glances back and forth between everyone with a worried expression."
    n 1u "Look..."
    "Natsuki goes over and puts her hands down on Yuri's shoulders."
    n 1h "Yuri."
    n "You really are the most talented one here."
    n "And..."
    n "And you're going to help make the event a lot more fun and welcoming."
    n 1q "I mean, the cupcakes will probably help a lot too..."
    n 3h "But you're gonna make the atmosphere special."
    n "That'll be really important for the way that people feel during the performances."
    n "So..."
    n 4w "You need to stop being dumb and give yourself a little more credit!"
    "Natsuki releases her hands and turns around to face the other direction."
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 4a "W-what?"
    y "You didn't...really mean that, did you?"
    show yuri zorder 2 at t33
    show natsuki 5u zorder 3 at f31
    n "Um..."
    n "N-Not really, but..."
    show natsuki zorder 2 at t31
    "Yuri isn't the only one surprised."
    "Monika and I are also taken aback by Natsuki's words."
    "Natsuki, of all people, to be saying such encouraging things."
    "But I begin to understand."
    "Natsuki was trying to motivate everybody."
    "Even if it didn't work perfectly, I can tell that she tried."
    show yuri 2l zorder 3 at f33
    y "I'm sorry...for being dumb."
    y 2i "I'm going to do my best."
    y "And all of us are going to make it a really great event."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 5j "Yeah."
    show natsuki zorder 2 at t31
    show monika 2k zorder 3 at f32
    m "Yeah!"
    m 2b "I hope to see everyone do their best."
    m "But with that..."
    m "There's nothing more for today."
    m "So I guess it's time for us to head out."
    show monika zorder 2 at t32
    show natsuki 3k zorder 3 at f31
    n "Okay, but I'm staying here a bit longer."
    n "I barely got to do any reading today, so..."
    show natsuki zorder 2 at t31
    show monika 2a zorder 3 at f32
    m "Fair enough, there's nothing wrong with that."
    hide natsuki
    hide monika
    hide yuri
    with wipeleft
    "Everyone packs up their things."
    "I start to follow Monika and Yuri out the door as they chat between each other."
    play music t6 fadeout 1
    show natsuki 4g zorder 2 at t11
    n "Um, where are you going?"
    mc "Huh?"
    n 4c "We still need to figure out our plans for this weekend."
    n "You literally would've gotten home and realized that you didn't even have a way to contact me."
    mc "Oh, that's true..."
    mc "I have no idea how that slipped my mind."
    n 2c "Jeez, good thing I stopped you."
    n "I'm giving you my number, okay?"
    n 2q "Don't make it weird."
    "Natsuki gives me her number."
    n 1c "Okay..."
    n "I'm coming over on Saturday."
    n "I'll bring all the ingredients."
    mc "Wait!"
    mc "You're coming to {i}my{/i} house?"
    n 2c "Well, yeah."
    n "What's wrong with that?"
    mc "I mean..."
    mc "I just figured that since I'm the one helping, I would be going to your house..."
    n "Yeah, right."
    n 5x "Like I could have a guy over my house..."
    n "My dad would kill me."
    mc "Really?"
    mc "That's kinda strict, if you ask me."
    n 5r "Yeah..."
    "Natsuki down for a moment. Before I can say anything, she recovers."
    n 2q "Anyway..."
    n 2c "We have each other's numbers now."
    n "That's all I needed from you."
    n "I guess I'll text you when I'm coming over."
    mc "Alright, fine by me."
    n "Yeah."
    n 4a "I'm really gonna show you why I love baking so much."
    n "So you'd better look forward to it."
    mc "Oh?"
    mc "Didn't you say you were just going to give me the dirty work?"
    n 1r "Well--!"
    n "I was...just saying that."
    n 1q "It's not like I could act like...in front of everyone..."
    n "That I was looking forward to this."
    mc "Wait, really?"
    n 5w "Well, kind of!"
    n "Just because...I never got to bake with someone else before."
    n 5h "That's all it is, so..."
    mc "Alright, I get it."
    mc "Sorry for overreacting."
    mc "Anyway, I'll be heading out now."
    mc "See you on Saturday."
    n 5m "...See you then..."
    return

label ch23_end_yuri_s:
    $ ch24_scene = "yuri"
    mc "Well, I'll probably be most useful helping out Yuri..."
    show yuri zorder 3 at f33
    y 2n "M-Me...?"
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 4e "Are you serious?"
    n "Why would you--"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1i "Natsuki."
    m "I can already tell you're about to say something mean."
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 5r "N-No..."
    n "I was just saying--"
    n "Ugh..."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 2a "So, you'll be helping Yuri then, [player]?"
    show monika zorder 2 at t32
    mc "Yeah."
    mc "That's what I'm going to do."
    show yuri zorder 3 at f33
    y 1u "I'm glad."
    y "I have a bad habit of overthinking these sorts of things..."
    y "So I think your assistance will be very useful."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m "That's great to hear."
    m "Natsuki, will you be able to handle the baking yourself?"
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 3w "I mean, yeah."
    n "I already said I would be fine."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1i "Okay, okay..."
    "Everyone can tell that Natsuki is feeling a little sour."
    show monika zorder 2 at t32
    mc "So...is that everything we needed to go over?"
    show monika zorder 3 at f32
    m 1a "Yeah, that should be about it."
    m 2a "Are you guys excited?"
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 1i "Well, 'excited' may not be the right word..."
    y "But I suppose I'm looking forward to it a little bit."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m "Do you feel the same way, [player]?"
    show monika zorder 2 at t32
    mc "Me?"
    mc "Ah, I guess you could say I'm interested to see how it'll turn out..."
    show monika zorder 3 at f32
    m 2b "That's good enough for me!"
    m 2a "What about you, Natsuki?"
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 5s "..."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2h "Natsuki!"
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 1o "What??"
    n 1m "Why is everyone yelling at me?"
    n "I didn't even do anything...!"
    show natsuki 1n zorder 2 at t31
    show yuri zorder 3 at f33
    y 3n "N-no--!"
    y "That's not what I meant at all!"
    y 3o "A-Ah..."
    "Yuri anxiously glances between everyone in the room."
    y 2w "I-I'm sorry for this!"
    y 2v "I don't really know why [player] picked me..."
    y "And also..."
    y 2t "Your cupcakes are the best cupcakes I've ever had!"
    y "They go really well with my tea!"
    y "And nothing that I do for the event will compare to that, so..."
    y 4b "So..."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 3q "I get it, I get it."
    n 3h "I'm kinda surprised, though..."
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y "W-Why?"
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 3q "Um..."
    n "Well, I'm the one acting immature..."
    n "I already know that."
    n 5h "But you're trying to cheer me up all of a sudden..."
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y "I-I know I'm not very good at it..."
    y 2v "I'm sorry if I said something bad!"
    "Natsuki isn't the only one surprised."
    "Monika and I are also taken aback by Yuri's words."
    "When she already has trouble with words, trying to cheer someone up must be far out of her own comfort zone."
    "But I begin to understand."
    "Yuri was trying to motivate everybody."
    "Even if it didn't work perfectly, I can tell that she tried."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 1h "No..."
    n "I kinda appreciated it."
    n 1u "I'm sorry...for making a big deal out of nothing."
    n 1m "But I'm going to say this."
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 2e "...?"
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 4e "You better bet that my cupcakes are going to be the best part of the whole event!"
    show natsuki 4a zorder 2 at t31
    show yuri zorder 3 at f33
    y 2f "Ah..."
    y 1s "...I believe you."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2b "Yeah!"
    m "I hope to see everyone do their best."
    m "But with that..."
    m "There's nothing more for today."
    m "So I guess it's time for us to head out."
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n "Alright, let's get out of here, then."
    hide monika
    hide natsuki
    hide yuri
    with wipeleft
    "Everyone packs up their things."
    "I start to follow Monika and Natsuki out the door as they chat between each other."
    play music t6 fadeout 1
    show yuri 2t zorder 2 at t11
    y "U-Um--!"
    mc "Eh?"
    "I turn around."
    y "Sorry..."
    y 2s "I realized that I don't have any way of contacting you this weekend..."
    mc "Oh, you're right."
    mc "I can't believe that slipped my mind."
    mc "Should I give you my phone number?"
    y 1a "I think...that would be the best way, yes."
    mc "Alright, then..."
    "Yuri and I exchange phone numbers."
    y "Okay."
    y "Then, I'll be stopping by your house on Saturday..."
    mc "What?"
    mc "My house?"
    y 2t "I-Is that a problem...?"
    mc "No, not at all..."
    mc "I just thought that I would be the one going to your house, since I'm the one helping you."
    y "Ah, I suppose that makes sense..."
    y "But, if you don't mind..."
    y 1u "I think I would prefer going to your house."
    mc "Alright."
    mc "In that case, it won't be a problem."
    "I decide not to press Yuri for a reason."
    "It's not like it should matter much either way, so I'll just need to make sure my room is clean."
    mc "I hope I manage to make myself useful in some way..."
    mc "I'm not nearly as creative as you are."
    y 1a "Don't underestimate yourself, [player]."
    y "I think that we'll make a very productive team."
    y 1u "Even if you only chose me because you felt bad or something..."
    mc "Wait...!"
    mc "You don't actually think that, do you?"
    y 4b "..."
    y "I...don't know."
    y "It's difficult to come up with any other reason you may have chosen me..."
    mc "You're forgetting the one reason with the most common sense!"
    mc "I chose to help you because that's what I want to do."
    y 2v "B-But..."
    "Yuri thinks to herself with an extremely tense expression."
    mc "Yuri...you're overthinking this."
    mc "You wanted me to point out when you're overthinking, right?"
    y "Eh...?"
    y 4 "I...didn't realize..."
    mc "I'm telling you, I want to."
    mc "That's all there is to it."
    mc "Do you believe me?"
    y 1t "I..."
    "Yuri thinks really hard again."
    "She looks straight into my eyes for a long while."
    y 3l "...I believe you!"
    "As if it took her tremendous effort, Yuri finally says that and relaxes her expression."
    y 3s "And I'm really looking forward to Saturday."
    mc "Yeah..."
    mc "I am too."
    show yuri zorder 1 at thide
    hide yuri
    "After that exchange, I make my way out the door, and Yuri follows."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
