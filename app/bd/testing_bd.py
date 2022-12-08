import mysql.connector
import pandas as pd

conn = mysql.connector.connect(
  host="172.31.10.175",
  user="MainUser",
  password="MainPassword",
  database='Backoffice'
)

df = pd.read_sql(""" select * from user""", conn)

print(df)
