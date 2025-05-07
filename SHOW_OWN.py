from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import csv
def exc():
    os=Tk()
    os.title('Owner Details')
    os.geometry('900x250')
    os.resizable(False,False)
    with open('Owner.csv','r') as f:
        r=csv.reader(f)
        L=list(r)
    tree=ttk.Treeview(os)
    tree['show']='headings'
    tree['columns']=('Owner_Id','Owner_Name','Owner_Mobile_Num','Owner_Mail','Car_Id')
    tree.column('Owner_Id',width=150,minwidth=150,anchor=CENTER)
    tree.column('Owner_Name',width=150,minwidth=150,anchor=CENTER)
    tree.column('Owner_Mobile_Num',width=150,minwidth=150,anchor=CENTER)
    tree.column('Owner_Mail',width=200,minwidth=200,anchor=CENTER)
    tree.column('Car_Id',width=200,minwidth=200,anchor=CENTER)
    tree.heading('Owner_Id',text='Owner_Id',anchor=CENTER)
    tree.heading('Owner_Name',text='Owner_Name',anchor=CENTER)
    tree.heading('Owner_Mobile_Num',text='Owner_Mobile_Num',anchor=CENTER)
    tree.heading('Owner_Mail',text='Owner_Mail',anchor=CENTER)
    tree.heading('Car_Id',text='Car_Id',anchor=CENTER)
    j=0
    for i in range(1,len(L)):
        tree.insert('',j,text="",values=(L[i][0],L[i][1],L[i][2],L[i][3],L[i][4]))
        j+=1
    tree.pack()
    hsb=ttk.Scrollbar(os,orient='horizontal')
    hsb.configure(command=tree.xview)
    tree.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=X,side=BOTTOM)
    tree.pack()
    vsb=ttk.Scrollbar(os,orient='vertical')
    vsb.configure(command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)
    vsb.pack(fill=Y,side=RIGHT)
    tree.pack()
