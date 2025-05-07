from tkinter import *
from tkinter import messagebox
import csv
def exc():
    ar=Tk()
    ar.geometry('600x500')
    ar.title('Add car')
    ar.resizable(False,False)
    ar.configure(bg='grey')
    def da():
        if messagebox.askyesno('Exit','Do you really want to exit',parent=ar):
            ar.destroy()
    def ac():
        re=open('Car.csv')
        r=csv.reader(re)
        l=list(r)
        lt=['*','/','+','-','<','>','?',';',':','[',']','{','}','|','=','_','(',')','~','`','!','@','#','$','%','^','&']
        g=h=i=j=k=p=q=v=0
        for i in l:
            if cide.get()==i[0] or cide.get() in i:
                q=1
        if len(cide.get())!=4 or not(cide.get().isalnum()) or not(cide.get()[0].isalpha()) or not(cide.get()[1].isdigit()) or not(cide.get()[2].isdigit()) or not(cide.get()[3].isdigit()):
            g=1
        for x in lt:
            if x in cnme.get():
                h=1
        if not(prce.get().isdigit()) or int(prce.get())  not in range(50000,5000001):
            i=1
        if not(Ede.get().isdigit()) or int(Ede.get()) not in range(1980,2025):
            k=1
        if not(clre.get().isalpha()) or clre.get() not in ('Red','Blue','Yellow','Green','White','Black','Orange','Purple','Grey','Olive green','Navy Blue'):
            v=1
        if q==1:
            messagebox.showerror(title='Error',message='Given Car_Id already exists',parent=ar)
        if g==1 and q!=1:
            messagebox.showerror(title='Error',message='Car_Id is invalid(Eg-F001)/Exceeded the length',parent=ar)
        if h==1 and g!=1 and q!=1:
            messagebox.showerror(title='Error',message='Car_Name has only alphabets and numbers',parent=ar)
        if i==1 and h!=1 and g!=1 and q!=1:
            messagebox.showerror(title='Error',message='Price has only numbers/Price is not in given range(50000,50000000)',parent=ar)
        if k==1 and j!=1 and i!=1 and h!=1 and g!=1 and q!=1:
            messagebox.showerror(title='Error',message='Edition is which year it was made(only in numbers) and range(1980,2024)',parent=ar)
        if v==1  and k!=1 and j!=1 and i!=1 and h!=1 and g!=1 and q!=1:
            messagebox.showerror(title='Error',message="Invalid Colour Entered/Colour should be in (Red,Blue,Yellow,Green,White,Black,Orange,Purple,Grey,Olive green,Navy Blue)",parent=ar)
        if v!=1  and k!=1 and j!=1 and i!=1 and h!=1 and g!=1 and q!=1:
            with open('Car.csv','a',newline='') as fl:
                w=csv.writer(fl)
                L=[cide.get(),cnme.get(),int(prce.get()),'N',int(Ede.get()),clre.get()]
                w.writerow(L)
            messagebox.showinfo(title='Adding Car',message='Added car successfully',parent=ar)
            ar.destroy()
    LB=Label(ar,text='Adding Car',bg='black',fg='red',font=('Arial','30'))
    LB.place(x=140,y=70)
    cid=Label(ar,text='Car_Id',bg='black',fg='red',font=('Arial','16'))
    cnm=Label(ar,text='Car_Name',bg='black',fg='red',font=('Arial','16'))
    prc=Label(ar,text='Price($)',bg='black',fg='red',font=('Arial','16'))
    Ed=Label(ar,text='Edition',bg='black',fg='red2',font=('Arial','16'))
    clr=Label(ar,text='Colour',bg='black',fg='red2',font=('Arial','16'))
    cide=Entry(ar,font=('Arial','14'))
    cnme=Entry(ar,font=('Arial','14'))
    prce=Entry(ar,font=('Arial','14'))
    slde=Entry(ar,font=('Arial','14'))
    Ede=Entry(ar,font=('Arial','14'))
    clre=Entry(ar,font=('Arial','14'))
    cid.place(x=50,y=150)
    cide.place(x=180,y=150)
    cnm.place(x=50,y=200)
    prc.place(x=50,y=250)
    Ed.place(x=50,y=300)
    cnme.place(x=180,y=200)
    prce.place(x=180,y=250)
    Ede.place(x=180,y=300)
    clr.place(x=50,y=350)
    clre.place(x=180,y=350)
    Ey=Button(ar,text='Enter',bg='black',fg='red',font=('Arial','16'),command=ac)
    CC=Button(ar,text='Cancel',bg='black',fg='red',font=('Arial','16'),command=da)
    Ey.place(x=150,y=400)
    CC.place(x=280,y=400)

