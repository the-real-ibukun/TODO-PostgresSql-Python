#!/usr/bin/python
"""
STEPS

1. Ensure python has been set as a path variable
2. Download postgresSQL
3. Ensure you have pip installed and updated
4. Pip install psycopg2
5. Create DB in postgress
6. Connect to postgress and handle the connection object with connection.cursor() to execute queries
"""
import psycopg2
import sys
import pprint
 

def main():
    #Define our connection string
	conn_string = "host='localhost' dbname='todolist' user='postgres' password='postgres'"
 
	# print the connection string we will use to connect
	print ("Connecting to database\n	->%s" % (conn_string))
 
	# get a connection, if a connect cannot be made an exception will be raised here
	conn = psycopg2.connect(conn_string)
 
	# conn.cursor will return a cursor object, you can use this cursor to perform queries Allows Python code to execute PostgreSQL command in a database session. Cursors are created by the connection.cursor() method: they are bound to the connection for the entire lifetime and all the commands are executed in the context of the database session wrapped by the connection.
	cur = conn.cursor()
    
	print ("Connected!\n")
    

def create_tables():
    """ create tables in the PostgreSQL database"""
    conn = None
    try:
        # read the connection parameters
        
        # connect to the PostgreSQL server
        conn_string = "host='localhost' dbname='todolist' user='postgres' password='postgres'"
        conn = psycopg2.connect(conn_string)
        
        cur = conn.cursor()
        
        cur.execute('''CREATE TABLE COMPANY
      (ID INT PRIMARY KEY     NOT NULL,
      NAME           TEXT    NOT NULL,
      AGE            INT     NOT NULL,
      ADDRESS        CHAR(50),
      SALARY         REAL);''')
        print ("Table created successfully")
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
 
def insert():
    conn = None
    id = None
    try:
        conn_string = "host='localhost' dbname='todolist' user='postgres' password='postgres'"
        conn = psycopg2.connect(conn_string)
        cur = conn.cursor()

        name = input("Enter new todo: ")

        cur.execute("INSERT INTO TODO (name) VALUES (%s) ",(name,))
        print ("INSERTED", "\n")
        
        cur.execute("SELECT id, name from TODO")
        rows = cur.fetchall()
        print("UPDATED TODO'S")
        for row in rows: 
            print ("ID = ", row[0])
            print ("NAME = ", row[1], "\n")

        
        # commit the changes
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
     
    
    
def fetchall():
    conn = None
    try:
        conn_string = "host='localhost' dbname='todolist' user='postgres' password='postgres'"
        conn = psycopg2.connect(conn_string)
        cur = conn.cursor()
        
        print("AVAILABLE TODO'S")
        
        cur.execute("SELECT id, name from TODO")
        rows = cur.fetchall()
        for row in rows: 
            print ("ID = ", row[0])
            print ("NAME = ", row[1], "\n")

        
         
        # commit the changes
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    
    



def update():
    conn = None 
    try:
    
        conn_string =  " host='localhost' dbname='todolist' user='postgres' password='postgres' "
        conn = psycopg2.connect(conn_string)
        cur = conn.cursor()
        print("AVAILABLE TODO'S")
        #Display all TOdo
        cur.execute("SELECT id, name from TODO")
        rows = cur.fetchall()
        for row in rows: 
            print ("ID = ", row[0])
            print ("NAME = ", row[1], "\n")
        
        print("EDIT TODO'S")
        #Request for ID    
        idd = input("Enter the TODO ID: ")
        name  = input("Enter the NEW TODO: ")
        print("\n")
        
        cur.execute(''' UPDATE TODO set name = (%s) where id = (%s) ''',(name, idd))
        
        cur.execute("SELECT id, name from TODO")
        rows = cur.fetchall()
        print("UPDATED TODO'S")
        for row in rows: 
            print ("ID = ", row[0])
            print ("NAME = ", row[1], "\n")
            
        conn.commit()
        cur.close()
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()      

            
            
def delete():  
    conn = None 
    try:
    
        conn_string =  " host='localhost' dbname='todolist' user='postgres' password='postgres' "
        conn = psycopg2.connect(conn_string)
        cur = conn.cursor()
        print("AVAILABLE TODO'S")
        #Display all TOdo
        cur.execute("SELECT id, name from TODO")
        rows = cur.fetchall()
        for row in rows: 
            print ("ID = ", row[0])
            print ("NAME = ", row[1], "\n")
        
        print("DELETE TODO'S")
        #DELETE for ID    
        idd = input("Enter the TODO ID: " )
        print("\n")
        
            
        
        cur.execute(''' DELETE FROM TODO where id = (%s) ''',(idd))
        
        cur.execute("SELECT id, name from TODO")
        rows = cur.fetchall()
        print("UPDATED TODO'S")
        for row in rows: 
            print ("ID = ", row[0])
            print ("NAME = ", row[1], "\n")
            
        conn.commit()
        cur.close()
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()      
        
        
print ("   *** WELCOME TO TODO APPLICATION ***   ", "\n")      
    
if __name__ == '__main__':
    fetchall()
    
act = input("To create todo enter - c , edit todo  -e or delete todo -d: ")    

if act == "c":
    insert()
elif act == "e":
    update()
elif act == "d":
    delete()
else:
    print("This is an invaid input")
    
 
    
 