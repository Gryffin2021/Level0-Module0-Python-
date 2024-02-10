from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Make a variable equal to a positive number less than 4 using random.randInt(0, 3)
    number = random.randint(0, 3)
    # 2. Print your variable to the console
    print(number)
    # 3. Get the user to enter something that they think is awesome
    inquiry = simpledialog.askstring(title="Question", prompt="What is something you think is awesome?")
    # 4. If your variable is  0
    if number == 0:
        # -- tell the user whatever they entered is awesome!
        messagebox.showinfo(title="Result", message="That is AWESOME!")
    # 5. If your variable is  1
    if number == 1:
        # -- tell the user whatever they entered is ok.
        messagebox.showinfo(title="Result", message="Eh, that's ok...")
    # 6. If your variable is  2
    if number == 2:
        # -- tell the user whatever they entered is boring.
        messagebox.showinfo(title="Result", message="That's boring.")
    # 7. If your variable is  3
    if number == 3:
        # -- invent your own message to give to the user (be nice).
        messagebox.showinfo(title="Result", message="Why would anybody care about something that stupid???")
    # Run the window's .mainloop() method
    window.mainloop()