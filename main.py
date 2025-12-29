import tkinter as tk
import random

class RPSGame:
    def __init__(self, root):
        self.root = root
        self.root.title("RPS Battle Arena - Python Game")
        self.root.geometry("500x520")
        self.root.config(bg="#1e293b") # Dark Theme

        # --- Variables ---
        self.user_score = 0
        self.comp_score = 0

        # --- UI Elements ---
        # Title
        tk.Label(root, text="ROCK PAPER SCISSORS", font=("Impact", 24), bg="#1e293b", fg="#facc15").pack(pady=20)

        # Scoreboard
        self.score_label = tk.Label(root, text="Player: 0  |  Computer: 0", font=("Arial", 16, "bold"), bg="#1e293b", fg="white")
        self.score_label.pack(pady=10)

        # Display Result Area
        self.result_label = tk.Label(root, text="Choose your weapon! 👇", font=("Arial", 14), bg="#1e293b", fg="#22d3ee", height=4)
        self.result_label.pack(pady=20)

        # Buttons Frame
        btn_frame = tk.Frame(root, bg="#1e293b")
        btn_frame.pack(pady=20)

        # Game Buttons with Emojis
        btn_rock = tk.Button(btn_frame, text="✊\nRock", font=("Arial", 12, "bold"), bg="#ef4444", fg="white", width=10, height=3,
                             command=lambda: self.play("Rock"))
        btn_rock.grid(row=0, column=0, padx=10)

        btn_paper = tk.Button(btn_frame, text="✋\nPaper", font=("Arial", 12, "bold"), bg="#22c55e", fg="white", width=10, height=3,
                              command=lambda: self.play("Paper"))
        btn_paper.grid(row=0, column=1, padx=10)

        btn_scissors = tk.Button(btn_frame, text="✌️\nScissors", font=("Arial", 12, "bold"), bg="#3b82f6", fg="white", width=10, height=3,
                                 command=lambda: self.play("Scissors"))
        btn_scissors.grid(row=0, column=2, padx=10)

        # Footer
        tk.Label(root, text="Man vs Machine | Built with Python", font=("Arial", 10), bg="#1e293b", fg="#64748b").pack(side=tk.BOTTOM, pady=20)

    # --- Game Logic ---
    def play(self, user_choice):
        options = ["Rock", "Paper", "Scissors"]
        comp_choice = random.choice(options)

        # Determine Winner
        if user_choice == comp_choice:
            result = "It's a Tie! 🤝"
            color = "#facc15" # Yellow
        elif (user_choice == "Rock" and comp_choice == "Scissors") or \
             (user_choice == "Paper" and comp_choice == "Rock") or \
             (user_choice == "Scissors" and comp_choice == "Paper"):
            result = "You Win! 🎉"
            color = "#4ade80" # Green
            self.user_score += 1
        else:
            result = "Computer Wins! 🤖"
            color = "#f87171" # Red
            self.comp_score += 1

        # Update UI
        self.result_label.config(text=f"You chose: {user_choice}\nComputer chose: {comp_choice}\n\n{result}", fg=color)
        self.score_label.config(text=f"Player: {self.user_score}  |  Computer: {self.comp_score}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RPSGame(root)
    root.mainloop()