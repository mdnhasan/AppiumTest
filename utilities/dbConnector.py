import pyodbc

connect_string=("Driver={SQL Server};"
                         "Server=192.168.97.52;"
                         "Database=AMBSZM;"
                         "Trusted_Connection=yes;"
                         "uid=sa;"
                         "pwd=oLdViCtOrY2008")


cnxn=pyodbc.connect(connect_string)
cursor=cnxn.cursor()

cursor.execute("select * from config")

result=cursor.fetchall()

for x in result:
    print(x)

