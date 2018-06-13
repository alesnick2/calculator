# -*- coding: UTF-8 -*-
"""
Name
    GUI development.py

Purpose
    This python script is used to develop the calculator GUI module.
    
Revision Dates
    13-JUN-2018 (ALE) [0.1]: Initial Version
"""

_authors_    = ["Andre Lesnick"]
_version_    = "0.1"
_maintainer_ = ""

_status_     = "Development"

#INCLUDES
from tkinter import *


calculator = Tk()
calculator.title('Calculator')
calculator.geometry("400x550")
calculator.resizable(0,0)

class Application (Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		self.createDisplay()


	def createDisplay(self):
		self.display = Entry (self, font = ("Helvetica", 27), justify = RIGHT)
		self.display.insert (0, "0")
		self.display.grid(row = 0, column = 0)

a = Application(calculator).grid()
calculator.mainloop()





