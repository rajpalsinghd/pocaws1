import mysql.connector
from mysql.connector import Error


#This function is responsible for getting a connection object.
def get_connection():
 try:
    #connection string for amazon rds.
    connection = mysql.connector.connect(host='rajdb.c08axwwkzq2b.ap-south-1.rds.amazonaws.com',db='mydatabase',user='admin',password='rajpal123')
    if connection.is_connected():
      return connection
    else:return None;
 except Exception as e:
   print("Enter the error in logs",e)
   return None

#This function is responsible for getting cursor object.
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

  
  
#This function is responsible for creating a table(alredy decided for learning purpose).  
def create_table(cursor):
 if cursor==None:
  return False
 cursor.execute("Create table users (username varchar(255), email varchar(255),domain varchar(255))")
 return True

#This function is responsible for adding user credentials(user object).
def add_our_user(connection,cursor,user):
 try:
  sql = "INSERT INTO users (username, email,domain) VALUES (%s, %s,%s)"  
  val = (user['username'],user['email'],user['domain'])
  print(sql)
  print(val)
  cursor.execute(sql, val)
  connection.commit()
  print(cursor.rowcount)
  return(cursor.rowcount)
 except Exception as e:
   print(e)
   return None         
      
#This function is responsible for returning list of users.
def get_all_users(cursor):
 sql="Select * from users"
 cursor.execute(sql)
 print("I am in get_all_users helper")
 result=cursor.fetchall()
 print("I am ",result)
 return result
 
#This function is responsible for closing connection successfully.
def close_connection(connection,cursor):
 if(connection):connection.close()
 if(cursor):cursor.close()

 
