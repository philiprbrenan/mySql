import mysql.connector

# Connect to server
cnx = mysql.connector.connect(host="127.0.0.1", port=3306, user="root", password="root")   # Connect
cur = cnx.cursor()                                                                         # Create cursor
cur.execute("SELECT CURDATE()")                                                            # Execute a query
row = cur.fetchone()                                                                       # Fetch row 
print("Current date is: {0}".format(row[0]))
cur.execute("CREATE DATABASE test")
cur.execute("CREATE TABLE test.people(name text, phone text)")
cur.execute("INSERT INTO  test.people values('aaa', 111)")
cur.execute("INSERT INTO  test.people values('bbb', 222)")
cur.execute("INSERT INTO  test.people values('ccc', 333)")
cur.execute("INSERT INTO  test.people values('ddd', 444)")
cur.execute("INSERT INTO  test.people values('eee', 555)")
cur.execute("SELECT COUNT(*) FROM test.people")
row = cur.fetchone()                                                                       # Fetch row 
print("The number of rows is ", row[0])

cnx.close()                                                                                # Close   
