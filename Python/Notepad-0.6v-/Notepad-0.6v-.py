import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog as fd
from tkinter import colorchooser as ch
from tkinter import colorchooser
from  time import  strftime
from tkcalendar import Calendar
from tkinter import *


win = Tk()
win.geometry('560x450')
win.title('Notepad_0.6v')

def OpenFile():
    fd.askopenfilename()

def SaveFile():
    fd.asksaveasfilename()

def colorPicer():
    color = ch.askcolor()
    text.configure(fg=color[1])

def clearTextInputQ():
    text.delete("1.0", "end")

def colorPicerFons():
    color = ch.askcolor()
    text.configure(bg=color[1])
    
def my_popup(e): 
   my_menu.tk_popup(e.x_root, e.y_root)

def Quit():
    quit()

# Первой Size-текст
def new_window1():
    my_w = tk.Toplevel(win)
    my_w.title('Size-текст-0.5v')
    my_w.geometry("250x200")

    font1=['times', 12, 'normal']
    
    def my_fun(str1):
        if(str1=='plus'):
            font1[1]=font1[1]+2
        else:
            font1[1]=font1[1]-2
        text.config(font=font1)
    
    def my_fun2(value):
        font1[1]=my_scale1.get()
        text.config(font=font1)
    
    def colorSizeFons():
        color = ch.askcolor()
        text.configure(fg=color[1])

    my_scale1 = tk.Scale(my_w, from_=12, to=26, orient='horizontal',command=my_fun2)
    my_scale1.grid(row=2,column=1,padx=4)

    b1=tk.Button(my_w, text='+',command=lambda:my_fun('plus'))
    b1.grid(row=2,column=2)

    b2=tk.Button(my_w, text='-', command=lambda:my_fun('minus'))
    b2.grid(row=2,column=3)

    b3=tk.Button(my_w, text='Изменить Цвет', command=colorSizeFons)
    b3.grid(row=3,column=4)

    my_w.mainloop()
    # Первой Size-текст
     
# второй Canvas-Рисовалка.
def new_window():
    
    def on_canvas_click(event):
        x, y =  event.x, event.y
        canvas.create_oval(x-5, y-5, x+5, y+5, fill=current_color)

    def change_color():
        global current_color
        color = colorchooser.askcolor()
        if color[1] is not None:
            current_color = color[1]

    root = tk.Toplevel(win)
    root.title('Рисовалка-Python-0.5v')
    root.geometry('350x280')

    # current_color = "black"

    color_button = tk.Button(root, text="Выбрать цвет", command=change_color)
    color_button.pack(side="bottom")

    canvas = tk.Canvas(root, height=800, width=700)
    canvas.pack(fill="both")
    canvas.bind("<B1-Motion>", on_canvas_click)

    root.mainloop()
    # второй Canvas-Рисовалка.

# третие окно.
def my_calculate():

    test = tk.Toplevel(win)
    test.title('-0.5v-')

    def circle():
        c.create_oval(x, y, x + 30, y + 30, fill='red')

    def square():
        c.create_rectangle(x, y, x + 30, y + 30, fill='blue')


    def triangle():
        c.create_polygon(x, y, x- 15, y + 30, x + 15, y + 30,
                        fill='green', outline='black')

    def popup(e):
        global x, y
        x = e.x
        y = e.y
        menu.post(e.x_root, e.y_root)

    c = Canvas(test, width=300, height=300)
    c.pack()

    test.bind("<Button-3>", popup)

    menu = Menu(test, tearoff=0)
    menu.add_command(label="Круг", command=circle)
    menu.add_command(label="Квадрат", command=square)
    menu.add_command(label="Треугольник", command=triangle)

    test.mainloop()                
# третие окно.

#четвертое окно
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

    root = Tk()

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

    greeting = tk.Label(gut, text="Notepad_0.5v", width=25, height=5)
    greeting.pack()

    gut.mainloop()   
# Информация

# Информация
def newPomaq():

    gut = tk.Toplevel(win)
    gut.title('Информация')
    gut.geometry('250x200')

    def open_link():
        import webbrowser
        webbrowser.open("https://t.me/nic293nechepaev")

    link_label = Label(gut, text="Кликните здесь, что бы открыть Телеграмм!!", fg="blue", cursor="hand2", width=25, height=5)
    link_label.pack()

    link_label.bind("<Button-1>", lambda e: open_link())

    gut.mainloop()   
# Информация

# Часы
def myTeme():

    tqme = tk.Toplevel()
    tqme.title('Цифровые Часы')

    lable = Label(tqme, font=('aerial', 30), background='black', foreground='white')

    def time():
        string = strftime('%H:%M:%S %p')
        lable.config(text=string)
        lable.after(1000, time)

    lable.pack(anchor='center')
    time()

    tqme.mainloop()
# Часы

# календарь

def mycal():
    cali = tk.Toplevel()
    cali.title('Календарь')
    cali.geometry('400x400')

    cal = Calendar(cali, selectmode = 'day', year = 2020, month = 5, day = 22)
    cal.pack(pady = 20)

    def grad_date():
        date.config(text = "Selected Date is: " + cal.get_date())

    Button(cali, text = "Get Date",
       command = grad_date).pack(pady = 20)
 
    date = Label(cali, text = "")
    date.pack(pady = 20)

    cali.mainloop()
# календарь


win.bind("<Button-3>", my_popup)

my_menu = Menu(win, tearoff=0)
my_menu.add_command(label='Open File', command=OpenFile)
my_menu.add_command(label='Save File', command=SaveFile)
my_menu.add_separator()
my_menu.add_command(label='Цыфровый часы', command=myTeme)
my_menu.add_command(label='Календарь', command=mycal)
my_menu.add_separator()
my_menu.add_command(label='Color-Текст', command=colorPicer)
my_menu.add_command(label='Color-фон', command=colorPicerFons)
my_menu.add_command(label='Clear', command=clearTextInputQ)
my_menu.add_separator()
my_menu.add_command(label='Canvas-Рисовалка', command=new_window)
my_menu.add_command(label='Font-Текст', command=new_window1)
my_menu.add_separator()
my_menu.add_command(label='Quit File', command=Quit)

edit = Menu(win, tearoff=0)
edit.add_command(label='Color-текст', command=colorPicer)
edit.add_command(label='Color-фон', command=colorPicerFons)
edit.add_separator()
edit.add_command(label='Clear', command=my_clear)
edit.add_separator()
edit.add_command(label='Цыфровый часы', command=myTeme)
edit.add_command(label='Календарь', command=mycal)
edit.add_separator()
edit.add_command(label='Canvas-Рисовалка', command=new_window)
edit.add_command(label='Font', command=new_window1)
edit.add_separator()
edit.add_command(label='Canvas-угольники', command=my_calculate)
edit.add_separator()
edit.add_command(label='Счётчик слов', command=my_counter)

file = Menu(win, tearoff=0)
file.add_command(label='Open File', command=OpenFile)
file.add_command(label='Save File', command=SaveFile)
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

text = ScrolledText(win, height=450, width=350)
text.pack(side="right")

win.mainloop()