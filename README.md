# guessing-game
# The game engine first selects a code (string) of a certain length at random (and does not disclose this to the
player).
The player is allowed certain number of guesses to strategically guess the code.
After each guess, the game engine informs the player of the following:
1. Number of characters that are correct, but in the wrong place and
2. Number of characters that are correct and in the correct place.
Example : the game could start off with the computer generating the code : KMAFYM
The game engine starts by setting this code and informing the player that the code has 6 characters.
If the user guesses ABCDEF, then the engine informs the player that the he got 2 characters that are
present in the string but not in the right place. Then the user has to try again and so on ...
