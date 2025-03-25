import random
import tkinter as tk

# Game choices with ASCII signs
choices = {
    "Rock": """
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """,
    "Paper": """
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    """,
    "Scissors": """
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """
}

# Function to play the game
def play_game(user_choice):
    computer_choice = random.choice(list(choices.keys()))
    result = ""
    explanation = ""
    
    if user_choice == computer_choice:
        result = "It's a draw!"
        explanation = "Both chose the same. Try again!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You win!"
        explanation = f"{user_choice} beats {computer_choice}!"
    else:
        result = "You lose!"
        explanation = f"{computer_choice} beats {user_choice}!"
    
    user_label.config(text=f"You:")
    user_sign.config(text=choices[user_choice])
    computer_label.config(text=f"Computer:")
    computer_sign.config(text=choices[computer_choice])
    result_label.config(text=f"{result}\n{explanation}", fg="yellow" if result == "It's a draw!" else ("green" if result == "You win!" else "red"))

# Create GUI window
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("500x600")
root.configure(bg="#222831")

# Title Label
title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 20, "bold"), fg="#00ADB5", bg="#222831")
title_label.pack(pady=20)

# Display selection buttons
button_frame = tk.Frame(root, bg="#222831")
button_frame.pack(pady=10)

for choice in choices.keys():
    tk.Button(button_frame, text=choice, font=("Arial", 14, "bold"), command=lambda c=choice: play_game(c), bg="#393E46", fg="#EEEEEE", width=10, height=2, bd=5, relief="ridge").pack(side="left", padx=10)

# Labels for displaying results
user_label = tk.Label(root, text="You:", font=("Arial", 14, "bold"), fg="#EEEEEE", bg="#222831")
user_label.pack()
user_sign = tk.Label(root, text="", font=("Courier", 12, "bold"), fg="#00ADB5", bg="#222831")
user_sign.pack()

computer_label = tk.Label(root, text="Computer:", font=("Arial", 14, "bold"), fg="#EEEEEE", bg="#222831")
computer_label.pack()
computer_sign = tk.Label(root, text="", font=("Courier", 12, "bold"), fg="#00ADB5", bg="#222831")
computer_sign.pack()

result_label = tk.Label(root, text="", font=("Arial", 16, "bold"), fg="#00ADB5", bg="#222831")
result_label.pack(pady=20)

# Run the GUI
root.mainloop()
