from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv
from random import *
import ADD_CAR
import SHOW_ALL
import SHOW_UNSOLD
import DEL_CAR
import ADD_OWN
import SHOW_OWN
import DEL_OWN
import MOD_OWN
import MOD_CAR
rm=randint(1,3)
y=Tk()
y.geometry('1200x700')
y.resizable(False,False)
y.title('Car Showroom Database')
y.configure(bg='grey')
'''t=open('Car.csv','w',newline='')
w=csv.writer(t)
w.writerow(['Car_Id','Car_Name','Price($)','Sold','Edition','Colur'])
t.close()
p=open('Owner.csv','w',newline='')
e=csv.writer(p)
e.writerow(['Owner_Id','Owner_Name','Owner_Mobile_Num','Owner_Mail','Car_Id'])
p.close()'''
if rm==1:
    fp=PhotoImage(file="Chiron.png")
    bl=Label(y,image=fp)
    bl.place(x=220,y=120,relwidth=0.8,relheight=0.8)
elif rm==2:
    fp=PhotoImage(file="Laferrari.png")
    bl=Label(y,image=fp)
    bl.place(x=220,y=120,relwidth=0.8,relheight=0.8)
elif rm==3:
    fp=PhotoImage(file="VenomF5.png")
    bl=Label(y,image=fp)
    bl.place(x=220,y=120,relwidth=0.8,relheight=0.8)
fpt=PhotoImage(file="Sonic Motor Logo.png")
lbl=Label(y,image=fpt,compound='top').place(x=60,y=10)
def kp():
    if messagebox.askyesno('Exit','Do you really want to exit',parent=y):
        y.destroy()
def adc():
    ADD_CAR.exc()
def scr():
    SHOW_ALL.exc()
def acr():
    SHOW_UNSOLD.exc()
def dlc():
    DEL_CAR.exc()
def ado():
    ADD_OWN.exc()
def soo():
    SHOW_OWN.exc()
def doo():
    DEL_OWN.exc()
def moo():
    MOD_OWN.exc()
def mdc():
    MOD_CAR.exc()
D=Button(y,text='Add Cars',bg='black',fg='green2',font=('Arial','16'),command=adc)
D.place(x=60,y=200)
D1=Button(y,text='Modify Cars',bg='black',fg='green2',font=('Arial','16'),command=mdc)
D1.place(x=60,y=250)
D2=Button(y,text='Delete Cars',bg='black',fg='green2',font=('Arial','16'),command=dlc)
D2.place(x=60,y=300)
D3=Button(y,text='Add Owner',bg='black',fg='green2',font=('Arial','16'),command=ado)
D3.place(x=60,y=350)
D4=Button(y,text='Modify Owner',bg='black',fg='green2',font=('Arial','16'),command=moo)
D4.place(x=60,y=400)
D5=Button(y,text='Delete Owner',bg='black',fg='green2',font=('Arial','16'),command=doo)
D5.place(x=60,y=450)
D6=Button(y,text='Exit',bg='black',fg='green2',font=('Arial','16'),command=kp)
D6.place(x=60,y=650)
D7=Button(y,text='Show Cars',bg='black',fg='green2',font=('Arial','16'),command=scr)
D7.place(x=60,y=500)
D8=Button(y,text='Show Unsold Cars',bg='black',fg='green2',font=('Arial','16'),command=acr)
D8.place(x=60,y=550)
D9=Button(y,text='Show Owner details',bg='black',fg='green2',font=('Arial','16'),command=soo)
D9.place(x=60,y=600)
y.mainloop()
