import mysql.connector

# Connect to server
cnx = mysql.connector.connect(host="127.0.0.1", port=3306, user="root", password="root")   # Connect
cur = cnx.cursor()                                                                         # Create cursor
cur.execute("SELECT CURDATE()")                                                            # Execute a query
row = cur.fetchone()                                                                       # Fetch row 
print("Current date is: {0}".format(row[0]))

cur.execute("CREATE DATABASE test")                                                        # Create database
cur.execute("CREATE TABLE test.people(name text, phone text)")                             # Create table

cur.execute("INSERT INTO  test.people values('aaa', 111)")                                 # Load table  
cur.execute("INSERT INTO  test.people values('bbb', 222)")
cur.execute("INSERT INTO  test.people values('ccc', 333)")
cur.execute("INSERT INTO  test.people values('ddd', 444)")
cur.execute("INSERT INTO  test.people values('eee', 555)")

cur.execute("SELECT COUNT(*) FROM test.people")                                            # Count rows 
row = cur.fetchone()                                                                        
print("The number of rows is ", row[0])
cur.close()

cur = cnx.cursor()                                                                         # Create cursor
cur.execute("update test.people set phone = 666 where name = 'eee'");                      # Update
 
cur.execute("SELECT * FROM test.people")                                                   # Select 
results = cur.fetchall()

for r in results: 
  print(r)

cur.close()

cur = cnx.cursor()                                                                         # Create cursor
cur.execute("delete from test.people where phone = 666")                                   # Delete 
cur.execute("SELECT COUNT(*) FROM test.people")                                            # Count rows 
row = cur.fetchone()                                                                        
print("The number of rows after the delete is ", row[0])

cur.close()

cnx.close()                                                                                # Close   
