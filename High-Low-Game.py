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
root.geometry("600x400")
var = TK.IntVar()


def close2():
	starting_amount = starting_entry.get()
	update_money_amount.set("You have: $" + str(starting_amount))
	top.destroy()
top = TK.Toplevel(root)
aaa = Button(top, text="close", command = close2).place(x="50", y="50")
starting_entry = Entry(top)
starting_entry.place(x="60", y="80")


#functions for close and help
def close():
	root.quit()
def instructions():
	messagebox.showinfo("Help", "Instructions:\n1. You begin with $1000.\n2. Select if you think the next card drawn will br higher, lower, or the same as the current one.\n3. Enter an amount to bet.\n4. If you are correct you win your bet, if not you lose it.")
	
starting_card = random.randrange(1,14)	

#function for calculate
def calculate():
	global starting_amount
	global starting_card
	global logo
	card1 = random.randrange(1,14)
	numeric_bet = bet_entry.get()
	button_value = int(var.get())
	if numeric_bet.isnumeric() and button_value > 0:
		int_bet = int(numeric_bet)
		if int_bet > 0 and int_bet <= starting_amount:
			logo = PhotoImage(file="card"+str(card1)+".png")
			logo = logo.subsample(2, 2)
			image_label = Label(root, image = logo).place(x = 235, y= 110)
			update_card_value.set("The card value is: " + str(card1))
			if (button_value == 1 and card1 > starting_card) or (button_value == 2 and card1 < starting_card) or (button_value == 3 and card1 == starting_card):
				starting_amount = starting_amount + int_bet
				update_money_amount.set("You have: $" + str(starting_amount))
				update_money_change.set("You gained: $" + str(int_bet))
				starting_card = card1
			else:
				starting_amount = starting_amount - int_bet
				update_money_amount.set("You have: $" + str(starting_amount))
				update_money_change.set("You lost: $" + str(int_bet))
				starting_card = card1
		else:
			messagebox.showinfo("Error", "Please enter a valid bet")
	else:
		messagebox.showinfo("Error", "Please enter a valid bet")
				
#setting random initial card and picture
logo = PhotoImage(file="card"+str(starting_card)+".png")
logo = logo.subsample(2, 2)
image_label = Label(root, image = logo).place(x = 235, y= 110)

#welcome label and bottom banner	
welcome = Label(root, text = "Welcome to High-Low!", bg = "red", font="50", width="55", height="2").place(x="0")
bottom_banner = Label(root, text = "", bg = "red", height = "2", width = "85", font = "50").place(x="0",y="347")

#bet entry and label
bet_entry_label = Label(root, text = "Enter Bet:", font = "20").place(x="10", y= "270")
bet_entry = Entry(root, width="10")
bet_entry.place(x = "115", y = "277")

#card_value label and update
update_card_value = TK.StringVar()
update_card_value.set("The card value is: " + str(starting_card))
card_value = Label(root, textvariable = update_card_value, font = "30").place(x="225", y="80")

#money_amount labels and updates
update_money_amount = TK.StringVar()
update_money_amount.set("You have: $")
money_amount = Label(root, textvariable = update_money_amount, font = "30").place(x = "410", y = "210")
update_money_change = TK.StringVar()
update_money_change.set("")
money_change = Label(root, textvariable = update_money_change, font = "30").place(x="410", y= "170")


#close, help, and bet buttons
close_button = Button(root, text = "Close", command = close, font = "40").place(x="535",y="355", height="40", width="60")
help_button = Button(root, text = "Help", command = instructions, font= "40").place(x="470", y="355", height="40", width="60")
bet_button = Button(root, text = "Bet", font = "40", command = calculate).place(x="5",y = "355", height = "40", width = "60")

#radiobuttons
higher = Radiobutton(root, text = "Higher", variable = var, value = 1, font="20").place(x="10", y="120")
lower = Radiobutton(root, text = "Lower", variable = var, value = 2, font = "20").place(x="10", y="170")
same = Radiobutton(root, text = "Same", variable = var, value = 3, font = "20").place(x="10", y="220")

root.mainloop()
