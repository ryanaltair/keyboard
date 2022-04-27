
from PYKB import *


keyboard = Keyboard()

___ = TRANSPARENT
BOOT = BOOTLOADER
L1 = LAYER_TAP(1)

# Semicolon & Ctrl
SCC = MODS_TAP(MODS(RCTRL), ';')

keyboard.keymap = (
    # layer 0
    (
        '`',   1,   2,   3,   4,   5,   6,   7,   8,   9,   0, '-', '=', BACKSPACE,
        TAB,   Q,   W,   E,   R,   T,   Y,   U,   I,   O,   P, '[', ']', '|',
        CAPS,  A,   S,  D,   F,   G,   H,   J,   K,   L, ';', '"',    ENTER,
        LSHIFT, Z,   X,   C,   V,   B,   N,   M, ',', '.', '/',         UP,
        LCTRL,  LALT, LGUI,      SPACE,            L1, LEFT,DOWN,RIGHT
    ),

    # layer 1
    (
        ESC,  F1,  F2,  F3,  F4,  F5,  F6,  F7,  F8,  F9, F10, F11, F12, DEL,
        RGB_MOD, VAL_RGB,RGB_VAL,  E,   R,   T,   Y,   U,   UP,   O,SUSPEND,AUDIO_VOL_DOWN,AUDIO_VOL_UP,AUDIO_MUTE,
        RGB_TOGGLE,HUE_RGB,RGB_HUE,SAT_RGB, F,   G,   H,LEFT,DOWN,RIGHT, ';', '"',    ENTER,
        BT_TOGGLE,BT1,BT2, BT3,BT4,BT5,BT6,BT7, BT8, BT9, BT0,       UP,
        LCTRL,  LALT, LGUI,      SPACE,              ___, LEFT,DOWN,RIGHT
    )             
)

 

keyboard.verbose = False

keyboard.run()
