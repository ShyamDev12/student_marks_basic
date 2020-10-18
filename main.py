from tkinter import *
import pymysql
from tkinter import ttk
from tkinter import messagebox
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("STUDENTS DETAIL")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="STUDENT MARKS",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="black",fg="orange")
        title.pack(side=TOP,fill=X)

        #==============================all variable================================================================================#
        self.roll_data=StringVar()
        self.name_data=StringVar()
        self.physics_data=StringVar()
        self.chemistry_data=StringVar()
        self.maths_data=StringVar()
        self.biology_data = StringVar()
        self.english_data = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()



        #==================manage frame===============================#
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=100,width=450,height=580)

        m_title=Label(Manage_Frame,text="Manage Students",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        m_title.grid(row=0,columnspan=2,pady=10)

        rollno=Label(Manage_Frame,text="Roll No:",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        rollno.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        rolltxt=Entry(Manage_Frame,textvariable=self.roll_data,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        rolltxt.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        name = Label(Manage_Frame, text="Name:", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        nametxt = Entry(Manage_Frame,textvariable=self.name_data, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        nametxt.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        physics = Label(Manage_Frame, text="Physics:", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        physics.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        physicstxt = Entry(Manage_Frame,textvariable=self.physics_data, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        physicstxt.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        chem = Label(Manage_Frame, text="Chemistry:", bg="crimson", fg="white",font=("times new roman", 20, "bold"))
        chem.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        chemtxt = Entry(Manage_Frame,textvariable=self.chemistry_data, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        chemtxt.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        math = Label(Manage_Frame, text="Maths:", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        math.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        mathtxt = Entry(Manage_Frame,textvariable=self.maths_data, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        mathtxt.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        biology = Label(Manage_Frame, text="Biology:", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        biology.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        biologytxt = Entry(Manage_Frame, textvariable=self.biology_data, font=("times new roman", 15, "bold"), bd=5,relief=GROOVE)
        biologytxt.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        english = Label(Manage_Frame, text="English:", bg="crimson", fg="white", font=("times new roman", 20, "bold"))
        english.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        englishtxt = Entry(Manage_Frame, textvariable=self.english_data, font=("times new roman", 15, "bold"), bd=5,relief=GROOVE)
        englishtxt.grid(row=7, column=1, pady=10, padx=20, sticky="w")


    #===============buttons=================================================================================================#
        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="black")
        btn_Frame.place(x=15,y=500,width=410)

        Addbtn = Button(btn_Frame, text="Add", width=10,command=self.add_students).grid(row=0, column=0, padx=10, pady=10)
        updatebtn = Button(btn_Frame, text="Update", width=10,command=self.update_data).grid(row=0, column=1, padx=10, pady=10)
        deletebtn = Button(btn_Frame, text="Delete", width=10,command=self.delete_data).grid(row=0, column=2, padx=10, pady=10)
        clearbtn = Button(btn_Frame, text="Clear", width=10,command=self.clear).grid(row=0, column=3, padx=10, pady=10)









    #===========Detail Frame=========================================================================================#
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="black")
        Detail_Frame.place(x=500, y=100, width=800, height=580)

        search=Label(Detail_Frame,text="Search by",bg="black",fg="orange",font=("times new roman",20,"bold"))
        search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search = ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,font=("times new roman", 13, "bold"), state='readonly')
        combo_search['values'] = ("Roll_no", "Name:")
        combo_search.grid(row=0, column=1, padx=20, pady=10)

        searchtxt = Entry(Detail_Frame,textvariable=self.search_txt,width=20, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        searchtxt.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        searchbtn = Button(Detail_Frame, text="Search", width=10,pady=5,command=self.search_data).grid(row=0, column=3, padx=10, pady=10)
        showallbtn = Button(Detail_Frame, text="Show all", width=10,pady=5,command=self.fetch_data).grid(row=0, column=4, padx=10, pady=10)

    #=======================Table frame===============================================================================#
        Table_Frame =Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
        Table_Frame.place(x=10,y=70,width=760,height=500)


        scroll_x= Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y= Scrollbar(Table_Frame, orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_Frame,columns=("Roll","Name","Physics","Chemistry","Maths","Biology","English"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("Roll", text="Roll No:")
        self.Student_table.heading("Name", text="Name:")
        self.Student_table.heading("Physics", text="Physics mark:")
        self.Student_table.heading("Chemistry", text="Chemistry mark:")
        self.Student_table.heading("Maths", text="Maths mark:")
        self.Student_table.heading("Biology", text="Biology mark:")
        self.Student_table.heading("English", text="English mark:")
        self.Student_table['show']= 'headings'
        self.Student_table.column("Roll", width=100)
        self.Student_table.column("Name", width=100)
        self.Student_table.column("Physics", width=100)
        self.Student_table.column("Chemistry", width=100)
        self.Student_table.column("Maths", width=100)
        self.Student_table.column("Biology", width=100)
        self.Student_table.column("English", width=100)
        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_students(self):
        if self.roll_data.get()=="" or self.name_data.get()=="":
            messagebox.showerror("Error","All fields are required!!!")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="stm1")
            cur = con.cursor()
            cur.execute("insert into studentsmarks values(%s,%s,%s,%s,%s,%s,%s)", (self.roll_data.get(),
                                                                        self.name_data.get(),
                                                                        self.physics_data.get(),
                                                                        self.chemistry_data.get(),
                                                                        # self.maths_data.get('1.0',END)
                                                                        self.maths_data.get(),
                                                                        self.biology_data.get(),
                                                                        self.english_data.get()
                                                                        ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record has been inserted")


    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm1")
        cur = con.cursor()
        cur.execute("select * from studentsmarks")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()

    def clear(self):
        self.roll_data.set(""),
        self.name_data.set(""),
        self.physics_data.set(""),
        self.chemistry_data.set(""),
        self.maths_data.set(""),
        self.biology_data.set(""),
        self.english_data.set("")

    def get_cursor(self,ev):
        curosor_row=self.Student_table.focus()
        contents=self.Student_table.item(curosor_row)
        row=contents['values']
        self.roll_data.set(row[0]),
        self.name_data.set(row[1]),
        self.physics_data.set(row[2]),
        self.chemistry_data.set(row[3]),
        self.maths_data.set(row[4]),
        self.biology_data.set(row[5]),
        self.english_data.set(row[6])

    def update_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm1")
        cur = con.cursor()
        cur.execute("update studentsmarks set name=%s,physics=%s,chemistry=%s,maths=%s,biology=%s,english=%s where roll_no=%s",(
                                                                    self.name_data.get(),
                                                                    self.physics_data.get(),
                                                                    self.chemistry_data.get(),
                                                                    self.maths_data.get(),
                                                                    self.biology_data.get(),
                                                                    self.english_data.get(),
                                                                    self.roll_data.get()
                                                                    ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con = pymysql.connect(host="localhost",user="root",password="",database="stm1")
        cur = con.cursor()
        cur.execute("delete from studentsmarks where roll_no=%s",self.roll_data.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm1")
        cur = con.cursor()
        cur.execute("select * from studentsmarks where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()




root=Tk()
ob=Student(root)
root.mainloop()