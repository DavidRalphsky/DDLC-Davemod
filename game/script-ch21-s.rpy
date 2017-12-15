label ch21_main_s:
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
    show yuri zorder 2 at t32
    y "Thanks for keeping your promise, [player]."
    y 1a "I hope this isn't too overwhelming of a commitment for you."
    y 1u "Making you dive headfirst into literature when you're not accustomed to it..."
    show natsuki zorder 2 at i33
    n "Oh, come on! Like he deserves any slack."
    n 4e "You already had to be dragged here by Monika."
    n "I don't know if you plan to just come here and hang out, or what..."
    n "But if you don't take us seriously, then you won't see the end of it."
    show monika 2b onlayer front at l41
    m "Natsuki, you certainly have a big mouth for someone who keeps her manga collection in the clubroom."
    n 4o "M-M-M...!!"
    show monika onlayer front at lhide
    hide monika onlayer front
    "Natsuki finds herself stuck between saying \"Monika\" and \"Manga\"."
    show natsuki at h33
    n 1v "Manga is literature!!"
    show natsuki zorder 1 at thide
    hide natsuki
    "Swiftly defeated, Natsuki plops back into her seat."
    show yuri 2s zorder 2 at t11
    y "I'm sorry, [player]..."
    y "We'll make sure to put your comfort first, okay?"
    show yuri 2g
    "Yuri shoots Natsuki with a disappointed glance."
    y 1a "Um, anyway..."
    y "Now that you're in the club and all..."
    y "...Perhaps you might have interest in picking up a book to read?"
    mc "Well..."
    mc "I can't really say no either way."
    mc "Like you said, I'm in this club now."
    mc "So it only feels right for me to do something like that, if you ask."
    y 4b "W-Wait..."
    y "I didn't mean it like that!"
    y "Uu..."
    y "If you don't really want to, then forget I said anything, I guess..."
    mc "Ah--No, it's not that, Yuri."
    mc "I want to try to be a part of this club."
    mc "So even if I don't read often, I'd be happy to pick up a book if you wanted me to."
    y 3t "A-Are you sure...?"
    y "I just felt like..."
    y 3u "...Well, as Vice President and all..."
    y "...That I should help you get started on something you might like."
    "Yuri reaches into her bag and pulls out a book."
    y 1s "I didn't want you to feel left out..."
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
    show layer master


    "Now that everyone's settled in, I expected Monika to kick off some scheduled activities for the club."
    "But that doesn't seem to be the case."
    "Yuri's face is already buried in a book."
    "I can't help but notice her intense expression, like she was waiting for this chance."
    "Meanwhile, Natsuki is rummaging around in the closet."


    $ nextscene = poemwinner[0] + "_exclusive_" + str(eval(poemwinner[0][0] + "_appeal"))
    call expression nextscene

    return

label ch21_end_s:
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
    "My eyes land on Yuri and Natsuki."
    show yuri 2g zorder 2 at t21
    show natsuki 1g zorder 2 at t22
    "They gingerly exchange sheets of paper, sharing their respective poems."
    show yuri 2i at t21
    "As they read in tandem, I watch each of their expressions change."
    "Natsuki's eyebrows furrow in frustration."
    "Meanwhile, Yuri smiles sadly."
    show natsuki zorder 3 at f22
    n 1q "{i}(What's with this language...?){/i}"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 2f "Eh?"
    y "Um...did you say something?"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 2c "Oh, it's nothing."
    "Natsuki dismissively returns the poem to the desk with one hand."
    n "I guess you could say it's fancy."
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 2i "Ah-- Thanks..."
    y "Yours is...cute..."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 2h "Cute?"
    n 1h "Did you completely miss the symbolism or something?"
    n "It's clearly about the feeling of giving up."
    n "How can that be cute?"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3f "I-I know that!"
    y "I just meant..."
    y 3h "The language, I guess..."
    y "I was trying to say something nice..."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n "Eh?"
    n 4w "You mean you have to try that hard to come up with something nice to say?"
    n "Thanks, but it really didn't come out nice at all!"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 1i "Um..."
    y "Well, I do have a couple suggestions..."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 5x "Hmph."
    n "If I was looking for suggestions, I would have asked someone who actually liked it."
    n "Which people {i}did{/i}, by the way."
    n 5e "[player] liked it."
    n "So based on that, I'll gladly give you some suggestions of my own."
    n "First of all--"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 2l "Excuse me..."
    y "I appreciate the offer, but I've spent a long time establishing my writing style."
    y 2h "I don't expect it to change anytime soon, unless of course I come across something particularly inspiring."
    y "Which I haven't yet."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1o "Nn...!"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 1k "And [player] liked my poem too, you know."
    y "He even told me he was impressed by it."
    stop music fadeout 1.0
    "Natsuki suddenly stands up."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 4y "Oh?"
    n "I didn't realize you were so invested in trying to impress our new member, Yuri."
    play music t7
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 1n "E-Eh?!"
    y "That's not what I...!"
    y 1o "Uu..."
    y "You...You're just..."
    "Yuri stands up as well."
    y 2r "Maybe you're just jealous that [player] appreciates my advice more than he appreciated yours!"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1e "Huh! And how do you know he didn't appreciate {i}my{/i} advice more?"
    n "Are you that full of yourself?"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3h "I...!"
    y "No..."
    y "If I was full of myself..."
    y 1r "...I would deliberately go out of my way to make everything I do overly cutesy!"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1o "Uuuuuu...!"
    n 1f "Well, you know what?!"
    n "I wasn't the one whose boobs magically grew a size bigger as soon as [player] started showing up!!"
    show yuri 3p at h32
    show natsuki zorder 2 at t33
    y "N-Natsuki!!"
    show monika 3l behind yuri, natsuki at l41
    m "Um, Natsuki, that's a little--"
    show monika at h41
    show yuri 3p zorder 3 at f32
    show natsuki 1e zorder 3 at f33
    ny "This doesn't involve you!"
    show monika at lhide
    hide monika
    show yuri zorder 2 at t21
    show natsuki 1g zorder 2 at t22
    "Suddenly, both girls turn towards me, as if they just noticed I was standing there."
    show yuri zorder 3 at f21
    y 2n "[player]...!"
    y "She-- She's just trying to make me look bad...!"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 4w "That's not true!"
    n "She started it!"
    n 4e "If she could get over herself and learn to appreciate that {i}simple{/i} writing is more effective..."
    n "Then this wouldn't have happened in the first place!"
    n "What's the point in making your poems all convoluted for no reason?"
    n "The meaning should jump out at the reader, not force them to have to figure it out."
    n 1f "Help me explain that to her, [player]!"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3o "W-Wait!"
    y "There's a reason we have so many deep and expressive words in our language!"
    y 3w "It's the only way to convey complex feelings and meaning the most effectively."
    y "Avoiding them is not only unnecessarily limiting yourself...it's also a waste!"
    y 1t "You understand that, right, [player]?"
    show yuri zorder 2 at t21
    mc "Um...!"
    show yuri 1t zorder 3 at f21
    show natsuki 1e zorder 3 at f22
    ny "Well??"
    mc "..."
    show yuri zorder 2 at t21
    show natsuki 1g zorder 2 at t22
    "How did I get dragged into this in the first place?!"
    "It's not like I know anything about writing..."
    "But whomever I agree with, they'll probably think more highly of me!"
    menu:
        "So, of course that's going to be...!"
        "Natsuki.":
            call ch21_end_natsuki
        "Yuri.":
            call ch21_end_yuri

    scene bg club_day
    show monika 4b zorder 2 at t11
    with wipeleft_scene
    m "Okay, everyone!"
    m "It's just about time for us to leave."
    m "How did you all feel about sharing poems?"
    show monika 4a
    show yuri 1i zorder 2 at t31
    y "Well, I'd say it was worth it."
    show yuri behind natsuki at thide
    show natsuki 4q zorder 2 at t33
    hide yuri
    n "It was alright. Well, mostly."
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
    "And with that, everyone begins leaving."
    scene bg residential_day
    with wipeleft_scene
    "That was an interesting conflict between Yuri and Natsuki."
    "Their personalities clash normally..."
    "But the argument seemed to come out of nowhere!"
    "I wonder if it's a usual occurance..."
    "I shake my head, trying to dispel those thoughts."
    "It doesn't matter."
    "I have a poem to write."
    "Time to get to work."
    return
    

label ch21_end_natsuki:
    stop music fadeout 1.0
    mc "Um..."
    mc "Yuri!"
    mc "You're really talented."
    show yuri 4a at s21
    y "Eh? W-Well..."
    play music t8
    mc "But Natsuki has a point!"
    mc "I think that..."
    show yuri zorder 2 at t21
    "I wrack my brain in an attempt to back myself up."
    mc "I think that conveying feelings with few words..."
    mc "Can be just as impressive as well!"
    mc "It lets the reader's imagination take over."
    mc "And Natsuki's poem did a really good job at that!"
    show natsuki zorder 3 at f22
    n 5y "...Yeah!!"
    n "It did, didn't it?!"
    n "Ahah!"
    n "Shows how much {i}you{/i} know!"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 4b "T-That's not..."
    show yuri zorder 2 at t21
    mc "Natsuki..."
    mc "I think that's enough."
    show natsuki zorder 3 at f22
    n 1m "Huh?"
    n "Me?"
    n "But she was so mean to me...!"
    "Natsuki's voice whines."
    show natsuki zorder 2 at t22
    mc "Look..."
    mc "What we talked about yesterday was right."
    mc "Writing is a really personal thing."
    mc "And sharing it can definitely be hard."
    mc "It looks like we learned that today."
    mc "Even small criticism can lead to something pretty heated."
    mc "You don't need to feel threatened."
    mc "You're a great writer, Natsuki."
    show natsuki zorder 3 at f22
    n 1h "Ah--"
    "Natsuki's voice gets caught in surprise."
    n 1q "...Thanks for noticing."
    "She finally mutters that, barely audible."
    show natsuki zorder 2 at t22
    mc "Yuri..."
    show yuri zorder 3 at f21
    y 4a "...?"
    "Yuri looks at me dejectedly."
    "With a face like that, I can't help but feel bad for her as well."
    show yuri zorder 2 at t21
    mc "I'm sure that Natsuki didn't mean everything she said."
    mc "So you don't need to feel threatened, either."
    show yuri zorder 3 at f21
    y 2v "Well..."
    y "If you say so..."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1g "Hey...!"
    n "It's not like you need to apologize {i}for{/i} me, [player]."
    n 1w "Sheesh."
    "Natsuki takes a breath."
    n 1q "I..."
    n "The thing about..."
    n "Uu..."
    "Natsuki glances around the room."
    show natsuki zorder 3 at hf22
    n 1x "{i}Would everyone stop staring at me??{/i}"
    "Unsurprisingly, Natsuki has a harder time with it than she boasted."
    show natsuki zorder 3 at f22
    n 1i "Hmph."
    n "Anyway...!"
    n 1q "The thing about your boobs. I didn't mean it, okay?"
    n "That's all."
    "Natsuki looks away, avoiding eye contact with anyone."
    show natsuki zorder 2 at t22
    show yuri 4c zorder 3 at f21
    y "..."
    y "I-I'll go make some tea..."
    show yuri at lhide
    hide yuri
    show natsuki zorder 1 at thide
    show monika 4m zorder 2 at t11
    hide natsuki
    m "Well, now that we're past that..."
    m 4b "Everyone's read each other's poems, right?"
    m "I hope that it was worthwhile for everyone!"
    m 5 "Especially you, [player]!"
    m "And to be honest..."
    m "It's a nice change of pace from the lazing around we got a little too used to."
    m "Ahahaha!"
    mc "Ah, so my joining the club was responsible for ruining the atmosphere..."
    m 1d "No, not at all, not at all!"
    m "There's still time before we go home."
    m 1a "So we'll all relax for a bit."
    m "Of course, besides chatting, we do literature-related things in the clubroom..."
    m "So maybe you can take the chance to pick up a book, or do some writing."
    m 1b "After all, that's what the club is for!"
    with wipeleft
    "In the end, Monika's right."
    "Being in the Literature Club probably means I can't spend all my time doing nothing."
    "But in the end..."
    "...I guess it's been worth it so far."
    return

label ch21_end_yuri:
    stop music fadeout 1.0
    mc "Natsuki."
    mc "You're right that I liked your poem."
    show natsuki zorder 3 at f22
    n 1e "See??"
    show natsuki 1g zorder 2 at t22
    play music t8
    mc "Wait!"
    mc "That's not an excuse for you to be so mean!"
    mc "You shouldn't pick a fight just because someone's opinion is different."
    show natsuki zorder 3 at f22
    n 1m "That's not what happened at all!"
    n "Yuri wouldn't even take my poem seriously!"
    show natsuki zorder 2 at t22
    mc "Mm..."
    mc "I understand."
    mc "Yuri."
    show yuri zorder 3 at f21
    y 2t "Eh?"
    show yuri zorder 2 at t21
    mc "You're a seriously talented writer."
    mc "It's no secret that I was impressed."
    show yuri zorder 3 at f21
    y 2u "W-Well, that's..."
    show yuri zorder 2 at t21
    mc "But here's the thing."
    mc "No matter how simple or refined someone's writing style is..."
    mc "They're still putting feelings into it, and it becomes something really personal."
    mc "That's why Natsuki felt threatened when you said her poem was cute."
    show yuri zorder 3 at f21
    y 2v "I...see..."
    y "I didn't notice that I..."
    show yuri zorder 2 at t21
    y 2w "I-I'm sorry..."
    show yuri at s21
    y "Uuu..."
    show natsuki zorder 2 at t11
    show yuri zorder 1 at thide
    hide yuri
    mc "But Natsuki, you took it way too far!"
    mc "Yuri means well, and if you just told her how you felt..."
    mc "Then this wouldn't have happened in the first place."
    n 1e "Are you kidding?"
    n "That's exactly what I did!"
    n "It was {i}her{/i} that--"
    show natsuki zorder 2 at t22
    show monika 2i zorder 3 at f21
    m "Natsuki, I think that's enough."
    m "You both said some things that you didn't mean."
    m "Yuri apologized. Don't you think you should, too?"
    show monika zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1x "Nnn...!"
    show natsuki zorder 2 at t22
    "Natsuki clenches her fists."
    "In the end, nobody has taken her side."
    "She's trapped, at this point being defiant only because she can't handle the pressure."
    "I end up even feeling bad for her."
    show monika zorder 2 at t32
    show natsuki zorder 2 at t33
    show natsuki zorder 3 at f33
    n 2q "You know what?"
    n "I think I'll take a walk."
    n 2w "It'll spare me from having to look at all your faces right now."
    show natsuki zorder 1 at thide
    hide natsuki
    "Without warning, Natsuki snatches her own poem up from the desk and storms out."
    "On her way out, she crumples up the poem with her hands and throws it in the trash."
    show monika zorder 3 at f32
    m 1r "She really didn't need to do that..."
    show monika zorder 1 at thide
    hide monika
    "I look across the room."
    "Yuri has her chin buried in her hands while she stares down at her desk."
    "I gingerly approach her and sit in an adjacent chair."
    show yuri 4b zorder 2 at t11
    y "Sigh..."
    mc "Everything alright?"
    y "I'm so embarrassed..."
    y "I can't believe I acted like that."
    y "You probably hate me now..."
    mc "No--Yuri!"
    mc "How could anyone not have gotten frustrated after being treated like that?"
    mc "You handled it as well as anyone could."
    mc "I don't think any less of you."
    y 2v "Well..."
    y "...Alright, I believe you."
    y 2s "Thanks, [player]. You're too kind."
    y "I'm thankful to have you a part of this club now."
    mc "Er-- It's nothing."
    y 2v "One more thing..."
    y "Um, that one thing that Natsuki said..."
    y 4c "About...you know..."
    y "I would never do anything...so shameful..."
    y "So..."
    mc "...Eh?"
    mc "What thing did Natsuki say?"
    y 3n "--!"
    y "U-Um!"
    y 3q "Well, never mind that..."
    y "I-I'm going to go make some tea..."
    mc "Ah, good idea."
    mc "Make enough for more than one person, okay?"
    y "Y-Yeah."
    return

# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
