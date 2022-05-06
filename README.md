# Python-workshop

## Guess the number
The computer draws in the range 1 &ndash; 100. <br />
Ask the question: "Guess the number:" and should be answered from the keyboard.<br />
Check if the entered text is really a number and in the event of an error display the message "It's not a number!", Then go back to pt. 1<br />
If the number entered by the user is less than the random number, display the message "To small!", Then return to pt. 1.<br />
If the number given by the user is greater than the randomly selected number, display the message "To big!", Then go back to pt. 1.<br />
If the number entered by the user is equal to the number drawn, display the message "You win!" And exit the program.<br />

### Example:
```plaintext
Guess the number: Hi
It's not a number!
Guess the number: 50
To small!<br />
Guess the number: 75
To big!
Guess the number: 63
You win!
```
---

## Lottery simulator<br />

The computer draws 6 numbers from the range 1 &ndash; 49. <br />
The player's task is to correctly select the randomly selected numbers. Hitting 3, 4, 5 or 6 correct numbers is rewarded.

Program:<br />
will ask for the typed numbers and check the following conditions:<br />
 - whether the entered string is a valid number,<br />
 - whether the user has duplicated the number<br />
 - whether the number is in the range 1 &ndash; 49,<br />
 - after entering 6 numbers, it will sort them in ascending order and display on the screen,<br />
 - will draw 6 numbers from the range and display them on the screen,<br />
 - will tell the player how many numbers he hit.<br />

## Guess the number 2
The user will think of a number in the range 1 &ndash; 1000, and the computer will guess.<br />
He will do this in a maximum of 10 moves (provided the player is not cheating).<br />

The player's task will be to answer [*"To small"*], [*"To big"*], [*"You win"*].


## Guess the number 3
From *Guess the number 2*: <br />
With the help of the Flask framework, the User gets a form with three buttons: To small, To big, You win.<br />

## Dice
Many types of dice are used in board and paper RPG games, not only the well-known cubic ones.<br />
Therefore, the program is to simulate the projection of dice with different sides.<br />

### Cube code:<br />
xDy+z<br />

where:<br />
y – the type of dice to use (e.g. D6, D10),<br />
x – number of dice rolls; if we throw once, this parameter is negligible,<br />
z – a number to add (or subtract) to the dice roll (optional).<br />

### Example:
```plaintext 
2D10+10: 2 D10 throws, add 10 to the result,
D6: a simple throw of a cubic dice,
2D3: a throw of two three-sided dice,
D12-1: roll the D12 die, subtract 1 from the result.
```
### Program:<br />
- will accept such a code in the form of a string in the parameter,
- will recognize all input data:
  - type of cube,
  - the number of throws,
  - modifier,
  - if the given string is incorrect, it will return an appropriate message,
  - will simulate the throws and return the result.
  - Dice types found in the games: D3, D4, D6, D8, D10, D12, D20, D100.

## 2001

### Game Rules<br />
Each player starts with 0 points.
The player rolls 2 dice (standard six-sided dice).
The number of spots thrown is added to the total number of points.
Starting from the second round:
- if a player rolls a 7, he divides his number of points by that value, discarding the fractional part,
- if he rolls an 11, he multiplies the current number of points by that value.

The first player to score 2001 points wins.<br />
The other player is the computer.<br />
After each turn, display the current number of points.<br />
The player's throw should be performed after the user presses the enter key.<br />
The computer throw occurs automatically after the player's throw.<br />
End the program when the player or the computer reaches more than 2001 points.<br />
