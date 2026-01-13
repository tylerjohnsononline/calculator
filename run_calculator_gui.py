
import tkinter as tk
import tkinter
from tkinter import *


import user_interface_tool
import calculator

class Button_Input_Wrangler():
  def __init__(self):
    self.description = ""
    self.inter = tkinter.Tk()
    # self.description
  def pri(self):
    print(self.description)
  def zero(self):
    self.description = "0"
    calculator.button_writes_to_backend(command = self.description, 
                                        editing_list = Storage)
    display_image()
  def one(self):
    self.description = "1"
    calculator.button_writes_to_backend(command = self.description, 
                                        editing_list = Storage)
    display_image()
  def two(self):
    self.description = "2"
    calculator.button_writes_to_backend(command = self.description, 
                                        editing_list = Storage)
    display_image()
  def three(self):
    self.description = "3"
    calculator.button_writes_to_backend(command = self.description, 
                                        editing_list = Storage)
    display_image()
  def four(self):
    self.description = "4"
    calculator.button_writes_to_backend(command = self.description, 
                                        editing_list = Storage)
    display_image()
  def five(self):
    self.description = "5"
    calculator.button_writes_to_backend(command = self.description, 
                                        editing_list = Storage)
    display_image()
  def six(self):
    self.description = "6"
    calculator.button_writes_to_backend(command = self.description, 
                                        editing_list = Storage)
    display_image()
  def seven(self):
    self.description = "7"
    calculator.button_writes_to_backend(command = self.description, 
                                        editing_list = Storage)
    display_image()
  def eight(self):
    self.description = "8"
    calculator.button_writes_to_backend(command = self.description, 
                                        editing_list = Storage)
    display_image()
  def nine(self):
    self.description = "9"
    calculator.button_writes_to_backend(command = self.description, 
                                        editing_list = Storage)
    display_image()
  def plus(self):
    self.description = "+"
    calculator.button_writes_to_backend(command = self.description, 
                                        editing_list = Storage)
    display_image()
  def minus(self):
    self.description = "-"
    calculator.button_writes_to_backend(command = self.description, 
                                        editing_list = Storage)
    display_image()
  def multiply(self):
    self.description = "*"
    calculator.button_writes_to_backend(command = self.description, 
                                        editing_list = Storage)
    display_image()
  def divide(self):
    self.description = "/"
    calculator.button_writes_to_backend(command = self.description, 
                                        editing_list = Storage)
    display_image()
  def decimal(self):
    self.description = "."
    calculator.button_writes_to_backend(command = self.description, 
                                        editing_list = Storage)
    display_image()
  def equals(self):
    self.description = "="
    calculator.button_writes_to_backend(command = self.description, 
                                        editing_list = Storage)
    display_image()
  def answer(self):
    self.description = "ANSWER"
    calculator.button_writes_to_backend(command = self.description, 
                                        editing_list = Storage)
    display_image()
  def positive_negative(self):
    self.description = "+/-"
    calculator.button_writes_to_backend(command = self.description, 
                                        editing_list = Storage)
    display_image()
  def back(self):
    self.description = "back"
    calculator.button_writes_to_backend(command = self.description, 
                                        editing_list = Storage)
    display_image()
  def clear(self):
    self.description = "clear"
    calculator.button_writes_to_backend(command = self.description, 
                                        editing_list = Storage)
    display_image()

# number_operator_grid[i+1,j-1] = create_button("ANSWER", '')
# number_operator_grid[i+1,j-2] = create_button('+/-', '')
# number_operator_grid[i+1,j] = create_button('back', '')
# number_operator_grid[i+1,j-3] = create_button('clear', '')

# Wrangle.inter = Button_Input_Wrangler()
Storage = calculator.NumberOperatorOrder([], [], [], [], [''])
Wrangle = Button_Input_Wrangler()

def display_image():
  panel = Label(master=Wrangle.inter, text=F"equation {Storage.backend}")
  panel.grid(row = 5, column =5)
  panel = Label(master=Wrangle.inter, text=F"result {Storage.previous_answer[-1]}")
  panel.grid(row = 6, column =5)

def backend_writer_function():
  Wrangle.inter
  calculator.button_writes_to_backend(command= Wrangle,
                                      editing_list =Storage )
  display_image()
#   updatetyping, answer

def main():  
  Wrangle.inter.title("Custom Calculator")
#   Wrangle.inter = Button_Input_Wrangler()
  backend_writer_function()
  functions = [[Wrangle.one,Wrangle.four,Wrangle.seven,Wrangle.decimal,],
               [Wrangle.two,Wrangle.five,Wrangle.eight,Wrangle.zero,],
               [Wrangle.three,Wrangle.six,Wrangle.nine,Wrangle.equals],
               [Wrangle.plus,Wrangle.minus,Wrangle.multiply,Wrangle.divide],
               [Wrangle.answer,Wrangle.positive_negative, Wrangle.back,Wrangle.clear]
            #    [print_show],
               ]
  button_labels = [["1","4","7",".",],
                   ["2","5","8","0"],
                   ["3","6","9","="],
                   ["+","-","*","/"],
                   ["ANSWER", "+/-", "back","clear" ]
                #    ["print show"],
                   ]
  user_interface_tool.make_function_array_into_buttons(m=Wrangle.inter, arrays=functions, texts =button_labels, 
                                     default_text = False,)
  Wrangle.inter.mainloop()

if __name__ ==  "__main__":
  main()
  
  
calculator.button_writes_to_backend