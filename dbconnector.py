import pyodbc

def readlogin(username):
    cursor = Login.conn.cursor()
    query = "select * from Login.[common].[user] where username = '%s'" % (username)
    cursor.execute(query)
    for row in cursor:
        return(row[1])

def readcustomer():
    cursor = Login.conn.cursor()
    query = "select * from Login.[common].[customer] order by customer_no desc"
    cursor.execute(query)
    print('read customer')
    return cursor

class Login():
    conn = pyodbc.connect(
        "Driver={ODBC Driver 17 for SQL Server};"
        "Server=DESKTOP-K0P889B;"
        "Database=Login;"
        "Trusted_Connection=yes;"
)

readlogin(Login.conn)
