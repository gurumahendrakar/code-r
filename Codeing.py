# <<<<<<< HEAD
# # # # # #
# # # # # # date_of_birth = [f'Name : Guru ',f"Roll NO : 51",f"Collage Name : Cb Collage Bhalki"]
# # # # # # a = str(date_of_birth).encode()
# # # # # # store_previous_binary = ''
# # # # # # with open('texting.txt','rb')as file:
# # # # # #     store_previous_binary = file.readlines()
# # # # # # for i in store_previous_binary[0]:
# # # # # #     print(type(i))
# # # # # #
# # # # # #
# # # # # # import sys
# # # # # #
# # # # # # c = sys.argv
# # # # # # print(c[1:],c[:])
# # # # # #
# # # # # #
# # # # # # import random
# # # # # # x = 'Guru'
# # # # # # y = 'cool'
# # # # # # def fun():
# # # # # #     return 'Guru Mahendrakar'
# # # # # #
# # # # # # while True:
# # # # # #     eve = eval(input('Enter The input'),{'fun': fun,__builtins__: None,'x':x},{y:'y'})
# # # # # #     print(type(eve),eve)
# # # # # #
# # # # # #
# # # # # # Importing library
# # # # # # import qrcode
# # # # # #
# # # # # # qr = qrcode.QRCode(version=15,box_size=10,border=3)
# # # # # # data = 'https://www.geeksforgeeks.org/generate-qr-code-using-qrcode-in-python/'
# # # # # # qr.add_data(data)
# # # # # # qr.make(fit=True)
# # # # # # a = qr.make_image(fill = 'white',background = 'black')
# # # # # # a.save('songr.png')
# # # # # #
# # # # # # lista = [1,2,3,4,5]
# # # # # # # def check():
# # # # # # #     for i in range(6):
# # # # # # #         yield i
# # # # # # #
# # # # # # # a = check()
# # # # # # # print(list(a))
# # # # # # # print(list(a))
# # # # # # #print(list(map(lambda a :a if a<4 else -1,lista,)))
# # # # # # #
# # # # # # # import functools
# # # # # # #
# # # # # # # print(functools.reduce(lambda x,y:x+y,[1,2,3,4,5,6]))
# # # # #
# # # # # # # def tool(a,b):
# # # # # # #
# # # # # # #     print(a)
# # # # # # #
# # # # # # # a = [1,2,3,4,5,6]
# # # # # # #
# # # # # # # b = iter([7,8,9,10,11,12])
# # # # # # #
# # # # # # # a[4] = next(b)
# # # # # # # print(a)
# # # # # # #
# # # # # # # Enter_name = input("Enter A Name Brother")
# # # # # # # Enter_sirname = input("Enter a Sirname")
# # # # # # #
# # # # # # # print('Welcome To You Sir' if Enter_name == Enter_name.capitalize() else 'Please Follow Rules' if len(Enter_name)==4 else 'Not Followed rules by brother')
# # # # # #
# # # # # # import random
# # # # # # import time
# # # # # # # a = dict((('a','Guru'),('b','Cool')))
# # # # # # # b = a['Guru'] = "Mahendrakar"
# # # # # # # print(b)
# # # # # # #
# # # # # # Holder_names = []
# # # # # # Created_Holder_Account_numbers = []
# # # # # # Register_numbers = 741189185200
# # # # # # Holdername = input('Enter The Name : \t');AccountBalance = int(input('How Do You Money Have \t : '))
# # # # # # All_information_bank = {}
# # # # # # class Bank:
# # # # # #     global Register_numbers
# # # # # #     Register_numbers+= 1
# # # # # #     global Holder_names
# # # # # #     def __init__(self,Holdername,AccountBalance = 0,Register_number=Register_numbers):
# # # # # #
# # # # # #         self.__Owner_name = 'Guru Mahendrakar'
# # # # # #         self.__Owner_phonenumber = '7411891852'
# # # # # #         self.__Email_adress = 'GuruMahendrakar143@email.com'
# # # # # #         self.Name = Holdername
# # # # # #         self.Balance = AccountBalance
# # # # # #         self.Register_no = Register_number
# # # # # #         self.__notify__comformation()
# # # # # #         if input('You Want To Change Anyone')!='Yes':
# # # # # #             if self.Name not in Holder_names:
# # # # # #                 Holder_names.append(self.Name)
# # # # # #                 self.__information(self.Name, self.Balance, Register_number)
# # # # # #                 print('Thanks For Creating Account')
# # # # # #
# # # # # #             else:
# # # # # #                 print("Name Is Already Register in Bank")
# # # # # #         else:
# # # # # #             Holdername = input('Enter The Name Again : \t '); AccountBalance = input("Do You Have Money : \t")
# # # # # #             self.Name = Holdername
# # # # # #             self.Balance = AccountBalance
# # # # # #             self.__information(self.Name,self.Balance,Register_number)
# # # # # #             def __new__(self):
# # # # # #                 Holder_names.append(self.Name)
# # # # # #                 return type('Bank',(),dict((("Name",self.Name),("Balance",self.Balance))))
# # # # # #
# # # # # #
# # # # # #     def __notify__comformation(self):
# # # # # #         print("Name : {}\n"\
# # # # # #               "Register Number : {}\n"\
# # # # # #               "Account Balance : {}".format(self.Name,self.Register_no,self.Balance))
# # # # # #
# # # # # #
# # # # # #     def __Add_Money(self,AddMoney):
# # # # # #         Account_number = int(input("Enter Account Number : "))
# # # # # #         if Account_number == self.Register_no:
# # # # # #             self.Balance+=AddMoney
# # # # # #
# # # # # #
# # # # # #
# # # # # #     def __information(self,Name,Balance,Register_no):
# # # # # #         global Created_Holder_Account_numbers
# # # # # #         global  All_information_bank
# # # # # #         Created_Holder_Account_numbers = Created_Holder_Account_numbers.append((Name,(Balance,Register_no)))
# # # # # #         information_client = {Name:{Register_no: Balance}}
# # # # # #         All_information_bank[Name] = information_client
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # # object = Bank(Holdername,AccountBalance,Register_numbers)
# # # # # #
# # # # # # import json
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # # # class method():
# # # # # # #     def __init__(self,name,sirname):
# # # # # # #         print('This Is Method Class')
# # # # # # #         super().__init__()
# # # # # # #         self.name = name
# # # # # # #         self.sirname = sirname
# # # # # # #         self.roll = 28
# # # # # # #     def HelloBrother(self):
# # # # # # #         print('Welcome Method Object {} '.format(self))
# # # # # # #
# # # # # # # class method3:
# # # # # # #     def __init__(self):
# # # # # # #         self.collage = 'cb collage Bhlalki'
# # # # # # #         print('This Is Method-3 Class')
# # # # # # #
# # # # # # #     def method3_function(self):
# # # # # # #         print("Method3 Fucntion Brother ")
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # # class List:
# # # # # # #     def __init__(self,*args):
# # # # # # #         print("First Called Method2")
# # # # # # #         self.hello = "Guru"
# # # # # # #         self.args = args
# # # # # # #         self.value_counter  = -1
# # # # # # #
# # # # # # #
# # # # # # #
# # # # # # #     def __del__(self):
# # # # # # #         print("Finally Deleteb Object")
# # # # # # #
# # # # # # #     def __iter__(self):
# # # # # # #         return self
# # # # # # #
# # # # # # #     def __next__(self):
# # # # # # #         list_len = len(self.args)
# # # # # # #         try:
# # # # # # #             while list_len-1 != self.value_counter:
# # # # # # #                 self.value_counter+= 1
# # # # # # #
# # # # # # #
# # # # # # #                 return self.args[self.value_counter]
# # # # # # #             raise StopIteration
# # # # # # #         except:
# # # # # # #             self.value_counter = 0
# # # # # # #             return self.args[self.value_counter]
# # # # # # #
# # # # # # #
# # # # # # # method32  =  List(1,2,3)
# # # # # # # for i in iter(method32):
# # # # # # #     print(i,end=' ')
# # # # # # #     time.sleep(2)
# # # # # #
# # # # # #
# # # # # # # def value_taker(valuess):
# # # # # # #     def sum():
# # # # # # #         counter = 0
# # # # # # #         for values in valuess():
# # # # # # #             counter+=values
# # # # # # #         return counter
# # # # # # #     return sum
# # # # # # #
# # # # # # # def loop(odd_value_seprator):
# # # # # # #     odd_value_storer = []
# # # # # # #
# # # # # # #     def checker():
# # # # # # #          print(locals(),'locals')
# # # # # # #          print(dir())
# # # # # # #          for values in [1,2,3]:
# # # # # # #              if values%2!=0:
# # # # # # #                  odd_value_storer.append(values)
# # # # # # #
# # # # # # #          return odd_value_storer
# # # # # # #     return checker
# # # # # # #
# # # # # # # def value_transfer():
# # # # # # #     list = eval(input("Enter A Integers List"))
# # # # # # #     return list
# # # # # # #
# # # # # # # a = value_taker(loop(odd_value_seprator=value_transfer))
# # # # # # # print(a())
# # # # # #
# # # # # # #import pickle
# # # # # #
# # # # # # # class metho:
# # # # # # #     def __init__(self):
# # # # # # #         self.Guru = "Guru"
# # # # # # #         self.sirname = "Mahendrakar"
# # # # # # #
# # # # '''
# # # # json.loads = str to dict
# # # # json.dumps  = dict to str
# # # # json.load(Recive in String)
# # # # json.dump(obj,file)(take only str) = take only string
# # # import itertools
# #
# # # # pickle.loads  = binary to str
# # # # pickle.dumps = str to binary
# # # # pickle.dump((bytes,iterables),file) = Tumne jO Paas Kiye Hai Wahi Type Milega
# # # # pickle.load(file) = Tune Jo Uske Under Daala Hai Wahi Milega
# # # # '''
# # # # # # # ono1 = type('Guru',(),{'Guru': "Mahendrakar","Roll No ": 39,"Clg": "Cb Collage Bhalki"})
# # # # # # # on2 = type('Guru',(),{'Guru': "Xranger","Roll No ": 38,"Clg": "Cb Collage Bhalki"})
# # # # # # # on3 = type('Guru',(),{'Guru': "ValueAble","Roll No ": 36,"Clg": "Cb Collage Bhalki"})
# # # # # # # b = ono1.__dict__
# # # # # # # a  = 'guru'
# # # # # # # c = [1,2,3,4,5]
# # # # # #
# # # # # #
# # # # # # # class Student:
# # # # # # #     def __init__(self,name,roll):
# # # # # # #         self.name = name
# # # # # # #         self.roll = int(roll)
# # # # # # #
# # # # # # #     def Student_attendence(self):
# # # # # # #         print(f'{self.name},{self.roll}')
# # # # # # #
# # # # # # # with open('texting.txt','rb+') as ojec:
# # # # # # #         pickle.dump(Student('Guru',8),ojec)
# # # # # # #         pickle.dump(Student('Guruji',51),ojec)
# # # # # # #         with open('texting.txt','rb+') as f :
# # # # # # #             print(pickle.load(f).name)
# # # # # #
# # # # # #
# # # # # # # d = 'Guru'.encode()
# # # # # # # b = {}
# # # # # # # aa  = b.setdefault('Guru', "mahendrakar")
# # # # # # # print(b)
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # # # a = {}
# # # # # # # list = []
# # # # # # # import time
# # # # # # # c = time.time()
# # # # # # # for letters in string:
# # # # # # #     b = 0
# # # # # # #     if letters not in a:
# # # # # # #         b+= 1
# # # # # # #         a[letters] = b
# # # # # # #         print(letters,end="")
# # # # # # #     else:
# # # # # # #         b+= a[letters]+1
# # # # # # #         a[letters]= b
# # # # # # #         print(letters*a[letters],end="")
# # # # # # # print()
# # # # # # #
# # # # # # # print(time.time()-c)
# # # # # # # c = time.time()
# # # # # # # for letters in string:
# # # # # # #     if letters not in list:
# # # # # # #         list.append(letters)
# # # # # # #         print(letters,end="")
# # # # # # #     elif letters in list:
# # # # # # #         coiu = 0
# # # # # # #         for letter in list:
# # # # # # #             if letters==letter:
# # # # # # #                 coiu+= 1
# # # # # # #         print(letters*(coiu+1),end="")
# # # # # # # print()
# # # # # # # print(time.time()-c)
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # # import os
# # # # # # # print(os.getcwd())
# # # # # # # os.chdir(os.getcwd())
# # # # # # # a = os.path.join('C:','Users','Mahen','bitepy')
# # # # # # # print(os.mkdir('Sorting.py'))
# # # # # # # print(os.listdir(os.getcwd()))
# # # # # # # os.chdir(os.getcwd())
# # # # # # # os.mkdir('Sorting.py')
# # # # # # # os.rmdir('Sorting.py')
# # # # # # # print(os.listdir(os.getcwd()))
# # # # # #
# # # # # # # list = [-1,1,2,3,4,5,6]
# # # # # # # higher = 0
# # # # # # # for i in range(len(list)):
# # # # # # #     if list[i]>higher:
# # # # # # #         higher = list[i]
# # # # # # # print(higher)
# # # # # #
# # # # # # # class moreaboutcreated(object):
# # # # # # #     def __init__(self,name):
# # # # # # #         pass
# # # # # # # class one(type):
# # # # # # #     def __new__(cls, *args, **kwargs):
# # # # # # #
# # # # # # #         sea = 9
# # # # # # #         one2 = 0
# # # # # # #         try:
# # # # # # #             if one.one2==0:
# # # # # # #                 args[2][locals()['sea']] = 9
# # # # # # #                 one.one2+= 1
# # # # # # #                 return type('Guru',(),args[2])
# # # # # # #             elif one.one2==1:
# # # # # # #                 one.one2+= 1
# # # # # # #                 return  type(cls.__name__,(), {})
# # # # # # #             else:
# # # # # # #                 raise moreaboutcreated('No more object create brother')
# # # # # # #
# # # # # # #
# # # # # # #         except BaseException:
# # # # # # #             raise BaseException('No More create objects')
# # # # # # #
# # # # # # #
# # # # # # # class two(metaclass=one):
# # # # # # #     Codeing = "Python"
# # # # # # #     def __init__(self,name):
# # # # # # #         print("Two __init__")
# # # # # # #         self.python = "Interputed Langauge"
# # # # # # #         self.name = name
# # # # # # #
# # # # # # #     def tool(self):
# # # # # # #         print('Yo bo')
# # # # # # #
# # # # # # # b  = one()
# # # # # # # a = two('guru')
# # # # # # # print(a.sea)
# # # # # # #
# # # # # # #
# # # # # #
# # # # # # # class method(object):
# # # # # # #     def __init__(self,one):
# # # # # # #         self.one = one
# # # # # # #
# # # # # # #     def __set__(self, instance, value):
# # # # # # #         print('Executed')
# # # # # # #         print(instance,value)
# # # # # # #
# # # # # # #     def __get__(self, instance, owner):
# # # # # # #         print(instance,owner)
# # # # # # #
# # # # # # #     def __getattr__(self,value):
# # # # # # #         print(value)
# # # # # # #
# # # # # # #
# # # # # # # b = f.arange(10,20)
# # # # # # # # print(f.random.beta(f.arange(1,10),f.arange(10,20)))
# # # # # # # print(a>2)
# # # # # # # a = method('Guruji')
# # # # # # # class method2(method):
# # # # # # #     pass
# # # # # # #
# # # # # # # if __name__ == '__main__':
# # # # # # #     p = method2('Gur')
# # # # # # #     p.one
# # # # # # #
# # # # # # # import  numpy as f
# # # # # # #
# # # # # # # print(f.random.sample((5,4)))
# # # # # # # # print(help(f.random.random_sample))
# # # # # # # print(f.random.random((8,2)))
# # # # # # # a = f.arange(0,10)
# # # # # #
# # # # # #
# # # # #
# # # # # # def tool():
# # # # # #     a = 8
# # # # # #
# # # # # # class typemethod:
# # # # # #     name = 'Guru'
# # # # # #     def __init__(self,name,bases,cdict):
# # # # # #         self.name = name
# # # # # #         self.bases = bases
# # # # # #         self.cdict = cdict
# # # # # #
# # # # # #     cls_intances = {}
# # # # # #
# # # # # #
# # # # # #
# # # # # #     def __call__(cls,*args,**kwargs):
# # # # # #
# # # # # #
# # # # # #         if cls in typemethod.cls_intances :
# # # # # #             return "YOu Are Created More Objects"
# # # # # #         else:
# # # # # #             print(cls.cdict)
# # # # # #             typemethod.cls_intances[cls] = type(cls.name,cls.bases,cls.cdict)
# # # # # #             return type('Guru',(),{})
# # # # # #
# # # # # #
# # # # # #     def __add__(self,otherself):
# # # # # #         print("Entered")
# # # # # #         return self.name + otherself.name
# # # # # #
# # # # # # class Mymethod(metaclass=typemethod):
# # # # # #     online = 'Online Classes'
# # # # # #     def __init__(self):
# # # # # #
# # # # # #         self.name = "Syed Ali"
# # # # # #         self.sirname = "Chowdary"
# # # # # #
# # # # # #     def __mro__(self):
# # # # # #         print("Cooled Brother")
# # # # # #     def __add__(self,otherself):
# # # # # #         print("Entered")
# # # # # #         return self.name + otherself.name
# # # # # #
# # # # # # my = Mymethod
# # # # # #
# # # # # # my2 = typemethod('Guru','Fuck','Tool')
# # # # # #
# # # # # # print(my2)
# # # # # #
# # # # # #
# # # # # # 1,
# # # # # # 2,13
# # # # # # 3,12,14
# # # # # # 4,11,15,22,
# # # # # # 5,10,16,21,23
# # # # # # 6,9,17,20,24,27
# # # # # # 7,8,18,19,25,26,28
# # # # # #
# # # # # #
# # # # # # #
# # # # # # # decrease  = 0
# # # # # # # value = 0
# # # # # # # for i in range(6):
# # # # # # #     for ii in range(i+1):
# # # # # # #         print(value+i+1,end=" ")
# # # # # # #         value   = value  + 6 -decrease -  1
# # # # # # #         decrease = decrease + 1
# # # # # # #     decrease =  0
# # # # # # #     value  = 0
# # # # # # #     print()
# # # # # #
# # # # # #
# # # # # # #
# # # # # # # num = 6
# # # # # # # t = 0
# # # # # # # for row in range(num):
# # # # # # #     x = 0
# # # # # # #     for colums in range(row+1):
# # # # # # #         print(x+row+1,end=" ")
# # # # # # #         x+= num-1 - t
# # # # # # #         t = t + 1
# # # # # # #     t = 0
# # # # # # #     print()
# # # # # #
# # # # # #
# # # # # # # class calculate22:
# # # # # # #     def __init_(self,name,two):
# # # # # # #         self.integer = two
# # # # # # #         self.integer2 = name
# # # # # # #
# # # # # # #     def __call__(self,*args,**kwargs):
# # # # # # #         print("Executed")
# # # # # # #
# # # # # # #     def
# # # # # # #
# # # # # # # a = calculate22()
# # # # # # #
# # # # # # # import numpy as p
# # # # # # #
# # # # # # # print(p.arange(1,13).reshape(2,3,2))
# # # # # # # print(p.sum(p.arange(1,13).reshape(2,3,2),axis=0))# 0 colums 1 row
# # # # # # # a = p.dot(3.6,8.2)
# # # # # # # b = p.array(([1,2,3,4,5,6,7,],[8,9,10,11,12,13,14])).astype(int)
# # # # # # # print(b)
# # # # # # # # print(b>2)
# # # # # # # # print(2<b)
# # # # # # # # print(b==2)
# # # # # # # print(b.itemsize)
# # # # # # # def f():
# # # # # # #     for ii in range(0,6):
# # # # # # #         yield ii
# # # # # # # a = f()
# # # # # # #
# # # # # # #
# # # # # # # for i in a:
# # # # # # #     print(i)
# # # # # # #
# # # # # # # for ii in a:
# # # # # # #     print(ii)
# # # # # #
# # # # # #
# # # # # # #
# # # # # # # value = 22
# # # # # # # decrease = 0
# # # # # # # for ii in range(0,9):
# # # # # # #     for iii in range(ii+1):
# # # # # # #         print(value,end=' ')
# # # # # # #         value-= 8-iii
# # # # # # #     decrease+= 1
# # # # # # #     value = 22 - decrease
# # # # # # #     print()
# # # # # # #
# #
# # # # Gameover = False
# # # # import pygame
# # # # x=50 ;  y = 50
# # # # running = 0
# # # # running2 = 0
# # # # import  random
# # # # snakesize = 10
# # # # snakelist = [(50,50)]
# #
# # # # foodinteger = random.choice(list(range(200,900)))
# # # # score = 0
# # # # class Snake:
# # # #     global snakelist; global snakesize
# # # #     x = 50
# # # #     y= 50
# #
# # # #     Over = False
# # # #     Display = pygame.display.set_mode((1920,1000))
# #
# # # #     def __init__(self):
# # # #         pygame.display.set_caption("Snake Game")
# #
# # # #     def music(self, song):
# # # #         import pygame
# # # #         pygame.mixer.init()
# #
# # # #         pygame.mixer.music.load(song)
# # # #         pygame.mixer.music.play()
# #
# #
# # # #     @staticmethod
# # # #     def plot_snake(gamewindow,color,snakelist,snakesize):
# # # #         for x,y in snakelist:
# # # #             print(' : ' ,snakelist)
# # # #             pygame.draw.rect(gamewindow,color,[x,y,snakesize,snakesize])
# # # #     @staticmethod
# # # #     def food(surface,Color,x_size,y_size,foodsize):
# # # #         global snakesize
# # # #         global  foodinteger
# # # #         global score
# # # #         if abs(Snake.x - foodinteger)<20  and abs(Snake.y - foodinteger )<20:
# # # #             Snake().music(r"C:\Users\mahen\Downloads\snake (1).mp3")
# #
# #
# # # #             foodinteger = random.choice(list(range(200,900,10)))
# # # #             pygame.draw.rect(surface,Color,[x_size,y_size,foodsize,foodsize])
# # # #             snakesize+= 3
# # # #             score += 10
# # # #         else:
# # # #             pygame.draw.rect(surface, Color, [x_size, x_size, foodsize,foodsize])
# # # #     @staticmethod
# # # #     def MovementControl(event):
# # # #         global running,running2
# # # #         if event.key == pygame.K_UP:
# #
# # # #             running2 = 0
# # # #             running  = -23
# # # #         if event.key == pygame.K_DOWN:
# #
# # # #             running2 = 0
# # # #             running = +23
# # # #         if event.key  == pygame.K_LEFT:
# #
# # # #             running = 0
# # # #             running2 = -23
# #
# # # #         if event.key == pygame.K_RIGHT:
# # # #             running = 0
# # # #             running2  = 23
# #
# #
# # # #     def run(self):
# # # #         import pygame
# # # #         clock = pygame.time.Clock()
# #
# # # #         global x,y
# # # #         global snakesize
# # # #         global snakelist
# # # #         global  running,running2
# # # #         pygame.font.init()
# #
# # # #         var = 0
# #
# # # #         while not Snake.Over:
# # # #             if var%240==0:
# # # #                 self.music(r"C:\Users\mahen\Downloads\loco_contigo.mp3")
# #
# # # #             var+= 1
# #
# # # #             for event in pygame.event.get():
# # # #                 if event.type == pygame.QUIT:
# # # #                     Snake.Over = True
# # # #                 if event.type == pygame.KEYDOWN:
# # # #                     self.MovementControl(event= event)
# #
# # # #             a = pygame.font.Font(r"C:\Users\mahen\bitepy\yes\yes\photos\BrusselsCityPersonalUsed-L3Lon.otf",22)
# # # #             Snake.x+= running2
# # # #             Snake.y += running
# # # #             b =  a.render(f'Score : {score}',True,'brown')
# # # #             Snake.Display.fill('white')
# # # #             Snake.Display.blit(b, (1920/2-100, 0))
# #
# #
# #
# # # #             if Snake.x <0 or Snake.x > 1920 or Snake.y <0 or 1000<Snake.y:
# # # #                 snakelist.clear()
# # # #                 if Snake.x<0:
# # # #                     Snake.x = 1900;Snake.y = Snake.y
# # # #                     snakelist.append([Snake.x,Snake.y])
# #
# # # #                 elif Snake.y<0:
# # # #                     snakelist.clear()
# # # #                     if Snake.y < 0:
# # # #                         Snake.x = Snake.x
# # # #                         Snake.y = 1000
# # # #                         snakelist.append([Snake.x, Snake.y])
# #
# # # #                 elif Snake.x>1920:
# # # #                     snakelist.clear()
# # # #                     if Snake.x > 1920:
# # # #                         Snake.x = 0
# # # #                         Snake.y = Snake.y
# # # #                         snakelist.append([Snake.x, Snake.y])
# #
# # # #                 elif Snake.y>1000:
# #
# # # #                     Snake.x = Snake.x
# # # #                     Snake.y = 0
# # # #                     snakelist.append([Snake.x, Snake.y])
# #
# #
# # # #             if len(snakelist)>snakesize:
# # # #                 del snakelist[0:10]
# # # #             # if len(set((snakelist)))>1:
# # # #             #     if list(set(snakelist))[-1] in list(set(snakelist))[:len(snakelist)-1]:
# # # #             #         print(set(snakelist))
# # # #             #         Snake.Over = True
# #
# # # #             row = 0
# # # #             for x,y in snakelist:
# #
# #
# # # #                 if row==len(snakelist)-1:
# # # #                     pygame.draw.rect(Snake.Display,'blue',[x,y,20,20])
# # # #                 else:
# #
# # # #                     pygame.draw.rect(Snake.Display, 'green',[x, y, 20, 20])
# # # #                 row += 1
# #
# #
# # # #             Snake.food(Snake.Display,'dark blue',foodinteger,foodinteger,20)
# # # #             pygame.time.set_timer(50,100)
# #
# #
# # # #             clock.tick(30)
# #
# # # #             if (50,50) not in snakelist and (Snake.x,Snake.y) in snakelist:
# # # #                 over = False
# # # #                 import time
# # # #                 while not over:
# #
# # # #                     for event in pygame.event.get():
# # # #                         if event.type == pygame.QUIT:
# # # #                             over = True
# # # #                             Snake.Over = True
# #
# # # #                         if event.type == pygame.KEYDOWN:
# # # #                             if event.key == pygame.K_p:
# # # #                                 over = True
# # # #                                 continue
# #
# #
# #
# # # #                     a = pygame.font.Font(r"C:\Users\mahen\bitepy\yes\yes\photos\BrusselsCityPersonalUsed-L3Lon.otf", 22)
# # # #                     b = a.render(f'Game Over',True,'Black')
# # # #                     Snake.Display.fill('White')
# # # #                     Snake.Display.blit(b,(1920//2-150,400))
# # # #                     c = a.render('Enter To Play Press Enter',True,'Black')
# # # #                     Snake.Display.blit(c, (1920 //2-150, 425))
# # # #                     pygame.display.update()
# # # #                     print(event)
# # # #                     time.sleep(1)
# #
# # # #             snakelist.append((Snake.x,Snake.y))
# #
# #
# # # #             pygame.display.update()
# #
# #
# # # # a = Snake()
# # # # a.run()
# # # # print(snakelist)
# #
# # # # \
# #
# # # # class method:
# # # #     def __init__(self):
# # # #         self.Owner = 'Guru Mahendrakar'
# # # #     @staticmethod
# # # #     def NewMethod(Function):
# # # #         def CoolProject(name):
# # # #             print(name)
# # # #             print("Executed By CoolProject")
# # # #             return Function()
# # # #         return CoolProject
# #
# # # #     @NewMethod
# # # #     @staticmethod
# # # #     def NewMethoding():
# # # #         return "This Is Calle New Called Method"
# #
# # # # methods = method()
# # # # methods.NewMethoding()
# # # # #
# # # # #
# # # # # class method2(method):
# # # # #     def __init__(self,Owner):
# # # # #         self.name = "Hatt Lawde"
# # # # #
# # # # #         # super(method2, self).__init__()
# # # # #
# # # # #     def Method2(self):
# # # # #         print("Method 2 object")
# #
# # # # #
# # # # # one = method2("Mahendrakar")
# # # # # print(one.__dict__)
# # # # # print(method2.mro())
# # # # # print(one.__class__.__class__)
# # # # #
# # # # #
# # # # # a = 0
# #
# # # # # class method:g
# # # # #     global a
# # # # #     def __init__(self,name,bases,cdict):
# # # # #         self.bases = bases
# # # # #         print(name,bases,cdict)
# # # # #
# # # # #     print("Entered Brother")
# # # # #     name = 'Guru'
# # # # #     @staticmethod
# # # # #     def Method3():
# # # # #         def coolbrother():
# # # # #             print("You Are Correct Brother")
# # # # #         return coolbrother
# # # # #
# # # # #
# # # # #
# # # # # class method2(method):
# # # # #     def __init__(self):
# # # # #         self.collage = 'Cb Collage Bhakli'
# # # # #         method('Guru','Mahendrakar','Fresh')
# # # # #
# # # # #
# # # # #
# # # # # # print(type(method2.__dict__))
# # # # # def splitrer(nameupper):
# # # # #     def namespliter():
# # # # #         return nameupper().split()
# # # # #     return namespliter
# # # # # def nameupper(inputer_func):
# # # # #     def nameUpperer():
# # # # #         return inputer_func()
# # # # #     return nameUpperer
# # # # #
# # # # # def inputer():
# # # # #     name= 'Guru'
# # # # #     sirname = ' Mahendrakar'
# # # # #     return name +sirname
# # # # #
# # # # #
# # # # # a = splitrer(nameupper(inputer))
# # # # # print(a())
# #
# #
# # # # '''
# # # # json.loads = str to dict
# # # # json.dumps  = dict to str
# # # # json.load(Recive in String)
# # # # json.dump(obj,file)(take only str) = take only string
# #
# #
# # # # pickle.loads  = binary to str
# # # # pickle.dumps = str to binary
# # # # pickle.dump((bytes,iterables),file) = Tumne jO Paas Kiye Hai Wahi Type Milega
# # # # pickle.load(file) = Tune Jo Uske Under Daala Hai Wahi Milega
# # # # '''
# #
# # # # #
# # # # # file = open('texting.txt','w')
# # # # # list = ['Guru',"MotherFucker","SpecialGuest","Trolling Boys"]
# # # # # dict = {'Guru':"Mahendrakar","Thriller": "Movie Of The Boss","Brown": "Rang Dii"}
# # # # #
# # # # # class method:
# # # # #     def __init__(self, name):
# # # # #         self.name = name
# # # # #
# # # # # a = method('Fucker')
# # # # # b = str(['Guru',"Mahendrakar","IgKimi"])
# # # # #
# # # # # with open('texting.txt','rb+') as f :
# # # # #     pickle.dump(json.dumps(dict),f)
# # # # #
# #
# # # # #
# # # # # list = [1,2,3,4,5]
# # # # # for i in list:
# # # # #     if 4>i:
# # # # #         print(i)
# # # # #
# # # # #     if i>4:
# # # # #         print(i)
# # # # #
# # # # #     if i<5:
# # # # #         print(i)
# # # # #
# # # # #     if 5>i:
# # # # #         print(i)
# #
# #
# # # # # a = [[col for col in range(6) ] for i in range(6)]
# # # # # low = 0
# # # # # high = 6
# # # # # counting = 0
# # # # # xleft = 0
# # # # # for rows in range(6):
# # # # #     for up in range(low,high):
# # # # #         counting+= 1
# # # # #         a[rows][up] = counting
# #
# # # # #     for right in range(low+1,high):
# # # # #         counting+= 1
# # # # #         a[right][high-1] = counting
# #
# # # # #     for down in range(high-2,low,-1):
# # # # #         counting+= 1
# # # # #         a[high-1][down] = counting
# #
# #
# # # # #     for xleftt in range(high-1,low,-1):
# # # # #         counting+= 1
# # # # #         a[xleftt][xleft] = counting
# #
# # # # #     xleft+= 1
# # # # #     low+= 1
# # # # #     high-= 1
# #
# #
# #
# # # # rows = 0
# # # # for row in a:
# # # #     for colums in row:
# # # #         if rows==0:
# # # #             print(colums,end='    ')
# # # #         else:
# # # #             print(colums,end='   ')
# # # #     rows+= 1
# # # #     print()
# #
# # # # import os;import shutil
# # # # file =[]
# #
# # # # os.chdir(r'C:\Users\mahen\bitepy\yes')
# # # # for transfer in os.listdir(os.getcwd()):
# # # #     if transfer not in file:
# # # #         shutil.move(transfer,'yes')
# # # #     else:
# # # #         print(transfer)
# # # # print(os.getcwd()+'OIP.jpeg'.replace('\\\\','/'))
# # # # dict = {'name':{'Guru':'Mahendrakar','Soul':'Mother'}}
# # # # for i in dict:
# # # #     for ii in dict[i]:
# # # #         print(dict[i][ii])
# # # # list = [1,1,3,2,5,8,9]
# #
# # # # def quicksort(listing):
# # # #     global list
# # # #     pivot = listing[0]
# # # #     a = 1
# # # #     b = -1
# #
# # # #     while not listing[a]>pivot:
# # # #         a+= 1
# # # #         print('Executed')
# #
# # # #     while not listing[b]<=list[a]:
# # # #         b-= 1
# #
# # # #     if b<a:
# # # #         list[pivot],list[b] = list[b],list[pivot]
# #
# # # #     else:
# # # #         list[a],list[b] = list[a],list[b]
# #
# #
# # # #     return listing
# #
# # # # print(quicksort(quicksort(quicksort(list))))
# #
# #
# # # # Please Note You Can Basic Learner Please Time Too Forloop With this type
# #
# # # # integers= 0
# #
# # # # for row in range(6):
# # # #     for colums in range(row+1):
# # # #         print(integers,end=" ")
# # # #         integers+= 1
# # # #     integers = 0
# # # #     print()
# #
# # # # for row in range(6):
# # # #     for colums in range(row+1):
# # # #         integers+= 1
# # # #         print(integers,end=" ")
# #
# # # #     integers = 0
# # # #     print()
# # # # import random
# #
# # # # for rows in range(int(input("Enter Lines Of Number : "))):
# # # #     for colums in range(random.randint(0,20)):
# # # #         print(" ",end=" ")
# #
# #
# # # #     print("*",end=" ")
# # # #     if rows%10==0:
# # # #         print("Happy Birthday Guru Mahendrakar")
# #
# #
# # # # set1 = set([1,2,3,4])
# # # # set2 = set([5,6,7,8])
# #
# # # # print(set1.union(set2))
# # # # print(set2.difference(set1))
# # # # print(set1.intersection(set2))
# #
# #
# # # # import timeit
# #
# # # # def quicksort(lists):
# #
# # # #     if len(lists)<=1:
# # # #         return lists
# # # #     else:
# # # #         sequence = lists.pop()
# # # #     greater = []
# # # #     lower = []
# # # #     for items in lists:
# # # #         if items>sequence:
# # # #             greater.append(items)
# # # #         else:
# # # #             lower.append(items)
# #
# # # #     return (quicksort(lower)+[sequence] + quicksort(greater))
# # # # import time
# # # # a = time.time()
# # # # print(quicksort(list))
# # # # print(time.time()-a)
# # # # a = 0
# # # # def recursion():
# # # #     global a
# # # #     a+=1
# # # #     if a==5:
# # # #         return "A Now is : 5"
# #
# # # #     else:
# # # #         return recursion()
# # # # print(recursion())
# #
# #
# #
# #
# #
# # # # def decorator_2(decorator_1):
# # # #     def circus():
# # # #         print("Welcome To My Circus")
# # # #         print(decorator_1())
# #
# # # #     return circus
# #
# #
# # # # def Board_capitalize(decorator_2):
# # # #     def Board_():
# # # #         print("The Owner IS Guru Mahendrakar")
# # # #         print(decorator_2())
# # # #     return Board_
# #
# #
# # # # @Board_capitalize
# # # # @decorator_2
# # # # def decorator_1():
# # # #     Name = input("Enter Name : ")
# # # #     Sirname = input('Enter Sirname : ')
# # # #     return Name + Sirname
# #
# # # # decorator_1()
# #
# #
# #
# #
# # # # class name_setter:
# # # #     def __init__(self,Name,Sirname):
# # # #         self.Name = Name
# # # #         self.Sirname = Sirname
# #
# #
# # # #     @property
# # # #     def Sirname_Changer(self):
# # # #         return self.Sirname
# #
# # # #     @Sirname_Changer.setter
# # # #     def Sirname_Changer(self,New_name):
# # # #         self.Sirname = New_name
# #
# #
# # # # ame = name_setter("Nitin","Mahendrakar")
# # # # ame.Sirname_Changer = "Rathod"
# # # # print(ame.__dict__)
# # # # print(ame.Sirname)
# #
# #
# #
# # # # class Guru_range:
# # # #     def __init__(self,start,end):
# # # #         self.start = start
# # # #         self.end = end
# #
# # # #     def __iter__(self):
# # # #         return self
# #
# #
# # # #     def __next__(self):
# # # #         if self.start==self.end-1:
# # # #             raise StopIteration("Finished Work Do Not More Work")
# # # #         else:
# # # #             self.start+= 1
# # # #             return self.start
# # # # G = Guru_range(-1,8)
# #
# #
# # # # for ii in G:
# # #     # print(ii)
# #
# #
# #
# # # # array = [1,15,5,1,5,2,5,6,2]
# # # # print(array)
# # # # a  = 1
# # # # b = -1
# # # # pivot = 0
# # # # A_True = True
# # # # B_True =  True
# #
# # # # class quicksort:
# #
# # # #     @staticmethod
# # # #     def A_Handler():
# # # #         global array,a,b,A_True
# # # #         while not array[a]>array[pivot]:
# # # #             a+= 1
# #
# # # #             if a==len(array)-1:
# # # #                 A_True = False
# # # #                 break
# #
# # # #     @staticmethod
# # # #     def B_Handler():
# # # #         global array,a,b,B_True,pivot
# #
# # # #         while not array[b]<=array[pivot]:
# # # #             b-=1
# # # #             if abs(b)==len(array):
# # # #                 if pivot<len(array):
# # # #                     pivot+= 1
# # # #                 array[pivot],array[b] = array[b],array[pivot]
# # # #                 break
# #
# # # #             # 5   2   2   3   7   6
# # # #             # 0   1   2   3   4   5
# # # #             #-6  -5  -4  -3  -2  -1
# # # #         if array[b] in  array[a:] :
# # # #             array[a],array[b] = array[b],array[a]
# # # #         else:
# # # #             array[pivot],array[b] = array[b],array[pivot]
# #
# #
# #
# #
# # # # U = quicksort()
# # # # for i in range(3):
# # # #     U.A_Handler()
# # # #     U.B_Handler()
# # # # print(array)
# #
# #
# #
# # # # # class method:
# #
# # # # #     def __init__(self):
# # # # #         self.name = "GURU MAHENDRAKAR"
# #
# # # # #     def __get__(self):
# # # # #         return self.name
# #
# # # # #     def __set__(self,new_name):
# # # # #         print("Called Brother")
# # # # #         self.name = new_name
# # # # #         return self.name
# #
# # # # # a = method()
# # # # # a.name = "Guru"
# # # # # print(a.__set__("Guru Mahendrakar"))
# # # # # print(a.__get__())
# #
# #
# # # # from array import array
# # # # from cmath import pi
# # # # from copyreg import pickle
# #
# #
# #
# #
# #
# # # # list = [8,9,11,2,3,-1,2,5,2,5,3,2,3,56,67,7,73,32,2,2,3,5,6,6,78,8888,88888888888,999999999999,0000000,222222222,2222,2,222]
# #
# # # # x = 1
# # # # y = -1
# # # # pivot = 0
# # # # pivot_checker = pivot
# # # # class quicksort:
# # # #     def __sort__(self):
# # # #         while pivot!=len(list)-1:
# # # #             @staticmethod
# # # #             def x():
# # # #                 global x
# # # #                 while not list[x]>list[pivot]:
# #
# # # #                     if x==len(list)-1:
# # # #                         break
# #
# # # #                     else:
# # # #                         x+= 1
# #
# #
# # # #             @staticmethod
# # # #             def y():
# # # #                 global y,pivot,x,pivot_checker
# # # #                 while not list[y]<list[pivot]:
# #
# # # #                     if abs(y)==len(list)-pivot:
# # # #                         pivot+=1
# # # #                         if pivot>3:
# # # #                             x = pivot+1
# # # #                         y = -1
# # # #                         break
# #
# # # #                     else:
# # # #                         y-= 1
# # # #                 if list[y] in list[x:]:
# # # #                     list[x],list[y] = list[y],list[x]
# #
# # # #                 if list[y] not in list[x:]:
# # # #                     list[pivot],list[y] = list[y],list[pivot]
# #
# #
# # # #                 if x<len(list):
# # # #                     if list[y]==list[x] and x==len(list)-1:
# # # #                         list[pivot],list[y] = list[y],list[pivot]
# # # #             x()
# # # #             y()
# #
# # # # U  = quicksort()
# # # # import time
# # # # a = time.time()
# # # # U.__sort__()
# # # # print(time.time()-a)
# # # # print(list,x,y,pivot)
# #
# #
# #
# # # # class method:
# #
# # # #     @staticmethod
# # # #     def cool(One):
# # # #         print(" Decorator Uses This Function {}".format(One))
# #
# # # # method = method()
# #
# #
# # # # @method.cool
# # # # def mydetails():
# # # #     print(""" "Name"  : "Guru" """)
# #
# #
# # # # import time
# # # # from threading import Thread
# #
# # # # def youtube():
# # # #     print("Video Is Uploading Brother")
# # # #     time.sleep(3)
# # # #     print("video is Uploaded Brother")
# #
# #
# # # # def checking_copyright():
# # # #     print("Copyrighted sorry video was deleted ")
# #
# #
# # # # upload = Thread(target = youtube)
# # # # copy_check = Thread(target=checking_copyright)
# # # # upload.start()
# # # # upload.join()
# # # # copy_check.start()
# #
# #
# #
# # # # import tkinter
# #
# #
# # # # surface = tkinter.Tk()
# # # # surface.geometry("500x600")
# # # # surface.minsize(200,300)
# # # # surface.maxsize(600,800)
# # # # text_Name = tkinter.Label(surface,borderwidth = 8,text="Guru Mahendrakar",bg='black',foreground='white',padx=33,pady=55,relief=tkinter.SUNKEN)
# #
# # # # text_Name.pack(side=tkinter.LEFT,fill = tkinter.X)
# # # # text_Name.pack(side=tkinter.LEFT,fill=tkinter.Y)
# # # # surface.mainloop()
# #
# # # # import threading
# # # # import time
# # # # def own(arg):
# # # #     for i in range(arg):
# # # #         print("Threading Name : ",threading.current_thread().name)
# # # #         print("Threading Nows Working :",threading.active_count())
# # # #         time.sleep(2)
# # # #         print("---------------------------------------")
# # # # begin_time = time.time()
# # # # Target = threading.Thread(target=own,args = (5,))
# # # # Target2 = threading.Thread(target=own,args= (5,))
# # # # Target.name="Guru"
# # # # Target2.name = "Nitin"
# # # # Target.start()
# # # # Target2.start()
# # # # Target.join()
# # # # Target2.join()
# # # # print(time.time()-begin_time)
# #
# #
# #
# # # # import os
# # # # import shutil
# #
# # # # os.mkdir("photos_files")
# # # # for files in os.listdir(os.getcwd()):
# #
# #
# # # # import os
# # # # import shutil
# # # #shutil.move(path,file)
# #
# # # # list_photos = os.chdir("alworks")
# # # # list_photos_files = os.listdir(os.getcwd())
# # # # os.chdir(r"C:\Users\mahen\bitepy")
# # # # python_files = []
# # # # for files in os.listdir(r"C:\Users\mahen\bitepy"):
# # # #     if files.endswith(".py") or files.startswith('.git') or files.startswith('__pycache__')  or files.startswith("photos_filess"):
# # # #         python_files.append(files)
# #
# # # # class method:
# # # #     def __init__(self):
# # # #         self.one = "Guru Mahendrakar"
# #
# # # #     def __set__(self,name,value):
# # # #         print("Value Is Setted Brother")
# #
# #
# # # #     def __get__(self,one):
# # # #         print("Value Is Getted Brother")
# # # #         return one
# #
# # # #     def __del__(self):
# # # #         print("Garbage Collecter Is Executed")
# # # # a = method()
# # # #
# #
# # # #
# # # # string = "a=8 b=9 c=7"
# # # # string = list(map(lambda a : a.split("="),string.split(" ")))
# # # # a = dict(map(lambda x : [x[0],int(x[1])] ,sorted(string,key= lambda x :x[1])))
# # # #
# # # # print(a)
# #
# #
# #
# # # #iadd - means iterable to iterable ko plus karna hai to iadd use karo
# #
# #
# #
# # # # import itertools
# # # # import operator
# # # # import collections
# # # #
# # # #
# # # # a = itertools.combinations([1,2,3,4,5],3)
# # # # b = itertools.permutations([1,2,3,4,5],3)
# # # # c = itertools.chain([1,2,3,4,5]) # generator return
# # # # d = itertools.count(start = 1 ,step=1) # end nahi hai isme aap if else lagake break maroge to hi break hoga
# # # # e = itertools.groupby('aaabbbcccjlabioup',key= lambda x :  x=='a' or x=='b')
# # # #
# # # # print(list(a))
# # # # print(list(b))
# # # # print(list(c))
# # # # # print(list(d))
# # # #
# # # # for x in e :
# # # #     print(x[0],list(x[1]))
# # # #
# # # # print(list(itertools.islice([1,2,3,4,5],0,2)))
# # # #
# #
# #
# #
# # # #
# # # #
# # # # dict = [{"Car":50000},{"Car":20000},{"Car":30000}]
# # # #
# # # #
# # # # min = min(dict,key=lambda x: x['Car'])
# # # # max = max(dict,key=lambda x: x['Car'])
# # # # sorted = sorted(dict,key=lambda x:x['Car'])
# # # #
# # # # print(min) # min(iterable,key=func)
# # # # print(max) # max(iterable,key=func)
# # # # print(sorted) # sorted(iterable,key=func)
# #
# # # #
# # # # string = "Guru Mahe\ ndrakar  Ståle "
# # # #
# # # # print(string.encode(encoding= 'utf-8'))
# # # #
# # # # p = (string.encode('latin-1'))
# # # #
# # # # print(p.decode(encoding='latin-1'))
# #
# #
# # # # enocodeing = bytes(s,encoding = 'utf-8')
# # # #
# # # # print(enocodeing.decode(encoding='utf-8'))
# #
# # # # #
# # # # butes = bytearray('Guruji»»»øø�ɷ',encoding='utf-16')
# # # # butes[0] = 6
# # # # print(chr(butes[-1]))
# # # # #
# # # # print(butes.decode('utf-16'))
# #
# #
# # # # class method:
# # # #     def __init__(self) -> None:
# # # #         self.start = 0
# # # #         self.end = 8
# #
# #
# #
# # # #     def __next__(self):
# # # #         one_more = self.start
# # # #         if one_more<self.end:
# # # #             self.start+=1
# # # #             return one_more
# #
# # # #         else:
# # # #             raise StopIteration('not more have elements--')
# #
# # # # a = method()
# #
# #
# #
# #
# # # # class method3:
# # # #     def __init__(self):
# # # #         self.collage = "Cb college Bhalki"
# #
# #
# # # #     def fuckYOu(self):
# # # #         print('fuck you brother>>>>>>>>')
# #
# #
# # # # class method(type):
# # # #     def __init__(self,name,bases,cdict):
# #
# # # #         self.name = 'Guru'
# #
# #
# # # #     def __call__(self):
# # # #         return 'not class>. eExecuted brother'
# #
# #
# # # # class method2(metaclass = method):
# # # #     def __init__(self):
# # # #         self.sirname = "Mahendrakar"
# #
# #
# #
# # # # tyeeee = type('new-method',(method3,),{'name':"Guru Mahendrakar"})
# #
# # # # print(tyeeee().__dict__)
# #
# #
# #
# # # # import tkinter
# # # # from tkinter import ttk
# # # # from tkinter import messagebox
# #
# # # # import ttkthemes
# # # # window = ttkthemes.ThemedTk(theme='Equilux')
# # # # window.title('timepass')
# #
# #
# #
# # # # treeview = ttk.Treeview(window,columns=['#0','#1','2'],selectmode=tkinter.EXTENDED)
# # # # treeview.pack()
# #
# #
# # # # scale = ttk.Entry(window,text='Hello')
# # # # scale.pack()
# #
# # # # def selected(event):
# # # #     print(treeview.get_children())
# # # #     print(treeview.focus())
# # # #     print(treeview.item(treeview.focus()))
# # # #     s = messagebox.askyesno('Delte','You Want To Delete')
# # # #     treeview.delete(treeview.focus()) if s else messagebox.showinfo('information','Ok Deleting Cancel')
# #
# # # # for x in range(0,3):
# # # #     treeview.heading(x,text=['name','sirname','college'][x])
# #
# #
# # # # bb = treeview.insert('',0,text='details',values=['one','two','three'],open=True)
# #
# # # # treeview.insert(bb,text='fuck',index = 0 ,values=['four','five','six'],open=True)
# #
# # # # treeview.bind('<<TreeviewSelect>>',func=selected)
# #
# # # # if __name__ == '__main__':
# # # #     window.mainloop()
# #
# #
# #
# # # # list = [1,2,3,4,5,6,7,8]
# #
# # # # print(len(list)//2)
# # # # print((len(list)-1)//2)
# #
# #
# #
# # # # list = [1,2,55,333,555,888,8888,9999]
# # # # k,x,y = len(list),0,len(list)
# #
# # # # import time
# # # # while 1:
# #
# # # #     k = (x+y)//2
# #
# # # #     if 888!=list[k]:
# #
# # # #         if list[k]>888:
# # # #             y = k-1
# #
# # # #         else:
# # # #             x = k+1
# #
# # # #     else:
# # # #         print('target found-')
# # # #         break
# #
# #
# #
# # # # class method:
# # # #
# # # #     def __init__(self,name,sirname,rollno):
# # # #         self.name  = name
# # # #         self.sirname = sirname
# # # #         self.rollno = rollno
# # # #         self.information = 'Please Inherited for anthoer information!!'
# # # #
# # # #
# # # #
# # # # def __init__(self):
# # # #     self.nickname = 'nitin'
# # # #
# # # # class method2(method):
# # # #
# # # #     def __init__(self):
# # # #         super(method2, self).__init__('Guru','Mahendrkar',39)
# # # #
# # # #
# # # # method_ = method('Guru','Blaster',29)
# # # # method2_ = method2()
# # # #
# # # # print(5 not in [1,2,3])
# #
# #
# # # # a = 8
# #
# # # # def _you():
# # # #     print('Im Codeing..')
# #
# # # # if __name__ == '__main__':
# # # #     _you()
# # # #
# # # # class method:
# # # #     one_ = 8
# # # #
# # # #
# # # #     def _onee(self,a):
# # # #         print('_---_')
# # # #
# # # #
# # # # s  = method()
# # # #
# # # # s._onee('guru')+
# # # #
# # # # print(s._onee)
# #
# # # #
# # # # import typing
# # # # class mygenrator:
# # # #
# # # #     def __iter__(self):
# # # #         return self
# # # #
# # # #     def __next__(self):
# # # #         return self.
# # # #
# # # # class method:
# # # #
# # # #     def __iter__(self):
# # # #         return self
# # # #
# # # #     def __next__(self)-> str :
# # # #         a = ['Guru','Mahendrakar']
# # # #
# # # #         if a :
# # # #             return a[-1]
# # # #
# # # #
# # # #
# # # #
# # # # def funcGenrator()->typing.Generator:
# # # #
# # # #     print('__Genrator Entered__')
# # # #
# # # #     yield 'func yield'
# # # #     yield 'cool'
# # # #
# # # #
# # # # funcgenrator = funcGenrator()
# # # #
# # # # print(funcgenrator.__next__())
# #
# # # #
# # # #
# # # # for x in a:
# # # #     print(xx(x))
# # # # else:
# # # #     print('Data Was clear',list(a))
# # # #
# # # # butes = bytearray('Guruji%%%%',encoding='latin-1')
# # # # butes[0] = 65
# # # #
# # # # print(butes.decode('latin-1'))
# # # #
# #
# # # # a = itertools.chain(['Guurmau',1,2,3,4,5])
# # # # b = itertools.groupby('aaabbbcccddcc')
# # # # for x,y in b:
# # # #     print(x, list(y))
# #
# # # # import builtins
# # # # a = (x for x in range(3))
# # # # print(2 in a)
# # # #
# # # # x = 8
# # # #
# # # # class method:
# # # #     def __init__(self):
# # # #         self.name = [self.tool]
# # # #
# # # #     def tool(self,name):
# # # #         return name.upper()
# # # #
# # # #
# # # #
# # # #
# # # # a = method()
# #
# # # # def tool():
# # # #     for x in range(1):
# # # #         print(a.name[x]('Guru'))
# # # #
# # # # tool()
# #
# # # class method:
# #
# # #     def __init__(self,*args):
# # #         self.args = args
# #
# # #     def __str__(self):
# # #         return '{}'.format(list(self.args))
# #
# # #     def _SoBeautiful(self):
# # #         print('Hey Man !!')
# #
# # #     def uou(self):
# # #         print('How Many Likes In the Cool!!')
# #
# # # o = method(1,2,3,4,5)
# #
# # # # print(method.__dict__['uou'](1))
# #
# # # #
# # # # def tool():
# # # #     print('HOw Many Likes !! ')
# # # #
# # # # a  = tool
# # # # a.name = 'Guru'
# # # # a.name= 'Guru Mahendrakar'
# # # #
# # # # print(a.name)
# #
# # # #
# # # # class method:
# # # #     pass
# # # #
# # # #
# # # # class method2(method):
# # # #
# # # #     def __init__(self):
# # # #         self.name = "Guru"
# # # #
# # # #
# # # # a = method()
# # # # print('guruji')
# # # # print(method2.__bases__)
# #
# # # class method:
# #
# #
# # #     def __init_subclass__(cls, **kwargs):
# # #         print('you inherited your class any another class') # kisi class mein aap inhetance karoge to ye print hoga
# #
# #
# #
# # # a = method()
# #
# # # import  json
# #
# #
# # # # dict_ = f"""{dict.fromkeys(['Guru',"Pravin","Ajay"],"Hello Friends")}"""
# # # # dict_ = '{"Guru":"Mahendrakar","City":"Bhalki"}'
# #
# # # # print(json.loads(dict_)['Guru']) # (str to dict & strlist to list)
# # # # print(json.dumps([5,3,2,1],indent=4,sort_keys=True)) # (dict to str  & list to strlist)
# # # #
# # # # with open('texting.txt','w') as fw:
# # # #     json.dump({'Guru':"Mahendrakar"},fw) # andar jo type daal hai wahi milega --> ab maine normal dict daal hai json.load karne pe
# # # #                                             # normal dict return hoga ----- Maine Agar str dict dalta to str dict return karta
# # # #
# # # # with open('texting.txt') as f:
# # # #     print(type(json.load(f)))
# #
# # # #
# # # # import pickle
# # # #
# # # # dict_ = '{"Guru":"Mahendrakar","City":"Bhalki"}'
# # # #
# # # # with open('texting.txt','rb+') as f:
# # # #     pickle.dump(dict_,f) # stored( ��*       �&{"Guru":"Mahendrakar","City":"Bhalki"}�.) UTF-8 FORMAT
# # # #     # pickle.dump() # class ke object bhi jaa sakte hai
# # # #
# # # #
# # # # with open('texting.txt','rb') as f:
# # # #     print(pickle.load(f)) # return normal format UTF-8 to reading Foramt
# # # #
# # # #     # dump karte waqt jaisa object daala hai Wo HI type(dict,str,list,set,tuple,object) # milega
# # # #
# # # #
# #
# # # import functoolss
# #
# #
# # # # print(functoolss.addition.__code__.co_consts) # his return values
# # # # print(functoolss.addition.__code__.co_argcount) # kitne arguments dene hai funcion me batayega
# # # # print(functoolss.addition.__code__.co_varnames) # kitne function me object hai return karega
# #
# # # #---outputs----
# # # # (None, 'Guru')
# # # # 3
# # # # ('self', 'a', 'b', 'c')
# #
# # # import sys
# #
# # # # a = (x for x in range(10000000))
# # # # print(sys.getsizeof(a))
# # # #
# # # # b = [x for x in range(10000000)]
# # # # print(sys.getsizeof(b))
# #
# # # #
# # # # def tool():
# # # #     print('---cool--')
# # # #     for x in range(5):
# # # #         if x<2:
# # # #             yield x
# # # #
# # # #     print(locals())
# # # #     print(x)
# # # #
# # # # a = tool()
# # # # print(next(a))
# # # # print(next(a))
# # # # try:
# # # #     print(next(a))
# # # # except:
# # # #     pass
# # # # def tool2():
# # # #     for x in range(5):
# # # #         pass
# # # #
# # # #     locals()
# # # #     print(x)
# # # # print('----tool2---')
# # # # tool2()
# #
# # # # print(next([].__iter__()))
# #
# # # #
# # # # class method:
# # # #
# # # #     def __init__(self):
# # # #         self.name = 1
# # # #     def __index__(self):
# # # #         return self.name
# # # #
# # # #
# # # # a = method()
# # # #
# # # # print([1,2,3][a])
# #
# #
# # # # def _checking():
# # # #     a = 8
# # # #     for x in range(3):
# # # #         a = a-x
# # # #
# # # #     print(a)
# # # # a = _checking
# # # # print(a())
# # # # print(a())
# # # # print(a())
# #
# # # #
# # # #
# # # # class so:
# # # #
# # # #     __slots__ = ['name','sirname','__dict__']
# # # #     def __init__(self,name,sirname):
# # # #         self.name = name
# # # #         self.sirname =sirname
# # # #
# # # #         print(sys.getrefcount('Mahendrakar '))
# # # #     @property
# # # #     def __dict__(self):
# # # #         return globals()
# # # #
# # # #
# # # #
# # # # a = so('Guru',"Mahendrakar")
# # # # print(a.name)
# # # # a.cool = 'Gur'
# # # #
# # # # print(a.__dict__)
# # # # print(sys.getsizeof(a))
# #
# #
# # # # a = [1,2,3,4].__iter__()
# # # #
# # # # print(a.__next__())
# # # #
# # # #
# # # #
# # # # def __init__(self):
# # # #     print('__init__')
# # # #     self.one = 1
# # # #
# # # # print(type(__init__))
# # # # c = type('Guru',(),{'__dict__':{'Fuck'}})
# # # # print(id(0x00000172FF0D6EE0))
# # # #
# # # # class two:
# # # #
# # # #     def fun(self):
# # # #
# # # #         print('this is self',self.a)
# # # #
# # # # k = c()
# # # # twoo = two()
# # # # k.a = 'guru'
# # # # print(two.fun(k))
# # # #
# # # #
# # # #
# # # # a = str.encode('Guru',encoding='latin-1')
# # # # print(a.decode(encoding='raw_unicode_escape'))
# # # # print('\xff\xfeG\x00u\x00r\x00u\x00')
# #
# # # import collections
# #
# # # #
# # # # class king:
# # # #
# # # #     def __init__(self):
# # # #
# # # #         self.name = "Guru"
# # # #         self.sirname = "Mahendrakar"
# # # #
# # # #     def __repr__(self):
# # # #         print(self.name,self.sirname)
# # # #
# # # #
# # # #     def one(self):
# # # #         self.name = "Guruji Mahendrakar"
# # # #
# # # #
# # # # c = king()
# # # # c.__repr__()
# # # # c.one()
# # # #
# # # # k = king()
# #
# # # def trying():
# # #     pass
# #
# # # import sys
# #
# # # print(' Before_int__ 8 referances ',sys.getrefcount(1021))
# # # x = 1021
# # # print('__middle__',sys.getrefcount(1021))
# # # y  = 1021
# # # print(' after _int__ 8 referances ',sys.getrefcount(1021))
# #
# #
# # # print(id(x))
# # # print(id(y))
# #
# # # print(' Before _str__ 8 referances ',sys.getrefcount("Python"))
# # # s = "Python"
# # # ss = "Python"
# #
# # # print('Python  ',id(s))
# # # print('Python ',id(ss))
# #
# # # # var = input("Enter name : ")
# # # # print(id(var))
# #
# # # def fun():
# # #     return "Python"
# #
# # # print(fun)
# # # print('function adresss ',id(fun()))
# #
# # # a = "Python"
# #
# #
# # # print(' after __str__ 8 referances ',sys.getrefcount("Python"))
# #
# # # list = [1,5,2,5,2,15,5,0]
# # #
# # # for xi in range(len(list)):
# # #     for x in range(xi,len(list)):
# # #         #xi = 0
# # #
# # #         if list[xi]>list[x]:
# # #             print(x,end=' - ')
# # #             list[xi],list[x] = list[x],list[xi]
# # #
# # # print(list)
# #
# #
# #        #0 1 2 3
# #
# # # list = [3,2,0,2,1]
# # # i = 0
# # #
# # # while  i< len(list):
# # #     print(i)
# # #     j = 0
# # #     while j<len(list):
# # #         if list[i]>list[j]:
# # #             o = list[i]
# # #             list[i] = list[j]
# # #             list[j] = o
# # #
# # #         print(j,end=' ')
# # #         j+=1
# # #
# # #     i+=1
# # #     print()
# # #
# # # import dataclasses
# # # import collections
# # #
# # # @dataclasses.dataclass(frozen=True,order=True)
# # # class method:
# # #
# # #     name : str
# # #     sirname : str
# # #     age : int
# # #
# # #
# # # a = method('guru','mahendrakar',18)
# # # b = method('guru','mahen',17)
# # # #
# # # # print(sorted((a,b)))
# # #
# # # import sys
# # # namedtuple = collections.namedtuple('Guru'," a b c")
# # # s = namedtuple('s','b','ss')
# # #
# # # namedtuple.a = "Guru"
# # # namedtuple.b = "King"
# # # namedtuple.c = "HellO"
# # #
# # # print(s.index('s'))
# # # print(s)
# # #
# # #
# # # #
# # #
# # from contextlib import contextmanager
# # import sys
# # @contextmanager
# # def cntext():
# #     x = open('texting.txt','r')
# #     yield x
# #     x.close()
# import sys
# # def one():
# #     return open('texting.txt','r')
#
#
# # with one() as f:
# #     print(f.read())
#
# # with cntext() as ff:
# #     print(ff.read())
#
# # print(f.closed)
# # print(ff.closed)
#
# # from contextlib import contextmanager
# # from abc import ABC, abstractmethod
#
# # class a(ABC):
# #     @abstractmethod
# #     def car(self):
# #         print('__car__ a ')
#
# #     def bike(self):
# #         print('__bike__ a ')
#
#
# # class b(a):
#
# #     def car
#
# # bb = b()
#
# # #
# # import mysql.connector
# #
# # a = mysql.connector.connect(user='Guru',password='7411891852',host='localhost',database='world',port=3306)
# # myx = a.cursor()
# # myx.execute('create database pdb'
#
#
#
# # now_time = datetime.datetime.now()
# # expire_time = datetime.timedelta(days=#enter day how many day increse)->int type
# # expire_time = now_time + expire_time
#
#
# # import time
# # def days_checking():
#
#
# #         while True:
# #             now_time = datetime.datetime.now()
# #             c = ((now_time.day,
# #             now_time.month,
# #             int(now_time.second),
# #             now_time.year))
#
# #             d = (expire_time.day,
# #                 expire_time.month,
# #                 int(expire_time.second),
# #                 expire_time.year)
# #             if c != d:
# #                 print('__not expire__')
# #             else:
# #                 print('__expired__')
# #                 break
#
# # days_checking()
#
#
# # import datetime
# # import csv
# # import re
#
# # class datetime_cheking:
#
#
# #     def __init__(self) -> None:
# #        self.simcardrecharge = 'expire'
#
#
# #     def __expiretime__(self):
# #         with open('texting.txt') as time:
# #             print(time.readline)
# #             print(time.readline)
#
#
# #     def recharge(self):
#
# #         if self.simcardrecharge =='expire':
# #             recharge = int(input('\t 1 : 1 Month Subcription\n \
# #             2 : 2 Month Subcription\n \
# #             3 : 365 Days Subcription'))
#
# #             now_datetime = datetime.datetime.now()
#
# #             with open('texting.txt','w') as timee:
# #                 csv.writer(timee).writerows([['DAY','MONTH','YEAR'],
# #                 [now_datetime.day,now_datetime.month,
# #                 now_datetime.year]])
#
# #         else:
# #             print("Already Recharged")
#
#
# # x = datetime_cheking()
# # x.recharge()
# # x.
#
#
#
# # recharge = int(input('\t 1 : 1 Month Subcription\n \
# # #             2 : 2 Month Subcription\n \
# # # #             3 : 365 Days Subcription'))
# # import tkinter
# # from tkinter import messagebox,ttk
# #
# # time = datetime.datetime.now()
# #
# # import re
# # import pprint
# #
# #
# #
# #
# #  # isko aap sql me load karna hai ya kisi file me
# # import time
# # window = tkinter.Tk()
# # with open('texting.txt','r') as ff:
# #     time__ = ff.read()
# #     expire_time = re.findall("\d+",time__)
# #     expire_dict = {'Year':expire_time[0],
# #     "Month":expire_time[1],
# #     "Day":expire_time[2],
# #     "Hour":expire_time[3],
# #     "Minutes":expire_time[4],
# #     "Seconds":expire_time[5],
# #     "MiliSeconds":expire_time[6]}
# #
# # def expireing_check():
# #     while True:
# #         a = (expire_time)
# #         b  = (re.findall('\d+',str(datetime.datetime.now())))
# #         if (a[:-1]) == (b[:-1]):
# #             tkinter.Label(window,text='Recharge Was Expired').pack()
# #             time.sleep(0.20)
# #             break
# #
# #         else:
# #             print(a,b)
# #
# #
# #
# # expireing_check()
# #
#
# import time
#
# import numpy
#
# #
# # class method2:
# #     def __init__(self,roll):
# #         self.name = "Guru"
# #         self.sirname = "Mahendrakar"
# #         self.roll = roll
# #
# #     def __delattr__(self, item):
# #         print("__Delattr-__")
# #         self.__dict__.pop(item)
# #
# #
# #
# #
# #     def __and__(self, other):
# #         print(self,other)
# #
# #
# #     def __del__(self):
# #         print('Objects Are Cleared In Heap')
# #
# #
# #     def __lt__(self, other):
# #         print('__called__')
# #         return self.roll>other.roll
# #
# #
# #     def __gt__(self, other):
# #         return  self.roll>other.roll
# #
# #
# #
# #     def __and__(self,other):
# #         return self.roll & other.roll
# #
# #     def __class_getitem__(cls, item):
# #         print('__class getitem___`')
# #
# #     def one(self):
# #         print('__one__')
# #
# #
# # a = method2(8)
# # a.one
#
#
# a = str([1,2,3,4])
#
#
# print(a.replace('[','').replace(',','').replace(']',''))
# =======
# # # #
# # # # date_of_birth = [f'Name : Guru ',f"Roll NO : 51",f"Collage Name : Cb Collage Bhalki"]
# # # # a = str(date_of_birth).encode()
# # # # store_previous_binary = ''
# # # # with open('texting.txt','rb')as file:
# # # #     store_previous_binary = file.readlines()
# # # # for i in store_previous_binary[0]:
# # # #     print(type(i))
# # # #
# # # #
# # # # import sys
# # # #
# # # # c = sys.argv
# # # # print(c[1:],c[:])
# # # #
# # # #
# # # # import random
# # # # x = 'Guru'
# # # # y = 'cool'
# # # # def fun():
# # # #     return 'Guru Mahendrakar'
# # # #
# # # # while True:
# # # #     eve = eval(input('Enter The input'),{'fun': fun,__builtins__: None,'x':x},{y:'y'})
# # # #     print(type(eve),eve)
# # # #
# # # #
# # # # Importing library
# # # # import qrcode
# # # #
# # # # qr = qrcode.QRCode(version=15,box_size=10,border=3)
# # # # data = 'https://www.geeksforgeeks.org/generate-qr-code-using-qrcode-in-python/'
# # # # qr.add_data(data)
# # # # qr.make(fit=True)
# # # # a = qr.make_image(fill = 'white',background = 'black')
# # # # a.save('songr.png')
# # # #
# # # # lista = [1,2,3,4,5]
# # # # # def check():
# # # # #     for i in range(6):
# # # # #         yield i
# # # # #
# # # # # a = check()
# # # # # print(list(a))
# # # # # print(list(a))
# # # # #print(list(map(lambda a :a if a<4 else -1,lista,)))
# # # # #
# # # # # import functools
# # # # #
# # # # # print(functools.reduce(lambda x,y:x+y,[1,2,3,4,5,6]))
# # #
# # # # # def tool(a,b):
# # # # #
# # # # #     print(a)
# # # # #
# # # # # a = [1,2,3,4,5,6]
# # # # #
# # # # # b = iter([7,8,9,10,11,12])
# # # # #
# # # # # a[4] = next(b)
# # # # # print(a)
# # # # #
# # # # # Enter_name = input("Enter A Name Brother")
# # # # # Enter_sirname = input("Enter a Sirname")
# # # # #
# # # # # print('Welcome To You Sir' if Enter_name == Enter_name.capitalize() else 'Please Follow Rules' if len(Enter_name)==4 else 'Not Followed rules by brother')
# # # #
# # # # import random
# # # # import time
# # # # # a = dict((('a','Guru'),('b','Cool')))
# # # # # b = a['Guru'] = "Mahendrakar"
# # # # # print(b)
# # # # #
# # # # Holder_names = []
# # # # Created_Holder_Account_numbers = []
# # # # Register_numbers = 741189185200
# # # # Holdername = input('Enter The Name : \t');AccountBalance = int(input('How Do You Money Have \t : '))
# # # # All_information_bank = {}
# # # # class Bank:
# # # #     global Register_numbers
# # # #     Register_numbers+= 1
# # # #     global Holder_names
# # # #     def __init__(self,Holdername,AccountBalance = 0,Register_number=Register_numbers):
# # # #
# # # #         self.__Owner_name = 'Guru Mahendrakar'
# # # #         self.__Owner_phonenumber = '7411891852'
# # # #         self.__Email_adress = 'GuruMahendrakar143@email.com'
# # # #         self.Name = Holdername
# # # #         self.Balance = AccountBalance
# # # #         self.Register_no = Register_number
# # # #         self.__notify__comformation()
# # # #         if input('You Want To Change Anyone')!='Yes':
# # # #             if self.Name not in Holder_names:
# # # #                 Holder_names.append(self.Name)
# # # #                 self.__information(self.Name, self.Balance, Register_number)
# # # #                 print('Thanks For Creating Account')
# # # #
# # # #             else:
# # # #                 print("Name Is Already Register in Bank")
# # # #         else:
# # # #             Holdername = input('Enter The Name Again : \t '); AccountBalance = input("Do You Have Money : \t")
# # # #             self.Name = Holdername
# # # #             self.Balance = AccountBalance
# # # #             self.__information(self.Name,self.Balance,Register_number)
# # # #             def __new__(self):
# # # #                 Holder_names.append(self.Name)
# # # #                 return type('Bank',(),dict((("Name",self.Name),("Balance",self.Balance))))
# # # #
# # # #
# # # #     def __notify__comformation(self):
# # # #         print("Name : {}\n"\
# # # #               "Register Number : {}\n"\
# # # #               "Account Balance : {}".format(self.Name,self.Register_no,self.Balance))
# # # #
# # # #
# # # #     def __Add_Money(self,AddMoney):
# # # #         Account_number = int(input("Enter Account Number : "))
# # # #         if Account_number == self.Register_no:
# # # #             self.Balance+=AddMoney
# # # #
# # # #
# # # #
# # # #     def __information(self,Name,Balance,Register_no):
# # # #         global Created_Holder_Account_numbers
# # # #         global  All_information_bank
# # # #         Created_Holder_Account_numbers = Created_Holder_Account_numbers.append((Name,(Balance,Register_no)))
# # # #         information_client = {Name:{Register_no: Balance}}
# # # #         All_information_bank[Name] = information_client
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # # object = Bank(Holdername,AccountBalance,Register_numbers)
# # # #
# # # # import json
# # # #
# # # #
# # # #
# # # #
# # # #
# # # # # class method():
# # # # #     def __init__(self,name,sirname):
# # # # #         print('This Is Method Class')
# # # # #         super().__init__()
# # # # #         self.name = name
# # # # #         self.sirname = sirname
# # # # #         self.roll = 28
# # # # #     def HelloBrother(self):
# # # # #         print('Welcome Method Object {} '.format(self))
# # # # #
# # # # # class method3:
# # # # #     def __init__(self):
# # # # #         self.collage = 'cb collage Bhlalki'
# # # # #         print('This Is Method-3 Class')
# # # # #
# # # # #     def method3_function(self):
# # # # #         print("Method3 Fucntion Brother ")
# # # # #
# # # # #
# # # # #
# # # # # class List:
# # # # #     def __init__(self,*args):
# # # # #         print("First Called Method2")
# # # # #         self.hello = "Guru"
# # # # #         self.args = args
# # # # #         self.value_counter  = -1
# # # # #
# # # # #
# # # # #
# # # # #     def __del__(self):
# # # # #         print("Finally Deleteb Object")
# # # # #
# # # # #     def __iter__(self):
# # # # #         return self
# # # # #
# # # # #     def __next__(self):
# # # # #         list_len = len(self.args)
# # # # #         try:
# # # # #             while list_len-1 != self.value_counter:
# # # # #                 self.value_counter+= 1
# # # # #
# # # # #
# # # # #                 return self.args[self.value_counter]
# # # # #             raise StopIteration
# # # # #         except:
# # # # #             self.value_counter = 0
# # # # #             return self.args[self.value_counter]
# # # # #
# # # # #
# # # # # method32  =  List(1,2,3)
# # # # # for i in iter(method32):
# # # # #     print(i,end=' ')
# # # # #     time.sleep(2)
# # # #
# # # #
# # # # # def value_taker(valuess):
# # # # #     def sum():
# # # # #         counter = 0
# # # # #         for values in valuess():
# # # # #             counter+=values
# # # # #         return counter
# # # # #     return sum
# # # # #
# # # # # def loop(odd_value_seprator):
# # # # #     odd_value_storer = []
# # # # #
# # # # #     def checker():
# # # # #          print(locals(),'locals')
# # # # #          print(dir())
# # # # #          for values in [1,2,3]:
# # # # #              if values%2!=0:
# # # # #                  odd_value_storer.append(values)
# # # # #
# # # # #          return odd_value_storer
# # # # #     return checker
# # # # #
# # # # # def value_transfer():
# # # # #     list = eval(input("Enter A Integers List"))
# # # # #     return list
# # # # #
# # # # # a = value_taker(loop(odd_value_seprator=value_transfer))
# # # # # print(a())
# # # #
# # # # #import pickle
# # # #
# # # # # class metho:
# # # # #     def __init__(self):
# # # # #         self.Guru = "Guru"
# # # # #         self.sirname = "Mahendrakar"
# # # # #
# # '''
# # json.loads = str to dict
# # json.dumps  = dict to str
# # json.load(Recive in String)
# # json.dump(obj,file)(take only str) = take only string
# import itertools
#
# # pickle.loads  = binary to str
# # pickle.dumps = str to binary
# # pickle.dump((bytes,iterables),file) = Tumne jO Paas Kiye Hai Wahi Type Milega
# # pickle.load(file) = Tune Jo Uske Under Daala Hai Wahi Milega
# # '''
# # # # # ono1 = type('Guru',(),{'Guru': "Mahendrakar","Roll No ": 39,"Clg": "Cb Collage Bhalki"})
# # # # # on2 = type('Guru',(),{'Guru': "Xranger","Roll No ": 38,"Clg": "Cb Collage Bhalki"})
# # # # # on3 = type('Guru',(),{'Guru': "ValueAble","Roll No ": 36,"Clg": "Cb Collage Bhalki"})
# # # # # b = ono1.__dict__
# # # # # a  = 'guru'
# # # # # c = [1,2,3,4,5]
# # # #
# # # #
# # # # # class Student:
# # # # #     def __init__(self,name,roll):
# # # # #         self.name = name
# # # # #         self.roll = int(roll)
# # # # #
# # # # #     def Student_attendence(self):
# # # # #         print(f'{self.name},{self.roll}')
# # # # #
# # # # # with open('texting.txt','rb+') as ojec:
# # # # #         pickle.dump(Student('Guru',8),ojec)
# # # # #         pickle.dump(Student('Guruji',51),ojec)
# # # # #         with open('texting.txt','rb+') as f :
# # # # #             print(pickle.load(f).name)
# # # #
# # # #
# # # # # d = 'Guru'.encode()
# # # # # b = {}
# # # # # aa  = b.setdefault('Guru', "mahendrakar")
# # # # # print(b)
# # # #
# # # #
# # # #
# # # #
# # # # # a = {}
# # # # # list = []
# # # # # import time
# # # # # c = time.time()
# # # # # for letters in string:
# # # # #     b = 0
# # # # #     if letters not in a:
# # # # #         b+= 1
# # # # #         a[letters] = b
# # # # #         print(letters,end="")
# # # # #     else:
# # # # #         b+= a[letters]+1
# # # # #         a[letters]= b
# # # # #         print(letters*a[letters],end="")
# # # # # print()
# # # # #
# # # # # print(time.time()-c)
# # # # # c = time.time()
# # # # # for letters in string:
# # # # #     if letters not in list:
# # # # #         list.append(letters)
# # # # #         print(letters,end="")
# # # # #     elif letters in list:
# # # # #         coiu = 0
# # # # #         for letter in list:
# # # # #             if letters==letter:
# # # # #                 coiu+= 1
# # # # #         print(letters*(coiu+1),end="")
# # # # # print()
# # # # # print(time.time()-c)
# # # #
# # # #
# # # #
# # # #
# # # #
# # # # import os
# # # # # print(os.getcwd())
# # # # # os.chdir(os.getcwd())
# # # # # a = os.path.join('C:','Users','Mahen','bitepy')
# # # # # print(os.mkdir('Sorting.py'))
# # # # # print(os.listdir(os.getcwd()))
# # # # # os.chdir(os.getcwd())
# # # # # os.mkdir('Sorting.py')
# # # # # os.rmdir('Sorting.py')
# # # # # print(os.listdir(os.getcwd()))
# # # #
# # # # # list = [-1,1,2,3,4,5,6]
# # # # # higher = 0
# # # # # for i in range(len(list)):
# # # # #     if list[i]>higher:
# # # # #         higher = list[i]
# # # # # print(higher)
# # # #
# # # # # class moreaboutcreated(object):
# # # # #     def __init__(self,name):
# # # # #         pass
# # # # # class one(type):
# # # # #     def __new__(cls, *args, **kwargs):
# # # # #
# # # # #         sea = 9
# # # # #         one2 = 0
# # # # #         try:
# # # # #             if one.one2==0:
# # # # #                 args[2][locals()['sea']] = 9
# # # # #                 one.one2+= 1
# # # # #                 return type('Guru',(),args[2])
# # # # #             elif one.one2==1:
# # # # #                 one.one2+= 1
# # # # #                 return  type(cls.__name__,(), {})
# # # # #             else:
# # # # #                 raise moreaboutcreated('No more object create brother')
# # # # #
# # # # #
# # # # #         except BaseException:
# # # # #             raise BaseException('No More create objects')
# # # # #
# # # # #
# # # # # class two(metaclass=one):
# # # # #     Codeing = "Python"
# # # # #     def __init__(self,name):
# # # # #         print("Two __init__")
# # # # #         self.python = "Interputed Langauge"
# # # # #         self.name = name
# # # # #
# # # # #     def tool(self):
# # # # #         print('Yo bo')
# # # # #
# # # # # b  = one()
# # # # # a = two('guru')
# # # # # print(a.sea)
# # # # #
# # # # #
# # # #
# # # # # class method(object):
# # # # #     def __init__(self,one):
# # # # #         self.one = one
# # # # #
# # # # #     def __set__(self, instance, value):
# # # # #         print('Executed')
# # # # #         print(instance,value)
# # # # #
# # # # #     def __get__(self, instance, owner):
# # # # #         print(instance,owner)
# # # # #
# # # # #     def __getattr__(self,value):
# # # # #         print(value)
# # # # #
# # # # #
# # # # # b = f.arange(10,20)
# # # # # # print(f.random.beta(f.arange(1,10),f.arange(10,20)))
# # # # # print(a>2)
# # # # # a = method('Guruji')
# # # # # class method2(method):
# # # # #     pass
# # # # #
# # # # # if __name__ == '__main__':
# # # # #     p = method2('Gur')
# # # # #     p.one
# # # # #
# # # # # import  numpy as f
# # # # #
# # # # # print(f.random.sample((5,4)))
# # # # # # print(help(f.random.random_sample))
# # # # # print(f.random.random((8,2)))
# # # # # a = f.arange(0,10)
# # # #
# # # #
# # #
# # # # def tool():
# # # #     a = 8
# # # #
# # # # class typemethod:
# # # #     name = 'Guru'
# # # #     def __init__(self,name,bases,cdict):
# # # #         self.name = name
# # # #         self.bases = bases
# # # #         self.cdict = cdict
# # # #
# # # #     cls_intances = {}
# # # #
# # # #
# # # #
# # # #     def __call__(cls,*args,**kwargs):
# # # #
# # # #
# # # #         if cls in typemethod.cls_intances :
# # # #             return "YOu Are Created More Objects"
# # # #         else:
# # # #             print(cls.cdict)
# # # #             typemethod.cls_intances[cls] = type(cls.name,cls.bases,cls.cdict)
# # # #             return type('Guru',(),{})
# # # #
# # # #
# # # #     def __add__(self,otherself):
# # # #         print("Entered")
# # # #         return self.name + otherself.name
# # # #
# # # # class Mymethod(metaclass=typemethod):
# # # #     online = 'Online Classes'
# # # #     def __init__(self):
# # # #
# # # #         self.name = "Syed Ali"
# # # #         self.sirname = "Chowdary"
# # # #
# # # #     def __mro__(self):
# # # #         print("Cooled Brother")
# # # #     def __add__(self,otherself):
# # # #         print("Entered")
# # # #         return self.name + otherself.name
# # # #
# # # # my = Mymethod
# # # #
# # # # my2 = typemethod('Guru','Fuck','Tool')
# # # #
# # # # print(my2)
# # # #
# # # #
# # # # 1,
# # # # 2,13
# # # # 3,12,14
# # # # 4,11,15,22,
# # # # 5,10,16,21,23
# # # # 6,9,17,20,24,27
# # # # 7,8,18,19,25,26,28
# # # #
# # # #
# # # # #
# # # # # decrease  = 0
# # # # # value = 0
# # # # # for i in range(6):
# # # # #     for ii in range(i+1):
# # # # #         print(value+i+1,end=" ")
# # # # #         value   = value  + 6 -decrease -  1
# # # # #         decrease = decrease + 1
# # # # #     decrease =  0
# # # # #     value  = 0
# # # # #     print()
# # # #
# # # #
# # # # #
# # # # # num = 6
# # # # # t = 0
# # # # # for row in range(num):
# # # # #     x = 0
# # # # #     for colums in range(row+1):
# # # # #         print(x+row+1,end=" ")
# # # # #         x+= num-1 - t
# # # # #         t = t + 1
# # # # #     t = 0
# # # # #     print()
# # # #
# # # #
# # # # # class calculate22:
# # # # #     def __init_(self,name,two):
# # # # #         self.integer = two
# # # # #         self.integer2 = name
# # # # #
# # # # #     def __call__(self,*args,**kwargs):
# # # # #         print("Executed")
# # # # #
# # # # #     def
# # # # #
# # # # # a = calculate22()
# # # # #
# # # # # import numpy as p
# # # # #
# # # # # print(p.arange(1,13).reshape(2,3,2))
# # # # # print(p.sum(p.arange(1,13).reshape(2,3,2),axis=0))# 0 colums 1 row
# # # # # a = p.dot(3.6,8.2)
# # # # # b = p.array(([1,2,3,4,5,6,7,],[8,9,10,11,12,13,14])).astype(int)
# # # # # print(b)
# # # # # # print(b>2)
# # # # # # print(2<b)
# # # # # # print(b==2)
# # # # # print(b.itemsize)
# # # # # def f():
# # # # #     for ii in range(0,6):
# # # # #         yield ii
# # # # # a = f()
# # # # #
# # # # #
# # # # # for i in a:
# # # # #     print(i)
# # # # #
# # # # # for ii in a:
# # # # #     print(ii)
# # # #
# # # #
# # # # #
# # # # # value = 22
# # # # # decrease = 0
# # # # # for ii in range(0,9):
# # # # #     for iii in range(ii+1):
# # # # #         print(value,end=' ')
# # # # #         value-= 8-iii
# # # # #     decrease+= 1
# # # # #     value = 22 - decrease
# # # # #     print()
# # # # #
#
# # Gameover = False
# # import pygame
# # x=50 ;  y = 50
# # running = 0
# # running2 = 0
# # import  random
# # snakesize = 10
# # snakelist = [(50,50)]
#
# # foodinteger = random.choice(list(range(200,900)))
# # score = 0
# # class Snake:
# #     global snakelist; global snakesize
# #     x = 50
# #     y= 50
#
# #     Over = False
# #     Display = pygame.display.set_mode((1920,1000))
#
# #     def __init__(self):
# #         pygame.display.set_caption("Snake Game")
#
# #     def music(self, song):
# #         import pygame
# #         pygame.mixer.init()
#
# #         pygame.mixer.music.load(song)
# #         pygame.mixer.music.play()
#
#
# #     @staticmethod
# #     def plot_snake(gamewindow,color,snakelist,snakesize):
# #         for x,y in snakelist:
# #             print(' : ' ,snakelist)
# #             pygame.draw.rect(gamewindow,color,[x,y,snakesize,snakesize])
# #     @staticmethod
# #     def food(surface,Color,x_size,y_size,foodsize):
# #         global snakesize
# #         global  foodinteger
# #         global score
# #         if abs(Snake.x - foodinteger)<20  and abs(Snake.y - foodinteger )<20:
# #             Snake().music(r"C:\Users\mahen\Downloads\snake (1).mp3")
#
#
# #             foodinteger = random.choice(list(range(200,900,10)))
# #             pygame.draw.rect(surface,Color,[x_size,y_size,foodsize,foodsize])
# #             snakesize+= 3
# #             score += 10
# #         else:
# #             pygame.draw.rect(surface, Color, [x_size, x_size, foodsize,foodsize])
# #     @staticmethod
# #     def MovementControl(event):
# #         global running,running2
# #         if event.key == pygame.K_UP:
#
# #             running2 = 0
# #             running  = -23
# #         if event.key == pygame.K_DOWN:
#
# #             running2 = 0
# #             running = +23
# #         if event.key  == pygame.K_LEFT:
#
# #             running = 0
# #             running2 = -23
#
# #         if event.key == pygame.K_RIGHT:
# #             running = 0
# #             running2  = 23
#
#
# #     def run(self):
# #         import pygame
# #         clock = pygame.time.Clock()
#
# #         global x,y
# #         global snakesize
# #         global snakelist
# #         global  running,running2
# #         pygame.font.init()
#
# #         var = 0
#
# #         while not Snake.Over:
# #             if var%240==0:
# #                 self.music(r"C:\Users\mahen\Downloads\loco_contigo.mp3")
#
# #             var+= 1
#
# #             for event in pygame.event.get():
# #                 if event.type == pygame.QUIT:
# #                     Snake.Over = True
# #                 if event.type == pygame.KEYDOWN:
# #                     self.MovementControl(event= event)
#
# #             a = pygame.font.Font(r"C:\Users\mahen\bitepy\yes\yes\photos\BrusselsCityPersonalUsed-L3Lon.otf",22)
# #             Snake.x+= running2
# #             Snake.y += running
# #             b =  a.render(f'Score : {score}',True,'brown')
# #             Snake.Display.fill('white')
# #             Snake.Display.blit(b, (1920/2-100, 0))
#
#
#
# #             if Snake.x <0 or Snake.x > 1920 or Snake.y <0 or 1000<Snake.y:
# #                 snakelist.clear()
# #                 if Snake.x<0:
# #                     Snake.x = 1900;Snake.y = Snake.y
# #                     snakelist.append([Snake.x,Snake.y])
#
# #                 elif Snake.y<0:
# #                     snakelist.clear()
# #                     if Snake.y < 0:
# #                         Snake.x = Snake.x
# #                         Snake.y = 1000
# #                         snakelist.append([Snake.x, Snake.y])
#
# #                 elif Snake.x>1920:
# #                     snakelist.clear()
# #                     if Snake.x > 1920:
# #                         Snake.x = 0
# #                         Snake.y = Snake.y
# #                         snakelist.append([Snake.x, Snake.y])
#
# #                 elif Snake.y>1000:
#
# #                     Snake.x = Snake.x
# #                     Snake.y = 0
# #                     snakelist.append([Snake.x, Snake.y])
#
#
# #             if len(snakelist)>snakesize:
# #                 del snakelist[0:10]
# #             # if len(set((snakelist)))>1:
# #             #     if list(set(snakelist))[-1] in list(set(snakelist))[:len(snakelist)-1]:
# #             #         print(set(snakelist))
# #             #         Snake.Over = True
#
# #             row = 0
# #             for x,y in snakelist:
#
#
# #                 if row==len(snakelist)-1:
# #                     pygame.draw.rect(Snake.Display,'blue',[x,y,20,20])
# #                 else:
#
# #                     pygame.draw.rect(Snake.Display, 'green',[x, y, 20, 20])
# #                 row += 1
#
#
# #             Snake.food(Snake.Display,'dark blue',foodinteger,foodinteger,20)
# #             pygame.time.set_timer(50,100)
#
#
# #             clock.tick(30)
#
# #             if (50,50) not in snakelist and (Snake.x,Snake.y) in snakelist:
# #                 over = False
# #                 import time
# #                 while not over:
#
# #                     for event in pygame.event.get():
# #                         if event.type == pygame.QUIT:
# #                             over = True
# #                             Snake.Over = True
#
# #                         if event.type == pygame.KEYDOWN:
# #                             if event.key == pygame.K_p:
# #                                 over = True
# #                                 continue
#
#
#
# #                     a = pygame.font.Font(r"C:\Users\mahen\bitepy\yes\yes\photos\BrusselsCityPersonalUsed-L3Lon.otf", 22)
# #                     b = a.render(f'Game Over',True,'Black')
# #                     Snake.Display.fill('White')
# #                     Snake.Display.blit(b,(1920//2-150,400))
# #                     c = a.render('Enter To Play Press Enter',True,'Black')
# #                     Snake.Display.blit(c, (1920 //2-150, 425))
# #                     pygame.display.update()
# #                     print(event)
# #                     time.sleep(1)
#
# #             snakelist.append((Snake.x,Snake.y))
#
#
# #             pygame.display.update()
#
#
# # a = Snake()
# # a.run()
# # print(snakelist)
#
# # \
#
# # class method:
# #     def __init__(self):
# #         self.Owner = 'Guru Mahendrakar'
# #     @staticmethod
# #     def NewMethod(Function):
# #         def CoolProject(name):
# #             print(name)
# #             print("Executed By CoolProject")
# #             return Function()
# #         return CoolProject
#
# #     @NewMethod
# #     @staticmethod
# #     def NewMethoding():
# #         return "This Is Calle New Called Method"
#
# # methods = method()
# # methods.NewMethoding()
# # #
# # #
# # # class method2(method):
# # #     def __init__(self,Owner):
# # #         self.name = "Hatt Lawde"
# # #
# # #         # super(method2, self).__init__()
# # #
# # #     def Method2(self):
# # #         print("Method 2 object")
#
# # #
# # # one = method2("Mahendrakar")
# # # print(one.__dict__)
# # # print(method2.mro())
# # # print(one.__class__.__class__)
# # #
# # #
# # # a = 0
#
# # # class method:g
# # #     global a
# # #     def __init__(self,name,bases,cdict):
# # #         self.bases = bases
# # #         print(name,bases,cdict)
# # #
# # #     print("Entered Brother")
# # #     name = 'Guru'
# # #     @staticmethod
# # #     def Method3():
# # #         def coolbrother():
# # #             print("You Are Correct Brother")
# # #         return coolbrother
# # #
# # #
# # #
# # # class method2(method):
# # #     def __init__(self):
# # #         self.collage = 'Cb Collage Bhakli'
# # #         method('Guru','Mahendrakar','Fresh')
# # #
# # #
# # #
# # # # print(type(method2.__dict__))
# # # def splitrer(nameupper):
# # #     def namespliter():
# # #         return nameupper().split()
# # #     return namespliter
# # # def nameupper(inputer_func):
# # #     def nameUpperer():
# # #         return inputer_func()
# # #     return nameUpperer
# # #
# # # def inputer():
# # #     name= 'Guru'
# # #     sirname = ' Mahendrakar'
# # #     return name +sirname
# # #
# # #
# # # a = splitrer(nameupper(inputer))
# # # print(a())
#
#
# # '''
# # json.loads = str to dict
# # json.dumps  = dict to str
# # json.load(Recive in String)
# # json.dump(obj,file)(take only str) = take only string
#
#
# # pickle.loads  = binary to str
# # pickle.dumps = str to binary
# # pickle.dump((bytes,iterables),file) = Tumne jO Paas Kiye Hai Wahi Type Milega
# # pickle.load(file) = Tune Jo Uske Under Daala Hai Wahi Milega
# # '''
#
# # #
# # # file = open('texting.txt','w')
# # # list = ['Guru',"MotherFucker","SpecialGuest","Trolling Boys"]
# # # dict = {'Guru':"Mahendrakar","Thriller": "Movie Of The Boss","Brown": "Rang Dii"}
# # #
# # # class method:
# # #     def __init__(self, name):
# # #         self.name = name
# # #
# # # a = method('Fucker')
# # # b = str(['Guru',"Mahendrakar","IgKimi"])
# # #
# # # with open('texting.txt','rb+') as f :
# # #     pickle.dump(json.dumps(dict),f)
# # #
#
# # #
# # # list = [1,2,3,4,5]
# # # for i in list:
# # #     if 4>i:
# # #         print(i)
# # #
# # #     if i>4:
# # #         print(i)
# # #
# # #     if i<5:
# # #         print(i)
# # #
# # #     if 5>i:
# # #         print(i)
#
#
# # # a = [[col for col in range(6) ] for i in range(6)]
# # # low = 0
# # # high = 6
# # # counting = 0
# # # xleft = 0
# # # for rows in range(6):
# # #     for up in range(low,high):
# # #         counting+= 1
# # #         a[rows][up] = counting
#
# # #     for right in range(low+1,high):
# # #         counting+= 1
# # #         a[right][high-1] = counting
#
# # #     for down in range(high-2,low,-1):
# # #         counting+= 1
# # #         a[high-1][down] = counting
#
#
# # #     for xleftt in range(high-1,low,-1):
# # #         counting+= 1
# # #         a[xleftt][xleft] = counting
#
# # #     xleft+= 1
# # #     low+= 1
# # #     high-= 1
#
#
#
# # rows = 0
# # for row in a:
# #     for colums in row:
# #         if rows==0:
# #             print(colums,end='    ')
# #         else:
# #             print(colums,end='   ')
# #     rows+= 1
# #     print()
#
# # import os;import shutil
# # file =[]
#
# # os.chdir(r'C:\Users\mahen\bitepy\yes')
# # for transfer in os.listdir(os.getcwd()):
# #     if transfer not in file:
# #         shutil.move(transfer,'yes')
# #     else:
# #         print(transfer)
# # print(os.getcwd()+'OIP.jpeg'.replace('\\\\','/'))
# # dict = {'name':{'Guru':'Mahendrakar','Soul':'Mother'}}
# # for i in dict:
# #     for ii in dict[i]:
# #         print(dict[i][ii])
# # list = [1,1,3,2,5,8,9]
#
# # def quicksort(listing):
# #     global list
# #     pivot = listing[0]
# #     a = 1
# #     b = -1
#
# #     while not listing[a]>pivot:
# #         a+= 1
# #         print('Executed')
#
# #     while not listing[b]<=list[a]:
# #         b-= 1
#
# #     if b<a:
# #         list[pivot],list[b] = list[b],list[pivot]
#
# #     else:
# #         list[a],list[b] = list[a],list[b]
#
#
# #     return listing
#
# # print(quicksort(quicksort(quicksort(list))))
#
#
# # Please Note You Can Basic Learner Please Time Too Forloop With this type
#
# # integers= 0
#
# # for row in range(6):
# #     for colums in range(row+1):
# #         print(integers,end=" ")
# #         integers+= 1
# #     integers = 0
# #     print()
#
# # for row in range(6):
# #     for colums in range(row+1):
# #         integers+= 1
# #         print(integers,end=" ")
#
# #     integers = 0
# #     print()
# # import random
#
# # for rows in range(int(input("Enter Lines Of Number : "))):
# #     for colums in range(random.randint(0,20)):
# #         print(" ",end=" ")
#
#
# #     print("*",end=" ")
# #     if rows%10==0:
# #         print("Happy Birthday Guru Mahendrakar")
#
#
# # set1 = set([1,2,3,4])
# # set2 = set([5,6,7,8])
#
# # print(set1.union(set2))
# # print(set2.difference(set1))
# # print(set1.intersection(set2))
#
#
# # import timeit
#
# # def quicksort(lists):
#
# #     if len(lists)<=1:
# #         return lists
# #     else:
# #         sequence = lists.pop()
# #     greater = []
# #     lower = []
# #     for items in lists:
# #         if items>sequence:
# #             greater.append(items)
# #         else:
# #             lower.append(items)
#
# #     return (quicksort(lower)+[sequence] + quicksort(greater))
# # import time
# # a = time.time()
# # print(quicksort(list))
# # print(time.time()-a)
# # a = 0
# # def recursion():
# #     global a
# #     a+=1
# #     if a==5:
# #         return "A Now is : 5"
#
# #     else:
# #         return recursion()
# # print(recursion())
#
#
#
#
#
# # def decorator_2(decorator_1):
# #     def circus():
# #         print("Welcome To My Circus")
# #         print(decorator_1())
#
# #     return circus
#
#
# # def Board_capitalize(decorator_2):
# #     def Board_():
# #         print("The Owner IS Guru Mahendrakar")
# #         print(decorator_2())
# #     return Board_
#
#
# # @Board_capitalize
# # @decorator_2
# # def decorator_1():
# #     Name = input("Enter Name : ")
# #     Sirname = input('Enter Sirname : ')
# #     return Name + Sirname
#
# # decorator_1()
#
#
#
#
# # class name_setter:
# #     def __init__(self,Name,Sirname):
# #         self.Name = Name
# #         self.Sirname = Sirname
#
#
# #     @property
# #     def Sirname_Changer(self):
# #         return self.Sirname
#
# #     @Sirname_Changer.setter
# #     def Sirname_Changer(self,New_name):
# #         self.Sirname = New_name
#
#
# # ame = name_setter("Nitin","Mahendrakar")
# # ame.Sirname_Changer = "Rathod"
# # print(ame.__dict__)
# # print(ame.Sirname)
#
#
#
# # class Guru_range:
# #     def __init__(self,start,end):
# #         self.start = start
# #         self.end = end
#
# #     def __iter__(self):
# #         return self
#
#
# #     def __next__(self):
# #         if self.start==self.end-1:
# #             raise StopIteration("Finished Work Do Not More Work")
# #         else:
# #             self.start+= 1
# #             return self.start
# # G = Guru_range(-1,8)
#
#
# # for ii in G:
#     # print(ii)
#
#
#
# # array = [1,15,5,1,5,2,5,6,2]
# # print(array)
# # a  = 1
# # b = -1
# # pivot = 0
# # A_True = True
# # B_True =  True
#
# # class quicksort:
#
# #     @staticmethod
# #     def A_Handler():
# #         global array,a,b,A_True
# #         while not array[a]>array[pivot]:
# #             a+= 1
#
# #             if a==len(array)-1:
# #                 A_True = False
# #                 break
#
# #     @staticmethod
# #     def B_Handler():
# #         global array,a,b,B_True,pivot
#
# #         while not array[b]<=array[pivot]:
# #             b-=1
# #             if abs(b)==len(array):
# #                 if pivot<len(array):
# #                     pivot+= 1
# #                 array[pivot],array[b] = array[b],array[pivot]
# #                 break
#
# #             # 5   2   2   3   7   6
# #             # 0   1   2   3   4   5
# #             #-6  -5  -4  -3  -2  -1
# #         if array[b] in  array[a:] :
# #             array[a],array[b] = array[b],array[a]
# #         else:
# #             array[pivot],array[b] = array[b],array[pivot]
#
#
#
#
# # U = quicksort()
# # for i in range(3):
# #     U.A_Handler()
# #     U.B_Handler()
# # print(array)
#
#
#
# # # class method:
#
# # #     def __init__(self):
# # #         self.name = "GURU MAHENDRAKAR"
#
# # #     def __get__(self):
# # #         return self.name
#
# # #     def __set__(self,new_name):
# # #         print("Called Brother")
# # #         self.name = new_name
# # #         return self.name
#
# # # a = method()
# # # a.name = "Guru"
# # # print(a.__set__("Guru Mahendrakar"))
# # # print(a.__get__())
#
#
# # from array import array
# # from cmath import pi
# # from copyreg import pickle
#
#
#
#
#
# # list = [8,9,11,2,3,-1,2,5,2,5,3,2,3,56,67,7,73,32,2,2,3,5,6,6,78,8888,88888888888,999999999999,0000000,222222222,2222,2,222]
#
# # x = 1
# # y = -1
# # pivot = 0
# # pivot_checker = pivot
# # class quicksort:
# #     def __sort__(self):
# #         while pivot!=len(list)-1:
# #             @staticmethod
# #             def x():
# #                 global x
# #                 while not list[x]>list[pivot]:
#
# #                     if x==len(list)-1:
# #                         break
#
# #                     else:
# #                         x+= 1
#
#
# #             @staticmethod
# #             def y():
# #                 global y,pivot,x,pivot_checker
# #                 while not list[y]<list[pivot]:
#
# #                     if abs(y)==len(list)-pivot:
# #                         pivot+=1
# #                         if pivot>3:
# #                             x = pivot+1
# #                         y = -1
# #                         break
#
# #                     else:
# #                         y-= 1
# #                 if list[y] in list[x:]:
# #                     list[x],list[y] = list[y],list[x]
#
# #                 if list[y] not in list[x:]:
# #                     list[pivot],list[y] = list[y],list[pivot]
#
#
# #                 if x<len(list):
# #                     if list[y]==list[x] and x==len(list)-1:
# #                         list[pivot],list[y] = list[y],list[pivot]
# #             x()
# #             y()
#
# # U  = quicksort()
# # import time
# # a = time.time()
# # U.__sort__()
# # print(time.time()-a)
# # print(list,x,y,pivot)
#
#
#
# # class method:
#
# #     @staticmethod
# #     def cool(One):
# #         print(" Decorator Uses This Function {}".format(One))
#
# # method = method()
#
#
# # @method.cool
# # def mydetails():
# #     print(""" "Name"  : "Guru" """)
#
#
# # import time
# # from threading import Thread
#
# # def youtube():
# #     print("Video Is Uploading Brother")
# #     time.sleep(3)
# #     print("video is Uploaded Brother")
#
#
# # def checking_copyright():
# #     print("Copyrighted sorry video was deleted ")
#
#
# # upload = Thread(target = youtube)
# # copy_check = Thread(target=checking_copyright)
# # upload.start()
# # upload.join()
# # copy_check.start()
#
#
#
# # import tkinter
#
#
# # surface = tkinter.Tk()
# # surface.geometry("500x600")
# # surface.minsize(200,300)
# # surface.maxsize(600,800)
# # text_Name = tkinter.Label(surface,borderwidth = 8,text="Guru Mahendrakar",bg='black',foreground='white',padx=33,pady=55,relief=tkinter.SUNKEN)
#
# # text_Name.pack(side=tkinter.LEFT,fill = tkinter.X)
# # text_Name.pack(side=tkinter.LEFT,fill=tkinter.Y)
# # surface.mainloop()
#
# # import threading
# # import time
# # def own(arg):
# #     for i in range(arg):
# #         print("Threading Name : ",threading.current_thread().name)
# #         print("Threading Nows Working :",threading.active_count())
# #         time.sleep(2)
# #         print("---------------------------------------")
# # begin_time = time.time()
# # Target = threading.Thread(target=own,args = (5,))
# # Target2 = threading.Thread(target=own,args= (5,))
# # Target.name="Guru"
# # Target2.name = "Nitin"
# # Target.start()
# # Target2.start()
# # Target.join()
# # Target2.join()
# # print(time.time()-begin_time)
#
#
#
# # import os
# # import shutil
#
# # os.mkdir("photos_files")
# # for files in os.listdir(os.getcwd()):
#
#
# # import os
# # import shutil
# #shutil.move(path,file)
#
# # list_photos = os.chdir("alworks")
# # list_photos_files = os.listdir(os.getcwd())
# # os.chdir(r"C:\Users\mahen\bitepy")
# # python_files = []
# # for files in os.listdir(r"C:\Users\mahen\bitepy"):
# #     if files.endswith(".py") or files.startswith('.git') or files.startswith('__pycache__')  or files.startswith("photos_filess"):
# #         python_files.append(files)
#
# # class method:
# #     def __init__(self):
# #         self.one = "Guru Mahendrakar"
#
# #     def __set__(self,name,value):
# #         print("Value Is Setted Brother")
#
#
# #     def __get__(self,one):
# #         print("Value Is Getted Brother")
# #         return one
#
# #     def __del__(self):
# #         print("Garbage Collecter Is Executed")
# # a = method()
# #
#
# #
# # string = "a=8 b=9 c=7"
# # string = list(map(lambda a : a.split("="),string.split(" ")))
# # a = dict(map(lambda x : [x[0],int(x[1])] ,sorted(string,key= lambda x :x[1])))
# #
# # print(a)
#
#
#
# #iadd - means iterable to iterable ko plus karna hai to iadd use karo
#
#
#
# # import itertools
# # import operator
# # import collections
# #
# #
# # a = itertools.combinations([1,2,3,4,5],3)
# # b = itertools.permutations([1,2,3,4,5],3)
# # c = itertools.chain([1,2,3,4,5]) # generator return
# # d = itertools.count(start = 1 ,step=1) # end nahi hai isme aap if else lagake break maroge to hi break hoga
# # e = itertools.groupby('aaabbbcccjlabioup',key= lambda x :  x=='a' or x=='b')
# #
# # print(list(a))
# # print(list(b))
# # print(list(c))
# # # print(list(d))
# #
# # for x in e :
# #     print(x[0],list(x[1]))
# #
# # print(list(itertools.islice([1,2,3,4,5],0,2)))
# #
#
#
#
# #
# #
# # dict = [{"Car":50000},{"Car":20000},{"Car":30000}]
# #
# #
# # min = min(dict,key=lambda x: x['Car'])
# # max = max(dict,key=lambda x: x['Car'])
# # sorted = sorted(dict,key=lambda x:x['Car'])
# #
# # print(min) # min(iterable,key=func)
# # print(max) # max(iterable,key=func)
# # print(sorted) # sorted(iterable,key=func)
#
# #
# # string = "Guru Mahe\ ndrakar  Ståle "
# #
# # print(string.encode(encoding= 'utf-8'))
# #
# # p = (string.encode('latin-1'))
# #
# # print(p.decode(encoding='latin-1'))
#
#
# # enocodeing = bytes(s,encoding = 'utf-8')
# #
# # print(enocodeing.decode(encoding='utf-8'))
#
# # #
# # butes = bytearray('Guruji»»»øø�ɷ',encoding='utf-16')
# # butes[0] = 6
# # print(chr(butes[-1]))
# # #
# # print(butes.decode('utf-16'))
#
#
# # class method:
# #     def __init__(self) -> None:
# #         self.start = 0
# #         self.end = 8
#
#
#
# #     def __next__(self):
# #         one_more = self.start
# #         if one_more<self.end:
# #             self.start+=1
# #             return one_more
#
# #         else:
# #             raise StopIteration('not more have elements--')
#
# # a = method()
#
#
#
#
# # class method3:
# #     def __init__(self):
# #         self.collage = "Cb college Bhalki"
#
#
# #     def fuckYOu(self):
# #         print('fuck you brother>>>>>>>>')
#
#
# # class method(type):
# #     def __init__(self,name,bases,cdict):
#
# #         self.name = 'Guru'
#
#
# #     def __call__(self):
# #         return 'not class>. eExecuted brother'
#
#
# # class method2(metaclass = method):
# #     def __init__(self):
# #         self.sirname = "Mahendrakar"
#
#
#
# # tyeeee = type('new-method',(method3,),{'name':"Guru Mahendrakar"})
#
# # print(tyeeee().__dict__)
#
#
#
# # import tkinter
# # from tkinter import ttk
# # from tkinter import messagebox
#
# # import ttkthemes
# # window = ttkthemes.ThemedTk(theme='Equilux')
# # window.title('timepass')
#
#
#
# # treeview = ttk.Treeview(window,columns=['#0','#1','2'],selectmode=tkinter.EXTENDED)
# # treeview.pack()
#
#
# # scale = ttk.Entry(window,text='Hello')
# # scale.pack()
#
# # def selected(event):
# #     print(treeview.get_children())
# #     print(treeview.focus())
# #     print(treeview.item(treeview.focus()))
# #     s = messagebox.askyesno('Delte','You Want To Delete')
# #     treeview.delete(treeview.focus()) if s else messagebox.showinfo('information','Ok Deleting Cancel')
#
# # for x in range(0,3):
# #     treeview.heading(x,text=['name','sirname','college'][x])
#
#
# # bb = treeview.insert('',0,text='details',values=['one','two','three'],open=True)
#
# # treeview.insert(bb,text='fuck',index = 0 ,values=['four','five','six'],open=True)
#
# # treeview.bind('<<TreeviewSelect>>',func=selected)
#
# # if __name__ == '__main__':
# #     window.mainloop()
#
#
#
# # list = [1,2,3,4,5,6,7,8]
#
# # print(len(list)//2)
# # print((len(list)-1)//2)
#
#
#
# # list = [1,2,55,333,555,888,8888,9999]
# # k,x,y = len(list),0,len(list)
#
# # import time
# # while 1:
#
# #     k = (x+y)//2
#
# #     if 888!=list[k]:
#
# #         if list[k]>888:
# #             y = k-1
#
# #         else:
# #             x = k+1
#
# #     else:
# #         print('target found-')
# #         break
#
#
#
# # class method:
# #
# #     def __init__(self,name,sirname,rollno):
# #         self.name  = name
# #         self.sirname = sirname
# #         self.rollno = rollno
# #         self.information = 'Please Inherited for anthoer information!!'
# #
# #
# #
# # def __init__(self):
# #     self.nickname = 'nitin'
# #
# # class method2(method):
# #
# #     def __init__(self):
# #         super(method2, self).__init__('Guru','Mahendrkar',39)
# #
# #
# # method_ = method('Guru','Blaster',29)
# # method2_ = method2()
# #
# # print(5 not in [1,2,3])
#
#
# # a = 8
#
# # def _you():
# #     print('Im Codeing..')
#
# # if __name__ == '__main__':
# #     _you()
# #
# # class method:
# #     one_ = 8
# #
# #
# #     def _onee(self,a):
# #         print('_---_')
# #
# #
# # s  = method()
# #
# # s._onee('guru')+
# #
# # print(s._onee)
#
# #
# # import typing
# # class mygenrator:
# #
# #     def __iter__(self):
# #         return self
# #
# #     def __next__(self):
# #         return self.
# #
# # class method:
# #
# #     def __iter__(self):
# #         return self
# #
# #     def __next__(self)-> str :
# #         a = ['Guru','Mahendrakar']
# #
# #         if a :
# #             return a[-1]
# #
# #
# #
# #
# # def funcGenrator()->typing.Generator:
# #
# #     print('__Genrator Entered__')
# #
# #     yield 'func yield'
# #     yield 'cool'
# #
# #
# # funcgenrator = funcGenrator()
# #
# # print(funcgenrator.__next__())
#
# #
# #
# # for x in a:
# #     print(xx(x))
# # else:
# #     print('Data Was clear',list(a))
# #
# # butes = bytearray('Guruji%%%%',encoding='latin-1')
# # butes[0] = 65
# #
# # print(butes.decode('latin-1'))
# #
#
# # a = itertools.chain(['Guurmau',1,2,3,4,5])
# # b = itertools.groupby('aaabbbcccddcc')
# # for x,y in b:
# #     print(x, list(y))
#
# # import builtins
# # a = (x for x in range(3))
# # print(2 in a)
# #
# # x = 8
# #
# # class method:
# #     def __init__(self):
# #         self.name = [self.tool]
# #
# #     def tool(self,name):
# #         return name.upper()
# #
# #
# #
# #
# # a = method()
#
# # def tool():
# #     for x in range(1):
# #         print(a.name[x]('Guru'))
# #
# # tool()
#
# class method:
#
#     def __init__(self,*args):
#         self.args = args
#
#     def __str__(self):
#         return '{}'.format(list(self.args))
#
#     def _SoBeautiful(self):
#         print('Hey Man !!')
#
#     def uou(self):
#         print('How Many Likes In the Cool!!')
#
# o = method(1,2,3,4,5)
#
# # print(method.__dict__['uou'](1))
#
# #
# # def tool():
# #     print('HOw Many Likes !! ')
# #
# # a  = tool
# # a.name = 'Guru'
# # a.name= 'Guru Mahendrakar'
# #
# # print(a.name)
#
# #
# # class method:
# #     pass
# #
# #
# # class method2(method):
# #
# #     def __init__(self):
# #         self.name = "Guru"
# #
# #
# # a = method()
# # print('guruji')
# # print(method2.__bases__)

#
# def tyo():
#     yield 'Guru'
#
# def tyo2():
#     yield  'Mahendrakar'
#
#
# print(id([1,2,3,4,5]))
# print(id([1,2,3,4,5,6,2222]))

a = ''
b = []
c = {1,2}
d = ()




