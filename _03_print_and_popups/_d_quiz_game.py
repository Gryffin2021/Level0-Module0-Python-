from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    user_score = 0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    answer = simpledialog.askstring(title="Question Level = Ez Pz", prompt="If 2x = 10|-3|, what is x?")
    #      // 3.  Use an if statement to check if their answer is correct
    if answer == "15":
        #      // 4.  if the user's answer was correct, add one to their score
        messagebox.showinfo(title="Result", message="Correct! +1 point")
        user_score += 1
    else:
        messagebox.showinfo(title="Result", message="Incorrect! The answer was 15, -1 point")
        user_score -= 1
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
    answer1 = simpledialog.askstring(title="Question Level = A little bit harder", prompt="In most cases, how much in numerical value does the prefix kilo- represent?")
    if answer1 == "1000":
        messagebox.showinfo(title="Result", message="Nice job! +1 point")
        user_score += 1
    else:
        messagebox.showinfo(title="Result", message="Your quite the dim light-bulb... The answer was 1000, -1 point")
        user_score -= 1
    answer2 = simpledialog.askstring(title="Question Level = Middle of the road", prompt="What is 1 divided by 0? Please answer in word form if it is an expression and not a number.")
    if answer2 == "undefined":
        messagebox.showinfo(title="Result", message="Your killing it! +1 point")
        user_score += 1
    else:
        messagebox.showinfo(title="Result", message="smh rn... The answer was undefined, -1 point")
        user_score -= 1
    answer3 = simpledialog.askstring(title="Question Level = Pretty fudgin' hard", prompt="If the equation 569936821221962380720^3 + (−569936821113563493509)^3 + x^3 = 3 is true, what 18 digit value can x be?")
    if answer3 == "−472715493453327032":
        messagebox.showinfo(title="Result", message="WOW! +1 point")
        user_score += 1
    else:
        messagebox.showinfo(title="Result", message="bruh. The answer was −472715493453327032, -1 point")
        user_score -= 1
    answer4 = simpledialog.askstring(title="Question Level = The single hardest question humanity has ever faced...", prompt="What is Obama's last name?")
    if answer4 == "Obama":
        messagebox.showinfo(title="Result", message="Impossible... That has to be right! +1 point")
        user_score += 1
    else:
        messagebox.showinfo(title="Result", message="That was a hard one, we don't even know the answer... -1 point")
        user_score -= 1
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function
    resultfinal = str(user_score)
    messagebox.showinfo(title="Result", message="You got " + resultfinal + " points!")
    # Run the window's .mainloop() method
    window.mainloop()
