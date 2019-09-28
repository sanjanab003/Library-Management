c=0
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="0025",
  database="library"
)
mycursor = mydb.cursor()
mycursor.execute("select Name, M_Pass from member")
user=input("Enter username: ")
pas=input("Enter password: ")
row = mycursor.fetchone()
while row is not None:
  if(row[0]==user and row[1]==pas):
      print("Welcome", user)
      c=c+1
      break;
  else:
      pass;
      row = mycursor.fetchone()
if(c==0):
    print("Please register")
    u=input("Enter your name: ")
    p=input("Enter a password: ")
    add_member = ("INSERT INTO member "
               "(Name, M_Pass) "
               "VALUES (%s, %s)")
    data_member = (u,p)
    mycursor.execute(add_member, data_member)
    mydb.commit()
    print("Member, ", u, " is succesfully added.")




    


        
    



    
