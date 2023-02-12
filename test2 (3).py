from doctest import master
from tkinter import *
import urllib.request
import re

import pywhatkit

root = Tk()
root.config(bg="red")
root.title("Alvinnnnnnn!!!")



BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

playlist = []
namep=[]
songdetails = []

def add_to():
	play = "You -> Added " + e.get()
	txt.insert(END, "\n" + play+" song")
	user = e.get().lower()
	namep.append(user)

	e.delete(0, END)

def showplaylist():
	txt.insert(END, "\n" + "Alvin -> Your playlist is: ")
	for item in namep:
		txt.insert(END, "\n" +item)
	e.delete(0, END)

def play():
	play = "You -> " + e.get()
	txt.insert(END, "\n" + play)
	user = e.get().lower()
	txt.insert(END, "\n" + "Alvin -> Playing "+user)
	artist = user+" song"
	artist = artist.replace(" ", "+")
	t = "https://www.youtube.com/results?search_query=" + artist
	html = urllib.request.urlopen(t)
	video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
	z = "https://www.youtube.com/watch?v=" + video_ids[0]
	pywhatkit.playonyt(z)
	e.delete(0, END)

def saveplaylist():

	user = e.get().lower()
	name = user + ".txt"
	f = open(name, "w") #creating file
	#write into file
	f = open(name, "a")
	for item in namep:
		f.write(item + "\n")
	f.close()
	e.delete(0, END)
	txt.insert(END, "\n" + "Alvin -> Playlist saved as "+name+" !!!!!")

def playplaylist():
	user = e.get().lower()
	name = user + ".txt"
	f = open(name, "r")  # creating file
	for i in f.readlines():
		i = i + "song"
		artist = i.replace("\n", "+")
		artist = artist.replace(" ", "+")
		t = "https://www.youtube.com/results?search_query=" + artist
		html = urllib.request.urlopen(t)
		video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
		z = "https://www.youtube.com/watch?v=" + video_ids[0]
		pywhatkit.playonyt(z)
	e.delete(0, END)
	txt.insert(END, "\n" + "Alvin -> Playeeeeieiiiiing playlist " +user+" !!!")

# Send function
def send():
	send = "You -> " + e.get()
	txt.insert(END, "\n" + send)

	user = e.get().lower()

	if (user == "hello"):
		txt.insert(END, "\n" + "Alvin -> Hi there, how can I help?")

	elif (user == "hi" or user == "hii" or user == "hiiii" or user=="hey"):
		txt.insert(END, "\n" + "Alvin -> Hi there, what can I do for you?")

	elif (user == "how are you"):
		txt.insert(END, "\n" + "Alvin -> fine! and you")

	elif (user == "fine" or user == "i am good" or user == "i am doing good"):
		txt.insert(END, "\n" + "Alvin -> Great! how can I help you.")

	elif (user == "thanks" or user == "thank you" or user == "now its my time"):
		txt.insert(END, "\n" + "Alvin -> My pleasure !")

	elif (user == "what do you sell" or user == "what kinds of items are there" or user == "have you something"):
		txt.insert(END, "\n" + "Alvin -> We have coffee and tea")

	elif (user == "tell me a joke" or user == "tell me something funny" or user == "crack a funny line"):
		txt.insert(
			END, "\n" + "Alvin -> What did the buffalo say when his son left for college? Bison.! ")

	elif (user == "goodbye" or user == "see you later" or user == "see yaa"):
		txt.insert(END, "\n" + "Alvin -> Have a nice day!")

	elif (user == "which lab is your favourite?" or user == "which is your favourite lab?" or user == "which lab is your favourite"):
		txt.insert(END, "\n" + "Alvin -> why do you even askkkk..Obviously Advanced Programming Lab")

	else:
		txt.insert(END, "\n" + "Alvin -> Sorry! I didn't understand that")

	e.delete(0, END)

alvinicon = PhotoImage(file=r"your_img.png")
lable1 = Label(root, image=alvinicon)
lable1.place(x=0,y=0,relwidth=1,relheight=1)
			   #fg=TEXT_COLOR, text="Alvinnnnnnnnnn!!!!!", font=FONT_BOLD, pady=10, width=20, height=1).grid(row=0)

txt = Text(root, bg="#A52A2A", fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

send = Button(root, text="Sup?", font=FONT_BOLD, bg=BG_GRAY,
			command=send).grid(row=2, column=1)

play = Button(root, text="Play", font=FONT_BOLD, bg="red",
			command=play).grid(row=2, column=2)



add_to = Button(root, text="Add to Playlist", font=FONT_BOLD, bg="#EB5406",
			command=add_to).grid(row=2, column=3)

show = Button(root, text="Show Playlist", font=FONT_BOLD, bg="#A52A2A",
			command=showplaylist).grid(row=2, column=4)

save = Button(root, text="Save Playlist", font=FONT_BOLD, bg="#800080",
			command=saveplaylist).grid(row=2, column=5)

playplaylist = Button(root, text="Play Playlist", font=FONT_BOLD, bg="#9966CB",
			command=playplaylist).grid(row=2, column=6)


root.mainloop()


