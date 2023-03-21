#####CODE BY TUCUNAS

from time import sleep 
import pyautogui as auto
from tkinter import *
from tkinter import messagebox

windown = Tk()
menu = Menu(windown)
windown.config(menu = menu)
global msg_c
global msg_q

def spam():
    sleep(5)
    global info1
    info1 = Entry1.get()
    global info2
    info2 = Entry2.get()
    isInt = isinstance(info2, int)
    if info1 == '':
        messagebox.showerror('ERRO','Digite um valor valido!' )
    if isInt == False:
        messagebox.showerror('ERRO', 'Digite um valor valido!')
    auto.keyDown('alt')
    auto.press('tab')
    auto.keyUp('alt')
    for i in range(int(info2)):
        auto.write(info1)
        auto.press('enter')
    

windown.title('SpamBot by Tucunare')
filemenu = Menu(menu)
menu.add_cascade(label = 'Opções', menu = filemenu)
filemenu.add_command(label = 'Contato')
filemenu.add_separator()
filemenu.add_command(label = 'Sair', command = windown.quit)
Label(windown, text = 'Digite a mensagem e a quantidade de envios').grid(padx = 15, pady = 15)
Label(windown, text = 'Mensagem').grid(padx = 20)
Entry1 = Entry(windown, width = 25)
Entry1.grid()
Label(windown, text = 'Quantidade').grid(padx = 20)
Entry2 = Entry(windown, width = 25)
Entry2.grid()
btn_save = Button(windown,text = 'Spam', command=spam)
btn_save.grid(pady = 10)
Label(windown, text = 'O programa da alt + tab então deixe o chat em segundo plano!').grid(pady = 11)
windown.mainloop()