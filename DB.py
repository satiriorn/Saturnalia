import mysql.connector,os

class DataBase:
    def __init__(self):
        self.db = mysql.connector.connect(
            host=os.getenv("HOST"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            database="heroku_c93f6b06b535bb4"
        )
        self.cursor = self.db.cursor()

    def GetCursor(self):
        return self.cursor

    def Commit(self):
        self.db.commit()

    def CheckUser(self, first_name, username, chat_id):
        sql = "SELECT count(*) FROM heroku_c93f6b06b535bb4.user WHERE Name = '%s'" % first_name
        self.cursor.execute(sql)
        for x in self.cursor:
            if int(x[0]) == 0:
                DataBase.Insert(self,first_name,username, chat_id)

    def Insert(self, first_name, username, chat_id):
        s = "INSERT INTO heroku_c93f6b06b535bb4.user(Name,Username,chatID) VALUES(%s, %s, %s)"
        val = (first_name,  username, chat_id)
        self.cursor.execute(s, val)
        self.Commit()