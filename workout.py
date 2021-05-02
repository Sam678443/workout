import tkinter as tk

root = tk.Tk()

canvas1 = tk.Canvas(root, width = 500, height = 450)
canvas1.pack()

label1 = tk.Label(root, text = 'Enter the day: (Ex : monday) ')
canvas1.create_window(100, 100, window = label1)

entry1 = tk.Entry(root)
canvas1.create_window(290, 100, window = entry1)


def MONDAY():
	global monday
	monday = {'Barbell Bench Press' : "12 8 6 4 12",
	'Incline Dumbell Press' : "8 6 6 6 6",
	'Incline Fly' : "8 6 6 6 6",
	'Dips' : "8 6 6 6 6",
	'Weighted Sit-Ups' : "10 10 10 10 10",
	'Kneeling Cable Crunch' : "8 8 8 8 8"}

	for key, value in monday.items():
		print("\nWorkout : {} \nSets : 5 \nReps {}\n\n###############".format(key,value))

def TUESDAY():

	tuesday = {'Barbell Squats' : "12 10 8 8 6",
	'Dumbell Lunge' : "12 12 12 12",
	'Leg Press' : "10 10 8 6 6",
	'Leg Extension' : "12 12 12 12 12",
	'Barbell Straight Leg Deadlift' : "12 8 8 6 6",
	'Lying Leg Curl' : "8 8 8 8 8",
	'Calf Raises' : "12 10 10 8 12"}

	for key, value in tuesday.items():
		print("\nWorkout : {} \nSets : 5 \nReps {}\n\n###############".format(key,value))

def WEDNESDAY():

	wednesday = {'Underhand Pull-Ups' : "10 10 10 10 10",
	'Alternating Bicep Curl' : "12 10 8 8 8",
	'EZ Bar Curl' : "12 10 8 6 6",
	'Lying Triceps Extension' : "10 8 8 8 10",
	'Cable Pushdown' : "12 8 8 6 6",
	'Lying Leg Curl' : "8 8 8 8 8",
	'Dumbell Overhead Extensions' : "8 8 6 6 6"}

	for key, value in wednesday.items():
		print("\nWorkout : {} \nSets : 5 \nReps {}\n\n###############".format(key,value))

def THURSDAY():
	print("Break!! \nTake a break man, you've earned it!")

def FRIDAY():

	friday = {'Seated Dumbell Shoulder Press' : "12 10 8 8 6",
	'Bent Over Lateral Raises' : "12 10 8 8 8",
	'Front Raises' : "10 10 8 8 8",
	'Lateral Raise' : "12 10 10 10 8",
	'Cable Upright Row' : "12 10 8 8 8",
	'Medecine Ball Russian Twist' : "10 10 8 8 8",
	'Leg Raise' : "12 10 10 10 8"}

	for key, value in friday.items():
		print("\nWorkout : {} \nSets : 5 \nReps {}\n\n###############".format(key,value))


def SATURDAY():
	print("Break!! Take a break man you're going too hard!!")

def SUNDAY():
	sunday = {'Light Jog' : "7km",
	'Yoga' : "45 mins",
	'Foam Roll' : "Calves, Hip Flexors, Pecs",
	'Stretch' : "Calves, Hip Flexors, Pecs, Glutes"}
	for key, value in sunday.items():
		print("\n {} : {}\n\n#############".format(key, value))

def workout_plan():
	workout = str(entry1.get())

	if workout == "monday":
		print("Let's goooo!!!")
	elif workout == "tuesday":
		print("Well perhaps it is! Here's what you're doing...")
		TUESDAY()
	elif workout == "wednesday":
		print("Already?! That was quick. Here's the plan")
		WEDNESDAY()
	elif workout == "thursday":
		print("Let's goo!!")
		THURSDAY()
	elif workout == "friday":
		print("TGIF!! Here it is...")
		FRIDAY()
	elif workout == "saturday":
		print("It's the weekend...")
		SATURDAY()
	elif workout == "sunday":
		print("here it is")
		SUNDAY()
# else:
# 	print("ERROR Not Defined\n\nTry again")


button1 = tk.Button(root, text = 'See Workout Plan', command = workout_plan, bg = 'orange')
canvas1.create_window(270, 150, window=button1)

root.mainloop()