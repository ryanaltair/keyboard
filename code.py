from PYKB import *


keyboard = Keyboard()

___ = TRANSPARENT
BOOT = BOOTLOADER
L1 = LAYER_TAP(1)
L2 = LAYER_TAP(2)
L3 = LAYER_TAP(3)
L4 = LAYER_TAP(4)
L2F = LAYER_TAP(2, D)
L3B = LAYER_TAP(3, B)
LSFT4 = LAYER_MODS(4, MODS(LSHIFT))
RSFT4 = LAYER_MODS(4, MODS(RSHIFT))

# Semicolon & Ctrl
SCC = MODS_TAP(MODS(RCTRL), ';')

keyboard.keymap = (
    # layer 0
    (
        '`',   1,   2,   3,   4,   5,   6,   7,   8,   9,   0, '-', '=', BACKSPACE,
        TAB,   Q,   W,   E,   R,   T,   Y,   U,   I,   O,   P, '[', ']', '|',
        CAPS,  A,   S,   D,   F,   G,   H,   J,   K,   L, SCC, '"',    ENTER,
        LSHIFT, Z,   X,   C,   V, B,   N,   M, ',', '.', '/',         RSHIFT,
        LCTRL, LALT,LGUI ,          SPACE,            L1, L2,  L3, L4
    ),
    
    # layer 1
    (
        ESC,  F1,  F2,  F3,  F4,  F5,  F6,  F7,  F8,  F9, F10, F11, F12, DEL,
        ___, PGUP,  UP, PGDN, ___, ___, ___, ___, ___, ___,SUSPEND,___,___,___,
        ___,LEFT,DOWN,RIGHT,___, ___, ___, ___, ___, ___, ___, ___,      ___,
        ___, ___, ___, ___, ___,BOOT, ___,MACRO(0), ___, ___, ___,       ___,
        ___, ___, ___,                ___,               ___, ___, ___,  ___
    ),

    # layer 2
    (
        ESC,  F1,  F2,  F3,  F4,  F5,  F6,  F7,  F8,  F9, F10, F11, F12, DEL,
        ___, PGUP,  UP, PGDN, ___, ___, ___,PGUP, ___, ___, ___,AUDIO_VOL_DOWN,AUDIO_VOL_UP,AUDIO_MUTE,
        ___, LEFT,DOWN,RIGHT, ___, ___,LEFT,DOWN, UP,RIGHT, ___, ___,      ___,
        ___, ___, ___, ___, ___, ___,PGDN, ___, ___, ___, ___,           ___,
        ___, ___, ___,                ___,               ___, ___, ___,  ___
    ),

    # layer 3
    (
        BT_TOGGLE,BT1,BT2, BT3,BT4,BT5,BT6,BT7, BT8, BT9, BT0, ___, ___, ___,
        ___, PGUP,  UP, PGDN, ___, ___,___,USB_TOGGLE,___,___,___,___,___, ___,
        ___,LEFT,DOWN,RIGHT, ___, ___, ___, ___, ___, ___, ___, ___,      ___,
        ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,           ___,
        ___, ___, ___,                ___,               ___, ___, ___,  ___
    ),

    # layer 4
    (
        '`', ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,
        ___, PGUP,  UP, PGDN, ___, ___, ___, ___, ___, ___, ___, ___, ___, ___,
        ___, LEFT,DOWN,RIGHT,___, ___, ___, ___, ___, ___, ';', ___,      ___,
        ___, ___, ___, ___, ___,   B, ___, ___, ___, ___, ___,           ___,
        ___, ___, ___,                ___,               ___, ___, ___,  ___
    ),
)


def macro_handler(dev, n, is_down):
    if is_down:
        dev.send_text('You pressed macro #{}\n'.format(n))
    else:
        dev.send_text('You released macro #{}\n'.format(n))

def pairs_handler(dev, n):
    dev.send_text('You just triggered pair keys #{}\n'.format(n))


keyboard.macro_handler = macro_handler
keyboard.pairs_handler = pairs_handler

# Pairs: J & K, U & I
keyboard.pairs = [{35, 36}, {20, 19}]

keyboard.verbose = False

keyboard.run()
