from tkinter import ttk
from tkinter import *

root = Tk()

numbers = StringVar()
numbers.set("0")
value_a = 0
value_b = 0
value_c = 0
operation = ""


	
	
class Calculator():
	def __init__(self, root):
		root.title("Calculator")
		root.geometry("450x450")
		root.resizable(width = False, height = False)
		
		self.number_entry = Entry(root, text = numbers, width = 50)
		self.number_entry.grid(row = 0, columnspan = 4)
		self.button7 = Button(root, text = "7", command=lambda: self.add_value("7")).grid(row = 1, column = 0, ipadx=47.5, sticky=W+E)
		self.button8 = Button(root, text = "8", command=lambda: self.add_value("8")).grid(row = 1, column = 1, ipadx=47.5,sticky=W+E)
		self.button9 = Button(root, text = "9", command=lambda: self.add_value("9")).grid(row = 1, column = 2, ipadx=47.5,sticky=W+E)
		self.buttonMultiplication = Button(root, text = "X", command=lambda: Calculator.multiplication()).grid(row = 1, column = 3, ipadx=47.5,sticky=W+E)
		self.button4 = Button(root, text = "4", command=lambda: self.add_value("4")).grid(row = 2, column = 0, sticky=W+E)
		self.button5 = Button(root, text = "5", command=lambda: self.add_value("5")).grid(row = 2, column = 1, sticky=W+E)
		self.button6 = Button(root, text = "6", command=lambda: self.add_value("6")).grid(row = 2, column = 2, sticky=W+E)
		#self.buttonSubtraction = Button(root, text = "-").grid(row = 2, column = 3, sticky=W+E)
		self.button1 = Button(root, text = "1", command=lambda: self.add_value("1")).grid(row = 3, column = 0, sticky=W+E)
		self.button2 = Button(root, text = "2", command=lambda: self.add_value("2")).grid(row = 3, column = 1, sticky=W+E)
		self.button3 = Button(root, text = "3", command=lambda: self.add_value("3")).grid(row = 3, column = 2, sticky=W+E)
		self.buttonAddition = Button(root, text = "+", command=lambda: Calculator.addition()).grid(row = 3, column =3, sticky=W+E)
		#self.buttonPlusMinus = Button(root, text = "+/-").grid(row = 4, column = 0, sticky=W+E)
		self.button0 = Button(root, text = "0", command=lambda: self.add_value("0")).grid(row = 4, column = 1, sticky=W+E)
		#self.buttonDecimal = Button(root, text = ".").grid(row = 4, column = 2, sticky=W+E)
		self.buttonEqual = Button(root, text = "=", command=lambda: Calculator.equal()).grid(row = 4, column = 3, sticky=W+E)
		
	def add_value(self, value):
		number_append = numbers.get() + value
		numbers.set(number_append)
		
	def addition():
		global value_a, value_b, value_c, operation
		value_b = float(numbers.get())
		value_c = value_a + value_b
		value_a = value_c
		numbers.set("0")
		print(value_a, value_b, value_c)
		operation = "addition"
	def equal():
		if operation == "addition":
			Calculator.addition()
		if operation == "multiplication":
			Calculator.multiplication()
		numbers.set(str(value_c))
		
	def multiplication():
		global value_a, value_b, value_c, operation
		value_b = float(numbers.get())
		value_c = value_a * value_b
		value_a = value_c
		numbers.set("0")
		print(value_a, value_b, value_c)
		operation = "multiplication"
		
		
Calculator(root)
root.mainloop() 
