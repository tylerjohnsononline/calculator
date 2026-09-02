

import tkinter as tk
import tkinter
from tkinter import *


def make_function_array_into_buttons(m, arrays, texts =False, 
                                     default_text = False,
                                     zero_zero= (0,0),
                                     text_colors=False, bg_colors=False, default_fontsize = 10 ,
                                     reliefs = False,
                                     sizing = False, #( height, width)
                                     ): #leftmost buttons going down first column
    if texts == False:
      texts = [["" for __ in xx ] for xx in arrays]
      if default_text != False:
        texts = [[f"{default_text}" for __ in yy ] for yy in arrays ]

    buttons = [[tk.Button(master = m,) for __ in xx ] for xx in arrays]
    for horizontal_index, commands in enumerate(buttons):
      for index, func in enumerate(commands):
         buttons[horizontal_index][index] = tk.Button(master = m, 
                 height=3,
                 width=5,
                 text=f"{texts[horizontal_index][index]}", 
                 command = arrays[horizontal_index][index]
               ) 
         if text_colors!=False:
           buttons[horizontal_index][index].config(foreground=text_colors[horizontal_index][index])
         if bg_colors != False:
           buttons[horizontal_index][index].config(bg=bg_colors[horizontal_index][index])
         if reliefs != False:
           buttons[horizontal_index][index].config(relief=reliefs[horizontal_index][index])
         if sizing != False:
           buttons[horizontal_index][index].config(width=sizing[horizontal_index][index][1],
                                                   height=sizing[horizontal_index][index][0])
         buttons[horizontal_index][index].config(font= ("Segoe UI",default_fontsize,))
         buttons[horizontal_index][index].grid(row = index+zero_zero[0], column =horizontal_index+zero_zero[1]) 



def exampleprinter():
  print(42)
def exprint():
  print(13)
def main():
  m = tkinter.Tk()

  m.title("simple GUI")
 
  functions = [[exampleprinter],
               [exprint]]
  names = [["print 42"],["print 13"]]
  make_function_array_into_buttons(m=m,arrays= functions, texts=names, default_text= "")
  m.mainloop()




if __name__ ==  "__main__":
  main()
  

