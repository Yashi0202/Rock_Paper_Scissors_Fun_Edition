import tkinter as tk
from tkinter import messagebox, ttk
import random
from playsound import playsound
import threading

# ASCII Art Symbols
rock_symbol = '''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper_symbol = '''   _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors_symbol = '''   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

symbols = [rock_symbol, paper_symbol, scissors_symbol]
choices = ['Rock', 'Paper', 'Scissors']

def play_sound(file):
    threading.Thread(target=playsound, args=(file,), daemon=True).start()

class RPSGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors for Kids")
        self.root.configure(bg='#FFF0F5')

        self.user_score = 0
        self.computer_score = 0
        self.rounds_played = 0
        self.total_rounds = 3

        # Title
        self.title_label = tk.Label(root, text="🎮 Let's Play Rock Paper Scissors!", font=("Comic Sans MS", 24, "bold"), fg="#A020F0", bg="#FFF0F5")
        self.title_label.pack(pady=10)

        # Dropdown to select rounds
        self.dropdown_frame = tk.Frame(root, bg="#FFF0F5")
        self.dropdown_frame.pack()
        tk.Label(self.dropdown_frame, text="Choose Rounds: 🎲", font=("Comic Sans MS", 14), bg="#FFF0F5").pack(side=tk.LEFT)
        self.rounds_var = tk.StringVar()
        self.rounds_dropdown = ttk.Combobox(self.dropdown_frame, textvariable=self.rounds_var, values=["3", "5", "7"], width=5, font=("Comic Sans MS", 12))
        self.rounds_dropdown.set("3")
        self.rounds_dropdown.pack(side=tk.LEFT)

        # Start/Restart Button
        self.start_btn = tk.Button(root, text="🚀 Start Game", font=("Comic Sans MS", 14), bg="#C1E1C1", command=self.start_game)
        self.start_btn.pack(pady=5)

        # Buttons for Rock, Paper, Scissors
        self.buttons_frame = tk.Frame(root, bg="#FFF0F5")
        self.buttons = []
        for i, name in enumerate(choices):
            btn = tk.Button(self.buttons_frame, text=f"{['🪨', '📄', '✂️'][i]} {name}", font=("Comic Sans MS", 16), width=15, bg="#ADD8E6", command=lambda i=i: self.play_round(i))
            btn.pack(pady=5)
            self.buttons.append(btn)
        self.buttons_frame.pack(pady=10)

        # Result and Choices Display
        self.result_label = tk.Label(root, text="", font=("Comic Sans MS", 16), bg="#FFF0F5")
        self.result_label.pack(pady=5)

        self.user_choice_label = tk.Label(root, text="", font=("Comic Sans MS", 12), bg="#FFF0F5")
        self.user_symbol = tk.Label(root, text="", font=("Courier", 10), bg="#FFF0F5")
        self.computer_choice_label = tk.Label(root, text="", font=("Comic Sans MS", 12), bg="#FFF0F5")
        self.computer_symbol = tk.Label(root, text="", font=("Courier", 10), bg="#FFF0F5")

        self.score_label = tk.Label(root, text="", font=("Comic Sans MS", 14, "bold"), bg="#FFF0F5")

    def start_game(self):
        # Reset everything
        self.user_score = 0
        self.computer_score = 0
        self.rounds_played = 0
        self.total_rounds = int(self.rounds_var.get())

        # Clear previous display
        self.result_label.config(text="")
        self.user_choice_label.pack_forget()
        self.user_symbol.pack_forget()
        self.computer_choice_label.pack_forget()
        self.computer_symbol.pack_forget()
        self.score_label.config(text="")

        # Start new game
        self.update_ui("Game Started! Choose Rock, Paper or Scissors!")
        play_sound("click.wav")

    def play_round(self, user_choice):
        if self.rounds_played >= self.total_rounds:
            return  # Do nothing if game already over

        play_sound("click.wav")
        comp_choice = random.randint(0, 2)

        if user_choice == comp_choice:
            result = "🤝 It's a Draw!"
            play_sound("draw.wav")
        elif (user_choice - comp_choice) % 3 == 1:
            result = "🎉 You Win!"
            self.user_score += 1
            play_sound("win.wav")
        else:
            result = "😢 You Lose!"
            self.computer_score += 1
            play_sound("lose.wav")

        self.rounds_played += 1
        self.update_ui(result, user_choice, comp_choice)

        if self.rounds_played >= self.total_rounds:
            final_result = "🏁 Game Over! "
            if self.user_score > self.computer_score:
                final_result += "You Win the Match! 🏆"
            elif self.user_score < self.computer_score:
                final_result += "Computer Wins the Match! 🤖"
            else:
                final_result += "It's a Tie!"
            self.update_ui(final_result)

    def update_ui(self, message, user_choice=None, comp_choice=None):
        self.result_label.config(text=message)

        if user_choice is not None:
            self.user_choice_label.config(text=f"🧒 You chose: {choices[user_choice]}")
            self.user_symbol.config(text=symbols[user_choice])
            self.user_choice_label.pack()
            self.user_symbol.pack()

        if comp_choice is not None:
            self.computer_choice_label.config(text=f"💻 Computer chose: {choices[comp_choice]}")
            self.computer_symbol.config(text=symbols[comp_choice])
            self.computer_choice_label.pack()
            self.computer_symbol.pack()

        self.score_label.config(text=f"Score: You {self.user_score} - {self.computer_score} Computer")
        self.score_label.pack(pady=5)

# Run the App
root = tk.Tk()
app = RPSGame(root)
root.mainloop()

