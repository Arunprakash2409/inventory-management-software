#import modules of py tk
from tkinter import *
import sqlite3
import tkinter.messagebox

#To add the Data into the Data Base
conn = sqlite3.connect("E:\Store Management Software\Database\store.db")
c = conn.cursor()

result = c.execute("SELECT max(id) from inventory")
for r in result:
    id = r[0]
class Database:
    def __init__(self, master, *args, **kwargs):

        self.master = master
        self.heading = Label(master, text="update the database", font=('arial 40 bold'), fg='steelblue')
        self.heading.place(x=500,y=0)

       
        #labels of product detils on window
        #to display the name of fealds
        #id of the product
        self.id_le = Label(master,text="Enter ID", font=('arial 18 bold'))
        self.id_le.place(x=0, y=100)

        self.id_leb = Entry(master, width=25, font=('arial 18 bold'))
        self.id_leb.place(x=400, y=100)

        self.btn_search = Button(master, text="Search", width=15, height=2, bg='orange', command=self.Search)
        self.btn_search.place(x=850, y=100)
        #fealdes names
        #Name of product
        self.name_l = Label(master,text="Enter product Name", font=('arial 18 bold'))
        self.name_l.place(x=0, y=150)
        #Stock detils
        self.stock_l = Label(master,text="No of Stock", font=('arial 18 bold'))
        self.stock_l.place(x=0, y=200)
        #cost price
        self.cp_l = Label(master,text="Cost price", font=('arial 18 bold'))
        self.cp_l.place(x=0, y=250)
        #Selling price
        self.sp_l = Label(master,text="Selling price", font=('arial 18 bold'))
        self.sp_l.place(x=0, y=300)
        #total cost price
        self.totalcp_l = Label(master,text=" total Cost price", font=('arial 18 bold'))
        self.totalcp_l.place(x=0, y=350)
        #total selling price
        self.totalsp_l = Label(master,text="total selling price", font=('arial 18 bold'))
        self.totalsp_l.place(x=0, y=400)
        #vender
        self.vender_l = Label(master,text="vender Name", font=('arial 18 bold'))
        self.vender_l.place(x=0, y=450)
        #vender phone number
        self.vender_phone_l = Label(master,text="Vender phone Number", font=('arial 18 bold'))
        self.vender_phone_l.place(x=0, y=500)
       

        #Text box for the labels
        #product name
        self.name_e = Entry(master, width=25, font=('arial 18 bold'))
        self.name_e.place(x=400, y=150)
        #Stock
        self.stock_e = Entry(master, width=25, font=('arial 18 bold'))
        self.stock_e.place(x=400, y=200)
        #cost price
        self.cp_e = Entry(master, width=25, font=('arial 18 bold'))
        self.cp_e.place(x=400, y=250)
        #selling price
        self.sp_e = Entry(master, width=25, font=('arial 18 bold'))
        self.sp_e.place(x=400, y=300)
        #total number of cost price
        self.totalcp_e = Entry(master, width=25, font=('arial 18 bold'))
        self.totalcp_e.place(x=400, y=350)
        #total number of selling price
        self.totalsp_e = Entry(master, width=25, font=('arial 18 bold'))
        self.totalsp_e.place(x=400, y=400)
        #vender name
        self.vender_e = Entry(master, width=25, font=('arial 18 bold'))
        self.vender_e.place(x=400, y=450)
        #vender phone number
        self.vender_phone_e = Entry(master, width=25, font=('arial 18 bold'))
        self.vender_phone_e.place(x=400, y=500)
        
        #button for save data in to the database
        #Add the changed data into the the Data Base
        self.btn_add = Button(master, text="Update to Database", width=25, height=2, bg='steelblue', fg='white', command=self.update)
        self.btn_add.place(x=599, y=550)

        #database entry list box
        self.tBox = Text(master, width=45, height=30,)
        self.tBox.place(x=1100,y=80)
        self.tBox.insert(END, "ID has reached upto : " + str(id))
    
    def Search(self, *args, **kwargs):
        sql = "SELECT * FROM inventory WHERE id=?"
        result = c.execute(sql, (self.id_leb.get(), ))
        for r in result:
            self.n1 = r[1] #name
            self.n2 = r[2] #stock
            self.n3 = r[3] #cp
            self.n4 = r[4] #sp
            self.n5 = r[5] #totalcp
            self.n6 = r[6] #totalsp
            self.n7 = r[7] #assumed_profit
            self.n8 = r[8] #vender
            self.n9 = r[9] #vender_phone
        conn.commit()

        #insert into the entries to update
        self.name_e.delete(0, END)
        self.name_e.insert(0, str(self.n1))

        self.stock_e.delete(0, END)
        self.stock_e.insert(0, str(self.n2))

        self.cp_e.delete(0, END)
        self.cp_e.insert(0, str(self.n3))

        self.sp_e.delete(0, END)
        self.sp_e.insert(0, str(self.n4))

        self.totalcp_e.delete(0, END)
        self.totalcp_e.insert(0, str(self.n5))

        self.totalsp_e.delete(0, END)
        self.totalsp_e.insert(0, str(self.n6))

        self.vender_e.delete(0, END)
        self.vender_e.insert(0, str(self.n8))

        self.vender_phone_e.delete(0, END)
        self.vender_phone_e.insert(0, str(self.n9))

    def update(self, *args, **kwargs):
        # update the field's
        self.u1 = self.name_e.get()
        self.u2 = self.stock_e.get()
        self.u3 = self.cp_e.get()
        self.u4 = self.sp_e.get()
        self.u5 = self.totalcp_e.get()
        self.u6 = self.totalsp_e.get()
        self.u7 = self.vender_e.get()
        self.u8 = self.vender_phone_e.get()

        query = "UPDATE inventory SET name=?, stock=?,cp=?, sp=?, totalcp=?, totalsp=?, vender=?, vender_phoneno=? WHERE id=?"
        c.execute(query, (self.u1, self.u2, self.u3, self.u4, self.u5, self.u6, self.u7, self.u8,  self.id_leb.get()))
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Update is done database")

root = Tk()
b = Database(root)

root.geometry("1920x1080+0+0")
root.title("update the database")
root.mainloop()