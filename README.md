# Jarned-V1

- A small hackpad used to automate the simpler things in life.
  
A practical mini keyboard for people who need to do things faster.

CASE:
<img width="1198" height="764" alt="Screenshot 2026-08-03 105643" src="https://github.com/user-attachments/assets/51a370b1-788c-40f7-81b8-3cc58eec5c38" />
 />

PCB:
<img width="733" height="665" alt="image" src="https://github.com/user-attachments/assets/1ddc04f9-6eb8-41f4-bc41-4f225b85bc57" />

Schematic:
<img width="698" height="368" alt="image" src="https://github.com/user-attachments/assets/212be115-3665-4c83-97c8-73df4121f9ec" />

How to use yourself!
Just download the files above, get your PCB and other parts, download the KMK firmware and enjoy!
All the keys are set to F13, F14 ect. so you can make your own shortcuts through Windows!

BOM:
- 1 Seeed XIAO RP2040#
- 5x MX-Style switches
- 1 EC11 Rotary Encoder
- 1 0.91" OLED
- 5x white blank DSA keycaps
- 4x M3x16mm screws
- 4x M3x5mx4mm heatset inserts

Features:
- 5 Keys that are set to F13,14,15 ect.
- A rotary encoder (volume knob) that can be used to increase, decrease and mute audio
- An OLED screen that can be set to anything within the screen size
- Custom PCB and 3D printable case
- KMK firmware on a Seeduino XIAO RP2040

How to run locally:
All that is needed is Curcuit Python 10.2.1 (or the one that corresponds with your chip), the latest KMK firmware and the libaries listed below from the Adafuit CircuitPython bundle and the Adafruit CircuitPython Fonts libraries:
- adafruit_displayio_ssd1306.mpy
- adafruit_display_text

How it works:
- The Jarned V1 features direct pin scanning for simplicity.
- It also has a XIAO monuted on the bottom of the case to leave room for the OLED
- KMK was used with an OLED to keep the code simple and accessibl
- F13-17 mapped keys to be able to add your own shortcuts through Windowsd

Credits:
KMK documentation - massive help in the coding process
The HackClub Stardance community - helped my really simple problems.

