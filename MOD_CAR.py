from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv
def exc():
    def dm():
        if messagebox.askyesno('Exit','Do you really want to exit',parent=po):
            po.destroy()
    def cm():
        def cbm():
            if messagebox.askyesno('Exit','Do you really want to exit',parent=dl):
                dl.destroy()
        def ecn():
            h=v=0
            lt=['*','/','+','<','>','?',';',':','[',']','{','}','|','=','_','(',')','~','`','!','@','#','$','%','^','&']
            with open('Car.csv') as f:
                r=csv.reader(f)
                L=list(r)
            for i in L:
                if i[0]==Cne.get():
                    h=1
                    i[1]=Cme.get()
            for j in lt:
                if j in Cme.get():
                    v=1
            if h==0:
                messagebox.showerror('Error','No such Car Exists',parent=dl)
            elif v==1:
                messagebox.showerror('Error','Car_Name has only alphabets(or numbers in some cases)',parent=dl)
            else:
                t=open('Car.csv','w',newline='')
                wt=csv.writer(t)
                wt.writerows(L)
                t.close()
                messagebox.showinfo('Updated','Updated the Car_name Successfully',parent=dl)
                dl.destroy()
            
        dl=Tk()
        dl.configure(bg='grey')
        dl.resizable(False,False)
        dl.geometry('500x300')
        dl.title('Updating Car_Name')
        Cn=Label(dl,text="Car_Id",bg='black',fg='red',font=('Arial','16'))
        Cne=Entry(dl,font=('Arial','16'))
        Cm=Label(dl,text="Car_Name",bg='black',fg='red',font=('Arial','16'))
        Cme=Entry(dl,font=('Arial','16'))
        Cn.place(x=50,y=100)
        Cne.place(x=210,y=100)
        Cm.place(x=50,y=150)
        Cme.place(x=210,y=150)
        EB=Button(dl,text='Enter',bg='black',fg='red',font=('Arial','16'),command=ecn)
        CB=Button(dl,text='Cancel',bg='black',fg='red',font=('Arial','16'),command=cbm)
        EB.place(x=50,y=200)
        CB.place(x=160,y=200)
    def pc():
        def cpm():
            if messagebox.askyesno('Exit','Are you sure you want to exit',parent=kl):
                kl.destroy()
        def epn():
            v=h=w=0
            with open('Car.csv') as f:
                r=csv.reader(f)
                L=list(r)
            for i in L:
                if i[0]==Cne.get():
                    h=1
                    i[2]=Cre.get()
            if not(Cre.get().isdigit()):
                v=1
            elif int(Cre.get()) not in range(50000,5000001):
                w=1
            if h==0:
                messagebox.showerror('Error','No such Car Exists',parent=kl)
            elif v==1 or w==1:
                messagebox.showerror('Error','Price is a number between 50000 and 5000000',parent=kl)
            else:
                t=open('Car.csv','w',newline='')
                wt=csv.writer(t)
                wt.writerows(L)
                t.close()
                messagebox.showinfo('Updated','Updated the Price Successfully',parent=kl)
                kl.destroy()
            
        kl=Tk()
        kl.configure(bg='grey')
        kl.resizable(False,False)
        kl.geometry('500x300')
        kl.title('Updating Price')
        Cn=Label(kl,text="Car_Id",bg='black',fg='red',font=('Arial','16'))
        Cne=Entry(kl,font=('Arial','16'))
        Cr=Label(kl,text="Price($)",bg='black',fg='red',font=('Arial','16'))
        Cre=Entry(kl,font=('Arial','16'))
        Cn.place(x=50,y=100)
        Cne.place(x=210,y=100)
        Cr.place(x=50,y=150)
        Cre.place(x=210,y=150)
        EB=Button(kl,text='Enter',bg='black',fg='red',font=('Arial','16'),command=epn)
        CB=Button(kl,text='Cancel',bg='black',fg='red',font=('Arial','16'),command=cpm)
        EB.place(x=50,y=200)
        CB.place(x=160,y=200)
    def ed():
        def edm():
            if messagebox.askyesno('Exit','Are you sure you want to exit',parent=ll):
                ll.destroy()
        def edn():
            v=h=w=0
            with open('Car.csv') as f:
                r=csv.reader(f)
                L=list(r)
            for i in L:
                if i[0]==Cne.get():
                    h=1
                    i[4]=Cee.get()
            if not(Cee.get().isdigit()):
                v=1
            elif len(Cee.get().strip())!=4:
                w=1
            if h==0:
                messagebox.showerror('Error','No such Car Exists',parent=ll)
            elif v==1 or w==1:
                messagebox.showerror('Error','Edition is the year it was released',parent=ll)
            else:
                t=open('Car.csv','w',newline='')
                wt=csv.writer(t)
                wt.writerows(L)
                t.close()
                messagebox.showinfo('Updated','Updated the Edition Successfully',parent=ll)
                ll.destroy()
            
        ll=Tk()
        ll.configure(bg='grey')
        ll.resizable(False,False)
        ll.geometry('500x300')
        ll.title('Updating Edition')
        Cn=Label(ll,text="Car_Id",bg='black',fg='red',font=('Arial','16'))
        Cne=Entry(ll,font=('Arial','16'))
        Ce=Label(ll,text="Edition",bg='black',fg='red',font=('Arial','16'))
        Cee=Entry(ll,font=('Arial','16'))
        Cn.place(x=50,y=100)
        Cne.place(x=210,y=100)
        Ce.place(x=50,y=150)
        Cee.place(x=210,y=150)
        EB=Button(ll,text='Enter',bg='black',fg='red',font=('Arial','16'),command=edn)
        CB=Button(ll,text='Cancel',bg='black',fg='red',font=('Arial','16'),command=edm)
        EB.place(x=50,y=200)
        CB.place(x=160,y=200)
    def clr():
        def ecm():
            if messagebox.askyesno('Exit','Are you sure you want to exit',parent=yl):
                yl.destroy()
        def ecl():
            v=h=0
            with open('Car.csv') as f:
                r=csv.reader(f)
                L=list(r)
            for i in L:
                if i[0]==Cne.get():
                    h=1
                    i[5]=Cle.get()
            if Cle.get() not in ('Red','Blue','Yellow','Green','White','Black','Orange','Purple','Grey','Olive green','Navy Blue'):
                v=1
            if h==0:
                messagebox.showerror('Error','No such Car Exists',parent=yl)
            elif v==1:
                messagebox.showerror('Error','Colours available are (Red,Blue,Yellow,Green,White,Black,Orange,Purple,Grey,Olive green,Navy Blue) also it is case sensitive',parent=yl)
            else:
                t=open('Car.csv','w',newline='')
                wt=csv.writer(t)
                wt.writerows(L)
                t.close()
                messagebox.showinfo('Updated','Updated the Colour Successfully',parent=yl)
                yl.destroy() 
        yl=Tk()
        yl.configure(bg='grey')
        yl.resizable(False,False)
        yl.geometry('500x300')
        yl.title('Updating Colour')
        Cn=Label(yl,text="Car_Id",bg='black',fg='red',font=('Arial','16'))
        Cne=Entry(yl,font=('Arial','16'))
        Cl=Label(yl,text="Edition",bg='black',fg='red',font=('Arial','16'))
        Cle=Entry(yl,font=('Arial','16'))
        Cn.place(x=50,y=100)
        Cne.place(x=210,y=100)
        Cl.place(x=50,y=150)
        Cle.place(x=210,y=150)
        EB=Button(yl,text='Enter',bg='black',fg='red',font=('Arial','16'),command=ecl)
        CB=Button(yl,text='Cancel',bg='black',fg='red',font=('Arial','16'),command=ecm)
        EB.place(x=50,y=200)
        CB.place(x=160,y=200)
    po=Tk()
    po.geometry('600x400')
    po.configure(bg='grey')
    po.resizable(False,False)
    po.title('Modifying Car Details')
    b=Button(po,text='Modify Car_Name',bg='black',fg='green2',font=('Arial','16'),command=cm)
    b1=Button(po,text='Modify Price($)',bg='black',fg='green2',font=('Arial','16'),command=pc)
    b2=Button(po,text='Modify Edition',bg='black',fg='green2',font=('Arial','16'),command=ed)
    b3=Button(po,text='Modify Colour',bg='black',fg='green2',font=('Arial','16'),command=clr)
    b4=Button(po,text='Exit',bg='black',fg='green2',font=('Arial','16'),command=dm)
    b.place(x=50,y=100)
    b1.place(x=50,y=150)
    b2.place(x=50,y=200)
    b3.place(x=50,y=250)
    b4.place(x=50,y=300)
