label ch23_main_n:
    scene bg club_day
    with dissolve_scene_half
    play music t3
    show monika 1g at l21
    m "Aw, man..."
    m "I'm the last one here again!"
    mc "Don't worry, I just walked in too."
    show yuri 1f zorder 3 at f22
    y "Were you practicing piano again?"
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 1l "Yeah..."
    m "Ahaha..."
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y 1m "You must have a lot of determination."
    y "Starting this club, and now picking up piano..."
    show yuri 1a zorder 2 at t22
    show monika zorder 3 at f21
    m 1a "Well, maybe not determination..."
    m "But I guess passion."
    "I look around the room..."
    mc "Hold on..."
    mc "Where is Sayori?"
    mc "Oh, there you are."
    hide monika
    hide yuri
    with wipeleft
    "Sayori is sitting at a desk in the corner of the room, looking down at nothing."
    "I walk over to her."
    mc "Hey, Sayori."
    show sayori 1k zorder 2 at t11
    "I wave my hand in front of her face."
    s 1n "Huh--?"
    mc "You're spacing out again."
    s "A-Ah..."
    s 4l "Ehehe, sorry..."
    s "Don't mind me."
    s 4y "You can go talk to everyone else."
    mc "Huh..."
    mc "Is everything alright?"
    s 1h "O-Of course!"
    s "Why wouldn't it be?"
    mc "It just feels like you're a little off..."
    mc "Sorry for assuming things."
    s "Jeez, you worry too much about me."
    s 4r "I'm fine, see?"
    show sayori at h11
    "Sayori shows me a big smile. It seems forced."
    s 1a "Don't let me distract you from having fun with everyone."
    mc "Well...alright."
    mc "If you say so."
    show sayori zorder 1 at thide
    hide sayori
    "I worriedly glance at Sayori before turning back toward everyone else."
    "But the conversation has already dispersed, with everyone back at their usual activities."
    "Maybe I should ask Monika if she's noticed anything about Sayori recently..."
    "Since they've been preparing for the festival, they must be spending a lot of time together."
    "I timidly approach Monika, who is shuffling through some papers at her desk."
    show monika 2b zorder 2 at t11
    m "[player]! What's up?"
    mc "Hey, this might sound a little strange, but..."
    mc "Have you noticed anything up with Sayori recently?"
    m 1d "Anything up with her...?"
    m "In what way do you mean?"
    mc "Maybe I'm reading into it a little too much, but she seems a bit downcast today..."
    m "Oh? You think so?"
    m "I can't say I've noticed anything about her..."
    "Monika peers across the room at Sayori, who is idly dragging a rubber eraser up and down her desk."
    m "Maybe there is something on her mind..."
    m 2a "But I'm surprised I'm not the one asking you, [player]."
    m "You certainly know her a lot better than I do."
    mc "Yeah, but she's never really like this..."
    mc "She's always talked to me about things that bothered her."
    mc "But this time, when I asked her, she was really dismissive."
    mc "...Sorry, I know it's not your problem!"
    mc "I just wanted to ask if you knew anything, so I'll drop it now..."
    m 1g "No, no..."
    m "It's important to me, too."
    m 1e "I mean, I'm also friends with her..."
    m "And I also care about the well-being of my club members, you know?"
    m 1i "Maybe I'll try talking to her myself..."
    mc "Really? Are you sure about that...?"
    mc "She seemed like she wanted to be left alone..."
    m "Are you sure?"
    m "Maybe she just has a hard time bringing it up with the person of interest..."
    mc "Person of interest...?"
    mc "What do you mean by that?"
    m 2e "I'm saying that maybe the thing on her mind is you, [player]."
    mc "Me...?"
    mc "How on Earth would you come to that conclusion?"
    m 1j "Well..."
    m "I probably shouldn't say too much, but..."
    m 1a "Sayori talks about you more than anything else, you know?"
    m "She's been so much happier ever since you've joined the club."
    m "Maybe she's just sorting out her feelings, y'know?"
    mc "What?"
    mc "No way..."
    mc "Sayori...was always the cheery one."
    mc "She's always been full of sunshine."
    mc "It's not any different now than it always has been."
    m 5 "Ehehe."
    m "You're so funny, [player]."
    m "Have you thought that maybe you've always seen her as so cheerful..."
    m "...because that's just how she is when she's around you?"
    "I don't know how to respond to that."
    m 1n "Ah...I said too much."
    m "I'm sorry...what do I know, anyway?"
    m 1a "I didn't mean to jump to conclusions, so you should just forget about what I said."
    m "I'll try to talk to her, so try not to think about it for now."
    mc "Alright..."
    "Monika smiles meaningfully."
    "I know she said to forget about it..."
    "But I already know that I won't be able to get her words out of my head."
    show monika zorder 1 at thide
    hide monika
    "Monika stands up from her desk and walks across the room to where Sayori is sitting."
    "I watch her kneel down next to Sayori and gently talk to her."
    "But she's keeping her voice so quiet that I can't hear her from here."
    "I sigh and sit myself down."
    "I know Sayori told me not to worry about her, and to have fun with everyone else..."
    "But that's impossible to do when she's behaving like this."
    "Exactly how much do I care about her, that I'm letting this weigh me down so much?"
    "Now it feels like I'm the one behaving out of the ordinary..."
    "But there's nothing I can do besides wait for Monika."

    if y_appeal > 1:
        jump ch23_start_yuri_n
    elif poemwinner[0] == "yuri":
        jump ch23_start_yuri_n
    else:
        jump ch23_start_none_n

label ch23_start_yuri_n:
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
    mc "I was just feeling a bit uneasy about Sayori."
    y 2t "Sayori...?"
    mc "Yeah...she seems a little off today, but when I asked her about it, she didn't want to admit it to me."
    mc "So I can't help but wonder if something happened to her."
    y 3u "Oh?"
    y "That's quite romantic..."
    mc "Eh...?"
    y 4c "S-Sorry!"
    y "I didn't mean to say something stupid...!"
    mc "It's not that, I just didn't want you to misunderstand."
    mc "Sayori and I have just been friends for a long time, that's all."
    y 2l "Ah...I see..."
    y 2f "Then perhaps it is unusual for her to be dismissive to you about her feelings..."
    mc "Or maybe I'm just reading into it a little too much..."
    y 1u "[player]..."
    y "The world is full of meaning, often hidden deep beneath plain sight."
    y 1s "And there are many untold mysteries behind every person, no matter how well you may know them."
    mc "Ah..."
    mc "So you think that there might be something behind it after all?"
    y 1l "Mm..."
    y "I think that Sayori is a very complex person."
    y 1h "Her mannerisms on the outside don't always match what may be going on inside her head..."
    y "And she may not always know what she wants."
    y "I noticed her strange behavior today, too..."
    y "And I also feel some concern for her."
    y 1f "But in your case, it looked like she was fully occupying your thoughts, wasn't she?"
    mc "Well..."
    mc "I guess that was the case."
    y 3u "Sayori..."
    y "She really...means a lot to you, doesn't she?"
    mc "Ah--I...I guess..."
    mc "But you don't need to put it that way!"
    mc "We're just good friends, that's all..."
    y 2t "..."
    "Yuri suddenly looks deeply into my eyes."
    "Her expression is gentle and curious, as if she was searching for something."
    "Embarrassed, I avert my gaze."
    y 2m "Sometimes..."
    y "A person's mysteries are untold even to themselves."
    y 2a "And you, as someone honest and caring..."
    y "May uncover feelings you weren't aware were in you."
    y 4b "T-That is..."
    y "I think that..."
    y "She would be a very fortunate person..."
    y "To have you...feel that way about her."
    mc "Yuri..."
    mc "You're giving me too much credit."
    mc "I'm a pretty simple guy."
    mc "So I think I'm pretty good at understanding my own feelings."
    mc "I'm not nearly as sophisticated as you."
    y 2t "A-Ah..."
    y "That's not...a compliment, is it?"
    mc "It is what it is."
    mc "Anyway, as long as we're here, why don't we do some reading?"
    y 2s "Well..."
    y "As long as you're okay with it."
    mc "Yeah."
    mc "I should be taking my mind off this whole thing anyway."


    if not y_exclusivewatched and poemwinner[0] == "yuri":
        call yuri_exclusive_2_ch3
    else:
        jump ch23_start_none_n
    return

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
    "I wonder what she was talking about with Sayori..."
    return

label ch23_start_none_n:
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
    "I wonder what she was talking about with Sayori..."
    return

label ch23_end_n:
    stop music fadeout 1.0
    scene bg club_day
    show monika 4b zorder 2 at t32
    with wipeleft_scene
    play music t3
    m "...Okay, everybody!"
    m "We're all done sharing poems, right?"
    m "Why don't we start figuring out the rest of the festival preparations?"
    m "Let's decide what everyone will be doing this weekend."
    show monika zorder 3 at f32
    m 1a "As for myself..."
    m "Sayori and I are going to be printing and assembling all the poetry pamphlets."
    m "And as for Yuri..."
    m 1d "..."
    m 3n "Yuri, you can..."
    m "Ah... Um..."
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
    m 2i "Wait, I've got it!"
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
    m "Yuri has a pretty heavy task to handle."
    m "It would probably go a long way to give her a hand."
    m 1m "Or you could help Sayori, and I'd help Yuri."
    m 1a "You two do seem to be especially...cooperative."
    show monika zorder 2 at t32
    mc "Ah--"
    mc "That's..."
    "Is Monika suggesting I spend the weekend with one of the club members?"
    show yuri 1u zorder 3 at f33
    y "Ah..."
    y "I...suppose I wouldn't mind a bit of help..."
    show yuri zorder 2 at t33
    "They both look straight at me."
    menu:
        "But of course, I'm going to go with--"
        "Yuri.":
            call ch23_end_yuri_n
        "Sayori.":
            call ch23_end_sayori_n
    scene bg residential_day
    with wipeleft_scene
    $ ch24_name = ch24_scene.capitalize()
    if ch24_name == "yuri":
        "I can't believe this!"
        "[ch24_name] is going to be coming to my house on Saturday...?"
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

label ch23_end_sayori_n:
    $ ch24_scene = "sayori"
    mc "I mean..."
    mc "If it's going to be anyone, then I prefer helping Sayori."
    mc "I mean, we're already neighbors, and--"
    show yuri 2f zorder 3 at f33
    y "N-Naturally..."
    show monika 1e zorder 3 at f32
    m "Very well."
    m "I'll help Yuri."
    m 3a "And with that, we can adjourn this meeting!"
    return

label ch23_end_yuri_n:
    $ ch24_scene = "yuri"
    mc "Well, I'll probably be most useful helping out Yuri..."
    show yuri zorder 3 at f33
    y 2n "M-Me...?"
    show yuri zorder 2 at t33
    y "W-well..."
    y 1u "I'm glad!"
    y "I have a bad habit of overthinking these sorts of things..."
    y "So I think your assistance will be very useful."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m "That's great to hear."
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
    hide monika
    hide yuri
    with wipeleft
    "Everyone packs up their things."
    "I start to follow Monika out the door..."
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
