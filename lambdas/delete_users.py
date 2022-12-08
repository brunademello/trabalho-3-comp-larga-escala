import json
import mysql.connector

conn = mysql.connector.connect(
  host="",
  user="MainUser",
  password="MainPassword",
  database='Backoffice'
)

def delete_users(payload):    
        
    delete_item = f"""DELETE FROM user WHERE id = {payload['data']['user_id']} """    
    
    conn.execute(delete_item)