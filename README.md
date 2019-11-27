# ecco distortion effect
 A reverse engineered implementation of the Ecco The Dolphin waving-effect 
 seen in the background of text screens

 This was written by debugging the game in an emulator until the code for 
 the effect was located, then reimplementing it in python, and iteratively 
 simplifying it. 

 The point of this was to prototype a version of the effect for the 
 [Death Generator](https://github.com/foone/SierraDeathGenerator/).

 Info on my reverse engineering efforts are in 
 [this twitter thread](https://twitter.com/Foone/status/1156799835296555010)

## The effect:
 The input is a 384x224 image, and it's drawn line-by-line but with a 
 different starting horizontal offset. The offsets are calculated using a
 double-indirect memory lookup and some math, but for this code I've 
 simplified all that by preprocessing all the calculations into a single 
 lookup. The input frame number is added to the line number, truncated to
 256 (the size of the lookup table), and those resulting values are used
 as horizontal offsets.
 
 Because they're added together, when animated (at 60hz) this causes the 
 effect to scroll up the screen. 

 Because of the truncation to 256, this means the whole effect is 256 
 frames long, and loops. 

## Files

* background.png: The undistorted background image used by Ecco the Dolphin
* generate.py: Calculates the shifting of each line, based on an input frame number
* ecco.py: A simple pygame script to display the resulting shifts.

## License:

All the code is GPL3, the background.png file is taken from the 
Sega Genesis/Megadrive game "Ecco the Dolphin" by Novotrade International, 1992.