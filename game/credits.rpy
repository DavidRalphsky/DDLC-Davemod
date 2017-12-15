label postcredits_loop:
    $ persistent.autoload = "postcredits_loop"
    $ config.keymap['game_menu'] = []
    $ config.keymap['hide_windows'] = []
    $ renpy.display.behavior.clear_keymap_cache()
    $ quick_menu = False
    $ config.skipping = False
    $ config.allow_skipping = False
    scene black
    show mask_2
    show mask_3
    "I look into the void..."
    "And the void stares back."
    pause 99999
    $ pause()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
