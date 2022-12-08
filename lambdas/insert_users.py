import json
import mysql.connector

conn = mysql.connector.connect(
  host="",
  user="MainUser",
  password="MainPassword",
  database='Backoffice'
)

def insert_users(payload):
    
    for item in payload['data']:
        
        insert_item = f"""INSERT INTO user (is_active, created_date, name) 
                          VALUES ('{item['is_active']}', '{item['created_date']}', '{item['name']}')"""
    
    
        conn.execute(insert_item)
        
        
        
        




