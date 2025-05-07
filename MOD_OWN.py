from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv
def exc():
    def km():
        if messagebox.askyesno('Exit','Do you really want to exit',parent=mo):
            mo.destroy()
    def mon():
        def mof():
            v=0
            w=0
            lt=['*','/','+','-','<','>','?',';',':','[',']','{','}','|','=','_','(',')','~','`','!','@','#','$','%','^','&','0','1','2','3','4','5','6','7','8','9']
            with open('Owner.csv','r') as f:
                r=csv.reader(f)
                L=list(r)
            for i in L:
                if Oide.get()==i[0]:
                    i[1]=Oime.get()
                    v=1
            for i in lt:
                if i in Oime.get():
                    w=1
            if v==0:
                messagebox.showerror(title='Error',message='Given Owner_Id does not exist',parent=ab)
            elif w==1:
                messagebox.showerror(title='Error',message='Owner_Name has only alphabets',parent=ab)
            else:
                f1=open('Owner.csv','w',newline='')
                w=csv.writer(f1)
                w.writerows(L)
                f1.close()
                messagebox.showinfo(title='Modified Name',message='Modified Successfully',parent=ab)
                ab.destroy()
        def mw():
            if messagebox.askyesno('Exit','Do you really want to exit',parent=ab):
                ab.destroy()
        ab=Tk()
        ab.geometry('500x300')
        ab.resizable(False,False)
        ab.title('Modify Owner_Name')
        ab.configure(bg='grey')
        Oid=Label(ab,text='Owner_Id',fg='red',bg='black',font=('Arial','16'))
        Oide=Entry(ab,font=('Arial','14'))
        Oim=Label(ab,text='Owner_Name',fg='red',bg='black',font=('Arial','16'))
        Oime=Entry(ab,font=('Arial','14'))
        Oid.place(x=50,y=100)
        Oide.place(x=200,y=100)
        Oim.place(x=50,y=150)
        Oime.place(x=200,y=150)
        Ey=Button(ab,text='Enter',bg='black',fg='red',font=('Arial','16'),command=mof)
        CC=Button(ab,text='Cancel',bg='black',fg='red',font=('Arial','16'),command=mw)
        Ey.place(x=50,y=200)
        CC.place(x=160,y=200)
    def mun():
        def mt():
            if messagebox.askyesno('Exit','Do you really want to exit',parent=ac):
                ac.destroy()
        def mn():
            v=0
            w=0
            with open('Owner.csv','r') as f:
                r=csv.reader(f)
                L=list(r)
            if not(Oine.get().isdigit()) or len(Oine.get())!=10:
                v=1
            for i in L:
                if Oide.get()==i[0]:
                    i[2]=Oine.get()
                    w=1
            if w==0:
                messagebox.showerror(title='Error',message='Given Owner_Id does not exist',parent=ac)
            elif v==1:
                messagebox.showerror(title='Error',message='Mobile Number is 10 digit Number',parent=ac)
            else:
                f1=open('Owner.csv','w',newline='')
                w=csv.writer(f1)
                w.writerows(L)
                f1.close()
                messagebox.showinfo(title='Modified Mobile Number',message='Modified Successfully',parent=ac)
                ac.destroy()
            
        ac=Tk()
        ac.geometry('500x300')
        ac.resizable(False,False)
        ac.title('Modify Owner_Number')
        ac.configure(bg='grey')
        Oid=Label(ac,text='Owner_Id',fg='red',bg='black',font=('Arial','16'))
        Oide=Entry(ac,font=('Arial','14'))
        Oin=Label(ac,text='Owner_Number',fg='red',bg='black',font=('Arial','16'))
        Oine=Entry(ac,font=('Arial','14'))
        Oid.place(x=50,y=100)
        Oide.place(x=210,y=100)
        Oin.place(x=50,y=150)
        Oine.place(x=210,y=150)
        Ey=Button(ac,text='Enter',bg='black',fg='red',font=('Arial','16'),command=mn)
        CC=Button(ac,text='Cancel',bg='black',fg='red',font=('Arial','16'),command=mt)
        Ey.place(x=50,y=200)
        CC.place(x=160,y=200)
    def mml():
        def mtt():
            if messagebox.askyesno('Exit','Do you really want to exit',parent=ad):
                ad.destroy()
        def mm():
            v=0
            w=0
            nnl=['@gmail.com','@yahoo.com','@microsoft.com']
            with open('Owner.csv','r') as f:
                r=csv.reader(f)
                L=list(r)
            for i in nnl:
                if i in Oile.get():
                    w=1
            for i in L:
                if Oide.get()==i[0]:
                    i[3]=Oile.get()
                    v=1
            if v==0:
                messagebox.showerror(title='Error',message='Given Owner_Id does not exist',parent=ad)
            elif w==0:
                messagebox.showerror(title='Error',message='Invalid Email entered',parent=ad)
            else:
                f1=open('Owner.csv','w',newline='')
                w=csv.writer(f1)
                w.writerows(L)
                f1.close()
                messagebox.showinfo(title='Modified Owner_Mail',message='Modified Successfully',parent=ad)
                ad.destroy()
            
        ad=Tk()
        ad.geometry('500x300')
        ad.resizable(False,False)
        ad.title('Modify Owner_Mail')
        ad.configure(bg='grey')
        Oid=Label(ad,text='Owner_Id',fg='red',bg='black',font=('Arial','16'))
        Oide=Entry(ad,font=('Arial','14'))
        Oil=Label(ad,text='Owner_Mail',fg='red',bg='black',font=('Arial','16'))
        Oile=Entry(ad,font=('Arial','14'))
        Oid.place(x=50,y=100)
        Oide.place(x=210,y=100)
        Oil.place(x=50,y=150)
        Oile.place(x=210,y=150)
        Ey=Button(ad,text='Enter',bg='black',fg='red',font=('Arial','16'),command=mm)
        CC=Button(ad,text='Cancel',bg='black',fg='red',font=('Arial','16'),command=mtt)
        Ey.place(x=50,y=200)
        CC.place(x=160,y=200)
    def mcd():
        def mkt():
            if messagebox.askyesno('Exit','Do you really want to exit',parent=ae):
                ae.destroy()
        def mr():
            v=w=m=0
            with open('Owner.csv','r') as f:
                r=csv.reader(f)
                L=list(r)
            with open('Car.csv','r') as f2:
                r2=csv.reader(f2)
                L2=list(r2)
            for i in L:
                if i[0]==Oide.get():
                    v=1
                    m=i[4]
                    i[4]=Cde.get()
            for i in L2:
                if (i[0],i[3])==(Cde.get(),'N'):
                    w=1
            if v==0:
                messagebox.showerror('Error',"No such Owner_Id exists",parent=ae)
            elif w==0:
                messagebox.showerror('Error',"The Car is already sold/doesn't exist",parent=ae)
            else:
                f1=open('Owner.csv','w',newline='')
                w=csv.writer(f1)
                w.writerows(L)
                f1.close()
                for i in L2:
                    if i[0]==m:
                        i[3]='N'
                    if i[0]==Cde.get():
                        i[3]='Y'
                f3=open('Car.csv','w',newline='')
                w3=csv.writer(f3)
                w3.writerows(L2)
                f3.close()
                messagebox.showinfo(title='Modified Car_Id',message='Modified Successfully',parent=ae)
                ae.destroy()
        ae=Tk()
        ae.geometry('500x300')
        ae.resizable(False,False)
        ae.title('Modify Car_Id')
        ae.configure(bg='grey')
        Oid=Label(ae,text='Owner_Id',fg='red',bg='black',font=('Arial','16'))
        Oide=Entry(ae,font=('Arial','14'))
        Cd=Label(ae,text='Car_Id',fg='red',bg='black',font=('Arial','16'))
        Cde=Entry(ae,font=('Arial','14'))
        Oid.place(x=50,y=100)
        Oide.place(x=210,y=100)
        Cd.place(x=50,y=150)
        Cde.place(x=210,y=150)
        Ey=Button(ae,text='Enter',bg='black',fg='red',font=('Arial','16'),command=mr)
        CC=Button(ae,text='Cancel',bg='black',fg='red',font=('Arial','16'),command=mkt)
        Ey.place(x=50,y=200)
        CC.place(x=160,y=200)
    mo=Tk()
    mo.geometry('800x400')
    mo.resizable(False,False)
    mo.title('Modify Owner Data')
    mo.configure(bg='grey')
    b=Button(mo,text='Modify Owner_Name',bg='black',fg='green2',font=('Arial','16'),command=mon)
    b1=Button(mo,text='Modify Owner_Number',bg='black',fg='green2',font=('Arial','16'),command=mun)
    b2=Button(mo,text='Modify Owner_Mail',bg='black',fg='green2',font=('Arial','16'),command=mml)
    b3=Button(mo,text='Modify Car_Id',bg='black',fg='green2',font=('Arial','16'),command=mcd)
    b4=Button(mo,text='Exit',bg='black',fg='green2',font=('Arial','16'),command=km)
    b.place(x=50,y=100)
    b1.place(x=50,y=150)
    b2.place(x=50,y=200)
    b3.place(x=50,y=250)
    b4.place(x=50,y=300)
