label ch4_main:
    stop music fadeout 2.0
    scene bg residential_day with dissolve_scene_full

    play music t6

    if ch4_scene == "natsuki":
        "It's already Saturday."
        "I've been getting increasingly anxious about Natsuki's upcoming visit."
        "I keep telling myself there's no reason to be nervous, but it doesn't help much."
        "I wonder if she'll act any different when it's just the two of us?"
        "Meanwhile, she's been texting me a lot."
        "We sent each other one after exchanging numbers to double-check, but it turned into conversation."
        "She's almost a different personality on the phone, using tons of emoji and cute language."
        "She also really likes complaining about things, but I kind of saw that one coming."
        
        call ch4_exclusive_natsuki
    elif ch4_scene == "yuri":
        "It's already Saturday."
        "I've been getting increasingly anxious about Yuri's upcoming visit."
        "I keep telling myself there's no reason to be nervous, but it doesn't help much."
        "Yuri is clearly an introvert and also an intimate person in general."
        "There's no doubt that she'll open up a little bit when it's just the two of us."
        "Meanwhile, we've even been texting occasionally."
        "She was extremely apprehensive at first, but it wasn't long before I was already learning more about her."
        
        call ch4_exclusive_yuri
    else:
        "I'm worried about Sayori."
        "Why did she leave class? She seemed unhappy."
        "That smile didn't fool me, she's upset about something."
        "We're supposed to work on the project this weekend, maybe I can ask her then."
        "Or should I go check up on her?"
        menu:
            "I don't know how to deal with this. What do I do?"
            "Check up on her.":
                call sayori_exclusive4
            "I should give her some space.":
                jump ch5_main
    return

label ch4_end:
    play music t10 fadeout 2.0
    show sayori 1ba zorder 2 at t11
    mc "Sayori--"
    mc "I thought you didn't want to come over today!"
    s 2bl "Ahaha, well..."
    s "I tried staying in my room..."
    s "But my imagination was being really mean to me..."
    s 1by "So I had to come here and see it for myself."
    mc "See what?"
    mc "What are you talking about?"
    s "You know..."
    s "How much fun you were having with everyone else."
    s 1bt "It makes me...really happy..."
    s "That you've made such good friends."
    s "That's all that matters to me."
    "Tears start to fall down Sayori's face."
    s 4bv "That's all that matters to me--!"
    s "Why am I feeling this way, [player]?"
    s "I'm supposed to be happy for you."
    s 4bw "Why does it feel like my heart is splitting in half?"
    s "It hurts so much..."
    s "Everything hurts so much..."
    s "This would be so much better if I could just disappear!"
    mc "Sayori, don't say that!"
    s 1bw "It's true, [player]!"
    s "If I wasn't here, then you wouldn't have to waste your sympathy on me!"
    s "You wouldn't have to put up with me being selfish!"
    s 1bv "Monika was right..."
    s "I should just..."
    mc "Monika...?"
    mc "Monika was right about what?"
    s "..."
    mc "Sayori..."
    mc "What I said before is true."
    mc "I'm not going to let this continue."
    mc "Caring about you like this isn't the burden your mind is making it out to be."
    mc "It's something that makes me happy."
    mc "It's something that I wouldn't trade for anything else."
    mc "So, even if it takes an entire lifetime..."
    mc "I'm going to be by your side until you don't feel any more pain."
    s 1bk "B-But..."
    "Sayori looks away."
    "I put a hand on her shoulder to reassure her."
    s "I'm scared, [player]..."
    s "I'm really scared..."
    mc "What are you scared of, Sayori?"
    s "I'm scared that..."
    s "That I might like you more than you like me..."
    mc "Sayori...?"
    s 1bu "It's true, isn't it?"
    s "I was weak and started to like you too much..."
    s "I did this to myself."
    s "[player]..."
    s 4bw "I like you so much that I want to die!"
    s "That's how I feel!"
    s 2bv "And...and..."
    mc "That's enough, Sayori..."
    mc "I don't want you to hurt anymore."
    "I slide my hand down Sayori's arm and squeeze her hand in my own."
    mc "Do you remember how I said I always know what's best for you?"
    mc "Do you still believe me?"
    "Wordlessly, Sayori nods."
    mc "Even if you don't understand all of your own feelings..."
    mc "I know what you need the most right now."
    mc "And that's what I'm going to give to you."
    show black zorder 4 with dissolve_cg
    menu:
        mc "Sayori..."
        "I love you.":
            $ sayori_confess = True
            hide black with dissolve_cg
            call ch4_end_yes
        "You'll always be my dearest friend.":
            $ sayori_confess = False
            hide black with dissolve_cg
            call ch4_end_no
    return

label ch4_end_yes:
    mc "I love you."
    s 1bv "Eh--?"
    mc "Those are my true feelings."
    mc "So...there's no way you could like me more than I like you."
    mc "I should have realized it sooner."
    mc "But spending time with everyone at the club..."
    mc "Making new friends..."
    mc "And having fun with you every day..."
    mc "It helped me realize that you are truly the most important person to me."
    mc "That's why I'll accept any of your burdens."
    mc "As long as we continue like this every day..."
    mc "With you by my side..."
    mc "Then I know we'll both be happy."
    s "[player]..."
    $ persistent.clear[8] = True
    scene s_cg3 with dissolve_cg
    "Suddenly, Sayori wraps her arms tightly around me."
    s "[player]..."
    s "Is this...really okay?"
    mc "Yeah."
    "I hold Sayori in my arms and pull her closer."
    mc "You'll never have to let go of me again."
    s "I love you, [player]..."
    s "I want to be with you forever."
    mc "Me too."
    s "..."
    "I feel Sayori's grip around me weaken a little bit."
    s "What is this...?"
    mc "Sayori...?"
    s "I'm supposed to be happy right now..."
    s "I always thought this would be the happiest moment for me."
    s "But why...?"
    s "Even now..."
    s "Why won't the rainclouds go away?"
    s "They're not going away at all, [player]..."
    mc "It's okay, Sayori..."
    mc "It might take some time for things to get better again."
    mc "But no matter how long it takes, I'll be there every step of the way."
    mc "That's all that matters right now."
    s "O-Okay..."
    s "I...trust you..."
    scene bg house
    show sayori 1bv zorder 2 at i11
    with dissolve_cg
    "Sayori and I slowly release each other."
    mc "So..."
    mc "I guess that makes the festival tomorrow...our first date, huh?"
    s 1by "Ehehe..."
    s "What are you saying?"
    s "I don't want to think about those things, you know?"
    s "I want everything to be the same as it always has been."
    s "Even if we really are...a couple."
    s 1bk "I don't know if I could handle anything more right now..."
    s "It's really new and scary to me."
    mc "I understand."
    mc "We'll go at whatever pace suits you best."
    s 1bd "Hey, [player]..."
    "Sayori gazes at me once again, smiling sadly."
    s 4bd "Even if I get really, really sad..."
    s "This is the best thing for me...right?"
    mc "Huh?"
    "I don't really understand what Sayori means by that."
    mc "Are you saying that this is making you feel sad, Sayori?"
    s 4bk "I-I don't know..."
    s "I don't understand what I'm feeling."
    s "It felt like a bunch of thorns when you told me you love me..."
    s 4bd "But that's why I want to trust you."
    s "You know what's best for me..."
    mc "...Yeah."
    mc "I do."
    mc "That's my promise."
    show sayori zorder 1 at thide
    hide sayori
    "I say that, but in reality, I've never felt more uncertain when it comes to Sayori."
    "I know that I love her, and she loves me."
    "But I'm having as much trouble understanding Sayori's feelings as she is."
    "Even though I can comfort her..."
    "I keep wondering if I should be doing something more, or something different."
    "I know these thoughts will continue to plague me until things are back to the way they were."
    "Is that what Sayori meant by not wanting anything to change?"
    "I don't know."
    "But I know that I'll give it everything I've got."
    "Sayori is the most important person to me."
    "And I'll do whatever it takes to have a happy future with her."
    return


label ch4_end_no:
    mc "You'll always be my dearest friend."
    mc "What you need most is for things to be like they've always been."
    mc "Monika told me the truth..."
    mc "She told me how much happier you seemed after I joined the club."
    mc "I know you're struggling with some really difficult feelings right now."
    mc "But..."
    mc "Please trust me that I know what's best...and what will make you happy in the end."
    mc "I promise I'll help get things back to the way they were."
    s 1bt "I..."
    s "I...see..."
    "Sayori forces a smile through an incredibly pained expression."
    s "Ahaha..."
    s "Is this what it feels like...to die?"
    s "I should write a poem about this..."
    mc "Sayori--"
    s "It's okay."
    s "This is just my punishment...remember?"
    s "For being so selfish..."
    s "So please..."
    s "Please don't worry about these stupid feelings."
    s "I know you're right."
    s "I knew this whole time that there's no happiness down that path."
    s "That's why I came here..."
    s "Just so I could get the answer I needed to hear."
    s "And the other thing..."
    s "You're also right that I just want it to go back to the way it was."
    s "I realize that now."
    s "You really do know me better than anyone, [player]."
    s 4bv "I'll trust you with anything..."
    s "Anything at all..."
    s "So..."
    show sayori zorder 1 at thide
    hide sayori
    "Sayori's smile finally breaks."
    "All of a sudden, she turns around and drops to her knees."
    s "{i}AAAAAaaaaAAAAAAAAHH!!!!{/i}"
    "Clutching her head with both hands, she screams as loudly as she can."
    "I'm so shocked that I don't know how to react."
    show sayori 4bt zorder 2 at t11
    s "..."
    show sayori at lhide
    hide sayori
    "Sayori looks over her shoulder and flashes me one more weak smile before turning around and running off."
    mc "Sayori!"
    "..."
    "I'm left helplessly standing in the front of my house."
    "Why am I feeling so horrible about this?"
    "There's nothing more that I could have done."
    "The most I can do is support Sayori through her feelings and help her on the path that's right."
    "But I'm having as much trouble understanding Sayori's feelings as she is."
    "Even though I can comfort her..."
    "I keep wondering if I should be doing something more, or something different."
    "I know these thoughts will continue to plague me until things are back to the way they were."
    "I'm going to give it everything I've got."
    "Sayori will always be my dearest friend."
    "And I'll do whatever it takes to put a smile on her face every day."

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
