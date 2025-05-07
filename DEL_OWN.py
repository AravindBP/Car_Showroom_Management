from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv
def exc():
    def ds():
        if messagebox.askyesno('Error','Are you sure you want to exit',parent=od):
            od.destroy()
    def dod():
        L=[]
        m=0
        v=0
        with open('Owner.csv','r') as ng:
            rn=csv.reader(ng)
            ln=list(rn)
        with open('Owner.csv','r') as f:
            r=csv.reader(f)
            l=list(r)
        for i in l:
            if i[0]!=Oide.get():
                L.append(i)
            if i[0]==Oide.get():
                m=i[4]
                v=1
        if v!=1:
            messagebox.showerror(title='Error',message='No such Owner exists',parent=od)
        if v==1:
            fl=open('Owner.csv','w',newline='')
            w=csv.writer(fl)
            w.writerows(L)
            fl.close()
            T=[]
            with open('Car.csv','r') as ft:
                rt=csv.reader(ft)
                lt=list(rt)
            pl=open('Car.csv','w',newline='')
            wl=csv.writer(pl)
            for i in lt:
                if i[0]==m:
                    i[3]='N'
                    T.append(i)
                else:
                    T.append(i)
            wl.writerows(T)
            pl.close()
            messagebox.showinfo(title='Removing Owner',message='Removed Owner Successfully',parent=od)
            od.destroy()
    od=Tk()
    od.title('Delete Owner')
    od.geometry('500x300')
    od.configure(bg='grey')
    Oid=Label(od,text='Owner_Id',fg='red',bg='black',font=('Arial','16'))
    Oide=Entry(od,font=('Arial','16'))
    Oid.place(x=50,y=150)
    Oide.place(x=160,y=150)
    Ey=Button(od,text='Enter',bg='black',fg='red',font=('Arial','16'),command=dod)
    CC=Button(od,text='Cancel',bg='black',fg='red',font=('Arial','16'),command=ds)
    Ey.place(x=50,y=200)
    CC.place(x=160,y=200)
