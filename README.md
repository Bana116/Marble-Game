# Marble-Game
The board game contains two rows of pits: the bottom row belongs to Play 1, and the top row belongs to Player 2.

# Overview of the Game

The board game contains two rows of pits: the bottom row belongs to Play 1, and the top row belongs to Player 2. Each pit begins with four marbles. Players take turns selecting pits from their own to redistribute the marbles counter-clockwise around the board. The game continues until one player’s row becomes empty. When this happens, the remaining marbles are counted to determine the winner. 

# Game Rules 

# Starting conditions 

The board contains 2 x 6 pits, each starting with 4 marbles
Player 1 controls the button row 
Player 2 controls the top row 
Player 1 always goes first.

# Turns 

A player may only click pits on their own row 
Clicking an empty pit is not allowed and results in a warning message. 
When a player selects a pit: 
All marbles from that pit are collected 
The marbles are distributed one-by-one into subsequent pits 
Distribution wraps across rows when reaching the end of a row 

# Turn Switching 
After sowing marbles, the turn switches to the other player automatically. 
Only the active players row remains clickable 
The UI updates the current turn label and enables/disables buttons accordingly

# End Game

The game ends when either row becomes empty. The remaining marbles in both rows are counted and displayed in a game-over message. The player with the higher total wins. Tie is possible. 

After the final score is shown, the window closes automatically.

# How to Run the Program 

Make sure you have Python 3 installed on your computer. 
Download the file named: Tutorial11_1_Bana_Asmaa.py
Open a terminal or command prompt.
Navigate to the folder where the file is saved. 
For example: macOS cd/Users/YourName/Desktop
Run the program 
Mac/Linux: python3 Tutorial11_1_Bana_Asmaa.py 
The Marble Game window will open automatically. 


# GUI layout and buttons 

# Tkinter GUI library

Buttons 
Labels 
Frames
Message boxes for alerts and end-game notifications

# Summary 

The program provides a complete, interactive version of two player marble-sowing game with clear turn-based control, rules enforcement and a clean graphical interface. It is robust against invalid moves and offers full gameplay until a final winner is declared.
