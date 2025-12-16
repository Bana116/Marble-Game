# University of Toronto
# Faculty of Information
# Bachelor of Information Program
# INF 452H - Design Studio V: Coding
#
# Student Name: <Asmaa Bana>
# Student Number: <1012819611>
# Supervisor: Dr. Maher Elshakankiri
#
# Tutorial 11, Problem 1
# Purpose: Marbles Game - Implementation Tutorial 11
# Date Created: <2025/11/19>
# Date Modified: <d2025/11/19>

import tkinter as tk 
from tkinter import messagebox 

class MarbleGame: 
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Marble Game")
        
        # Game State [player1_row, player2_row]
        self.board = [[4] * 6, [4] * 6]
        self.player = 1 # 1 or 2
        
        # MAIN LAYOUT
        main_frame = tk.Frame(self.window)
        main_frame.pack(padx=10, pady=10)
        
        # Board (left side)
        board_container = tk.Frame(main_frame)
        board_container.grid(row=0, column=0, padx=10)
        
        # Scoreboard (right side)
        self.score_container = tk.Frame(
            main_frame, bd=2, relief="groove", padx=15, pady=15
        )
        self.score_container.grid(row=0, column=1, padx=10)
        
        # Info label ---
        self.info_label =tk.Label(
            board_container, text="Player 1's Turn", font=("Arial", 16)
        )
        self.info_label.pack(pady=10)
        
        # --- Game board ---
        self.board_frame = tk.Frame(board_container)
        self.board_frame.pack()
        
        # Player 2 (top row)
        self.pits_p2 = []
        for i in range(6):
            btn = tk.Button(
                self.board_frame, 
                text=str(self.board[1][i]),
                width=6, 
                height=2, 
                command=lambda i=i: self.processPitClick(2, i)
            )
            self.pits_p2.append(btn)
        for col, btn in enumerate(reversed(self.pits_p2)):
            btn.grid(row=0, column=col)
            
        # Player 1 (button row)
        self.pits_p1 = []
        for i in range(6):
            btn = tk.Button(
                self.board_frame, 
                text=str(self.board[0][i]),
                width=6, 
                height=2,
                command=lambda i=i: self.processPitClick(1, i)
            )
            self.pits_p1.append(btn)
            btn.grid(row=1, column=i)
            
        # Rest Button
        self.reset_button = tk.Button(
            board_container, text="RESET GAME", font=("Arial", 12),
            command=self.reset_game, bg="lightgray"
        )
        self.reset_button.pack(pady=15)
        
        # --- SCOREBOARD PANEL ---
        tk.Label(
            self.score_container, text="Scoreboard", font=("Arial", 16, "bold")
        ).pack(pady=5)
        
        self.p1_label = tk.Label(
            self.score_container, text="Player 1: 24", font=("Arial", 14)
        )
        self.p1_label.pack(pady=5)
        
        self.p2_label = tk.Label(
            self.score_container, text="Player 2: 24", font=("Arial", 14)
        )
        self.p2_label.pack(pady=5)
        
        self.turn_label = tk.Label(
            self.score_container, text="Current Turn:\nPlayer 1",
            font=("Arial", 14, "bold")
        )
        self.turn_label.pack(pady=15)
        
        self.update_display()
        self.window.mainloop()
    
    # === Helper functions ===   
    def count_seeds(self):
        return sum(self.board[0]), sum(self.board[1])
    
    def game_over(self):
        return sum(self.board[0]) == 0 or sum(self.board[1]) == 0
    
    # === when a pit is clicked ===
    def processPitClick(self, player, pitIndex):
        # Enforced turns
        if player != self.player:
            messagebox.showinfo("Not your turn", f"It's Player {self.player}'s turn!")
            return 
    
        row = 0 if player == 1 else 1
        
        # Empty pit?
        if self.board[row][pitIndex] == 0:
            messagebox.showinfo("Empty pit", "That pit is empty! Pick another one.")
            return

        # Sow marbles
        seeds = self.board [row][pitIndex]
        self.board[row][pitIndex] = 0 
        
        r, c = row, pitIndex
        while seeds > 0:
            c += 1
            if c > 5:
                c = 0 
                r = 1 - r # switch rows
            self.board[r][c] += 1
            seeds -= 1
        
        # Update board first   
        self.update_display()
        
        # Check game over
        if self.game_over():
            self.end_game()
            return 
        
        # Switch turns
        self.player = 2 if self.player == 1 else 1
        self.info_label.config(text=f"Player {self.player}'s Turn")
        self.turn_label.config(text=f"Current Turn:\nPlayer {self.player}")
        
    
    def update_display(self):
        # Update the numbers of all pits
        for i in range(6): 
            self.pits_p1[i].config(text=str(self.board[0][i]))
            self.pits_p2[i].config(text=str(self.board[1][i]))
            
        # Update scoreboard labels
        p1, p2 = self.count_seeds()
        self.p1_label.config(text=f"Player 1: {p1}")
        self.p2_label.config(text=f"Player 2: {p2}")
        
        # Enable/Disable rows based on whose turn it is
        if self.player ==1:
            # Player 1's turn
            for btn in self.pits_p1:
                btn.config(state="normal")
            for btn in self.pits_p2:
                btn.config(state="disabled")      
        else:
            for btn in self.pits_p1:
                btn.config(state="disabled")
            for btn in self.pits_p2:
                btn.config(state="normal")
 
    # ==== Reset Game Feature ====
    def reset_game(self):
        self.board = [[4] * 6, [4] * 6]
        self.player = 1 
        self.info_label.config(text="Player 1's Turn")
        self.turn_label.config(text="Current Turn:\nPlayer 1")
        self.update_display()
        
    # ===== End Game ====
    def end_game(self):
        p1, p2 = self.count_seeds()
        
        if p1 > p2:
            winner = "Player 1"
        elif p2 > p1: 
            winner = "Player 2"
        else: 
            winner = "Tie!"
    
        messagebox.showinfo(
            "Game Over", 
            f"Final Scores:\nP1: {p1}\nP2: {p2}\nWinner: {winner}"
        )
        self.window.destroy()
        
# Start the game 
MarbleGame()
