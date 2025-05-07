from tkinter import *
from tkinter import ttk
import csv
def exc():
    cr=Tk()
    cr.geometry('900x250')
    cr.title('All Cars')
    cr.resizable(False,False)
    f=open('Car.csv')
    r=csv.reader(f)
    L=list(r)
    tree=ttk.Treeview(cr)
    tree['show']='headings'
    tree['columns']=('Car_Id','Car_Name','Price($)','Sold','Edition','Colour')
    tree.column('Car_Id',width=150,minwidth=150,anchor=CENTER)
    tree.column('Car_Name',width=150,minwidth=150,anchor=CENTER)
    tree.column('Price($)',width=150,minwidth=150,anchor=CENTER)
    tree.column('Sold',width=150,minwidth=150,anchor=CENTER)
    tree.column('Edition',width=150,minwidth=150,anchor=CENTER)
    tree.column('Colour',width=150,minwidth=150,anchor=CENTER)
    tree.heading('Car_Id',text='Car_Id',anchor=CENTER)
    tree.heading('Car_Name',text='Car_Name',anchor=CENTER)
    tree.heading('Price($)',text='Price($)',anchor=CENTER)
    tree.heading('Sold',text='Sold',anchor=CENTER)
    tree.heading('Edition',text='Edition',anchor=CENTER)
    tree.heading('Colour',text='Colour',anchor=CENTER)
    j=0
    for i in range(1,len(L)):
        tree.insert('',j,text="",values=(L[i][0],L[i][1],L[i][2],L[i][3],L[i][4],L[i][5]))
        j=j+1
    tree.pack()
    hsb=ttk.Scrollbar(cr,orient='horizontal')
    hsb.configure(command=tree.xview)
    tree.configure(xscrollcommand=hsb.set)
    hsb.pack(fill=X,side=BOTTOM)
    tree.pack()
    vsb=ttk.Scrollbar(cr,orient='vertical')
    vsb.configure(command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)
    vsb.pack(fill=Y,side=RIGHT)
    tree.pack()

