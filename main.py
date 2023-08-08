from tkinter import *
from path_relative import *
from tkinter import messagebox as m
import csv
from tkinter import ttk
import re
import ast
from functools import partial
from tkinter import messagebox as mbox
import tkinter.font as font

#unoccupied houses display
def search():
    global house
    house=[]
    class unonode:
        def __init__(self,fno=None,price=None,bhk=None,status=None,contact=None,type=None,next=None):
            self._fno=fno
            self._price=price
            self._bhk=bhk
            self._status=status
            self._contact=contact
            self._type=type
            self._next=next
    class unoccupied:#class
        def __init__(self):
            self._head=unonode()
            pos=self._head
            with open('unoccupied_final.csv',"r") as csvfile:
                data=csv.reader(csvfile,delimiter=",")
                for i in data:
                  if not i:
                    pass
                  else:
                    pos._next=unonode(i[0],i[1],i[2],i[3],i[4],i[5],pos._next)
                    pos=pos._next
        def display(self):
            pos=self._head
            s=''
            l=[]
            
            
            while pos._next is not None:
                s='Flat no.: '+ pos._next._fno+"   "+'Price: '+pos._next._price+"\n"+pos._next._bhk+"    "+pos._next._status+"   "+" Contact number: "+pos._next._contact+"   "+pos._next._type.capitalize()+'\n' 
                l.append(s)  
                global house
                house.append(pos._next._fno)
                pos=pos._next
            return l
        def link_delete(self,flat):
            pos=self._head
            while pos._next is not None:
                if pos._next._fno==flat:
                    pos._next=pos._next._next
                    break
                pos=pos._next
        def delete(self,flat):
            import csv
            data=[]
            with open('unoccupied_final.csv', 'r') as file:
                for row in csv.reader(file):
                  data.append(row)
            with open('unoccupied_final.csv', 'w') as file1:
               writer = csv.writer(file1)
               for i in data: 
                if not i:
                    pass
                else:
                 if i[0]!= flat:
                    writer.writerow(i)

 

    def sign():
        win = Toplevel(root)
        win.geometry("1200x900")
        win.title("SIGN UP")

        global regex
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        def check(email):
         if(re.fullmatch(regex, email)):
            return True
         else:
            return False
        def sign_up():
                if entry_1.get()=='' or entry_2.get()=='' or entry_3.get()=='' or entry_4.get()=='':
                    m.showerror("Error","All fields are mandatory")
                else:
                    if entry_1.get() not in house:
                        m.showerror("Error","Enter valid Flat number")
                        sign()
                    elif  not (entry_4.get().isdigit()) or len(entry_4.get())<10 :
                        m.showerror("Error","Enter valid Mobile number")
                        sign()
                    elif not (check(entry_3.get())):
                        m.showerror("Error","Enter valid Email id")
                        sign()
                    elif not(entry_2.get().isalpha()):
                        m.showerror("Error","Name must be alphabets")
                        sign()
                    else:
                        new= Toplevel(win)
                        new.geometry("1200x900")
                        new.title("BOOKING")
                        image_back = PhotoImage(file=relative_to_assets("thank.png"))
                        l = Label(new,image=image_back)
                        l.place(x=0,y=0)
                        user=Label(new,text=entry_1.get(),font=('Helvetica',19))
                        user.place(x=822,y=565)
                        import random
                        import string
                        # get random string of letters and digits
                        source = string.ascii_letters + string.digits
                        result_str = ''.join((random.choice(source) for i in range(6)))
                        pass_w=result_str
                        passw=Label(new,text=pass_w,font=('Helvetica',19))
                        passw.place(x=822,y=619.5)
                        flat_no=entry_1.get()
                        unc=unoccupied()
                        unc.link_delete(str(flat_no))
                        unc.delete(str(flat_no))
                        f=open("user_details.txt","a")
                        line=str(flat_no)+','+str(entry_2.get())+','+str(entry_4.get())+','+str(pass_w)+','+'To be occupied'+','+str(entry_3.get())+'\n'
                        f.write(line)
                        f.close()
                        new.mainloop() 
                        #entry_1 is flat no.
                        #entry_2 is name
                        #entry_3 is email
                        #entry_4 is contact no.
                       
                    

        image_background = PhotoImage(
        file=relative_to_assets("BG.png"))

        label = Label(
        win,
        image=image_background
    )
        label.place(x=0, y=0)

        entry_1 = Entry(win,
                bd=0,
                bg="#D9D9D9",
                highlightthickness=0,
                fg="black",
                font=("Courier","18")
            )
        entry_1.place(
                x=735.0,
                y=258.0,
                width=387.0,
                height=52.0
            )
            
        entry_2 = Entry(win,
                bd=0,
                bg="#D9D9D9",
                highlightthickness=0,
                fg="black",
                font=("Courier","18")
            )
        entry_2.place(
                x=735.0,
                y=362.0,
                width=387.0,
                height=52.0
            )

        entry_3 = Entry(win,
                bd=0,
                bg="#D9D9D9",
                highlightthickness=0,
                fg="black",
                font=("Courier","16")
    )
        entry_3.place(
                x=735.0,
                y=470.0,
                width=387.0,
                height=52.0
            )

        entry_4 = Entry(win,
                bd=0,
                bg="#D9D9D9",
                highlightthickness=0,
                fg="black",
                font=("Courier","18")
    )
        entry_4.place(
                x=735.0,
                y=575.0,
                width=387.0,
                height=52.0
            )

        button_image_1 = PhotoImage(
                file=relative_to_assets("button_1.png"))
                
        button_1 = Button(win,
                image=button_image_1,
                borderwidth=0,
                highlightthickness=0,
                command=sign_up ,
                relief="flat")

        button_1.place(
                x=810.0,
                y=710.0,
                width=215,
                height=60)
        win.resizable(False,False)
        win.mainloop()

    root =Toplevel(first)
    root.geometry('1800x1800')
    root.title('Kaushalya Alacrity Apartments')
    main_frame=Frame(root)
    main_frame.pack(fill=BOTH,expand=1)
    #create canvas
    my_canvas=Canvas(main_frame)
    my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
    #create scrollbar
    my_scrollbar=ttk.Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT,fill=Y)
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>',lambda e : my_canvas.configure(scrollregion=my_canvas.bbox('all')) )
    second_frame= Frame(my_canvas)
    my_canvas.create_window((0,0),window=second_frame,anchor='nw')
    p=0
    for i in unoccupied().display():
        
        frame_body=Frame(second_frame,width=380, height=150,background='lightblue', highlightbackground='black',highlightthicknes=3)
        frame_body.grid(row=p+1,column=0,padx=20,pady=20,ipadx=5,ipady=5,columnspan=2)
        l3=Label(frame_body,text= i,font=('Helvetica',24),fg='#1A1A1A',width=80,height=5)
        l3.grid(row=p,column=0,padx=10,pady=10)
        b1=Button(frame_body,text='REGISTER NOW',font=('Helvetica',15),bg='#98F5FF',fg='#1A1A1A',command=sign)
        b1.grid(row=p+1,column=1,padx=20,pady=10)
        p+=1
    root.mainloop()
def login():
    
    class Node:
      def __init__(self,flatno=None,name=None,phn=None,pwd=None,owship=None,mail=None,next=None):
        self.flatno=flatno
        self.name=name
        self.phn=phn
        self.pwd=pwd
        self.owship=owship
        self.mail=mail
        self.next=next
    class occupied_details():
        def __init__(self):
         self.head=Node()
         self.dummyend=Node()
         self.head.next=self.dummyend
        def create(self):
         with open("user_details.txt","r") as file:
            reader=file.readlines()
            
            for x in reader:
                row=list(x.split(','))
                self.head.next=Node(row[0],row[1],row[2],row[3],row[4],row[5],self.head.next)
         return ""
        def check(self):#,user_name,pass_word):
         temp=self.head
         global flatno
         global pwd
         global name
         flatno=[]
         pwd=[]
         while temp.next is not None:
            flatno.insert(0,(temp.flatno))
            pwd.insert(0,(temp.pwd))
            temp=temp.next
         return " "
        def display(self):
         temp=self.head
         global rows
         rows = []
         while temp.next !=None:
            rows.insert(0,[temp.flatno,temp.name,temp.owship,temp.mail])
            temp=temp.next
    def maintanance():
     class maintnode:#class1
        def __init__(self,item=None,next=None):
            self._item=item 
            self._next=next
     class maintenance:
        def __init__(self):
            self._head=maintnode()
            pos=self._head
            with open('maintaenance_final.csv',"r") as csvfile:
                data=csv.reader(csvfile,delimiter=",")
                for i in data:
                  pos._next=maintnode(i,pos._next)
                  pos=pos._next
        def display(self,flat):
            pos=self._head
            user.after(100, user.destroy())
            btn.after(100, btn.destroy())
            btn1.after(100, btn1.destroy())
            months=['FLAT NO','JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
            while pos._next is not None:
                myFont = font.Font(family='Times',size=17)
                if pos._next._item [0] == flat :
                    y=100
                    for i in range(13):
                        month=Label(new,text=months[i],font=myFont,fg='white',bg='black')        
                        month.place(x=400,y=y)
                        month=Label(new,text=':',font=myFont,fg='white',bg='black')        
                        month.place(x=580,y=y) 
                        y+=50
                    y=100
                    for i in range(13):
                        month=Label(new,text=pos._next._item [i],font=myFont,fg='white',bg='black')        
                        month.place(x=650,y=y)
                        y+=50
                pos=pos._next
                
     maintenance().display(usernam) #loginned flat no. should be passed as the parameter
    def display():
     
        occu=Toplevel()
        occu.geometry('1800x1800')
        occu.title('Kaushalya Alacrity Apartments')
        occu_frame=Frame(occu)
        occu_frame.pack(fill=BOTH,expand=1)
        #create canvas
        canvas=Canvas(occu_frame)
        canvas.pack(side=LEFT,fill=BOTH,expand=1)
        #create scrollbar
        scrollbar=ttk.Scrollbar(occu_frame,orient=VERTICAL,command=canvas.yview)
        scrollbar.pack(side=RIGHT,fill=Y)
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>',lambda e : canvas.configure(scrollregion=canvas.bbox('all')) )
        new_frame= Frame(canvas)
        canvas.create_window((0,0),window=new_frame,anchor='nw')
        c=0
        for i in rows:
            data='Flat no.: '+str(i[0])+'    '+str(i[1])+'\n'+str(i[2]).capitalize()+'\t'+'Email id: '+str(i[3])
            frame_bod=Frame(new_frame,width=380, height=150,background='lightblue', highlightbackground='black',highlightthicknes=3)
            frame_bod.grid(row=c+1,column=0,padx=20,pady=20,ipadx=5,ipady=5,columnspan=2)
            l3=Label(frame_bod,text=data,font=('Helvetica',24),fg='#1A1A1A',width=80,height=5)
            l3.grid(row=c,column=0,padx=10,pady=10)
            c+=1
        occu.mainloop()
    def validate():
    
     if username.get() =="":
        mbox.showerror('ERROR','ALL FIELDS ARE MANDATORY')
     elif password.get() =="":
        mbox.showerror('ERROR','ALL FIELDS ARE MANDATORY')
     elif username.get() not in flatno:
        mbox.showerror('ERROR','INVALID CREDENTIALS')
     elif password.get() not in pwd:
        mbox.showerror('ERROR','INVALID CREDENTIALS')
     else:
        global usernam
        usernam=username.get()
        inde_x=flatno.index(username.get())
        i_n=(list(rows[inde_x]))
        use_r=i_n[1]
        global new
        global user
        global btn
        global btn1
        new= Toplevel()
        new.geometry("1200x850")
        new.configure(bg='black')
        new.title("DETAILS")
        myFont = font.Font(family='Times',size=23)
        user=Label(new,text=("Welcome!!!!",use_r),font=myFont,fg='white',bg='black')        
        user.place(x=400,y=100)
        btn=Button(new,text="Details",command = display)
        btn.place(
            x=450.0,
            y=300.0,
            width=216.5,
            height=61.5)
        btn1=Button(new,text="Maintainence",command = maintanance)
        btn1.place(
            x=450.0,
            y=400.0,
            width=216.5,
            height=61.5)  
    win = Toplevel(first)
    win.title('LOGIN')
    win.geometry("1200x900")
    username = StringVar()
    password = StringVar()
    a=occupied_details()
    a.create()
    a.check()
    a.display()
    image_background = PhotoImage(
    file=relative_to_assets("logbg.png"))
    label = Label(
win,
image=image_background
)
    label.place(x=0, y=0)

    entry1_user_name = Entry(win,
            textvariable=username,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0,
            fg="black",
            font=("Courier","15")
)
    entry1_user_name.place(
            x=735.0,
            y=260.0,
            width=387.0,
            height=52.0
        )
    entry2_pwd = Entry(win,
            textvariable=password,
            bd=0,
            bg="#D9D9D9",
            highlightthickness=0,
            fg="black",
            font=("Courier","15")
)
    entry2_pwd.place(
            x=735.0,
            y=376.0,
            width=387.0,
            height=52.0
        )
    button_image_1 = PhotoImage(
            file=relative_to_assets("button.png"))
    button_1 = Button(win,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=validate,
            relief="flat"
)
    button_1.place(
            x=810.0,
            y=710.0,
            width=216.5,
            height=61.5
)
    win.resizable(False,False)
    win.mainloop()

def about():
    abt=Toplevel()
    abt.geometry('886x689')
    abt.title('Kaushalya Alacrity Apartments')
    image_bg = PhotoImage( file=relative_to_assets("about-us.png"))
    label = Label(abt,image=image_bg)
    label.place(x=0, y=0)
    abt.resizable(False,False)
    abt.mainloop()
def locate():
    loc=Toplevel()
    loc.geometry('886x689')
    loc.title('Kaushalya Alacrity Apartments')
    image_bg = PhotoImage( file=relative_to_assets("locat.png"))
    label = Label(loc,image=image_bg)
    label.place(x=0, y=0)
    loc.resizable(False,False)
    loc.mainloop()
def contact():
    contac=Toplevel()
    contac.geometry('633x249')
    contac.title('Kaushalya Alacrity Apartments')
    image_bg = PhotoImage( file=relative_to_assets("contact-detail.png"))
    label = Label(contac,image=image_bg)
    label.place(x=0, y=0)
    contac.resizable(False,False)
    contac.mainloop()

first =Tk()
first.geometry('1400x1024')
first.title('Kaushalya Alacrity Apartments')
image_background = PhotoImage(
    file=relative_to_assets("Desktop.png"))
label = Label(first,image=image_background)
label.place(x=0, y=0)
button_image_1 = PhotoImage(
            file=relative_to_assets("login.png"))
            
button_1 = Button(first,image=button_image_1,borderwidth=0,background='lightblue',highlightthickness=0,command=login ,relief="flat")
button_1.place(x=78.0,y=227.0,width=217,height=50)
button_image_2 = PhotoImage(
            file=relative_to_assets("search.png"))
            
button_2 = Button(first,image=button_image_2,borderwidth=0,background='lightblue',highlightthickness=0,command=search ,relief="flat")
button_2.place(x=78.0,y=332.0,width=217,height=50)
button_image_3 = PhotoImage(
            file=relative_to_assets("about.png"))
            
button_3 = Button(first,image=button_image_3,borderwidth=0,highlightthickness=0, command=about ,relief="flat")
button_3.place(x=618.0,y=40.0,width=218,height=37)
button_image_4 = PhotoImage(
            file=relative_to_assets("location.png"))
            
button_4 = Button(first,image=button_image_4,borderwidth=0,highlightthickness=0,command=locate  ,relief="flat")
button_4.place(x=814.0,y=40.0,width=214,height=36)
button_image_5 = PhotoImage(
            file=relative_to_assets("contact.png"))
            
button_5 = Button(first,image=button_image_5,borderwidth=0,highlightthickness=0  ,command=contact ,relief="flat")
button_5.place(x=1019.0,y=40.0,width=205,height=36)

first.mainloop()