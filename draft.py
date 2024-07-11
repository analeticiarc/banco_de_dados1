import pandas as pd
import sqlite3

data = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David']
})

# create a Connection

conn = sqlite3.connect('mydatabase.db')

# Use the to_sql method to save the DataFrame data.to_sql
data.to_sql(
    'client', conn,
    if_exists = 'replace',
    index= False
)

# closing teh connection
conn.close()

conn = sqlite3.connect('mydatabase.db')

cursos = conn.cursor()

# a sequencia precisa ser SELECT -> FROM -> WERE
query = '''
    SELECT Name As Nome
    FROM client
    WERE Nome = 'Alice'
'''

pd.read_sql_query(query, conn)