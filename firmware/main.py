#imports
import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.scanners.keypad import KeysScanner
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.extensions.display.ssd1306 import SSD1306Driver

#keys :)
KEYS_PINS = (
    board.D10,
    board.D9,
    board.D8,
    board.D0,
    board.D1,
)
keyboard.matrix = KeysScanner(KEYS_PINS)

#keymap :)
keyboard.keymap = [[KC.F13, KC.F14, KC.F15, KC.F16, KC.F17]]


#encoder
encoder_handler = EncoderHandler()
keyboard.modules = [encoder_handler]
encoder_handler.pins = (
    (board.D6, board.D3, board.D2, False),
)
encoder_handler.map = [((KC.VOLD, KC.VOLU, KC.MUTE),), #left = voldown right = volup press = mute
                       ]

#display
display = Display(
    display=SSD1306Driver(i2c=board.I2C(), device_address=0x3C, width=128, height=32),
        entries=[
            TextEntry(text='Stardance - Jarned V1', x=64, y=16, x_anchor='M', y_anchor='M'),
        ],
        height=32,
        width=128,
        flip=False,       
)
keyboard.extensions.append(display)


#make it run :0
if __name__ == "__main__":
    keyboard.go()