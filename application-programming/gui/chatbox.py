#! /usr/bin/env python
import tkinter as tk
from tkinter.messagebox import showinfo, showwarning, showerror
from tkinter.ttk import Combobox, Style
from functools import partial

def noop(*args, **kwargs):
  pass


def onresize(value):
  pass

class Chatbox:
  def __init__(self):
    self.name = 'Chatbox'
    
    self.top = tk.Tk()
    self.top.title(self.name)
    self.top.geometry('1200x750')

    tk.Label(self.top, text=self.name, font='"Microsoft YaHei" -16 bold').pack()
    tk.Button(
      self.top, 
      text='新对话', 
      bg='gray', 
      fg='white', 
      activebackground='blue', 
      activeforeground='white', 
      command=noop).pack(fill=tk.X, expand=1)
    tk.Scale(self.top, from_=0, to=10, orient=tk.HORIZONTAL, command=onresize).pack()




  def run(self):
    self.top.mainloop()


if __name__ == '__main__':
  chatbox = Chatbox()
  chatbox.run()
