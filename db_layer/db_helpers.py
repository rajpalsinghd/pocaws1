import mysql.connector
from mysql.connector import Error



def get_connection():
 try:
    connection = mysql.connector.connect(host='rajdb.c08axwwkzq2b.ap-south-1.rds.amazonaws.com',db='mydatabase',user='admin',password='rajpal123')
    if connection.is_connected():
      return connection
    else:return None;
 except Exception as e:
   print("Enter the error in logs",e)
   return None


def get_cursor_object(connection):
 if connection==None:
  return None
 else:
  try:
    if connection.is_connected():
      return connection.cursor()
    else:
      return None
  except Exception as e:
   print(e)
   return None

def create_table(cursor):
 if cursor==None:
  return False
 cursor.execute("Create table users (username varchar(255), email varchar(255),domain varchar(255))")
 return True

def add_our_user(connection,cursor,user):
 try:
  sql = "INSERT INTO users (username, email,domain) VALUES (%s, %s,%s)"  
  val = (user['username'],user['email'],user['domain'])
  cursor.execute(sql, val)
  connection.commit()
  return(cursor.rowcount)
 except Exception as e:
   return None         
      
  
def get_all_users(cursor):
 sql="Select * from users"
 cursor.execute(sql)
 print("I am in get_all_users helper")
 result=cursor.fetchall()
 print("I am ",result)
 return result
 

def close_connection(connection,cursor):
 if(connection):connection.close()
 if(cursor):cursor.close()

 