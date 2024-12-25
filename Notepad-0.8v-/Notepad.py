import tkinter as tk
from __init__ import *
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
from tkinter import filedialog as fd
from tkinter import colorchooser as ch
from tkinter import colorchooser
from tkinter import INSERT, Menu, Label, Frame, Button, Text, Canvas  # Add specific imports
from time import strftime
from tkcalendar import Calendar

win = tk.Tk()
win.geometry('560x450')
win.title('Notepad_0.8v')

is_modified = False
original_title = 'Notepad_0.8v'
setup_window_closing(win, is_modified)

from AllProgramm.line_numbers import LineNumberWidget
line_numbers_widget = LineNumberWidget(win)
line_numbers = line_numbers_widget.main_text

text_widget = line_numbers
status_bar = StatusBar(line_numbers, text_widget)

# Функции    
def size_text():
    new_window1_size_text(win, line_numbers)

def my_calculate_win():
    my_calculate_window(win)

is_modified = False
original_title = 'Notepad_0.7v'

def update_title():
   if is_modified:
       win.title(f'*{original_title}')
   else:
       win.title(original_title)

def on_text_change(event=None):
   global is_modified
   is_modified = True
   update_title()
line_numbers.bind('<<Modified>>', on_text_change)

def OpenFile(): # Функция открытей фаела
    global is_modified
    file_path = fd.askopenfilename()
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                line_numbers.delete('1.0', 'end')
                line_numbers.insert('1.0', content)
            is_modified = False
            update_title()
        except Exception as e:
            messagebox.showerror("Error", str(e))

def SaveFile(): # Функция сохранение фаела
    global is_modified
    file_path = fd.asksaveasfilename(defaultextension=".txt",
                                   filetypes=[("Text files", "*.txt"),
                                            ("All files", "*.*")])
    if file_path:
       try:
            with open(file_path, 'w', encoding='utf-8') as file:
               content = line_numbers.get('1.0', 'end-1c')
               file.write(content)
            is_modified = False
            update_title()
       except Exception as e:
           messagebox.showerror("Error", str(e))

def colorPicer():
    color = ch.askcolor()
    if color[1] is not None:
        line_numbers.configure(fg=color[1])

def clearTextInputQ():
    line_numbers.delete("1.0", "end")

def colorPicerFons():
    color = ch.askcolor()
    if color[1] is not None:
        line_numbers.configure(bg=color[1])
    
def my_popup(e): 
   my_menu.tk_popup(e.x_root, e.y_root)

def on_click(event):
    print("Клик")

def my_copy():
    line_numbers.insert(INSERT, line_numbers.get("1.0", "end-1c"))

def Quit():
    quit()
# Функции Notepad-0.7v

win.bind("<Button-1>", on_click)

# четвертое окно
def my_counter():
    def counter():
        output.delete("0.0","end")
        filename = fd.askopenfilename()

        with open(filename) as file:
            text = file.read()
            
        text = text.replace("\n", " ")
        text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "").replace("—", "")
        text = text.lower()
        words = text.split()
        nonrep_words = list()
        
        for word in words:
            if word in nonrep_words:
                pass
            else:
                nonrep_words.append(word)
        
        output.insert("end","Amount of words: %d\n" % len(words))
        output.insert("end","Amount of nonrepeatable words: %d\n" % len(nonrep_words))

    root = tk.Tk()

    frame = Frame(root)
    frame.grid()

    title = Label(frame, text="Word counter")
    title.grid(row=1, column=1)

    import_btn = Button(frame, text="Import file...", command=counter)
    import_btn.grid(row=2, column=1, pady=4)

    output = Text(frame, width=45, height=3)
    output.grid(row=4, columnspan=3)

    root.mainloop()
#четвертое окно

# чистка
def my_clear():
    ryt = tk.Toplevel()
    ryt.title('Clear-text-0.5v-')
    ryt.geometry()

    def clearTextInput():
        textExample.delete("1.0", "end")

    textExample = tk.Text(ryt, height=10)
    textExample.pack()
    btnRead = tk.Button(ryt, height=1, width=10, text="Clear", command=clearTextInput)

    btnRead.pack()

    ryt.mainloop()
# чистка 

# Информация
def newInfa():

    gut = tk.Toplevel(win)
    gut.title('Информация')
    gut.geometry('250x200')

    greeting = tk.Label(gut, text="Notepad_0.8v \n\n Nicolas nech", width=25, height=5)
    greeting.pack()

    gut.mainloop()   
# Информация

win.bind("<Button-3>", my_popup)

my_menu = Menu(win, tearoff=0)
my_menu.add_command(label='Open File', command=OpenFile)
my_menu.add_command(label='Save File', command=SaveFile)
my_menu.add_separator()
my_menu.add_command(label='copy-text', command=my_copy)
my_menu.add_separator()
my_menu.add_command(label='Цыфровый часы', command=myTeme)
my_menu.add_command(label='Календарь', command=mycal)
my_menu.add_separator()
my_menu.add_command(label='Выбор Цвета', command=myStytsColor)
my_menu.add_separator()
my_menu.add_command(label='Color-Текст', command=colorPicer)
my_menu.add_command(label='Color-фон', command=colorPicerFons)
my_menu.add_command(label='Clear', command=clearTextInputQ)
my_menu.add_separator()
my_menu.add_command(label='Canvas-Рисовалка', command=new_window)
my_menu.add_command(label='Font-Текст', command=size_text)
my_menu.add_separator()
my_menu.add_command(label='Quit File', command=Quit)

edit = Menu(win, tearoff=0)
edit.add_command(label='Color-текст', command=colorPicer)
edit.add_command(label='Color-фон', command=colorPicerFons)
edit.add_separator()
edit.add_command(label='Clear', command=my_clear)
edit.add_separator()
edit.add_command(label='Canvas-Рисовалка', command=new_window)
edit.add_command(label='Font Size', command=size_text)
edit.add_separator()
edit.add_command(label='Canvas-угольники', command=my_calculate_win)

edit.add_separator()
edit.add_command(label='чётчик слов', command=my_counter)

file = Menu(win, tearoff=0)
file.add_command(label='Open File', command=OpenFile)
file.add_command(label='Save File', command=SaveFile)
file.add_separator()
file.add_command(label='Выбор Цвета', command=myStytsColor)
file.add_separator()
file.add_command(label='Цыфровый часы', command=myTeme)
file.add_command(label='Календарь', command=mycal)
file.add_separator()
file.add_command(label='Auto-закрытие', command=lambda: windowsOpenWin(win))
file.add_separator()
file.add_command(label='Quit File', command=Quit)

editVersions = Menu(win, tearoff=0)
editVersions.add_command(label='Помощь', command=newPomaq)
editVersions.add_command(label='Информация о версии', command=newInfa)

menu = Menu(win, tearoff=0)
menu.add_cascade(label='File', menu=file)
menu.add_cascade(label='Edit', menu=edit)
menu.add_cascade(label='Version', menu=editVersions)
win.config(menu=menu)

win.mainloop()