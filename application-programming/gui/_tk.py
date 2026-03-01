#! /usr/bin/env python
import tkinter as tk
from tkinter.messagebox import showinfo, showwarning, showerror
from tkinter.ttk import Combobox, Style
from functools import partial

def resize(value):
  pass

top = tk.Tk()
top.title('ChatGPT')
top.geometry('1150x700')

label = tk.Label(top, text='欢迎使用chatgpt！', font=('Helvetica', 22, 'bold'))
label.pack()

btn = tk.Button(top, text='关闭', bg='gray', fg='white', activeforeground='black', command=top.quit)
btn.pack()

scale = tk.Scale(top, from_=0, to=9, orient=tk.HORIZONTAL, command=resize)
scale.set(3)
scale.pack()

frame = tk.Frame(top)
scrollbar = tk.Scrollbar(frame)

listbox = tk.Listbox(frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


values = ['gpt-3.5-turbo', 'gemini-2.5-pro', 'qwen-plus']
combobox = Combobox(top, values=values).pack()


if __name__ == '__main__':
  top.mainloop()
