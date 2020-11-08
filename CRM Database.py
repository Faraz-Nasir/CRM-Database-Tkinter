from tkinter import *
import mysql.connector
import csv#USED TO TRANSFER DATA TO EXCEL
from tkinter import ttk

root=Tk()
root.title('CRM Database')
root.geometry('400x500')

#INITALISE CONNECTION WITH MYSQL CONNECTOR
#CHECK TO SEE IF CONNECTION TO MYSQL WAS CREATED
mydb = mysql.connector.connect(
                host='localhost',
                user='root',
                passwd='root',
                database="crm_database",
        )

#Create A Cursor and initialize it

my_cursor=mydb.cursor()

#Create Database(DONE ONLY ONCE)
#my_cursor.execute("CREATE DATABASE CRM_DATABASE")

#CHECK TO SEE IF DATABASE WAS CREATED
#my_cursor.execute("SHOW DATABASES")
#for db in my_cursor:
 #       print(db)


#CREATE A TABLE(ONLY ONCE)
#my_cursor.execute("CREATE TABLE customers (first_name VARCHAR(255),last_name VARCHAR(255),zipcode INT(10),price_paid DECIMAL(10,2),user_id INT AUTO_INCREMENT PRIMARY KEY)")

#SHOW CURSOR


#ALTER TABLE
'''(USED FOR MULTILINE COMMENTS)
my_cursor.execute("""ALTER TABLE customers ADD(
        email VARCHAR(255),
        address_1 VARCHAR(255),
        address_2 VARCHAR(255),
        city VARCHAR(50),
        country VARCHAR(255),
        phone VARCHAR(255),
        payment_method VARCHAR(50),
        discount_code VARCHAR(255))"""
                  )
'''
def add_customer():
        sql_command="INSERT INTO customers (first_name,last_name,zipcode,price_paid,email,address_1,address_2,city,state,country,phone,payment_method,discount_code) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values=(first_name_box.get(),last_name_box.get(),zipcode_box.get(),price_paid_box.get(),email_box.get(),address1_box.get(),address2_box.get(),city_box.get(),state_box.get(),country_box.get(),phone_box.get(),payment_box.get(),discount_code_box.get())
        my_cursor.execute(sql_command,values)
        mydb.commit()
        clear_fields()

#WRITE TO FILE
def write_to_csv(result):
        with open('customers.csv','a',newline="") as f:
            w = csv.writer(f, dialect='excel')
            for record in result:
                w.writerow(record)


def list_customers():
        list_customer_query=Tk()
        list_customer_query.title("Database")
        list_customer_query.geometry('800x400')
        list_customer_query.resizable(0,0)


        my_cursor.execute("SELECT * from customers")
        result = my_cursor.fetchall()
        # HERE index is to enumerate and x is to result
        # enumerate is used for indexing from 0
        for index,x in enumerate(result):
                lookup_label=Label(list_customer_query,text=f'{x}\n')
                lookup_label.grid(row=index,column=0)
        csv_button=Button(list_customer_query,text="EXPORT DATA TO AN EXCEL FILE",command=lambda: write_to_csv(result))
        csv_button.grid(row=index+1,column=0)

def search_customers():
        search_customers=Tk()
        search_customers.title("Search Customers")
        search_customers.geometry('500x500')

        def search_Query():

                    searched=search_box.get()
                    sql=f'SELECT * FROM customers WHERE {order} = %s '
                    type=(searched, )
                    result=my_cursor.execute(sql,type)
                    result=my_cursor.fetchall()
                    if not result:
                            result="Record Not Found"
                    test.destroy()
                    search_label=Label(search_customers,text=result)
                    search_label.grid(row=2,column=0,padx=10)

        search_box_btn = Button(search_customers, text="Search", command=search_Query)
        search_box_btn.grid(row=1, column=1, padx=10, pady=10)

        drop = ttk.Combobox(search_customers, value=["Search By ..", "Last Name", "Email Address", "Customer Id"])
        drop.current(0)
        drop.grid(row=0, column=2)
        selected = drop.get()
        order=' '
        if selected == "Search By ..":
                test = Label(search_customers, text="Hey You Forgot To Pick A Selection")
                order = 'last_name'
                test.grid(row=3, column=0)
        if selected == "Last Name":
                test = Label(search_customers, text="Hey You Picked Last Name")
                order = 'last_name'
                test.grid(row=3, column=0)
        if selected == "Email Address":
                test = Label(search_customers, text="Hey You Picked Email Address")
                order = 'email'
                test.grid(row=3, column=0)
        if selected == "Customer Id":
                test = Label(search_customers, text="Hey You Picked Customer Id")
                order = 'oid'
                test.grid(row=3, column=0)

        # Entry Box To Search For Customers
        search_box = Entry(search_customers)
        search_box.grid(row=0, column=1, padx=10, pady=10)

        search_box_label = Label(search_customers, text="Search Customer ")
        search_box_label.grid(row=0, column=0, padx=10, pady=10)

def clear_fields():
        first_name_box.delete(0,END)
        last_name_box.delete(0, END)
        address1_box.delete(0, END)
        address2_box.delete(0, END)
        state_box.delete(0, END)
        city_box.delete(0, END)
        phone_box.delete(0, END)
        country_box.delete(0,END)
        state_box.delete(0, END)
        zipcode_box.delete(0, END)
        email_box.delete(0, END)
        username_box.delete(0, END)
        payment_box.delete(0, END)
        discount_code_box.delete(0, END)
        price_paid_box.delete(0, END)




#CREATING GRAPHS
title_label=Label(root,text="CRM DATABASE",font=("Helvetica",16))
title_label.grid(row=0,column=0,columnspan=2,pady=10)

#LABEL'S
first_name_label=Label(root,text="First Name").grid(row=1,column=0,sticky="W",padx=10)
last_name_label=Label(root,text="Last Name").grid(row=2,column=0,sticky="W",padx=10)
address1_label=Label(root,text="Address 1").grid(row=3,column=0,sticky="W",padx=10)
address2_label=Label(root,text="Address 2").grid(row=4,column=0,sticky="W",padx=10)
city_label=Label(root,text="City").grid(row=5,column=0,sticky="W",padx=10)
state_label=Label(root,text="State").grid(row=6,column=0,sticky="W",padx=10)
zipcode_label=Label(root,text="Zipcode").grid(row=7,column=0,sticky="W",padx=10)
country_label=Label(root,text="Country").grid(row=8,column=0,sticky="W",padx=10)
phone_label=Label(root,text="Phone").grid(row=9,column=0,sticky="W",padx=10)
email_label=Label(root,text="Email Address").grid(row=10,column=0,sticky="W",padx=10)
username_label=Label(root,text="Username").grid(row=11,column=0,sticky="W",padx=10)
payment_method_label=Label(root,text="Payment Method").grid(row=12,column=0,sticky="W",padx=10)
discount_code_label=Label(root,text="Discount Code").grid(row=13,column=0,sticky="W",padx=10)
price_paid_label=Label(root,text="Price Paid").grid(row=14,column=0,sticky="W",padx=10)


#CREATE ENTRY
first_name_box=Entry(root)
first_name_box.grid(row=1,column=1)

last_name_box=Entry(root)
last_name_box.grid(row=2,column=1)

address1_box=Entry(root)
address1_box.grid(row=3,column=1)

address2_box=Entry(root)
address2_box.grid(row=4,column=1)

city_box=Entry(root)
city_box.grid(row=5,column=1)

state_box=Entry(root)
state_box.grid(row=6,column=1)

zipcode_box=Entry(root)
zipcode_box.grid(row=7,column=1)

country_box=Entry(root)
country_box.grid(row=8,column=1)

phone_box=Entry(root)
phone_box.grid(row=9,column=1)

email_box=Entry(root)
email_box.grid(row=10,column=1)

username_box=Entry(root)
username_box.grid(row=11,column=1)

payment_box=Entry(root)
payment_box.grid(row=12,column=1)

discount_code_box=Entry(root)
discount_code_box.grid(row=13,column=1)

price_paid_box=Entry(root)
price_paid_box.grid(row=14,column=1)

#CREATE BUTTONS

add_customer_buttons=Button(root,text="Add customer to DataBase",command=add_customer)
add_customer_buttons.grid(row=15,column=0,padx=10,pady=10)

clear_fields_buttons=Button(root,text="Clear Fields",command=clear_fields)
clear_fields_buttons.grid(row=15,column=1,padx=10,pady=10)

list_customres_button=Button(root,text="List Customers",command=list_customers)
list_customres_button.grid(row=16,column=0,padx=10,pady=10)

search_customers_button=Button(root,text="Search Customers",command=search_customers)
search_customers_button.grid(row=16,column=1,padx=10,pady=10)



root.mainloop()