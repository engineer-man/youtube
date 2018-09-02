# author: filip

import tkinter
import tkinter.simpledialog
import tkinter.messagebox
import tkinter.ttk as ttk
import time
import random
import _thread

#the player's attributes.
hunger = 100
fun = 100
health = 100
day = 0
money = 0
sick = False
alive = True
meatApplied = False

#Constants (easy to change game rules)
SICK_PERCENTAGE = 10
DAY_DURATION = 5 #In seconds
TAMA_NAME = "n/a"
HUNGER_UPDATE = 400 #In ms
FUN_UPDATE = 400
HEALTH_UPDATE = 400
MONEY_ADD = 1
HUNGER_ADD = 10
FUN_ADD = 5
HEALTH_ADD = 8
MEAT_DURATION = 5 #In sec

#won't allow to have 2 game instances running
gameStarted = False

#-------------------------------------------------------------------

def startGame(event):
	start()

#-------------------------------------------------------------------

def start():
	global gameStarted, hunger, fun, health, alive, day, money

	if gameStarted == False:
		gameStarted = True
		hunger = 100
		fun = 100
		health = 100
		day = 0
		money = 0
		sick = False
		alive = True
		startLabel.config(text="たまごっち")
		update()

#-------------------------------------------------------------------

def update():

	updateDay()
	updateDisplay()
	updateNeeds()

#-------------------------------------------------------------------

def updateDisplay():

	global hunger, fun, health, day

	if hunger <= 75:
		catPic.config(image = hungryphoto)
		imageLabel.config(text="HUNGRY")
	elif sick == True:
		catPic.config(image = deadphoto)
		imageLabel.config(text="ILL")
	elif fun < 80:
		catPic.config(image = sadphoto)
		imageLabel.config(text="BORED")
	else:
		catPic.config(image = normalphoto)
		imageLabel.config(text="")

	progressBar() #initialize progress bars
	hungerLabel.config(text=str(hunger))
	funLabel.config(text=str(fun))
	healthLabel.config(text=str(health))

	dayLabel.config(text="day: " + str(day) + "    money: " + str(money))

	catPic.after(100, updateDisplay)

#-------------------------------------------------------------------

def updateNeeds():

	updateHunger()
	updateFun()
	updateHealth()
	updateMoney()

	isAlive()

#-------------------------------------------------------------------

def updateHunger():

	global hunger, sick

	if meatApplied == False: hunger -= 1

	if alive == True:
		hungerLabel.after(HUNGER_UPDATE, updateHunger)

#-------------------------------------------------------------------

def updateFun():

	global fun, sick

	fun -= 1

	if alive == True:
		if sick == True: #If tama's sick its needs will detoriate quicker
			funLabel.after(int(FUN_UPDATE / 2), updateFun)
		else:
			funLabel.after(FUN_UPDATE, updateFun)

#-------------------------------------------------------------------

def updateHealth():

	global health, sick

	isSick()

	if sick == True:
		health -= 1

	if alive == True:
		healthLabel.after(HEALTH_UPDATE, updateHealth)

#-------------------------------------------------------------------

def updateDay():

	global day

	if alive == True:
		day += 1
		dayLabel.after(DAY_DURATION * 1000, updateDay)

#-------------------------------------------------------------------

def updateMoney():

	global money

	if alive == True:
		money += MONEY_ADD
		dayLabel.after(300, updateMoney)

#-------------------------------------------------------------------

def updateLabel(turns, description):

	global day

	if alive == True:
		statusLabel.config(text=description)
		time.sleep(turns)
		statusLabel.config(text=" ")

#-------------------------------------------------------------------

def feed():

	global hunger, sick

	if hunger <= 88:
		if sick == True:
			hunger += HUNGER_ADD // 2
			_thread.start_new_thread(updateLabel, (3,TAMA_NAME + " doesn't want to eat."))
		else:
			hunger += HUNGER_ADD
	else:
		_thread.start_new_thread(updateLabel, (3, "Don't overfeed " + TAMA_NAME))

#-------------------------------------------------------------------

def play():

	global fun, sick

	if sick == False:
		if fun <= 95:
			fun += FUN_ADD
		else:
			_thread.start_new_thread(updateLabel, (3, TAMA_NAME + " doesn't want to play!"))
	else:
		_thread.start_new_thread(updateLabel, (3, TAMA_NAME + " doesn't want to play if it's sick!"))

#-------------------------------------------------------------------

def heal():

	global health, sick, HUNGER_UPDATE

	if sick == True:
		sick = False
		skullPhoto.config(image = skullNo)
		HUNGER_UPDATE //= 2
		if health <= 92:
			health += HEALTH_ADD
		else:
			health == 100
	else:
		_thread.start_new_thread(updateLabel, (3, TAMA_NAME + " is healthy!"))

#------------------------------------------------------------------

def isSick():

	global sick, HUNGER_UPDATE

	if sick != True:
		if random.randint(1,100) <= SICK_PERCENTAGE:
			sick = True
			skullPhoto.config(image = skull)
			HUNGER_UPDATE *= 2
			_thread.start_new_thread(updateLabel, (2, TAMA_NAME + " is sick!"))

#-------------------------------------------------------------------

def isAlive():

	global hunger, fun, health, alive

	if hunger <= 0 or fun <= 0 or health <= 0:
		catPic.config(image = deadphoto)
		_thread.start_new_thread(updateLabel, (2, TAMA_NAME + " has died!"))
		startLabel.config(text="Game Over!")
		endGame()
		if tkinter.messagebox.askyesno("Play again?", "Do you want to play again?"):
			start()
		return False

	if alive == True:
		hungerBar.after(100,isAlive)

#-------------------------------------------------------------------

def endGame():

	global alive, gameStarted

	alive = False
	gameStarted = False

#-------------------------------------------------------------------

def progressBar():

	global hunger, fun, health

	hungerBar["value"] = hunger
	funBar["value"] = fun
	healthBar["value"] = health

	if alive == True:
		hungerBar.after(100,progressBar)

#-------------------------------------------------------------------

def meatFun():
	_thread.start_new_thread(meatFunction, (MEAT_DURATION,));

#-------------------------------------------------------------------

def meatFunction(delay):

	global HUNGER_UPDATE,meatApplied,money

	if money >= 15:
		if alive == True:
			btnFeed.config(state="disabled")
			money -= 15
			meatApplied = True

			_thread.start_new_thread(updateLabel, (3, TAMA_NAME + " is eating!"))
			time.sleep(delay)
			btnFeed.config(state="normal")
			meatApplied = False
	else:
		_thread.start_new_thread(updateLabel, (3, "You don't have enough money for meat!"))

#-------------------------------------------------------------------

def ballFun():

	global FUN_UPDATE,money

	if money >= 50:
		FUN_UPDATE += int(FUN_UPDATE / 12)
		money -= 50
		_thread.start_new_thread(updateLabel, (3, "You upgraded your toys!"))
	else:
		_thread.start_new_thread(updateLabel, (3, "You don't have enough money for new toys!"))

#-------------------------------------------------------------------

def hospitalFun():

	global SICK_PERCENTAGE,money

	if money >= 25:
		SICK_PERCENTAGE -= 1
		money -= 25
		_thread.start_new_thread(updateLabel, (3, TAMA_NAME + " will be healthier from now on!"))

	else:
		_thread.start_new_thread(updateLabel, (3, "You don't have enough money for hospital treatment!"))
#-------------------------------------------------------------------

def rules():
	tkinter.messagebox.showinfo( TAMA_NAME,
		"たまごっち" + TAMA_NAME + ", these are the rules!\n\n" +
		"1. Don't let " + TAMA_NAME + "'s needs fall to zero, it will die!\n" +
		"2. If " + TAMA_NAME + " gets sick, cure it as soon as possible! It doesn't eat or play until you do and its needs detoriate quicker.\n" +
		"3. Too much of everything hurts. Do not feed " + TAMA_NAME + " when it's full!\n" +
		"4. The more you play with " + TAMA_NAME + ", the less enjoyment it gets. Try to change things up a little" +
		"\n\nShop:\n"+
		"Piece of meat: Fills " + TAMA_NAME + " so you don' have to feed it for a period of time\n" +
		"Ball: Decreases the decay rate of " + TAMA_NAME + "'s fun\n" +
		"Hospital: Decreases " + TAMA_NAME + "'a percentage of falling sick\n")

#---All-the-ugly-code-----------------------------------------------

#create a GUI window.
root = tkinter.Tk()
root.title("たまごっち!")
root.geometry("500x500")
root.resizable(0,0)

#Tamagotchi"s needs progress bars
s = ttk.Style()
s.theme_use("clam")
#s.configure("red.Horizontal.TProgressbar", background="red")
hungerBar = ttk.Progressbar(root, orient="horizontal", mode="determinate", length="200", variable="hunger")
hungerBar.place(relx=0.75, rely=0.07, anchor="center")
funBar = ttk.Progressbar(root, orient="horizontal", mode="determinate", length="200", variable="fun")
funBar.place(relx=0.75, rely=0.12, anchor="center")
healthBar = ttk.Progressbar(root, orient="horizontal", mode="determinate", length="200", variable="health")
healthBar.place(relx=0.75, rely=0.17, anchor="center")
progressBar() #initialize progress bars

#Tamagotchi"s labels /what a shitcode
startLabel = tkinter.Label(root, text="Tamagotchi! Press space to start.", font=("Helvetica", 12))
startLabel.pack()
hungerLabel = tkinter.Label(root, text=str(hunger), font=("Helvetica", 12))
hungerText = tkinter.Label(root, text="Hunger: ", font=("Helvetica", 12))
hungerLabel.place(relx=0.35, rely=0.07, anchor="w")
hungerText.place(relx=0.35, rely=0.07, anchor="e")
funLabel = tkinter.Label(root, text=str(fun), font=("Helvetica", 12))
funText = tkinter.Label(root, text="Fun: ", font=("Helvetica", 12))
funLabel.place(relx=0.35, rely=0.12, anchor="w")
funText.place(relx=0.35, rely=0.12, anchor="e")
healthLabel = tkinter.Label(root, text=str(health), font=("Helvetica", 12))
healthText = tkinter.Label(root, text="Health: ", font=("Helvetica", 12))
healthLabel.place(relx=0.35, rely=0.17, anchor="w")
healthText.place(relx=0.35, rely=0.17, anchor="e")
dayLabel = tkinter.Label(root, text="day: " + str(day) + "    money: " + str(money), font=("Helvetica", 12))
dayLabel.place(relx=0.5, rely=0.22, anchor="center")
imageLabel = tkinter.Label(root, text="", font=("Helvetica", 12))
imageLabel.place(relx=0.5, rely=0.685, anchor="center")
statusLabel = tkinter.Label(root, text="", font=("Helvetica", 12))
statusLabel.place(relx=0.5, rely=0.27, anchor="center")

#Tamagotchi's pictures
hungryphoto = tkinter.PhotoImage(file="tama/tama_hungry.png")
normalphoto = tkinter.PhotoImage(file="tama/tama_normal.png")
sadphoto = tkinter.PhotoImage(file="tama/tama_sad.png")
deadphoto = tkinter.PhotoImage(file="tama/tama_dead.png")
playingphoto = tkinter.PhotoImage(file="tama/tama_playing.png")

meat = tkinter.PhotoImage(file = "emoji/meat.png")
ball = tkinter.PhotoImage(file = "emoji/ball.png")
hospital = tkinter.PhotoImage(file = "emoji/hospital.png")
skull = tkinter.PhotoImage(file = "emoji/skull.png")
skullNo = tkinter.PhotoImage(file = "emoji/skullNo.png")

#Adds the Tamagotchi image onto the canvas
catPic = tkinter.Label(root, image=normalphoto)
catPic.place(relx=0.5, rely=0.47, anchor="center")
skullPhoto = tkinter.Label(root, image=skullNo)
skullPhoto.place(relx=0.85, rely=0.325, anchor="center")

#Buttons
btnFeed = tkinter.Button(root, text="Feed Tama", command=feed, activebackground="lightblue")
btnFeed.place(relx=0.3, rely=0.75, anchor="center")
btnPlay = tkinter.Button(root, text="Play with Tama", command=play, activebackground="lightblue")
btnPlay.place(relx=0.5, rely=0.75, anchor="center")
btnHeal = tkinter.Button(root, text="Heal Tama", command=heal, activebackground="lightblue")
btnHeal.place(relx=0.7, rely=0.75, anchor="center")
meatButton = tkinter.Button(root, command=meatFun,  image=meat, activebackground="lightblue")
meatButton.place(relx=0.3, rely=0.9, anchor="center")
ballButton = tkinter.Button(root, command=ballFun, image=ball ,activebackground="lightblue")
ballButton.place(relx=0.5, rely=0.9, anchor="center")
hospButton = tkinter.Button(root, command=hospitalFun, image=hospital , activebackground="lightblue")
hospButton.place(relx=0.7, rely=0.9, anchor="center")

#run the "startGame" function when the space key is pressed.
root.bind("<space>", startGame)

#User inputs
TAMA_NAME = tkinter.simpledialog.askstring("Name", "What's Tamagotchi's name?", initialvalue = "Tamagotchi")
if not TAMA_NAME:
	TAMA_NAME = "Tamako"
else:
	TAMA_NAME = TAMA_NAME.upper()
rules()

#start the GUI
root.mainloop()
