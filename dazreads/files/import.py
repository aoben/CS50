#import library dependency. psycopg2 is a postgres library

import csv
import psycopg2

#connect to db - d10jbj0bu0oie5

conn = psycopg2.connect('postgresql://mgultkmabtmtfo:63bbf2d3b7a2eedf489c1ee0919bf0b83a938da5076e5e2ca1b1f80e0cb69e26@ec2-54-83-61-142.compute-1.amazonaws.com/d10jbj0bu0oie5')
cursor = conn.cursor() # creating cursor object

#check connection params
print(conn.get_dsn_parameters(), end='\n')

#truncate and commit table to make sure its empty. uncomment the lines below
    #cursor.execute("TRUNCATE TABLE books;")
    #conn.commit()                 
#open csv file for import

#with open('books.csv', 'r') as 'f':
read_book = csv.reader(open('/Users/Oben/Documents/CS50/Project1/dazreads/files/books.csv', 'r'))

next(read_book)          #skip the first row

# loop to insert records into db

    #for row in read_book:
    #cursor.execute("INSERT INTO public.books (isbn, title, author, year) VALUES (%s, %s, %s, %s);", row)
    #conn.commit()

#check records have been inserted
cursor.execute("SELECT COUNT(*) FROM books;")
record = cursor.fetchone()
print("You are connected to - ", record,"\n")