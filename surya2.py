
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="0025",
  database="library"
)
mycursor = mydb.cursor()
t=()

c=0
a=input('enter your M_ID')
b=input('enter password')


mycursor.execute("select * from member")
row=mycursor.fetchone()
while row is not None:
    if(a==row[1] and b==row[0]):
        c=c+1
        t=t+(row,)
        row=mycursor.fetchone()
    else:
        row=mycursor.fetchone()

for y in t:
    d=y[2]
        
if(c==1):
    print("Welcome, ", a)
    print(t)
    print("Books to be returned: ", d)
else:
    print("Incorrect")
