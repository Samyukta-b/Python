# Python code

This is a game of Cows and Bulls developed using Python (Tkinter library) for Words & Numbers.

## Instructions

In this game you will have to guess the four-letter word or four-digit number.
   - You will be given two hints - Cow and Bull.
   - 'Cow': number of correct letters/digits in the wrong position.
   - 'Bull': number of correct letter/digits in the correct position.
   - The guess word should not have repeated letters.

## Author Status

I'm not the solo author for this code. Credits/Collaburators : My team members.

### Enchant library

```bash
pip install pyenchant
pip list # to check if library is present
# then
import enchant
enchant.Dict("en_US") # This initializes a dictionary object for the English (US) dictionary.
```
Enchant is a module in python which is used to check the spelling of a word, to check if a word exists in dictionary or not.