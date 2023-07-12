from utilities import dbManager

dbManager.db_connect()
dbManager.getmyData("select top 10 * from config")