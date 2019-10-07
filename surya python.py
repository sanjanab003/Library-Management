
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

def loop():
    mycursor.execute("select * from member")
    row=mycursor.fetchone()
    while row is not None:
        if(a==row[1] and b==row[0]):
            global c
            global t
            c=c+1
            t=t+(row,)
            row=mycursor.fetchone()
        else:
            row=mycursor.fetchone()


loop()
for y in t:
    d=y[2]
if(c==1):
    print("Welcome, ", a)
    print(t)
    print("Books to be returned: ", d)
else:
    print("Incorrect")
  
 
   

d=input('enter the name of the book to be returned:')

loop()
if(row[2]==d):
    m=input('Are you sure to return the book', d)
    if(s=='yes'):
        sql_update="""update Member set No_books_borrowed=%s where M_ID=%s"""
        data=(No_books_borrowed-1,a)

        mycursor.execute(sql_update,data)

        connection.commit()

        sql_booksupdate="""update Member set books_borrowed=%s where M_ID=%s"""

        databookname=("no books borrowed" ,a)

        mycursor.execute(sql_booksupdate,databookname)

        connection.commit()

        books_sql="""update Books set Qty=%s where Book_Name=%s"""

        databooks=((Qty+1),d)

        mycursor.execute(books_sql,databooks)

        connection.commit()

    

sql_select_query="select status from books where M_ID='a'"
mycursor.execute(sql_select_query)



if (status=='Not Available'):

    avilable_update="""update Books set status=%s where M_ID=%s"""

    available_data=('Available',a)

    mycursor.execute(available_update,availablle_data)

    connection.commit()

print('The book has been succesfully returned')    









