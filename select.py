import mysql.connector

# Connect to server
cnx = mysql.connector.connect(host="127.0.0.1", port=3306, user="root", password="root")   # Connect
cur = cnx.cursor()                                                                         # Create cursor
cur.execute("SELECT CURDATE()")                                                            # Execute a query
row = cur.fetchone()                                                                       # Fetch row 
print("Current date is: {0}".format(row[0]))

cur.execute("CREATE TABLE people(name text, phone, text)")
cur.execute("INSERT INTO  people values('aaa', 111)");
cur.execute("INSERT INTO  people values('bbb', 222)");
cur.execute("SELECT COUNT(*) FROM people");
row = cur.fetchone()                                                                       # Fetch row 
print(row)

cnx.close()                                                                                # Close   
