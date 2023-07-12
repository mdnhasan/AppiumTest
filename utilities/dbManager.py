import pyodbc


def db_connect():
    global cnxn
    connect_string = ("Driver={SQL Server};"
                      "Server=192.168.97.52;"
                      "Database=AMBSZM;"
                      "Trusted_Connection=yes;"
                      "uid=sa;"
                      "pwd=oLdViCtOrY2008")

    cnxn = pyodbc.connect(connect_string)

def getmyData(query):
    cursor = cnxn.cursor()

    cursor.execute(query)

    result = cursor.fetchall()

    for x in result:
        print(x)
