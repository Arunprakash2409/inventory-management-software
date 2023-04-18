#main page of the project
#import modules of py tk
from tkinter import *
import sqlite3
import tkinter.messagebox
import datetime
import math
import os
import random
#access the Data Base
conn = sqlite3.connect("E:\Store Management Software\Database\store.db")
c = conn.cursor()

#date
date = datetime.datetime.now().date()

# temporary lists like sessions
products_list = []
product_price = []
product_quantity = []
product_id = []

#list for labels
labels_list = []
class Application:
    def __init__(self, master, *args, **kwargs):

        self.master = master
        # frames
        #stock on the view 
        self.left = Frame(master, width=950, height=1080, bg='white')
        self.left.pack(side=LEFT)
        #detiles view in the right
        self.right = Frame(master, width=920, height=1080, bg='lightblue')
        self.right.pack(side=RIGHT)

        #componts
        #titiles of the store 
        self.hending = Label(self.left, text="Arun mobile  Store", font=('arial 40 bold'), bg='white', fg='red')
        self.hending.place(x=230, y=0)
        #current Date 
        self.date_1 = Label(self.right, text="Today's date : " + str(date), font=('arial 20 bold'), bg='lightblue', fg='black')
        self.date_1.place(x=0, y=0)

        #tabel invoice======================================
        self.tproduct = Label(self.right, text="PRODUCT", font=('arial 15  bold'), bg='lightblue', fg='black')
        self.tproduct.place(x=0, y=60)

        self.tquantity = Label(self.right, text="QUANTITY", font=('arial 15  bold'), bg='lightblue', fg='black')
        self.tquantity.place(x=200, y=60)

        self.tamount = Label(self.right, text="AMOUNT", font=('arial 15  bold'), bg='lightblue', fg='black')
        self.tamount.place(x=400, y=60)

        #entery stuff
        self.enterid = Label(self.left, text="Enter the product's ID : ", font=('arial 18 bold'), bg='white')
        self.enterid.place(x=0, y=100)

        self.enteride = Entry(self.left, width= 30 , font=('arial 18 bold'), bg='lightblue')
        self.enteride.place(x=300, y=100)
        self.enteride.focus()
        #button
        self.search_btn = Button(self.left, text="Search", width=30, height=2, bg='orange', command=self.ajax)
        self.search_btn.place(x=700, y=150)

        #fill it letter by the function ajax
        self.productname = Label(self.left, text="", font=('arial 25 bold'), bg='white', fg='steelblue')
        self.productname.place(x=0, y=250)

        self.pprice = Label(self.left, text="", font=('arial 25 bold'), bg='white', fg='steelblue')
        self.pprice.place(x=0, y=300)
        #total lable
        self.total_l = Label(self.right, text="", font=('arial 25 bold'), bg='lightblue', fg='black')
        self.total_l.place(x=0, y=600)

        self.master.bind("<Return>", self.ajax)
        self.master.bind("<Up>", self.add_to_cart)
        self.master.bind("<space>", self.generate_bill)
    def ajax(self, *args, **kwargs):
        self.get_id = self.enteride.get()
        #get the product info with that id and fill in the labels above
        query = "SELECT * FROM inventory WHERE id=?"
        result = c.execute(query, (self.get_id, ))
        for self.r in result:
            self.get_id = self.r[0]
            self.get_name = self.r[1]
            self.get_price = self.r[4]
            self.get_stock = self.r[2]
            self.productname.configure(text="product's name :    " + str(self.get_name))
            self.pprice.configure(text="price's_RS         :    " + str(self.get_price))

        #create the quantity and the discount lable
        self.quantity_l = Label(self.left, text="Enter Quantity", font=('arial 18 bold'), bg='white')
        self.quantity_l.place(x=50, y=400)

        self.quantity_e = Entry(self.left, width=25, font=('arial 18 bold'), bg='lightblue')
        self.quantity_e.place(x=350, y=400)
        self.quantity_e.focus()
        #discount
        self.discount_l = Label(self.left, text="Discount", font=('arial 18 bold'), bg='white')
        self.discount_l.place(x=50, y=470)

        self.discount_e = Entry(self.left, width=25, font=('arial 18 bold'), bg='lightblue')
        self.discount_e.place(x=350, y=470)
        self.discount_e.insert(END, 0)
        #Button

        self.add_to_cart_btn = Button(self.left, text="add to card", width=30, height=2, bg='orange', command=self.add_to_cart)
        self.add_to_cart_btn.place(x=700, y=530)

        #generte bill and change
        self.change_l = Label(self.left, text="Amount given", font=('arial 18 bold'), bg='white')
        self.change_l.place(x=50, y=600)

        self.change_e = Entry(self.left, width=25, font=('arial 18 bold'), bg='lightblue')
        self.change_e.place(x=350, y=600)

        self.change_btn = Button(self.left, text="blance to give", width=30, height=2, bg='orange', command=self.change_func)
        self.change_btn.place(x=700, y=650)

        #Generate bill button
        self.bill_btn = Button(self.left, text="-BILL-", width=60, height=2, bg='orange', command=self.generate_bill)
        self.bill_btn.place(x=500, y=720)

    def add_to_cart(self, *args, **kwargs):
        #get the quqntity value and from the database
        self.quantity_value = int(self.quantity_e.get())
        if self.quantity_value > int(self.get_stock):
            tkinter.messagebox.showinfo("Error", "Not that many products in our inventory.")
        else:
            #calculate the price
            self.final_price = (float(self.quantity_value) * float(self.get_price)) - (float(self.discount_e.get()))
            
            products_list.append(self.get_name)
            product_price.append(self.final_price)
            product_quantity.append(self.quantity_value)
            product_id.append(self.get_id)

            self.x_index = 0
            self.y_index = 100
            self.counter = 0
            for self.p in products_list:
                self.tempname = Label(self.right, text=str(products_list[self.counter]), font=('arial 18 bold'), bg='lightblue', fg='black')
                self.tempname.place(x=0, y=self.y_index)
                labels_list.append(self.tempname)

                self.tempqt = Label(self.right, text=str(product_quantity[self.counter]), font=('arial 18 bold'), bg='lightblue', fg='black')
                self.tempqt.place(x=300, y=self.y_index)
                labels_list.append(self.tempqt)

                self.tempprice = Label(self.right, text=str(product_price[self.counter]), font=('arial 18 bold'), bg='lightblue', fg='black')
                self.tempprice.place(x=400, y=self.y_index)
                labels_list.append(self.tempprice)

                self.y_index +=40
                self.counter +=1

                #total configure
                self.total_l.configure(text="Total: Rs." + str(sum(product_price)))

                #delete
                self.quantity_l.place_forget()
                self.quantity_e.place_forget()
                self.discount_l.place_forget()
                self.discount_e.place_forget()
                self.productname.configure(text="")
                self.pprice.configure(text="")
                self.add_to_cart_btn.destroy()

                #autofocus to the enter id
                self.enteride.focus()
                self.enteride.delete(0, END)
    def change_func(self, *args, **kwargs):
        #get the amount gives by the customer and the amount by the computer
        self.amount_given = float(self.change_e.get())
        self.our_total = float(sum(product_price))

        self.to_give = self.amount_given - self.our_total

        #lable
        self.c_amount = Label(self.left, text="Change: Rs. " + str(self.to_give), font=('arial 18 bold'), fg='red', bg='white')
        self.c_amount.place(x=0, y=650)

    def generate_bill(self, *args, **kwargs):
        #create the bill before updating to the database
        directory = "E:/Store Management Software/invoice/" + str(date) + "/"
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Templates for the Bill
        company = "\t\t\t\tArun mobile store\n"
        address = "\t\t\t\tAt Palani\n"
        phone = "\t\t\t\t9080068664\n"
        sample = "\t\t\t\tInvoice\n"
        dt = "\t\t\t\t" + str(date)

        table_header = "\n\n\t\t-------------------------------------\n\t\tSN.\tproduct\tqty\tAmount\n\n\t\t-------------------------------------\n"
        final = company + address + phone + sample + dt + "\n" + table_header
        
        #open a file to write it to
        file_name = str(directory) + str(random.randrange(5000, 10000)) + ".rtf"
        f = open(file_name, 'w')
        f.write(final)
        # fill dynamics
        r = 1
        i = 0
        for t in products_list:
            f.write("\n\t\t" + str(r) + "\t" + str(products_list[i] +"      ")[:7] + "\t" + str(product_quantity[i]) + "\t" + str(product_price[i]))
            i += 1
            r += 1
        f.write("\n\n\t\tTotal : Rs." + str(sum(product_price)))
        f.write("\n\n\t\t\tThanks for Visiting.")
        os.startfile(file_name, "print")
        f.close()
        # decrease the stock
        self.x = 0
        
        initial = "SELECT * FROM inventory WHERE id=?"
        result = c.execute(initial, (product_id[self.x], ))
        
        for i in products_list:
            for r in result:
                self.old_stock = r[2]
            self.new_stock = int(self.old_stock) - int(product_quantity[self.x])

            #updating the stock
            sql = "UPDATE inventory SET stock=? WHERE id=?"
            c.execute(sql, (self.new_stock, product_id[self.x]))
            conn.commit()

            #insert into the transaction
            sql2 = "INSERT INTO transactions (product_name, quantity, amount, date) VALUES (?, ?, ?, ?)"
            c.execute(sql2, (products_list[self.x], product_quantity[self.x], product_price[self.x], date))
            conn.commit()

            self.x +=1

            for a in labels_list:
                a.destroy()

            del(products_list[:])
            del(product_id[:])
            del(product_quantity[:])
            del(product_price[:])
        
        self.total_l.configure(text="")
        self.c_amount.configure(text="")
        self.change_e.delete(0, END)
        self.enteride.focus()
        tkinter.messagebox.showinfo("Success", "Done everything smoothly")

root = Tk()
b = Application(root)

root.geometry("1920x1080+0+0")

root.mainloop()