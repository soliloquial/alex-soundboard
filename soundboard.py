from Tkinter import *
from subprocess import call
from string import split
from random import randint

phrases = []
for n in open("sounds.txt"):
	arr = split(n, ":")
	if(len(arr) > 2):
		phrases.append((arr[0],arr[1:]))
	elif(len(arr)==2):
		phrases.append((arr[0],[arr[1]]))
	else:
		phrases.append((arr[0],[arr[0]]))

class Application(Frame):
	def say_phrase(self, i):
		upper = len(phrases[i][1])-1
		index = randint(0,upper)
		print phrases[i][1][index]
		call(["say", '"' + phrases[i][1][index] + '"'])

	def createWidgets(self):
		i = 0
		for k in phrases:
			self.buttons[i] = Button(self)
			self.buttons[i]["text"] = k[0];
			self.buttons[i]["command"] = lambda arg=i: self.say_phrase(arg)
			self.buttons[i].pack()
			i = i+1

	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.buttons = {}
		self.pack()
		self.createWidgets()

root = Tk()
root.title("Alex Soundboard")
app = Application(master=root)
app.mainloop()
root.destroy()