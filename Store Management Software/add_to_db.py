#import modules of py tk
from tkinter import *
import sqlite3
import tkinter.messagebox

# to add the data  into the DataBase
conn = sqlite3.connect("E:\Store Management Software\Database\store.db")
c = conn.cursor()

result = c.execute("SELECT max(id) from inventory")
for r in result:
    id = r[0]
class Database:
    def __init__(self, master, *args, **kwargs):

        self.master = master
        self.heading = Label(master, text="Add to the database", font=('arial 40 bold'), fg='steelblue')
        self.heading.place(x=500,y=0)

       
        #labels of product detils on window
        # to display name's
        #Name of product
        self.name_l = Label(master,text="Enter product Name", font=('arial 18 bold'))
        self.name_l.place(x=0, y=100)
        #Stock detils
        self.stock_l = Label(master,text="No of Stock", font=('arial 18 bold'))
        self.stock_l.place(x=0, y=150)
        #cp
        self.cp_l = Label(master,text="Cost price", font=('arial 18 bold'))
        self.cp_l.place(x=0, y=200)
        #Sp
        self.sp_l = Label(master,text="Selling price", font=('arial 18 bold'))
        self.sp_l.place(x=0, y=250)
        #vender
        self.vender_l = Label(master,text="vender Name", font=('arial 18 bold'))
        self.vender_l.place(x=0, y=300)
        #vender phone number
        self.vender_phone_l = Label(master,text="Vender phone Number", font=('arial 18 bold'))
        self.vender_phone_l.place(x=0, y=350)
        #product id
        self.id_l = Label(master,text="Enter product ID", font=('arial 18 bold'))
        self.id_l.place(x=0, y=400)

        #entry box for the labels
        #to create text box
        #for name of the product
        self.name_e = Entry(master, width=25, font=('arial 18 bold'))
        self.name_e.place(x=400, y=100)
        #for stock Detiles
        self.stock_e = Entry(master, width=25, font=('arial 18 bold'))
        self.stock_e.place(x=400, y=150)
        #for cost price
        self.cp_e = Entry(master, width=25, font=('arial 18 bold'))
        self.cp_e.place(x=400, y=200)
        #for selling price
        self.sp_e = Entry(master, width=25, font=('arial 18 bold'))
        self.sp_e.place(x=400, y=250)
        #for vender Name
        self.vender_e = Entry(master, width=25, font=('arial 18 bold'))
        self.vender_e.place(x=400, y=300)
        #for vender phone number
        self.vender_phone_e = Entry(master, width=25, font=('arial 18 bold'))
        self.vender_phone_e.place(x=400, y=350)
        #for product ID
        self.id_e = Entry(master, width=25, font=('arial 18 bold'))
        self.id_e.place(x=400, y=400)

        #button for save data in to the database
        #for clear the all detiles enter in the text Box
        self.btn_clear = Button(master, text="Clear all Fields", width=25, height=2, bg='steelblue', fg='white', command=self.clear_all)
        self.btn_clear.place(x=399, y=460)
        #Add the data into the Data Base
        self.btn_add = Button(master, text="Add to Database", width=25, height=2, bg='steelblue', fg='white', command=self.get_items)
        self.btn_add.place(x=599, y=460)

        #database entry list box
        #To show how many data is entered in the Data Base
        self.tBox = Text(master, width=45, height=30,)
        self.tBox.place(x=1100,y=80)
        self.tBox.insert(END, "ID has reached upto : " + str(id))

        self.master.bind('<Return>', self.get_items)
        self.master.bind('<Up>', self.clear_all)
    def get_items(self, *args, **kwargs):
        #get from entries
        self.name = self.name_e.get()
        self.stock = self.stock_e.get()
        self.cp = self.cp_e.get()
        self.sp = self.sp_e.get()
        self.vender = self.vender_e.get()
        self.vender_phone = self.vender_phone_e.get()
        self.totalcp = float(self.cp) * float(self.stock)
        self.totalsp = float(self.sp) * float(self.stock)
        self.assumed_profit = float(self.totalsp - self.totalcp)

        self.id = self.id_e.get()
        
        #checking 

        if self.name == '' or self.stock == '' or self.cp == '' or self.sp == '' or self.id =='':
            tkinter.messagebox.showinfo("Error", "Please Fill All The Box")
        else:
            sql = "INSERT INTO inventory (name, stock, cp, sp, totalcp, totalsp, assumed_profit, vender, vender_phoneno, id) VALUES(?,?,?,?,?,?,?,?,?,?)"
            c.execute(sql, (self.name, self.stock, self.cp, self.sp, self.totalcp, self.totalsp, self.assumed_profit, self.vender, self.vender_phone, self.id))
            conn.commit()
            
            self.tBox.insert(END, "\n\nInseted " + str(self.name) + " into the database with id no : " + str(self.id_e.get()))
            
            tkinter.messagebox.showinfo("Success", "Successfully added to the database")
    
    def clear_all(self, *args, **kwargs):
        
        self.name_e.delete(0, END)
        self.stock_e.delete(0, END)
        self.cp_e.delete(0, END)
        self.sp_e.delete(0, END)
        self.vender_e.delete(0, END)
        self.vender_phone_e.delete(0, END)
        self.id_e.delete(0, END)
        

root = Tk()
b = Database(root)
#size of the display the output
root.geometry("1920x1080+0+0")
root.title("Add to the database")
root.mainloop()