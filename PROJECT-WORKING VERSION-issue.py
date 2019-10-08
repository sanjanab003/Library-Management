c=0
areMem=()
c1=0
t=()
u=""
p=""
q=""
b=0
a=0
user=""
pas=""
z=0
t1=()
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="0025",
  database="library"
)
mycursor = mydb.cursor()


def regName():
      print("Please register")
      global u
      global p
      u=input("Enter your name: ")
      p=input("Enter a password: ")

      

# function to register

def reg():
      
      add_member = ("INSERT INTO member "
               "(Name, M_Pass) "
               "VALUES (%s, %s)")
      data_member = (u,p)
      mycursor.execute(add_member, data_member)
      mydb.commit()


# function to loop through members' table      

def loopMem():
      mycursor.execute("select * from member")
      global c
      global t1
      row = mycursor.fetchone()
      while row is not None:
            if(row[0]==pas and row[1]==user):
                  c=c+1
                  t1=t1+(row,)
                  row=mycursor.fetchone()
            else:
                  row = mycursor.fetchone()

                  
def areMem():
      global areMem
      areMem=input("Are you a already a member of Sanchansu(Type in 'y' for yes and 'n' for no): ")

def ask():
      global user
      global pas
      user=input("Enter username: ")
      pas=input("Enter password: ")


# function to loop through the books

def loopBook(d):
    mycursor.execute("select * from books")
    global c1
    row=mycursor.fetchone()
    while row is not None:
        if(row[1]==d):
            global t
            t=t+(row,)
            c1=c1+1
            row=mycursor.fetchone()
        else:
            row=mycursor.fetchone()
            
# function to ask for user's choice

def inp():
    global q
    q=input("Enter the name of the book you want to borrow: ")


# function to issue book

def iss(e,f):
    op= """ update books set Qty = %s where Book_Name = %s """
    op3= """ update member set Books_borrowed = %s where M_Pass = %s"""
    dat=(e,f)
    dat3=(f,pas)
    mycursor.execute(op,dat)
    mycursor.execute(op3,dat3)
    if(e==0):
          op2= """ update books set Status = %s where Book_Name= %s """
          dat2= ("Not available", f)
          mycursor.execute(op2,dat2)
    else:
          pass;
    mydb.commit()
    print("Book borrowed successfully")


def tup():
    global a
    global b
    for x in t:
        a=x[1]
        b=x[4]-1
def tup1():
      global z
      for p in t1:
        z=p[2]

def issue(r):
      inp()
      loopBook(q)
      tup()
      if(c1>0):
            print(t)
            if(b+1>0):
                  q2=input("Do you want to borrow this book: ")
                  if(q2=='y'):
                        if(r=="NULL"):
                              iss(b,a)
                        else:
                              print("Please return book before borrowing")
                  else:
                        pass;
            else:
                  print("Sorry Book currently not available")
      else:
            print("Sorry no matching results")


# checking for membership


areMem()
      
if(areMem=="y"):
      ask()
      loopMem()
      tup1()
      if(c==1):
            print("Welcome,", user)
            print("Books borrowed by you: ", z)
            print("Books to be returned: ", z)
            issue(z)
                        
      else:
            print("Incorrect password or username")
      
elif(areMem=="n"):
      regName()
      loopMem()
      if(c==1):
            print("Username or password is already taken")
      else:
            reg()
            print("You are now a member of Sanchansu.")
            print()
            issue()
else:
      print("Please give a valid answer")
      
      

  




