<<<<<<< HEAD
# import tkinter.ttk
#
# from tkinter import filedialog,colorchooser,Tk
#
# from tkinter import *
# from PIL import *
# from PIL import Image,ImageTk
# from tkinter import filedialog,colorchooser
#
#
# # #---------------------------------------------------------Window Create-------------------------------------------------------------------------------
# window = Tk() #Creating window
# window.title("Practice")
# window.iconbitmap(r"C:\Users\mahen\Downloads\icons8-wi-fi-fair-48 (1).ico")
#
#
# window.geometry("400x400")
#
#
#
# # #------------------------------------------------------------Labels-------------------------------------------------------------------------------------------
# # #
# # #
# # #
# # #
# # #
# # #
# # # StringVar = StringVar()
# # # IntVar = IntVar()
# # # IntVar.set(8)
# # #
# # # StringVar.set("Hey What'app Buddy?")
# # #
# # # dog_image = Image.open("dogresize_image.png")
# # # dog_image = ImageTk.PhotoImage(dog_image)
#
# # # label = Label(window,
# # #               text="Hey Whats'app \n Guru Mahendrakar\nAge 18\nCollage : CB Collage Bhalki",
# # #               font='myfont4.ttf 15 bold italic overstrike underline',
# # #               image=dog_image,
# # #               underline=1,
# # #               wraplength=3,#........horizental letters ko vertical me likhta hai
# # #               disabledforeground='white',
# # #               cursor=('circle','spider','heart'),
# # #               compound='bottom',
# # #               state='normal',
# # #               justify='left',
# # #               padx=(20),
# # #               pady=(20),
# # #               background='black',
# # #               foreground='white',
# # #               borderwidth=15,
# # #               relief='ridge',
# # #               textvariable= StringVar,
# # #
# # #               )
# # # label.pack(side='left',fill='both',expand='True')
# # #
# # #
#
#
#
#
#
#
#
#
# # #--------------------------------------------------button------------------------------------------------------------------------------------------
#
#
#
#
#
# # # image = Image.open('dogresize_image.png')
# # # image = ImageTk.PhotoImage(image)
# # #
# # #
# # # def executed():
# # #     print("Clicked Me!")
# # #
# # #
# # # button = Button(window,
# # #                 text='Click Me',
# # #                 image=image,width=200,
# # #                 height=50,
# # #                 compound='left',
# # #                 bg='green',fg='black',
# # #                 activeforeground='red',
# # #                 activebackground='blue',
# # #                 border=5,
# # #                 borderwidth=5,
# # #                 relief='sunken',
# # #                 overrelief='raised',
# # #                 command=executed,
# # #                 # wraplength=5-> #........horizental letters ko vertical me likhta hai
# # #                 cursor='circle',
# # #                 state='normal',
# # #                 highlightcolor='black',
# # #                 highlightthickness=11,
# # #                 anchor='nw',
# # #                 )
# # # button.flash() # Thodi Der Tak Button Ko Invisble Rakhata Hai (miliseconds me wapas jaata hai)
# # # button.pack()
#
#
#
#
#
#
#
#
#
# # #---------------------------------------------------Frames------------------------------------------------------------------------------
#
# # #........................................................ Grid Help...........................................................................
# # #IMPORTANT READ FIRST : -> Frames Ke Saath Grid() Use Karke Aur Ek Frame Pe Pack Use Karsakte ho
#
#
#
#
# # #........................................................Frames Help.........................................................................................
# # #FRAME BANAKE KE BAAD :-> Frame Ke Grid() Ke Madat Se Kuch Bhi Spon Kiya To Sirf Grid() Hi Use karna Padega
# # # & Frame Me Pack() Ki Madat Se Kuch Bhi Spon Kiya To Sirf Pack Use Karna Padega
# # # place () Bhi O Dono Ki Taraha Hi Kaam Karta Hai
#
#
#
# # # ...............................................4 Frames Created Down..............................................................
#
#
#
#
# # # frameOne = Frame(window,bg='yellow',name='frameOone')
# # # frameOne.pack(side=LEFT,fill='both')
# # # label = Label(frameOne,text="Click Me!",bg='red',fg='green')
# # # label.pack(side=RIGHT)
# # #
#
#
#
#
#
# # # frameOne = Frame(window,bg='green',padx=25)
# # # frameOne.pack(side=LEFT,fill='both')
# # # label = Label(frameOne,text="Click Me!",bg='red',fg='green')
# # # label.grid(row=0,column=0)
# # #
#
#
#
#
# # # frameOne = Frame(window,bg='red',padx=25)
# # # frameOne.pack(side=LEFT,fill='both')
# # # label = Label(frameOne,text="Click Me!",bg='red',fg='green')
# # # label.grid(row=0,column=0)
# # #
#
#
#
#
# # # frameOne = Frame(window,bg='yellow',padx=25)
# # # frameOne.pack(side=LEFT,fill='both')
# # # label = Label(frameOne,text="Click Me!",bg='red',fg='green')
# # # label.grid(row=1,column=0)
#
#
#
#
#
#
#
#
# # #------------------------------------------------------CheckButton--------------------------------------------------------------------------------
#
#
#
#
# # #
# # #
# # # FrameOone = Frame(window,highlightthickness=3,highlightcolor='gray')
# # # FrameOone.grid(row=0,column=0)
# # #
# # #
# # # Dosa = StringVar()
# # # Chicken = IntVar()
# # # Idli = IntVar()
# # #
# # # Dosa.set(False)
# # #
# # #
# # # dog_image = Image.open("dogresize_image.png")
# # # dog_image = ImageTk.PhotoImage(dog_image)
# # #
# # #
# # # def OrderChecking():
# # #     print(Dosa.get())
# # #
# # #     print(f"Agent Ne {checkbox1.cget('text')} Order Kardiya Hai")
# # #
# # #
# # # checkbox1 = Checkbutton(FrameOone,text='Dosa',
# # #                         variable=Dosa,
# # #                         command=OrderChecking,
# # #                         onvalue='Dosa',
# # #                         offvalue='none',
# # #                         offrelief='solid',
# # #                         borderwidth=2,
# # #                         overrelief='solid',
# # #                         height=10,
# # #                         width=200,
# # #                         foreground='green',
# # #                         bg='gray',
# # #                         highlightthickness=3,
# # #                         highlightcolor='red',
# # #                         justify='right',
# # #                         image= dog_image,
# # #                         compound='right',
# # #                         state='normal',
# # #                         )
# # #
# # #
# # #
# # #
# # # checkbox1.grid(row=0,column=0)
# # #
# # #
#
#
#
# # #-------------------------------------------------------------Entrybox--------------------------------------------------------------------------------
#
#
# # # frameOone = Frame(window,width=0,height=1000,bg='blue')
# # # frameOone.pack(side='left',anchor='e',fill='y')
# # #
# # #
# # #
# # # scro = Scrollbar(frameOone,
# # #                  orient=HORIZONTAL,
# # #                  bg='blue',
# # #                  )
# # # scro.pack(side='bottom',fill='x')
# # #
# # # entry = Entry(frameOone,
# # #               width=100,
# # #               bg='black',
# # #               fg='white',
# # #               cursor='circle',
# # #               readonlybackground='black',
# # #               state='normal',
# # #               insertwidth=10,
# # #               insertbackground='white',
# # #               insertontime=40,
# # #               insertborderwidth=50,
# # #               selectborderwidth=5,
# # #               selectbackground='pink',
# # #               selectforeground='green',
# # #               font='myfont4.ttf 19 italic underline overstrike',
# # #               justify='left',
# # #               highlightthickness=3,
# # #               highlightbackground='yellow',
# # #               highlightcolor='green',
# # #               xscrollcommand=scro,
# # #               border=3,
# # #               borderwidth=6,
# # #               relief='sunken',
# # #               show='+'
# # #               )
# # #
# # #
# # #
# # # entry.pack(side='left',fill='y')
# # # scro.config(command=entry.xview)
# # #
# # #
# # #
#
#
# # #----------------------------------------------------Radiobutton--------------------------------------------------------------------------
#
# # #
# # # frameOone = Frame(window,bg='green',width=50,height=50)
# # # frameOone.pack(side=LEFT,anchor='nw',fill='y')
# # #
# # # image_ = Image.open('dogresize_image.png')
# # # image_ = ImageTk.PhotoImage(image_)
# # #
# # # IntVar = StringVar()
# # # IntVar.set(0)
# # #
# # # def command_():
# # #     print("Command Executed Brother")
# # #
# # #
# # # rdxbutton = Radiobutton(window,
# # #                         width=100,
# # #                         text='dosa',
# # #                         value=1,
# # #                         variable=IntVar,
# # #                         bg='red',
# # #                         fg='blue',
# # #                         underline=1,
# # #                         activebackground='green',
# # #                         activeforeground='yellow',
# # #                         overrelief='sunken',
# # #                         image=image_,
# # #                         compound='left',
# # #                         justify='right',
# # #                         command=command_,
# # #                         highlightcolor='black', # touch karne kaad  black color ayega radiobutton me....
# # #                         highlightbackground='pink',  #touch karne se pehle pink color ayega radiobutton me..
# # #                         borderwidth=15)
# # #
# # # rdxbutton.pack(side=LEFT, fill='y')
# # #
#
#
#
# # #--------------------------------------------------------------Listbox---------------------------------------------------------------------------
#
#
# # #
# # #
# # # def __delete(event=None):
# # #     print(listbox.curselection())
# # #     listbox.delete(listbox.size()-1,END)
# # #
# # #
# # # def __clear():
# # #     count = 0
# # #     for index in listbox.curselection():
# # #         listbox.delete(index-count,index-count)
# # #         count+=1
# # #
# # #
# # #
# # # variable = StringVar()
# # #
# # # listbox = Listbox(window,
# # #                   bg='black',
# # #                   fg='white',
# # #                   border=3,
# # #                   borderwidth=5,
# # #                   relief='sunken',
# # #                   cursor='hand2',
# # #                   highlightbackground='yellow',
# # #                   highlightcolor='green',
# # #                   highlightthickness=5,
# # #                   selectforeground='pink'
# # #                   ,selectborderwidth=3,
# # #                   selectbackground='white',
# # #                   selectmode='multiple',
# # #                   listvariable=variable,
# # #                   )
# # #
# # # for products in [i for i in range(100)]:
# # #     listbox.insert(END,products)
# # #
# # #
# # # listbox.pack()
# # # # listbox.bind('<<ListboxSelect>>',__command)
# # #
# # # dlt_button = Button(window,text='Delete',bg='green',command=__clear)
# # # dlt_button.pack()
# # #
#
#
#
# # #---------------------------------------------------Scale---------------------------------------------------------------------------
# # #
# # #
# # #
# # #
# # #
# # # frameOone = Frame(window,bg='blue',height=400)
# # # frameOone.grid(row=0,column=0)
# # #
# # # label = Label(frameOone,text='guruji',
# # #               width=20,
# # #               height=20,
# # #               bg='red',
# # #               )
# # # label.pack(side=LEFT)
# # #
# # # def __you(scale):
# # #     print("Scale Is Hear Brother",scale)
# # #
# # # variable = IntVar()
# # # scale = Scale(frameOone,
# # #               from_=0,
# # #               to=1000,
# # #               orient=VERTICAL,
# # #               variable=variable,
# # #               command=__you,
# # #               resolution=50,
# # #               showvalue=10,
# # #               bg='black',
# # #               troughcolor='black',
# # #               sliderrelief='groove',
# # #               sliderlength=100,
# # #               state='normal',
# # #               tickinterval=10,
# # #               fg='white',
# # #               font='myfont4.ttf 19 italic underline')
# # #
# # # scale.config(width=15)
# # # scale.pack(side=LEFT,
# # #
# # #            anchor='nw',
# # #            fill='y')
#
#
#
# # #-------------------------------------------------------Combobox-----------------------------------------------------------------------------
#
# # # def comboboxselected(event):
# # #
# # #     a =combobox.get()
# # #     print(a,event)
# # #
# # #
# # # Bolle = Scrollbar(window,orient='vertical')
# # # Bolle.pack(side='right',fill='both')
# # # combobox = tkinter.ttk.Combobox(window,width=30,
# # #                                 height=10,
# # #                                 values=['dosa','chicken','paratha','Gobikisabzi'],
# # #                                 state='readonly',
# # #                                 justify='center',
# # #                                 # show = '-'
# # #                                 exportselection=True,
# # #                                 # postcommand=cool,#kitne baar combobox pe click kiya
# # #
# # #                                 )
# # # combobox.pack()
# # # combobox.set('Chicken')
# # # Bolle.configure(bg='green')
# # # listbox.config(yscrollcommand=Bolle)
# # # combobox.bind('<<ComboboxSelected>>',cool)
# # # Bolle.config(command=listbox.yview)
# # #
#
#
#
#
#
#
# # #--------------------------------------------------------------------Spinbox-----------------------------------------------------------------------------------------------
#
#
# # #
# # #
# # #
# # #
# # # def spinselect():
# # #     print(spin.get()
# # #           )
# # #
# # #
# # # spin = Spinbox(window,width=30,
# # #                from_= 0,
# # #                to=10,
# # #                wrap=True,
# # #                command=spinselect,
# # #                buttondownrelief='sunken',
# # #                buttoncursor='hand2',
# # #                buttonbackground='red',
# # #                borderwidth=5,
# # #                increment=3,
# # #                insertontime=1000,
# # #                state='readonly',
# # #                bg='green',
# # #                fg='red',
# # #                insertbackground='green',
# # #                selectbackground='yellow',
# # #                selectforeground='black',
# # #                selectborderwidth=7
# # #                )
# # # spin.pack()
# # #
# # # spin.bind('<<Increment>>')
# # #
# # # spin.bind('<<Decrement>>')
# # #
#
#
# # #-------------------------------------------------------------------------------------------------------------------------------------------------
#
# # frameOone= Frame(window,width=200,height=300,bg='green',border=5)
# # frameOone2 = Frame(window,width=200,height=300,bg='green',border=5)
# # frameOone3 = Frame(window,width=200,height=300,bg='green',border=5)
#
# # button = Button(frameOone,text='One',width=10,height=10)
# # button2 = Button(frameOone,text='Two',width=10,height=10)
# # button3 = Button(frameOone,text='Three',width=10,height=10)
# # button4 = Button(frameOone,text='Four',width=10,height=10,bg='green')
# # button5 = Button(frameOone,text='Five',width=10,height=10)
# # button6 = Button(frameOone,text='Six',width=10,height=10)
# # button7 = Button(frameOone,text='Seven',width=10,height=10)
# # button8 = Button(frameOone,text='Eight',width=10,height=10)
# # button9 = Button(frameOone,text='Nine',width=10,height=10)
# # button10 = Button(frameOone,text='Ten',width=10,height=10)
#
# # frameOone.pack(side=LEFT,anchor='nw',fill='both')
#
#
# # button.pack(side=LEFT,anchor='nw',fill='x')
# # button2.pack(side=LEFT, anchor='w',fill='y')
# # window.mainloop()
#
#
# from tkinter import ttk,Tk,colorchooser,Button,Label,Frame
#
#
# #-----------------------------------------------Toplevel_window____________________________________________________________
#
# # frameOone = Frame(window,bg='green')
# # frameOone.pack(side='left',anchor='nw')
# #
# # def toplevel():
# #
# #     # Ye SAme hamare original window tarah kaam karta hai
# #
# #     new = Toplevel(window) # Isko Pack or grid karne ki zarorat nahi hai
# #     button = Button(new,text='Click Me To Destroy',command=lambda  :   new.destroy())
# #     button.pack(side='left', fill='both', expand=1)
# #
# #
# # menu2 = Menu(window,tearoff=0)
# # menu2.add_command(label='newwindow',command=toplevel)
# # menu2.add_command(label='1')
# # menu2.add_command(label='2')
# # menu2.add_command(label='3')
# # menu2.add_command(label='4')
# #
# # menu = Menu(frameOone)
# # menu.add_cascade(label='Settings',menu = menu2)
# # window.config(menu=menu)
# #
#
#
# #--------------------------------------------Calendar & DataEntry---------------------------------------------------------
#
#
#
# import tkcalendar
#
# #
# # a = StringVar()
# # def selected_date():
# #     print(calendar.get_date())
# #
# #
# # calendar = tkcalendar.Calendar(window,selectmode='day',year=2022,month=12,day=23,cursor='hand2',date_pattern='dd/mm/yyyy' )
# # calendar.pack(fill='both',expand=1)
# #
# #
# # button = Button(window,text='Submit',command=selected_date)
# # button.pack()
# #
# #
# # #-------------------------------------------------------Data Entry ---------------------------------------------------
#
#
# # def date_picker():
# #     print("Your Date Is : {} ".format(calendar.get_date()))
# #
# # calendar = tkcalendar.DateEntry(window,selectmode='day',year=2022,month=12,day=23,cursor='hand2',date_pattern='dd/mm/yyyy',state='readonly' )
# # calendar.pack(fill='both') # expand mat dena data entry me koi mat puch mujhe bhi malum nahi hai
# #
# # button = Button(window,text='Hy Bro',command=date_picker)
# # button.pack()
#
=======
import tkinter.ttk
<<<<<<< HEAD
from tkinter import filedialog,colorchooser,Tk
=======
from tkinter import *
from PIL import *
from PIL import Image,ImageTk
from tkinter import filedialog,colorchooser
>>>>>>> a61a249b50f3ad60a15e2e96bd630d1606ad1418

# #---------------------------------------------------------Window Create-------------------------------------------------------------------------------
window = Tk() #Creating window
window.title("Practice")
window.iconbitmap(r"C:\Users\mahen\Downloads\icons8-wi-fi-fair-48 (1).ico")

<<<<<<< HEAD
=======
window.geometry("400x400")
>>>>>>> a61a249b50f3ad60a15e2e96bd630d1606ad1418


# #------------------------------------------------------------Labels-------------------------------------------------------------------------------------------
# #
# #
# #
# #
# #
# #
# # StringVar = StringVar()
# # IntVar = IntVar()
# # IntVar.set(8)
# #
# # StringVar.set("Hey What'app Buddy?")
# #
# # dog_image = Image.open("dogresize_image.png")
# # dog_image = ImageTk.PhotoImage(dog_image)

# # label = Label(window,
# #               text="Hey Whats'app \n Guru Mahendrakar\nAge 18\nCollage : CB Collage Bhalki",
# #               font='myfont4.ttf 15 bold italic overstrike underline',
# #               image=dog_image,
# #               underline=1,
# #               wraplength=3,#........horizental letters ko vertical me likhta hai
# #               disabledforeground='white',
# #               cursor=('circle','spider','heart'),
# #               compound='bottom',
# #               state='normal',
# #               justify='left',
# #               padx=(20),
# #               pady=(20),
# #               background='black',
# #               foreground='white',
# #               borderwidth=15,
# #               relief='ridge',
# #               textvariable= StringVar,
# #
# #               )
# # label.pack(side='left',fill='both',expand='True')
# #
# #








# #--------------------------------------------------button------------------------------------------------------------------------------------------





# # image = Image.open('dogresize_image.png')
# # image = ImageTk.PhotoImage(image)
# #
# #
# # def executed():
# #     print("Clicked Me!")
# #
# #
# # button = Button(window,
# #                 text='Click Me',
# #                 image=image,width=200,
# #                 height=50,
# #                 compound='left',
# #                 bg='green',fg='black',
# #                 activeforeground='red',
# #                 activebackground='blue',
# #                 border=5,
# #                 borderwidth=5,
# #                 relief='sunken',
# #                 overrelief='raised',
# #                 command=executed,
# #                 # wraplength=5-> #........horizental letters ko vertical me likhta hai
# #                 cursor='circle',
# #                 state='normal',
# #                 highlightcolor='black',
# #                 highlightthickness=11,
# #                 anchor='nw',
# #                 )
# # button.flash() # Thodi Der Tak Button Ko Invisble Rakhata Hai (miliseconds me wapas jaata hai)
# # button.pack()









# #---------------------------------------------------Frames------------------------------------------------------------------------------

# #........................................................ Grid Help...........................................................................
# #IMPORTANT READ FIRST : -> Frames Ke Saath Grid() Use Karke Aur Ek Frame Pe Pack Use Karsakte ho




# #........................................................Frames Help.........................................................................................
# #FRAME BANAKE KE BAAD :-> Frame Ke Grid() Ke Madat Se Kuch Bhi Spon Kiya To Sirf Grid() Hi Use karna Padega
# # & Frame Me Pack() Ki Madat Se Kuch Bhi Spon Kiya To Sirf Pack Use Karna Padega
# # place () Bhi O Dono Ki Taraha Hi Kaam Karta Hai



# # ...............................................4 Frames Created Down..............................................................




# # frameOne = Frame(window,bg='yellow',name='frameOone')
# # frameOne.pack(side=LEFT,fill='both')
# # label = Label(frameOne,text="Click Me!",bg='red',fg='green')
# # label.pack(side=RIGHT)
# #





# # frameOne = Frame(window,bg='green',padx=25)
# # frameOne.pack(side=LEFT,fill='both')
# # label = Label(frameOne,text="Click Me!",bg='red',fg='green')
# # label.grid(row=0,column=0)
# #




# # frameOne = Frame(window,bg='red',padx=25)
# # frameOne.pack(side=LEFT,fill='both')
# # label = Label(frameOne,text="Click Me!",bg='red',fg='green')
# # label.grid(row=0,column=0)
# #




# # frameOne = Frame(window,bg='yellow',padx=25)
# # frameOne.pack(side=LEFT,fill='both')
# # label = Label(frameOne,text="Click Me!",bg='red',fg='green')
# # label.grid(row=1,column=0)








# #------------------------------------------------------CheckButton--------------------------------------------------------------------------------




# #
# #
# # FrameOone = Frame(window,highlightthickness=3,highlightcolor='gray')
# # FrameOone.grid(row=0,column=0)
# #
# #
# # Dosa = StringVar()
# # Chicken = IntVar()
# # Idli = IntVar()
# #
# # Dosa.set(False)
# #
# #
# # dog_image = Image.open("dogresize_image.png")
# # dog_image = ImageTk.PhotoImage(dog_image)
# #
# #
# # def OrderChecking():
# #     print(Dosa.get())
# #
# #     print(f"Agent Ne {checkbox1.cget('text')} Order Kardiya Hai")
# #
# #
# # checkbox1 = Checkbutton(FrameOone,text='Dosa',
# #                         variable=Dosa,
# #                         command=OrderChecking,
# #                         onvalue='Dosa',
# #                         offvalue='none',
# #                         offrelief='solid',
# #                         borderwidth=2,
# #                         overrelief='solid',
# #                         height=10,
# #                         width=200,
# #                         foreground='green',
# #                         bg='gray',
# #                         highlightthickness=3,
# #                         highlightcolor='red',
# #                         justify='right',
# #                         image= dog_image,
# #                         compound='right',
# #                         state='normal',
# #                         )
# #
# #
# #
# #
# # checkbox1.grid(row=0,column=0)
# #
# #



# #-------------------------------------------------------------Entrybox--------------------------------------------------------------------------------


# # frameOone = Frame(window,width=0,height=1000,bg='blue')
# # frameOone.pack(side='left',anchor='e',fill='y')
# #
# #
# #
# # scro = Scrollbar(frameOone,
# #                  orient=HORIZONTAL,
# #                  bg='blue',
# #                  )
# # scro.pack(side='bottom',fill='x')
# #
# # entry = Entry(frameOone,
# #               width=100,
# #               bg='black',
# #               fg='white',
# #               cursor='circle',
# #               readonlybackground='black',
# #               state='normal',
# #               insertwidth=10,
# #               insertbackground='white',
# #               insertontime=40,
# #               insertborderwidth=50,
# #               selectborderwidth=5,
# #               selectbackground='pink',
# #               selectforeground='green',
# #               font='myfont4.ttf 19 italic underline overstrike',
# #               justify='left',
# #               highlightthickness=3,
# #               highlightbackground='yellow',
# #               highlightcolor='green',
# #               xscrollcommand=scro,
# #               border=3,
# #               borderwidth=6,
# #               relief='sunken',
# #               show='+'
# #               )
# #
# #
# #
# # entry.pack(side='left',fill='y')
# # scro.config(command=entry.xview)
# #
# #
# #


# #----------------------------------------------------Radiobutton--------------------------------------------------------------------------

# #
# # frameOone = Frame(window,bg='green',width=50,height=50)
# # frameOone.pack(side=LEFT,anchor='nw',fill='y')
# #
# # image_ = Image.open('dogresize_image.png')
# # image_ = ImageTk.PhotoImage(image_)
# #
# # IntVar = StringVar()
# # IntVar.set(0)
# #
# # def command_():
# #     print("Command Executed Brother")
# #
# #
# # rdxbutton = Radiobutton(window,
# #                         width=100,
# #                         text='dosa',
# #                         value=1,
# #                         variable=IntVar,
# #                         bg='red',
# #                         fg='blue',
# #                         underline=1,
# #                         activebackground='green',
# #                         activeforeground='yellow',
# #                         overrelief='sunken',
# #                         image=image_,
# #                         compound='left',
# #                         justify='right',
# #                         command=command_,
# #                         highlightcolor='black', # touch karne kaad  black color ayega radiobutton me....
# #                         highlightbackground='pink',  #touch karne se pehle pink color ayega radiobutton me..
# #                         borderwidth=15)
# #
# # rdxbutton.pack(side=LEFT, fill='y')
# #



# #--------------------------------------------------------------Listbox---------------------------------------------------------------------------


# #
# #
# # def __delete(event=None):
# #     print(listbox.curselection())
# #     listbox.delete(listbox.size()-1,END)
# #
# #
# # def __clear():
# #     count = 0
# #     for index in listbox.curselection():
# #         listbox.delete(index-count,index-count)
# #         count+=1
# #
# #
# #
# # variable = StringVar()
# #
# # listbox = Listbox(window,
# #                   bg='black',
# #                   fg='white',
# #                   border=3,
# #                   borderwidth=5,
# #                   relief='sunken',
# #                   cursor='hand2',
# #                   highlightbackground='yellow',
# #                   highlightcolor='green',
# #                   highlightthickness=5,
# #                   selectforeground='pink'
# #                   ,selectborderwidth=3,
# #                   selectbackground='white',
# #                   selectmode='multiple',
# #                   listvariable=variable,
# #                   )
# #
# # for products in [i for i in range(100)]:
# #     listbox.insert(END,products)
# #
# #
# # listbox.pack()
# # # listbox.bind('<<ListboxSelect>>',__command)
# #
# # dlt_button = Button(window,text='Delete',bg='green',command=__clear)
# # dlt_button.pack()
# #



# #---------------------------------------------------Scale---------------------------------------------------------------------------
# #
# #
# #
# #
# #
# # frameOone = Frame(window,bg='blue',height=400)
# # frameOone.grid(row=0,column=0)
# #
# # label = Label(frameOone,text='guruji',
# #               width=20,
# #               height=20,
# #               bg='red',
# #               )
# # label.pack(side=LEFT)
# #
# # def __you(scale):
# #     print("Scale Is Hear Brother",scale)
# #
# # variable = IntVar()
# # scale = Scale(frameOone,
# #               from_=0,
# #               to=1000,
# #               orient=VERTICAL,
# #               variable=variable,
# #               command=__you,
# #               resolution=50,
# #               showvalue=10,
# #               bg='black',
# #               troughcolor='black',
# #               sliderrelief='groove',
# #               sliderlength=100,
# #               state='normal',
# #               tickinterval=10,
# #               fg='white',
# #               font='myfont4.ttf 19 italic underline')
# #
# # scale.config(width=15)
# # scale.pack(side=LEFT,
# #
# #            anchor='nw',
# #            fill='y')



# #-------------------------------------------------------Combobox-----------------------------------------------------------------------------

# # def comboboxselected(event):
# #
# #     a =combobox.get()
# #     print(a,event)
# #
# #
# # Bolle = Scrollbar(window,orient='vertical')
# # Bolle.pack(side='right',fill='both')
# # combobox = tkinter.ttk.Combobox(window,width=30,
# #                                 height=10,
# #                                 values=['dosa','chicken','paratha','Gobikisabzi'],
# #                                 state='readonly',
# #                                 justify='center',
# #                                 # show = '-'
# #                                 exportselection=True,
# #                                 # postcommand=cool,#kitne baar combobox pe click kiya
# #
# #                                 )
# # combobox.pack()
# # combobox.set('Chicken')
# # Bolle.configure(bg='green')
# # listbox.config(yscrollcommand=Bolle)
# # combobox.bind('<<ComboboxSelected>>',cool)
# # Bolle.config(command=listbox.yview)
# #






# #--------------------------------------------------------------------Spinbox-----------------------------------------------------------------------------------------------


# #
# #
# #
# #
# # def spinselect():
# #     print(spin.get()
# #           )
# #
# #
# # spin = Spinbox(window,width=30,
# #                from_= 0,
# #                to=10,
# #                wrap=True,
# #                command=spinselect,
# #                buttondownrelief='sunken',
# #                buttoncursor='hand2',
# #                buttonbackground='red',
# #                borderwidth=5,
# #                increment=3,
# #                insertontime=1000,
# #                state='readonly',
# #                bg='green',
# #                fg='red',
# #                insertbackground='green',
# #                selectbackground='yellow',
# #                selectforeground='black',
# #                selectborderwidth=7
# #                )
# # spin.pack()
# #
# # spin.bind('<<Increment>>')
# #
# # spin.bind('<<Decrement>>')
# #


# #-------------------------------------------------------------------------------------------------------------------------------------------------

# frameOone= Frame(window,width=200,height=300,bg='green',border=5)
# frameOone2 = Frame(window,width=200,height=300,bg='green',border=5)
# frameOone3 = Frame(window,width=200,height=300,bg='green',border=5)

# button = Button(frameOone,text='One',width=10,height=10)
# button2 = Button(frameOone,text='Two',width=10,height=10)
# button3 = Button(frameOone,text='Three',width=10,height=10)
# button4 = Button(frameOone,text='Four',width=10,height=10,bg='green')
# button5 = Button(frameOone,text='Five',width=10,height=10)
# button6 = Button(frameOone,text='Six',width=10,height=10)
# button7 = Button(frameOone,text='Seven',width=10,height=10)
# button8 = Button(frameOone,text='Eight',width=10,height=10)
# button9 = Button(frameOone,text='Nine',width=10,height=10)
# button10 = Button(frameOone,text='Ten',width=10,height=10)

# frameOone.pack(side=LEFT,anchor='nw',fill='both')


# button.pack(side=LEFT,anchor='nw',fill='x')
# button2.pack(side=LEFT, anchor='w',fill='y')
# window.mainloop()


from tkinter import ttk,Tk,colorchooser,Button,Label,Frame


#-----------------------------------------------Toplevel_window____________________________________________________________

# frameOone = Frame(window,bg='green')
# frameOone.pack(side='left',anchor='nw')
#
# def toplevel():
#
#     # Ye SAme hamare original window tarah kaam karta hai
#
#     new = Toplevel(window) # Isko Pack or grid karne ki zarorat nahi hai
#     button = Button(new,text='Click Me To Destroy',command=lambda  :   new.destroy())
#     button.pack(side='left', fill='both', expand=1)
#
#
# menu2 = Menu(window,tearoff=0)
# menu2.add_command(label='newwindow',command=toplevel)
# menu2.add_command(label='1')
# menu2.add_command(label='2')
# menu2.add_command(label='3')
# menu2.add_command(label='4')
#
# menu = Menu(frameOone)
# menu.add_cascade(label='Settings',menu = menu2)
# window.config(menu=menu)
#


#--------------------------------------------Calendar & DataEntry---------------------------------------------------------



<<<<<<< HEAD
=======
import tkcalendar
>>>>>>> a61a249b50f3ad60a15e2e96bd630d1606ad1418
#
# a = StringVar()
# def selected_date():
#     print(calendar.get_date())
#
#
# calendar = tkcalendar.Calendar(window,selectmode='day',year=2022,month=12,day=23,cursor='hand2',date_pattern='dd/mm/yyyy' )
# calendar.pack(fill='both',expand=1)
#
#
# button = Button(window,text='Submit',command=selected_date)
# button.pack()
#
#
# #-------------------------------------------------------Data Entry ---------------------------------------------------

<<<<<<< HEAD
>>>>>>> 36d4c510ec930594b4677a1cc42194afa02bdbcd
# def date_picker():
#     print("Your Date Is : {} ".format(calendar.get_date()))
#
# calendar = tkcalendar.DateEntry(window,selectmode='day',year=2022,month=12,day=23,cursor='hand2',date_pattern='dd/mm/yyyy',state='readonly' )
# calendar.pack(fill='both') # expand mat dena data entry me koi mat puch mujhe bhi malum nahi hai
#
# button = Button(window,text='Hy Bro',command=date_picker)
# button.pack()
<<<<<<< HEAD
#
#
#
# #------------------------------------------------------fieldlog------------------------------------------------------------------
#
#
# # fieldlogopen = filedialog.askopenfilename(initialdir= 'C:\\Users\\mahen\\bitepy',
# #                                        initialfile='texting.txt',
# #                                        filetypes=([('Texting Files','*.txt'),('Python Files','*.py'),("AllFiles",'*.*')]))
# #
# # print(fieldlogg) # Returned Selected Item
# #
#
#
# #-----------------------------------------------------filedialog.asksavesfile()--------------------------------------------------
# import os
# # filedialogsaves  = filedialog.asksaveasfile(initialdir=os.getcwd(),
# #                                               filetypes=[("Textfilesave",".txt"),("Pythonfilesave",".py")])
# #
# #
# #
# # print(filedialogsaves.write('Guruji Mahendrakar'))
# #
#
#
# #---------------------------------------------Canvas------------------------------------------------------------------------------
#
#
# # canvas = Canvas(window,bg='yellow',height=250,width=250)
# # canvas.pack()
# #
# # line = canvas.create_line(0,0,250,10)
# # squrebracket = canvas.create_rectangle(40,100,200,200)
# # round = canvas.create_oval(20,20,80,50)
# # s = canvas.create_arc(0,90,240,250,width = 10,fill='green', )
#
#
# #------------------------------------------------------------Notebook-----------------------------------------------------------------------------------------
# #
# # print("Hey Man !")
# #
# # notebook = tkinter.ttk.Notebook(window)
# #
# # frame = Frame(notebook,width=400,height=400)
# # frame.pack(expand='True',fill='both')
# # frame2 = Frame(notebook,width=500,height=333)
# # frame2.pack(fill='both',expand=1)
# #
# #
# # button = Button(frame,text="Hey I'm Guru Brother")
# # button.pack(fill='both')
# #
# # notebook.add(frame,text='Hey Man! click me')
# # notebook.pack(expand=1,fill='both')
# # notebook.add(frame2,text='hlo Man Brother to you')
# #
#
#
#
# #---------------------------------------------------Treeview-------------------------------------------------------------
#
#
# #
# # treevieew = ttk.Treeview(window,columns=["Name","Sirname","Rollno","Cool"])
# #
# # treevieew.column("#0",width=0,stretch='no')
# # treevieew.heading('Name',text="Name")
# #
# # treevieew.pack(side='left')
# #
# #
# # treevieew.insert('','end',iid=0,text='Parent',values=["Guru","Mahendrakar",20],)
# #
# # treevieew.insert('','end',iid=5,text='Cool',values=[1,2,3,4])
# # treevieew.insert('','end',iid=6,text='Cool',values=['Nitin',"Mahendrakar",37])
# #
# # treevieew.pack(padx=20)
# #
# # treevieew.move(5,0,1)
# # treevieew.move(6,0,0)
# # treevieew.config(height=50)
# #
#
#
#
# #----------------------------------------------------------Canvas----------------------------------------------
#
#
# #
# # note_ = ttk.Notebook(window)
# #
# # frame = Frame(window)
# #
# # text_ = Label(frame,text='gurumahendrakar')
# # text_.pack()
# #
# # note_.add(frame,text='frame-1')
# #
# #
# # frame = Frame(window)
# #
# # text_ = Label(frame,text='Hey I m frame-2')
# # text_.pack()
# #
# # note_.add(frame,text='fucker')
# #
# # note_.pack()
# # window.mainloop()
# # note_ = ttk.Notebook(window)
# #
# # frame = Frame(window)
# #
# # text_ = Label(frame,text='gurumahendrakar')
# # text_.pack()
# #
# # note_.add(frame,text='frame-1')
# #
# #
# # frame = Frame(window)
# #
# # text_ = Label(frame,text='Hey I m frame-2')
# # text_.pack()
# #
# # note_.add(frame,text='fucker')
# #
# # note_.pack()
#
#
#
#
#
# if __name__ == '__main__':
#     window.mainloop()
#
import tkinter
from PIL import ImageTk,Image

a = tkinter.Tk()

b = ImageTk.PhotoImage(Image.open('html2.jpeg'))

label = tkinter.Label(a,text="Guru mahendrakar",image=b,width=100)
label.pack()
if __name__ == '__main__':
    a.mainloop()
=======
=======
def date_picker():
    print("Your Date Is : {} ".format(calendar.get_date()))

calendar = tkcalendar.DateEntry(window,selectmode='day',year=2022,month=12,day=23,cursor='hand2',date_pattern='dd/mm/yyyy',state='readonly' )
calendar.pack(fill='both') # expand mat dena data entry me koi mat puch mujhe bhi malum nahi hai

button = Button(window,text='Hy Bro',command=date_picker)
button.pack()
>>>>>>> a61a249b50f3ad60a15e2e96bd630d1606ad1418


#------------------------------------------------------fieldlog------------------------------------------------------------------


# fieldlogopen = filedialog.askopenfilename(initialdir= 'C:\\Users\\mahen\\bitepy',
#                                        initialfile='texting.txt',
#                                        filetypes=([('Texting Files','*.txt'),('Python Files','*.py'),("AllFiles",'*.*')]))
#
# print(fieldlogg) # Returned Selected Item
#


#-----------------------------------------------------filedialog.asksavesfile()--------------------------------------------------
import os
# filedialogsaves  = filedialog.asksaveasfile(initialdir=os.getcwd(),
#                                               filetypes=[("Textfilesave",".txt"),("Pythonfilesave",".py")])
#
#
#
# print(filedialogsaves.write('Guruji Mahendrakar'))
#


#---------------------------------------------Canvas------------------------------------------------------------------------------


# canvas = Canvas(window,bg='yellow',height=250,width=250)
# canvas.pack()
#
# line = canvas.create_line(0,0,250,10)
# squrebracket = canvas.create_rectangle(40,100,200,200)
# round = canvas.create_oval(20,20,80,50)
# s = canvas.create_arc(0,90,240,250,width = 10,fill='green', )


#------------------------------------------------------------Notebook-----------------------------------------------------------------------------------------
#
# print("Hey Man !")
#
# notebook = tkinter.ttk.Notebook(window)
#
# frame = Frame(notebook,width=400,height=400)
# frame.pack(expand='True',fill='both')
# frame2 = Frame(notebook,width=500,height=333)
# frame2.pack(fill='both',expand=1)
#
#
# button = Button(frame,text="Hey I'm Guru Brother")
# button.pack(fill='both')
#
# notebook.add(frame,text='Hey Man! click me')
# notebook.pack(expand=1,fill='both')
# notebook.add(frame2,text='hlo Man Brother to you')
#



#---------------------------------------------------Treeview-------------------------------------------------------------


#
# treevieew = ttk.Treeview(window,columns=["Name","Sirname","Rollno","Cool"])
#
# treevieew.column("#0",width=0,stretch='no')
# treevieew.heading('Name',text="Name")
#
# treevieew.pack(side='left')
#
#
# treevieew.insert('','end',iid=0,text='Parent',values=["Guru","Mahendrakar",20],)
#
# treevieew.insert('','end',iid=5,text='Cool',values=[1,2,3,4])
# treevieew.insert('','end',iid=6,text='Cool',values=['Nitin',"Mahendrakar",37])
#
# treevieew.pack(padx=20)
#
# treevieew.move(5,0,1)
# treevieew.move(6,0,0)
# treevieew.config(height=50)
#



#----------------------------------------------------------Canvas----------------------------------------------

<<<<<<< HEAD
#
# note_ = ttk.Notebook(window)
#
# frame = Frame(window)
#
# text_ = Label(frame,text='gurumahendrakar')
# text_.pack()
#
# note_.add(frame,text='frame-1')
#
#
# frame = Frame(window)
#
# text_ = Label(frame,text='Hey I m frame-2')
# text_.pack()
#
# note_.add(frame,text='fucker')
#
# note_.pack()
# window.mainloop()
# note_ = ttk.Notebook(window)
#
# frame = Frame(window)
#
# text_ = Label(frame,text='gurumahendrakar')
# text_.pack()
#
# note_.add(frame,text='frame-1')
#
#
# frame = Frame(window)
#
# text_ = Label(frame,text='Hey I m frame-2')
# text_.pack()
#
# note_.add(frame,text='fucker')
#
# note_.pack()


import itertools

for x in (itertools.chain([1,2,3,4])):
    print(x)
=======


if __name__ == '__main__':
    window.mainloop()



>>>>>>> a61a249b50f3ad60a15e2e96bd630d1606ad1418

>>>>>>> 36d4c510ec930594b4677a1cc42194afa02bdbcd
