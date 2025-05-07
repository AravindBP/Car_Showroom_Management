from tkinter import *
from tkinter import messagebox
import csv
def exc():
    def od():
        if messagebox.askyesno('Exit','Are you sure you want to exit',parent=dc):
            dc.destroy()
    def dcr():
        v=ct=0
        f=open('Car.csv')
        r=csv.reader(f)
        l=list(r)
        f.close()
        with open('Owner.csv','r') as f2:
                r2=csv.reader(f2)
                L2=list(r2)
        L=[]
        for i in l:
            if cide.get()!=i[0]:
                L.append(i)
            else:
                v+=1
        for i in L2:
            if cide.get()==i[4]:
                ct=1
        if v==0:
            messagebox.showerror(title='Error',message='No such Car_Id exists',parent=dc)
        elif ct==1:
            messagebox.showerror(title='Error',message="Can't delete as Car is already sold",parent=dc)
        else:
            fl=open('Car.csv','w',newline='')
            w=csv.writer(fl)
            w.writerows(L)
            fl.close()
            messagebox.showinfo(title='Removed record',message='Deleted record Successfully',parent=dc)
            dc.destroy()
    dc=Tk()
    dc.title('Remove car')
    dc.geometry('500x300')
    dc.resizable(False,False)
    dc.configure(bg='grey')
    cid=Label(dc,text='Car_Id',bg='black',fg='red',font=('Arial','16'))
    cide=Entry(dc,font=('Arial','16'))
    cid.place(x=50,y=100)
    cide.place(x=130,y=100)
    E=Button(dc,text='Enter',bg='black',fg='red',font=('Arial','16'),command=dcr)
    C=Button(dc,text='Cancel',bg='black',fg='red',font=('Arial','16'),command=od)
    E.place(x=50,y=150)
    C.place(x=180,y=150)

