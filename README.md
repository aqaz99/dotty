# Farkle Game - README

## Note - Currently ther eis no AI opponent to play against

## Overview

This is a Python-based adaptation of the popular dice game **Farkle**, designed for both gameplay and potential use in machine learning training. The game involves rolling dice, holding specific dice to score points, and deciding whether to bank your points or risk rolling again to maximize your score. The objective is to reach a target score of **1500 points**.

## Features

- **Dice Rolling Mechanics**: Simulates rolling six dice with random values between 1 and 6.
- **Scoring System**: Includes scoring rules for straights, triples, quadruples, quintuples, sextuples, and single dice (1s and 5s).
- **Player Interaction**: Allows players to hold specific dice and decide whether to bank points or keep rolling.
- **Win Condition**: Players win when they reach or exceed the required score of 1500.

## How to Play

1. Run the game script.
2. The game will start automatically, and you can roll the dice each round.
3. After rolling:
   - Decide which dice to hold by entering their numbers (e.g., `1 3 5` or `135`).
   - The held dice will be scored based on Farkle rules.
4. After scoring:
   - Choose whether to "Keep Rolling" (`K`) with the remaining dice or "Bank" (`B`) your points and move to the next round.
5. The game continues until you reach or exceed the target score of 1500.

## Scoring Rules

- **Straight (1, 2, 3, 4, 5, 6)**: 1500 points
- **Straight (2, 3, 4, 5, 6)**: 750 points
- **Straight (1, 2, 3, 4, 5)**: 500 points
- **Triples (e.g., three of a kind)**:
  - `1`: 1000 points (doubles for each additional die beyond three)
  - Other numbers: Value × 100 (doubles for each additional die beyond three)
- **Single Dice**:
  - `1`: 100 points each
  - `5`: 50 points each

## Requirements

- Python >= 3.6

## How to Run

1. Clone or download this repository.
2. Open a terminal/command prompt in the directory containing the script.
3. Run the script using Python:
   ```bash
   python farkle_game.py
   ```
4. Follow the on-screen instructions to play.

## Example Gameplay

```
--------------------
Game started
--------------------
Die 1: 3
Die 2: 5
Die 3: 1
Die 4: 6
Die 5: 2
Die 6: 4
Hold Dice: 3
--------------------
Score Score: (100) 0/1500
--------------------
Keep rolling or bank scored points and move to next round? X dice left
K/B: K
```

## Notes

- This implementation is intended for single-player mode.
- Input validation ensures only valid dice numbers are held.
- The game resets held dice after banking points.

## Future Enhancements (Optional)

- Add multiplayer functionality.
- Implement AI opponents for training purposes.
- Improve input handling and error messages.

Enjoy playing Farkle! 🎲

---
