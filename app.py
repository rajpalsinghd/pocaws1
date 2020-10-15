from flask import *
from db_layer.db_helpers import *
app=Flask(__name__)




@app.route("/api/user/register",methods=["POST"])
def add_user():
 try:
  if request.method=="POST":
   connection=None
   cursor=None
   user=request.get_json()
   user=user['user']
   connection=get_connection()
   if(connection):
     cursor=get_cursor_object(connection)
     if(cursor):
      c=add_our_user(connection,cursor,user)
      close_connection(connection,cursor)
      if(c):return Response(status=200)
      else:
       close_connection(connection,cursor)
       return Response(status=400) 
   else:
    close_connection(connection,cursor)
    return Response(status=400) 
 except Exception as e:
  print(e)
  return Response(status=400)

@app.route("/api/user/getusers",methods=["POST"])
def get_users():
 try:
    connection=None
    cursor=None
    users=[]
    connection=get_connection()
    if(connection):
     print("Connection established in getUsers")
     cursor=get_cursor_object(connection)
     if(cursor):users=get_all_users(cursor)
    close_connection(connection,cursor)  
    return jsonify({"users":users})
 except Exception as e:
  return "Some error and maintain logs"

if __name__=="__main__":
 connection=get_connection()
 #is_created=create_table(get_cursor_object(connection))
 #if(is_created):
 close_connection(connection,get_cursor_object(connection))
 app.run(port=4000)