from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv
def exc():
    def do():
        if messagebox.askyesno('Exit','Are you sure you want to exit',parent=ao):
            ao.destroy()
    def dc():
        a=b=c=d=e=k=z=0
        lt=['*','/','+','-','<','>','?',';',':','[',']','{','}','|','=','_','(',')','~','`','!','@','#','$','%','^','&','0','1','2','3','4','5','6','7','8','9']
        nnl=['@gmail.com','@yahoo.com','@microsoft.com']
        with open('Owner.csv','r') as nf:
            rd=csv.reader(nf)
            nl=list(rd)
            for i in nl:
                if oide.get()==i[0]:
                    a=1
        with open('Car.csv','r') as ff:
            dd=csv.reader(ff)
            ll=list(dd)
            for j in ll:
                if cide.get() in j:
                    z=1
            for i in ll:
                if (i[0],i[3])==(cide.get(),'Y'):
                    c=1
        if len(oide.get())!=4 or not(oide.get()[0].isalpha()) or not(oide.get()[1].isdigit()) or not(oide.get()[2].isdigit()) or not(oide.get()[3].isdigit()):
            b=1
        for i in lt:
            if i in onme.get():
                d=1
        if not(onue.get().isdigit()) or len(onue.get())!=10:
            e=1
        for i in nnl:
            if i in omle.get():
                k=1
        if a==1:
            messagebox.showerror(title='Error',message='Owner_Id Already Exists',parent=ao)
        if b==1 and a!=1:
            messagebox.showerror(title='Error',message='Invalid Owner_Id(Valid Eg-X001)',parent=ao)
        if d==1 and b!=1 and a!=1:
            messagebox.showerror(title='Error',message='Owner_Name has only alphabets',parent=ao)
        if e==1 and d!=1 and b!=1 and a!=1:
            messagebox.showerror(title='Error',message='Mobile Number is 10 digit number',parent=ao)
        if k==0 and e!=1 and d!=1 and b!=1 and a!=1:
            messagebox.showerror(title='Error',message='Invalid Mail entered',parent=ao)
        if z==0 and k!=0 and e!=1 and d!=1 and b!=1 and a!=1:
            messagebox.showerror(title='Error',message='No Such car is present',parent=ao)
        if c==1 and z!=0 and k!=0 and e!=1 and d!=1 and b!=1 and a!=1:
            messagebox.showerror(title='Error',message='Car is already sold',parent=ao)
        if c!=1 and z!=0 and k!=0 and e!=1 and d!=1 and b!=1 and a!=1:
            f=open('Owner.csv','a',newline='')
            w=csv.writer(f)
            L=[oide.get(),onme.get(),int(onue.get()),omle.get(),cide.get()]
            w.writerow(L)
            f.close()
            messagebox.showinfo(title='Adding Owner',message='Added owner Successfully',parent=ao)
            fl=open('Car.csv')
            r=csv.reader(fl)
            L=list(r)
            fl.close()
            for i in L:
                if cide.get()==i[0]:
                    i[3]='Y'
            t=open('Car.csv','w',newline='')
            wr=csv.writer(t)
            wr.writerows(L)
            t.close()
            ao.destroy()
    ao=Tk()
    ao.resizable(False,False)
    ao.geometry('600x500')
    ao.title('Add Owner')
    ao.configure(bg='grey')
    oid=Label(ao,text='Owner_Id',bg='black',fg='red',font=('Arial','16'))
    onm=Label(ao,text='Owner_Name',bg='black',fg='red',font=('Arial','16'))
    onu=Label(ao,text='Owner_Mobile_Num',bg='black',fg='red',font=('Arial','16'))
    oml=Label(ao,text='Owner_Mail',bg='black',fg='red',font=('Arial','16'))
    cid=Label(ao,text='Car_Id',bg='black',fg='red',font=('Arial','16'))
    oid.place(x=50,y=150)
    onm.place(x=50,y=200)
    onu.place(x=50,y=250)
    oml.place(x=50,y=300)
    cid.place(x=50,y=350)
    oide=Entry(ao,font=('Arial','14'))
    onme=Entry(ao,font=('Arial','14'))
    onue=Entry(ao,font=('Arial','14'))
    omle=Entry(ao,font=('Arial','14'))
    cide=Entry(ao,font=('Arial','14'))
    oide.place(x=270,y=150)
    onme.place(x=270,y=200)
    onue.place(x=270,y=250)
    omle.place(x=270,y=300)
    cide.place(x=270,y=350)
    Ey=Button(ao,text='Enter',bg='black',fg='red',font=('Arial','16'),command=dc)
    CC=Button(ao,text='Cancel',bg='black',fg='red',font=('Arial','16'),command=do)
    Ey.place(x=150,y=400)
    CC.place(x=280,y=400)
