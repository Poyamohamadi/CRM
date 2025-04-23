import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

class MyApp(tk.Tk):
    count:int = int()
    sql = "data" + ".db"

    def __init__(self):
        super(MyApp,self).__init__()
        self.Root()
        self.notexists()
        self.query_database()
        self.mainloop() # Run the MyApp's Main Loop

    def Root(self):
        self.window(
            title="CRM - Poyamohamadi",
            size_x="1000",size_y="550",)
        self.menu()
        self.table()
        self.entry()
        self.buttons()
        
    def window(self,title:str,size_x:str,size_y:str):
        '''Define Window'''
        self.title(title)
        self.geometry(f"{size_x}x{size_y}")
        self.resizable(False,False)
    
    def menu(self):
        '''Define Menu'''
        main_menu = tk.Menu(self)
        self.config(menu=main_menu)
        
        search_menu = tk.Menu(main_menu, tearoff=0)
        main_menu.add_cascade(label= 'ابزار',menu=search_menu)

        search_menu.add_command(
            label='جستجو',
            command=self.lookup)
        search_menu.add_separator()
        search_menu.add_command(
            label="تازه سازی جدول",
            command=self.query_database)
    
    def table(self):
        tree_frame = tk.Frame(self); tree_frame.pack(pady=10)
        tree_scroll = tk.Scrollbar(self)
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.my_tree = ttk.Treeview(self, yscrollcommand= tree_scroll.set, selectmode="browse")
        self.my_tree.pack()
        self.my_tree['columns'] = ("ZipCode","Address", "City", "State","Last Name","First Name","ID","oid")
        
        tree_scroll.config(command= self.my_tree.yview)
        
        self.my_tree.column("#0", width=0, stretch=tk.NO)
        self.my_tree.column("oid", width=0, stretch=tk.NO)
        self.my_tree.column("ID", anchor=tk.CENTER, width=100)
        self.my_tree.column("First Name", anchor=tk.E, width=140)
        self.my_tree.column("Last Name", anchor=tk.E, width=140)
        self.my_tree.column("State", anchor=tk.CENTER, width=140)
        self.my_tree.column("City", anchor=tk.CENTER, width=140)
        self.my_tree.column("Address", anchor=tk.CENTER, width=140)
        self.my_tree.column("ZipCode", anchor=tk.CENTER, width=140)

        self.my_tree.heading("#0", text="", anchor=tk.W)
        self.my_tree.heading("oid", text="", anchor=tk.W)
        self.my_tree.heading("ID", text="کد ملی", anchor=tk.CENTER)
        self.my_tree.heading("First Name", text="نام", anchor=tk.E)
        self.my_tree.heading("Last Name", text="نام خانوادگی", anchor=tk.E)
        self.my_tree.heading("State", text="استان", anchor=tk.CENTER)
        self.my_tree.heading("City", text="شهر", anchor=tk.CENTER)
        self.my_tree.heading("Address", text="آدرس", anchor=tk.CENTER)
        self.my_tree.heading("ZipCode", text="کد پستی", anchor=tk.CENTER)

        self.my_tree.bind("<<TreeviewSelect>>",self.select)

    def entry(self):
        data_frame = tk.LabelFrame(self, text="بخش ثبت / ویرایش",labelanchor= tk.NE)
        data_frame.pack(fill="x", expand="yes", padx=20)
        
        fn_label = tk.Label(data_frame, text="نام")
        fn_label.grid(row=0, column=7, padx=10, pady=10)
        self.fn_entry = tk.Entry(data_frame,justify=tk.RIGHT)
        self.fn_entry.grid(row=0, column=6, padx=10, pady=10)

        ln_label = tk.Label(data_frame, text="نام خانوادگی")
        ln_label.grid(row=1, column=7, padx=10, pady=10)
        self.ln_entry = tk.Entry(data_frame,justify=tk.RIGHT,)
        self.ln_entry.grid(row=1, column=6, padx=10, pady=10)

        id_label = tk.Label(data_frame, text= "کد ملی")
        id_label.grid(row=0, column=5, padx=10, pady=10)
        self.id_entry = tk.Entry(data_frame)
        self.id_entry.grid(row=0, column=4, padx=10, pady=10)

        address_label = tk.Label(data_frame, text="آدرس")
        address_label.grid(row=1, column=5, padx=10, pady=10)
        self.address_entry = tk.Entry(data_frame,justify=tk.RIGHT)
        self.address_entry.grid(row=1, column=4, padx=10, pady=10)

        city_label = tk.Label(data_frame, text="شهر")
        city_label.grid(row=0, column=3, padx=10, pady=10)
        self.city_entry = tk.Entry(data_frame,justify=tk.RIGHT)
        self.city_entry.grid(row=0, column=2, padx=10, pady=10)

        state_label = tk.Label(data_frame, text="استان")
        state_label.grid(row=1, column=3, padx=10, pady=10)
        self.state_entry = tk.Entry(data_frame,justify=tk.RIGHT)
        self.state_entry.grid(row=1, column=2, padx=10, pady=10)

        zip_label = tk.Label(data_frame, text="کد پستی")
        zip_label.grid(row=1, column=1, padx=10, pady=10)
        self.zip_entry = tk.Entry(data_frame)
        self.zip_entry.grid(row=1, column=0, padx=10, pady=10)
    
    def buttons(self):
        button_frame = tk.LabelFrame(self, text="بخش عملیات ها",labelanchor= tk.NE)
        button_frame.pack(fill="x", expand="yes", padx=20)

        update_button = tk.Button(button_frame, text="ایجاد ویرایش",command=self.update)
        update_button.grid(row=0, column=0, padx=10, pady=10)

        add_button = tk.Button(button_frame, text="افزودن",command=self.add)
        add_button.grid(row=0, column=1, padx=10, pady=10)

        remove_all_button = tk.Button(button_frame, text="پاک کردن جدول",command=self.remove_all )
        remove_all_button.grid(row=0, column=2, padx=10, pady=10)

        remove_many_button = tk.Button(button_frame, text="حذف",command=self.remove )
        remove_many_button.grid(row=0, column=4, padx=10, pady=10)

        move_up_button = tk.Button(button_frame, text="انتقال به بالا",command=self.up)
        move_up_button.grid(row=0, column=5, padx=10, pady=10)

        move_down_button = tk.Button(button_frame, text="انتقال به پایین",command=self.down)
        move_down_button.grid(row=0, column=6, padx=10, pady=10)

        select_record_button = tk.Button(button_frame, text="پاک کردن بخش ثبت / ویرایش",command=self.clear_entries)
        select_record_button.grid(row=0, column=7, padx=10, pady=10)
    
# ------------------------ Define Function --------------------------------
    def notexists(self):
        conn = sqlite3.connect(self.sql)

        c = conn.cursor()
        c.execute(""" 
                CREATE TABLE if not exists customers (
                    first_name text,
                    last_name text,
                    id integer,
                    address text,
                    city text,
                    state text,
                    zipcode text,
                    oid integer)
                """)
        conn.commit()
        conn.close()

    def select(self,event):
        self.fn_entry.delete(0, 'end')
        self.ln_entry.delete(0, 'end')
        self.id_entry.delete(0, 'end')
        self.address_entry.delete(0, 'end')
        self.city_entry.delete(0, 'end')
        self.state_entry.delete(0, 'end')
        self.zip_entry.delete(0, 'end')

        selected = self.my_tree.focus()
        values = self.my_tree.item(selected, 'values')
        try:
            self.fn_entry.insert(0, values[5])
            self.ln_entry.insert(0, values[4])
            self.id_entry.insert(0, values[6])
            self.address_entry.insert(0, values[1])
            self.city_entry.insert(0, values[2])
            self.state_entry.insert(0, values[3])
            self.zip_entry.insert(0, values[0])
        except :
            pass

    def lookup(self):
        self.search = tk.Toplevel(self)
        self.search.title("جستجو")
        self.search.geometry("400x200")
        values = ["نام","نام خانوادگی","کد ملی","آدرس","شهر","استان","کد پستی"]
        option = ttk.Combobox(self.search,values=values,justify=tk.CENTER)
        option.set("نام") ; option.pack(pady=(10,1))

        dict_value:dict = {"نام":"first_name",
                        "نام خانوادگی":"last_name",
                        "کد ملی":"id","آدرس":"address",
                        "شهر":"city","استان":"state","کد پستی":"zipcode"}
                        
        search_frame = tk.LabelFrame(self.search, text="جستجو",labelanchor= tk.NE)
        search_frame.pack(padx=10, pady=10)
        
        self.search_entry = tk.Entry(search_frame, font=("Helvetica", 16),justify=tk.CENTER)
        self.search_entry.pack(padx=20, pady=20)
        
        def search(value):
            lookup= self.search_entry.get()
            self.search.destroy()
        
            for record in self.my_tree.get_children():
                self.my_tree.delete(record)
            
            conn = sqlite3.connect(self.sql)
            c = conn.cursor()
            
            c.execute(f"SELECT rowid, * FROM customers WHERE {value} like ?", (lookup,))
            records = c.fetchall()
            
            for record in records: 
                self.my_tree.insert(parent='', index='end', text='', value=(record[7],record[4],record[5],record[6],record[2],record[1],record[3]))
            
            conn.commit()
            conn.close()
            
        search_button = tk.Button(self.search, text="جستجو",command=lambda :search(dict_value[option.get()]))
        search_button.pack(padx=20, pady=20)

    def query_database(self):
            for record in self.my_tree.get_children():
                self.my_tree.delete(record)
            
            conn = sqlite3.connect(self.sql)

            c = conn.cursor()
            c.execute("SELECT rowid, * FROM customers")
            records = c.fetchall()

            for record in records: 
                self.my_tree.insert(parent='', index='end', text='', value=(record[7],record[4],record[5],record[6],record[2],record[1],record[3],record[-1]))
                
            conn.commit()
            conn.close()
    
    def update(self):
        try:
            selected = self.my_tree.focus()
            values = []
            loop_values = [self.zip_entry.get(),self.address_entry.get(), self.city_entry.get(), self.state_entry.get(),self.ln_entry.get(),self.fn_entry.get(), self.id_entry.get()]
            _id = []
            for row in self.my_tree.get_children():
                _id.append(self.my_tree.item(row,'values')[-2])
            try:
                _id.remove(self.id_entry.get())
            except:pass
            if self.id_entry.get() in _id:
                raise ValueError

            for num,value in enumerate(loop_values):
                if value != '' and not value.isspace():
                    values.append(value)
                else:
                    values.append(self.my_tree.item(selected)['values'][num])

            count = self.my_tree.item(selected)['values'][-1]   
            self.my_tree.item(selected, text='', values=( values[0],values[1],values[2],values[3],values[4],values[5],values[-1]))
            
            conn = sqlite3.connect(self.sql)
            c = conn.cursor()
        
            c.execute(""" 
                    UPDATE customers SET
                    
                    first_name = :first,
                    last_name = :last,
                    address = :address,
                    city = :city,
                    state = :state,
                    zipcode = :zipcode,
                    id = :id
                    
                    WHERE oid = :oid """, 

                    {   
                        'first': self.my_tree.item(selected)['values'][5],
                        'last' : self.my_tree.item(selected)["values"][4],
                        'id': self.my_tree.item(selected)["values"][6],
                        'oid': count,
                        'address': self.my_tree.item(selected)["values"][1],
                        'city': self.my_tree.item(selected)["values"][2],
                        'state': self.my_tree.item(selected)["values"][3],
                        'zipcode': self.my_tree.item(selected)["values"][0],
                    } )

            conn.commit()
            conn.close()
            
            self.fn_entry.delete(0, 'end')
            self.ln_entry.delete(0, 'end')
            self.id_entry.delete(0, 'end')
            self.address_entry.delete(0, 'end')
            self.city_entry.delete(0, 'end')
            self.state_entry.delete(0, 'end')
            self.zip_entry.delete(0, 'end')
        except:pass

    def add(self):
        try:
            conn = sqlite3.connect(self.sql)
    
            if self.fn_entry.get() == '':
                messagebox.showerror("اخطار",'شما نام را وارد نکردید')
                raise ValueError
            if self.ln_entry.get() == '':
                messagebox.showerror("اخطار",'شما نام خانوادگی را وارد نکردید')
                raise ValueError
            if self.id_entry.get() == '':
                messagebox.showerror("اخطار",'شما کد ملی را وارد نکردید')
                raise ValueError            
            
            c = conn.cursor()
            c.execute("SELECT rowid, * FROM customers")
            records = c.fetchall()
            
            _id = []
            for row in self.my_tree.get_children():
                _id.append(self.my_tree.item(row,'values')[-2])

            if self.id_entry.get() in _id:
                raise ValueError
            list_oid = []
            for record in records:
                list_oid.append(int(record[-1]))
            self.count += 1
            while self.count in list_oid:
                self.count += 1
            else:
                self.count

            c.execute("INSERT INTO customers VALUES (:first, :last, :id, :address, :city, :state, :zipcode ,:oid)", 
                    {   'first': self.fn_entry.get(),
                        'last' : self.ln_entry.get(),
                        'id': self.id_entry.get(),
                        'address': self.address_entry.get(),
                        'city': self.city_entry.get(),
                        'state': self.state_entry.get(),
                        'zipcode': self.zip_entry.get(),
                        'oid': self.count
                    })
            
            conn.commit()

            conn.close()
            
            self.fn_entry.delete(0, 'end')
            self.ln_entry.delete(0, 'end')
            self.id_entry.delete(0, 'end')
            self.address_entry.delete(0, 'end')
            self.city_entry.delete(0, 'end')
            self.state_entry.delete(0, 'end')
            self.zip_entry.delete(0, 'end')
        
            #self.my_tree.delete(*self.my_tree.get_children())
            self.query_database()
        except ValueError:
            pass

    def remove_all(self):
        response = messagebox.askyesno("اخطار", "آیا مطمئن هستید که میخواهید همه چیز را پاک کنید؟")
        if response == 1:
            for record in self.my_tree.get_children():
                self.my_tree.delete(record)
                
            conn = sqlite3.connect(self.sql)

            c = conn.cursor()
            c.execute("DROP TABLE customers")
                
            conn.commit()
            conn.close()

            self.clear_entries()

            def create_table_again():
                conn = sqlite3.connect(self.sql)

                c = conn.cursor()
                c.execute(""" 
                        CREATE TABLE if not exists customers (
                            first_name text,
                            last_name text,
                            id integer,
                            address text,
                            city text,
                            state text,
                            zipcode text,
                            oid integer)
                        """)

                conn.commit()
                conn.close()
            create_table_again()
            
    def remove(self):
        response = messagebox.askyesno("اخطار", "آیا مطمئن هستید که میخواهید مورد انتخاب شده را حذف کنید؟")
        if response == 1:
            x = self.my_tree.selection()

            id_to_delete = self.my_tree.item(x, 'values')[-1]
            
            self.my_tree.delete(x)
            
            conn = sqlite3.connect(self.sql)

            c = conn.cursor()
            c.executemany("DELETE FROM customers WHERE oid = ?", id_to_delete )
        
            conn.commit()
            conn.close()
    
            self.clear_entries()

    def up(self):
        try:
            row = self.my_tree.selection()[0]
            down = self.my_tree.item(row,"values")
            up = self.my_tree.item(row[:-1]+str(int(row[-1])-1),"values")

            conn = sqlite3.connect(self.sql)
            c = conn.cursor()
            c.execute("""UPDATE customers SET
                    
                    first_name = :first,
                    last_name = :last,
                    address = :address,
                    city = :city,
                    state = :state,
                    zipcode = :zipcode,
                    id = :id
                    
                    WHERE oid = :oid """,{"first":down[-3],"last":down[-4],
                    "address":down[1],"city":down[2],"state":down[3],
                    "zipcode":down[0],"id":down[-2],"oid":up[-1]})

            c.execute("""UPDATE customers SET
                    
                    first_name = :first,
                    last_name = :last,
                    address = :address,
                    city = :city,
                    state = :state,
                    zipcode = :zipcode,
                    id = :id
                    
                    WHERE oid = :oid """,{"first":up[-3],"last":up[-4],
                    "address":up[1],"city":up[2],"state":up[3],
                    "zipcode":up[0],"id": up[-2],"oid":down[-1]})
                    
            conn.commit()
            conn.close()

            self.my_tree.move(row, self.my_tree.parent(row), self.my_tree.index(row)-1)
        except:pass

    def down(self):
        try:
            row = self.my_tree.selection()[0]
            up = self.my_tree.item(row,"values")
            down = self.my_tree.item(row[:-1]+str(int(row[-1])+1),"values")

            conn = sqlite3.connect(self.sql)
            c = conn.cursor()
            c.execute("""UPDATE customers SET
                    
                    first_name = :first,
                    last_name = :last,
                    address = :address,
                    city = :city,
                    state = :state,
                    zipcode = :zipcode,
                    id = :id
                    
                    WHERE oid = :oid """,{"first":down[-3],"last":down[-4],
                    "address":down[1],"city":down[2],"state":down[3],
                    "zipcode":down[0],"id":down[-2],"oid":up[-1]})

            c.execute("""UPDATE customers SET
                    
                    first_name = :first,
                    last_name = :last,
                    address = :address,
                    city = :city,
                    state = :state,
                    zipcode = :zipcode,
                    id = :id
                    
                    WHERE oid = :oid """,{"first":up[-3],"last":up[-4],
                    "address":up[1],"city":up[2],"state":up[3],
                    "zipcode":up[0],"id": up[-2],"oid":down[-1]})

            conn.commit()
            conn.close()
            self.my_tree.move(row, self.my_tree.parent(row), self.my_tree.index(row)+1)
        except:pass

    def clear_entries(self):
        self.fn_entry.delete(0,'end'); self.ln_entry.delete(0,'end'); self.id_entry.delete(0,'end')
        self.address_entry.delete(0,'end'); self.city_entry.delete(0,'end')
        self.state_entry.delete(0,'end'); self.zip_entry.delete(0,'end')

if __name__ == "__main__":
    MyApp()
