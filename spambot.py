#####CODE BY TUCUNAS --- 2023

from time import sleep 
import pyautogui as auto
from tkinter import *
from tkinter import messagebox
import webbrowser as web
import random

#############################################
                                            
windown = Tk()
menu = Menu(windown)
windown.config(menu = menu)

#############################################

def spam():
    sleep(3)
    global info1
    info1 = Entry1.get()
    global info2
    try:
        info2 = int(Entry2.get())
    except ValueError:
        messagebox.showerror('ERRO','Digite um valor valido!')
        return
    if info1 == '':
        messagebox.showerror('ERRO','Digite um valor valido!' )
        return
    auto.keyDown('alt')
    auto.press('tab')
    auto.keyUp('alt')
    for i in range(int(info2)):
        auto.write(info1)
        auto.press('enter')
        
#############################################
        
def github():
    web.open('https://github.com/S4turny/SpamBot.py/tree/main')    

##########DESIGN DA JANELA##########

windown.title('SpamBot by Tucunare')
filemenu = Menu(menu)
menu.add_cascade(label = 'Opções', menu = filemenu)
filemenu.add_command(label = 'Sair', command = windown.quit)
Label(windown, text = 'Digite a mensagem e a quantidade de envios').grid(padx = 15, pady = 15)
Label(windown, text = 'Mensagem').grid(padx = 20)
Entry1 = Entry(windown, width = 25)
Entry1.grid()
Label(windown, text = 'Quantidade').grid(padx = 20)
Entry2 = Entry(windown, width = 25)
Entry2.grid()
btn_save = Button(windown,text = 'Spam', command = spam)
btn_save.grid(pady = 10)
Button(windown, text='MINHA GITHUB',command = github).grid(padx = 10, pady = 8)
Label(windown, text = 'deixe o chat em segundo plano!').grid(pady = 11)

#############################################

windown.mainloop()