import tkinter
import random
from tkinter import messagebox

colours = ['Red','Blue','Green','Pink','Black', 
           'Yellow','Orange','White','Purple','Brown'] 
score = 0
timeleft = 30

def startGame(event):
	if timeleft == 30:
		timer()

	changeColor()

def changeColor():
	global score
	global timeleft

	if timeleft > 0:
		inputBox.focus_set()

		if inputBox.get().lower() == colours[0].lower():
			score += 1

		inputBox.delete(0, tkinter.END)

		random.shuffle(colours)

		colorlabel.config(text=str(colours[1]), fg=str(colours[0]))

		scorelabel.config(text="Score: "+str(score))

def timer():
	global timeleft

	if timeleft > 0:
		timeleft -= 1

		timelabel.config(text="Time left: "+str(timeleft))

		timelabel.after(1000, timer)
	else:
		endgame()

def endgame():
	global score
	global timeleft

	q = messagebox.askyesno("Play again", "Do you want to play again?") 

	if q:
		score = 0
		timeleft = 30

		scorelabel.config(text="Press Enter to start\n")
		timelabel.config(text="Time left: "+str(timeleft))
		colorlabel.config(text="")
	else:
		root.quit()


root = tkinter.Tk()

root.title("COLOR GAME")
root.geometry("400x300")

instructions = tkinter.Label(root, text = "Type in the colour\nof the words, and not the word text!\n", 
                                      font = ('Helvetica', 14))
instructions.pack()

scorelabel = tkinter.Label(root, text="Press Enter to start\n", font=('Helvetica', 14))
scorelabel.pack()

timelabel = tkinter.Label(root, text="Time left: "+str(timeleft), font=('Helvetica', 14))
timelabel.pack()

colorlabel = tkinter.Label(root, font = ('Helvetica', 60))
colorlabel.pack()

inputBox = tkinter.Entry(root, font =('Helvetica',15))

root.bind('<Return>', startGame)
inputBox.pack()
inputBox.focus_set()

root.mainloop()
