from tkinter import *

tk = Tk()
root = Tk()
tk.title('Кликер')

btn = Button(text='Клик!', width=15, height=7)
btn.pack()

n = 0  # переменная для счетчика


def nplus(event):
    global n
    n = n + 1
    label['text'] = str(n)









btn.bind('<Button-1>', nplus)

label = Label(tk, text=str(n), font=('Helvetica'))
label.pack()

tk.mainloop()