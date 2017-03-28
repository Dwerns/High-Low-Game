import tkinter as TK
from tkinter import Button, messagebox, Label, Radiobutton, PhotoImage, Entry
import random

#procedure for centering window
def center_window(width=300, height=200):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

#open root window  
root = TK.Tk()
center_window(600, 400)
root.geometry("700x400")
var = TK.IntVar()
root.resizable(0,0)

#functions for close and help
def close():
	root.quit()
def instructions():
	messagebox.showinfo("Help", "Instructions:\n1. Enter an amount to start with and click submit.\n2. Select if you think the next card drawn will br higher, lower, or the same as the current one.\n3. Enter an amount to bet.\n4. If you are correct you win your bet, if not you lose it.")

#function for submiting the starting amount
def submit():
	global starting_amount
	starting_amount = starting_amount_entry.get()
	try:
		starting_amount = round(float(starting_amount),2)
	except ValueError:
		messagebox.showinfo("Error", "Please enter a valid number")	
	else:
		if starting_amount > 0:
			update_money_amount.set("You have: $" + str(starting_amount))
			starting_amount_entry.config(state="disabled")
			bet_button.config(state="normal")
			submit_button.config(state="disabled")
		else:
			messagebox.showinfo("Error", "Please enter an amount greater than 0")
			
#setting the starting card to a random card			
starting_card = random.randrange(1,14)	

#function for calculate
def calculate():
	global starting_amount
	global starting_card
	global logo
	card1 = random.randrange(1,14)
	numeric_bet = bet_entry.get()
	button_value = int(var.get())
	try:
		numeric_bet = round(float(numeric_bet),2)
	except ValueError:
		messagebox.showinfo("Error", "Please enter a valid bet")
	else: 
		if numeric_bet > 0 and numeric_bet <= starting_amount and button_value > 0:
			logo = PhotoImage(file="card"+str(card1)+".png")
			logo = logo.subsample(2, 2)
			image_label = Label(root, image = logo).place(x = 490, y = 110)
			update_card_value.set("The card value is: " + str(card1))
			if (button_value == 1 and card1 > starting_card) or (button_value == 2 and card1 < starting_card) or (button_value == 3 and card1 == starting_card):
				starting_amount = round(float(starting_amount) + float(numeric_bet),2)
				update_money_amount.set("You have: $" + str(starting_amount))
				update_money_change.set("You gained: $" + str(numeric_bet))
				starting_card = card1
			else:
				starting_amount = round(float(starting_amount) - float(numeric_bet),2)
				update_money_amount.set("You have: $" + str(starting_amount))
				update_money_change.set("You lost: $" + str(numeric_bet))
				starting_card = card1
				if starting_amount == 0:
					messagebox.showinfo("Game Over", "You Lose!")
					root.quit()
		else:
			messagebox.showinfo("Error", "Please enter a bet greater than 0 and less than the current amount")
				
#setting random initial card and picture
logo = PhotoImage(file="card"+str(starting_card)+".png")
logo = logo.subsample(2, 2)
image_label = Label(root, image = logo).place(x = 490, y= 110)

#welcome label and bottom banner	
welcome = Label(root, text = "Welcome to High-Low!", bg = "red", font="50", width="64", height="2").place(x="0")
bottom_banner = Label(root, text = "", bg = "red", height = "2", width = "85", font = "50").place(x="0",y="348")

#bet entry and label, starting amount label and entry
bet_entry_label = Label(root, text = "Bet:", font = "20").place(x="10", y= "270")
bet_entry = Entry(root, width="10")
bet_entry.place(x = "55", y = "277")
starting_amount_label = Label(root, text = "Starting Amount:", font = "20").place(x="10", y="97")
starting_amount_entry = Entry(root, width="10")
starting_amount_entry.place(x="167",y="103")

#card_value label and update
update_card_value = TK.StringVar()
update_card_value.set("The card value is: " + str(starting_card))
card_value = Label(root, textvariable = update_card_value, font = "30").place(x="470", y="80")

#money_amount labels and updates
update_money_amount = TK.StringVar()
update_money_amount.set("You have: ")
money_amount = Label(root, textvariable = update_money_amount, font = "30", bg = "red").place(x = "150", y = "360")
update_money_change = TK.StringVar()
update_money_change.set("")
money_change = Label(root, textvariable = update_money_change, font = "30", bg = "red").place(x="330", y= "360")

#close, help, submit, and bet buttons
close_button = Button(root, text = "Close", command = close, font = "40").place(x="625",y="355", height="40", width="70")
help_button = Button(root, text = "Help", command = instructions, font= "40").place(x="550", y="355", height="40", width="70")
bet_button = Button(root, text = "Bet", font = "40", command = calculate, state="disabled")
bet_button.place(x="5",y = "355", height = "40", width = "70")
submit_button = Button(root, text = "Submit", command = submit)
submit_button.place(x="250", y="100", height = "25", width = "50")

#radiobuttons
higher = Radiobutton(root, text = "Higher", variable = var, value = 1, font="20").place(x="10", y="130")
lower = Radiobutton(root, text = "Lower", variable = var, value = 2, font = "20").place(x="10", y="180")
same = Radiobutton(root, text = "Same", variable = var, value = 3, font = "20").place(x="10", y="230")

root.mainloop()
