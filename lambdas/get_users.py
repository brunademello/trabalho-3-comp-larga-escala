import json
import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
  host="",
  user="MainUser",
  password="MainPassword",
  database='Backoffice'
)

def get_users():
    
    df = pd.read_sql(""" select * from user""", conn)
    
    users = df.name.tolist()
    
    return {
        'statusCode': 200,
        'body': json.dumps(users)
    }
    
get_users()