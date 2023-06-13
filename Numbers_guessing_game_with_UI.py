import random
import tkinter as tk
random_number = random.randint(1, 10)
tries_left = 3


# This function checks if the selected number is the same as the randomly generated number, and counts the tries left:
def number_checker(num_input):
    global tries_left
    clear_text_field()
    high_or_low = ""
    if num_input == random_number:
        text_widget.insert(tk.END, f"You guessed it! The random number was {random_number}.\nClick NEW GAME to start a\
 new game, or piss off(EXIT button).")
        game_end()
    else:
        tries_left -= 1
        if tries_left == 0:
            text_widget.insert(tk.END, f"You lost! The random number was {random_number}.\nClick NEW GAME to start a\
 new game, or piss off(EXIT button).")
            game_end()
        else:
            if num_input > random_number:
                high_or_low = "HIGH"
            else:
                high_or_low = "LOW"
            text_widget.insert(tk.END, f"Nope! Please, try again!\
 Your number is too {high_or_low}.\n{tries_left} tries left.")


# This function retrieves a value from the digit buttons clicked and passes it to the num comparison function
def button_click(value):
    number_checker(value)


# Clears the text field
def clear_text_field():
    text_widget.delete(1.0, tk.END)


# Resets the game by resetting the included values and enables the buttons once again
def game_reset():
    global tries_left
    tries_left = 3
    clear_text_field()

    # Generate a new random number
    global random_number
    random_number = random.randint(1, 10)

    button1.config(state=tk.NORMAL)
    button2.config(state=tk.NORMAL)
    button3.config(state=tk.NORMAL)
    button4.config(state=tk.NORMAL)
    button5.config(state=tk.NORMAL)
    button6.config(state=tk.NORMAL)
    button7.config(state=tk.NORMAL)
    button8.config(state=tk.NORMAL)
    button9.config(state=tk.NORMAL)
    button10.config(state=tk.NORMAL)


def game_end():
    # Disables the number buttons after the game is lost(the player can only start new game or exit)
    button1.config(state=tk.DISABLED)
    button2.config(state=tk.DISABLED)
    button3.config(state=tk.DISABLED)
    button4.config(state=tk.DISABLED)
    button5.config(state=tk.DISABLED)
    button6.config(state=tk.DISABLED)
    button7.config(state=tk.DISABLED)
    button8.config(state=tk.DISABLED)
    button9.config(state=tk.DISABLED)
    button10.config(state=tk.DISABLED)


root = tk.Tk()
root.geometry("600x500")
root.title("Numbers Guessing Game")

label = tk.Label(root, text="Numbers Guessing Game", font=("Arial", 15), fg="navy")
label.pack(padx=20, pady=20)

# Create text widget
text_widget = tk.Text(root, height=2)
text_widget.pack(padx=30, pady=30)

# Create buttons:
button_frame = tk.Frame(root)
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)

button1 = tk.Button(button_frame, text="1", font=("Arial", 15), command=lambda: button_click(1))
button1.grid(row=0, column=0, sticky=tk.W+tk.E)

button2 = tk.Button(button_frame, text="2", font=("Arial", 15), command=lambda: button_click(2))
button2.grid(row=0, column=1, sticky=tk.W+tk.E)

button3 = tk.Button(button_frame, text="3", font=("Arial", 15), command=lambda: button_click(3))
button3.grid(row=0, column=2, sticky=tk.W+tk.E)

button4 = tk.Button(button_frame, text="4", font=("Arial", 15), command=lambda: button_click(4))
button4.grid(row=1, column=0, sticky=tk.W+tk.E)

button5 = tk.Button(button_frame, text="5", font=("Arial", 15), command=lambda: button_click(5))
button5.grid(row=1, column=1, sticky=tk.W+tk.E)

button6 = tk.Button(button_frame, text="6", font=("Arial", 15), command=lambda: button_click(6))
button6.grid(row=1, column=2, sticky=tk.W+tk.E)

button7 = tk.Button(button_frame, text="7", font=("Arial", 15), command=lambda: button_click(7))
button7.grid(row=2, column=0, sticky=tk.W+tk.E)

button8 = tk.Button(button_frame, text="8", font=("Arial", 15), command=lambda: button_click(8))
button8.grid(row=2, column=1, sticky=tk.W+tk.E)

button9 = tk.Button(button_frame, text="9", font=("Arial", 15), command=lambda: button_click(9))
button9.grid(row=2, column=2, sticky=tk.W+tk.E)

button10 = tk.Button(button_frame, text="10", font=("Arial", 15), command=lambda: button_click(10))
button10.grid(row=3, column=0, sticky=tk.W+tk.E)

button_game_reset = tk.Button(button_frame, text="NEW GAME", font=("Arial", 15), bg="aquamarine", command=game_reset)
button_game_reset.grid(row=3, column=1, sticky=tk.W+tk.E)

button_game_exit = tk.Button(button_frame, text="EXIT", font=("Arial", 15), bg="yellow", command=root.quit)
button_game_exit.grid(row=3, column=2, sticky=tk.W+tk.E)


button_frame.pack(fill="x")

bottom_label = tk.Label(root, text="Rules Of The Game:\n\nYou have 3 tries to guess a number from 1 to 10.\nAfter each\
 failed try you will receive a hint on whether the number you entered is too high,\
 or too low.\n\nGood luck!", font=("Arial", 10), fg="olive")
label.pack(padx=10, pady=10)

bottom_label.pack(padx=10, pady=10)

root.mainloop()
