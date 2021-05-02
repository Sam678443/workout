from tkinter import *
import tkinter as tk
from datetime import datetime, date

root = tk.Tk()

font = ("Arial", 11, "bold")

canvas1 = tk.Canvas(root, width = 500, height = 450)
canvas1.pack()

label1 = tk.Label(root, text = 'This is your workout plan for today: ')
canvas1.create_window(165, 115, window = label1)

monday = "Barbell Bench Press\nSets : 5\nReps : 12 8 6 4 12\n\nIncline Dumbell Press\nSets : 5\nReps : 8 6 6 6 6\n\nIncline Fly\nSets : 5\nReps : 8 6 6 6 6\n\nDips\nSets : 5\nReps : 8 6 6 6 6\n\nWeighted Sit-Ups\nSets : 5\nReps : 10 10 10 10 10\n\nKneeling Cable Crunch\nSets : 5\nReps : 8 8 8 8 8"



def start():
	button1 = tk.Button(root, text = 'See Workout Plan', command = new_window, bg = 'DarkOliveGreen1')
	canvas1.create_window(270, 150, window = button1)
	quit()




def new_window():
	global canvas1
	canvas1
	# monday_display_var = monday_display()
	canvas1.destroy()
	canvas1= tk.Canvas(root, width = 500, height = 450)
	canvas1.pack()
	if datetime.today().isoweekday() == 4:
		label2 = tk.Label(root, text = monday , justify = LEFT, font = font, fg = 'gray26')
		canvas1.create_window(100, 230, window = label2)
		quit_button = tk.Button(root, text = 'QUIT', command = root.destroy, bg = 'firebrick1')
		canvas1.create_window(415,50, window = quit_button)
	if datetime.today().isoweekday() == 6:
		label2 = tk.Label(root, text = monday , justify = LEFT, font = 'Times')
		canvas1.create_window(100, 230, window = label2)
		quit_button = tk.Button(root, text = 'QUIT', command = root.destroy, bg = 'firebrick1')
		canvas1.create_window(415,50, window = quit_button)


def quit():
	quit_button = tk.Button(root, text = 'QUIT', command = root.destroy, bg = 'firebrick1')
	canvas1.create_window(270,270, window = quit_button)
	root.mainloop()
	if root.destroy == True:
		sys.exit(0)
		print("Have a great day! Goodbye!")
		x = False


if datetime.today().isoweekday() == 4:
	start()
elif datetime.today().isoweekday() == 6:
	start()
while x == True:
	tk.update_idletasks()
	tk.update()
	time.sleep(0.01)
# button1 = tk.Button(root, text = 'See Workout Plan', command = workout_plan, bg = 'orange')
# canvas1.create_window(270, 150, window=button1)

#Barbell Bench Press\n Sets : 5\n Reps : 12 8 6 4 12\n\nIncline Dumbell Press\nSets : 5\n Reps : 8 6 6 6 6\n\nIncline Fly\nSets : 5\n Reps : 8 6 6 6 6\n\nDips\n Sets : 5\nReps : 8 6 6 6 6\n\nWeighted Sit-Ups\nSets : 5\nReps : 10 10 10 10 10\n\nKneeling Cable Crunch\n Sets : 5\nReps : 8 8 8 8 8"
