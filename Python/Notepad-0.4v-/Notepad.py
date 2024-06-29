from tkinter import *
from pygments.token import Token
from pygments.lexers import PythonLexer
from tkinter.scrolledtext import ScrolledText 
import tkinter as tk
from functools import partial
from tkinter import filedialog as fd
from tkinter import font
from tkinter import colorchooser
from tkinter.font import BOLD, Font
import tkinter.font as tkFont
import tkinter.messagebox as mb
from tkinter import ttk
from tkinter.colorchooser import askcolor


root = Tk()
root.resizable(False, False)
root.title('Notepad-v0.4')
text = Text(root)

root.iconbitmap( 'icons/Notepad.ico' )
lexer = PythonLexer()

c = Canvas(root, bg="black", width=False, height=False)
c.pack()

global selected
selected = False

def open_file():
    fd.askopenfilename()
def save_file():
    fd.asksaveasfilename()

def Save_file():
    file_name = fd.asksaveasfilename(
    filetypes=(("TXT files", "*.txt"),
                ("HTML files", "*.html;*.htm"),
                ("All files", "*.*")))
    f = open(file_name, 'w')
    s = text.get(1.0, END)
    f.write(s)
    f.close()

def Open_file(): 
    open_file1 = fd.askopenfilename(
    filetypes=(("TXT files", "*.txt"),
            ("HTML files", "*.html;*.htm"),
            ("All files", "*.*")))       
    f = open(open_file1)
    s = f.read()
    text.insert(1.0, s)    
    f.close()

def New_File():
    file_New = open('New file.txt', 'a')
    file_New.close()

def Select_All():
   text.tag_add("sel", "1.0","end")
   text.tag_configure("start", background="black", foreground= "white")

def notebook():
    msg = "version 0.4"
    mb.showinfo("Инф-version", msg)

def Copy():
    global selected
    if text.selection_get():
        selected = text.selection_get()

def Paste():
    if selected:
        position = text.index(INSERT)
        text.insert(position, selected)
             
def Exit_quit():
    global root
    root.quit()        

def my_popup(e): 
   my_menu.tk_popup(e.x_root, e.y_root)

def color_text():
    color = colorchooser.askcolor()
    text.configure(fg=color[1])


statusbar = tk.Label(root, bg="White", text="html", fg="black", bd=1, relief=tk.SUNKEN, anchor=tk.W)
statusbar.pack(side=tk.BOTTOM, fill=tk.X)

c.file_menu = Menu(tearoff=0)
c.file_menu.add_command(label="New File", command = New_File)
c.file_menu.add_separator()
c.file_menu.add_command(label="Save File", command = save_file)
c.file_menu.add_command(label="Open File", command = open_file)
c.file_menu.add_separator()
c.file_menu.add_command(label="Exit", command = Exit_quit)

c.Edit_menu = Menu(tearoff=0)
c.Edit_menu.add_command(label="Color_picker", command = color_text)
c.Edit_menu.add_separator()
c.Edit_menu.add_command(label="Paste", command = Paste)    
c.Edit_menu.add_command(label="Copy", command = Copy)
c.Edit_menu.add_separator()
c.Edit_menu.add_command(label="Select All", command = Select_All)

c.View_menu = Menu(tearoff=0)
c.View_menu.add_command(label="version Notepad", command = notebook)

my_menu = Menu(root, tearoff=0)
my_menu.add_command(label="Color_picker", command = color_text)
my_menu.add_separator()
my_menu.add_command(label="Open_file", command = Open_file)
my_menu.add_command(label="Save_file", command = Save_file)
my_menu.add_separator()
my_menu.add_command(label="Paste", command = Paste)
my_menu.add_command(label="Copy", command = Copy)
my_menu.add_command(label="Select_All", command = Select_All)
my_menu.add_separator()
my_menu.add_command(label="Increase")
my_menu.add_command(label="Decrease")
my_menu.add_separator()
my_menu.add_command(label="Frame.Tab_1")
my_menu.add_command(label="Frame.Tab_2")
my_menu.add_separator()
my_menu.add_command(label="Exit_quit", command = Exit_quit)

c.main_menu = Menu(root, tearoff=0, bg="black")
c.main_menu.add_cascade(label="File", menu = c.file_menu)
c.main_menu.add_cascade(label="Edit", menu = c.Edit_menu)
c.main_menu.add_cascade(label="View", menu = c.View_menu)

root.bind("<Button-3>", my_popup)
root.wm_attributes('-alpha', 0.9)
root.config(bg="white")

text = ScrolledText(root, insertbackground="black", fg="black", bg="white", undo=True)
text.bind('<Any-KeyPress>')
text.pack(expand = True, fill = BOTH)

text.bind('<<Modified>>')

text.tag_config("keyword", foreground='blue')
text.tag_config("string_literal", foreground='red')

root.config(menu = c.main_menu)
root.mainloop()
