import sqlite3

conn = sqlite3.connect('movies800a.db')
cur = conn.cursor()


# Write a query that counts the number of actors. 
# Using Python send this query to SQLite and retrieve the answer.
query="select count(*) from actors"
answer = cur.execute(query).fetchone()
print(" there are ", answer, " actors")

# What is the type of data that is returned?
print("the data type is ", type(answer))

cur.close()