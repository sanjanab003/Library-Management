
  

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="1234",
  database="library"
)
mycursor = mydb.cursor()

a=input('enter your M_ID')
print(a)
c=mycursor.fetchone()
z=mycursor.no_books_borrowedcount
if(z>0):

    b=input('These are the Number Of  Books Borrowed:',z)
    print(b)
    x=select books_borrowed where M_ID = a
    print(x)
else:
    print('no books books borrowed')
d=input('enter the name of the book to be returned:')
e=input('enter the book_id of the book to be returned')
print(d)
print(a)
m=input('Are you sure to return the book', d)
s=input('Yes or No')
if(s=='yes'):
    sql_update="""update Member set No_books_borrowed=%s where M_ID=%s"""
    data=(No_books_borrowed-1,a)
    mycursor.execute(sql_update,data)
    connection.commit()
    sql_booksupdate="""update Member set books_borrowed=%s where M_ID=%s"""
    databookname=(     ,a)
    mycursor.execute(sql_booksupdate,databookname)
    connection.commit()
    books_sql="""update Books set Qty=%s where Book_Name=%s"""
    databooks=((Qty+1),d)
    mycursor.execute(books_sql,databooks)
   connection.commit()
status=mycursor.fetchone()   
if (status='Not Available'):
    avilable_update="""update Books set status=%s where M_ID=%s"""
    available_data=('Available',a)
    mycursor.execute(available_update,availablle_data)
    connection.commit()
print('The book has been succesfully returned')    
    
    



