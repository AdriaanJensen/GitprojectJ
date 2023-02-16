
from tkinter import*
import random


Root = Tk()
Root.geometry('400x400')
Root.resizable()
Root.title('Rock,paper,scissors')
Root.config(bg='seashell3')

Label(Root, text='Rock, Paper ,Scissors', font='arial 20 bold', bg='seashell2').pack()


User_take = StringVar()
