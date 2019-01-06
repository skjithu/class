import mysql.connector

class DataBase:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Python@12",
            database="ecomm"
        )

    def insertRowInTable(self,sql,values):
        mycursor = self.mydb.cursor()
        mycursor.execute(sql,values)
        self.mydb.commit()

    def selectRowFromTable(self,sql):
        mycursor = self.mydb.cursor()
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult

