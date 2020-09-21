import mysql.connector, os

class DataBase:
    def __init__(self):
        self.db = mysql.connector.connect(
            host=os.getenv("HOST"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            database="heroku_c93f6b06b535bb4"
        )

    def GetCursor(self):
        self.cursor = self.db.cursor()
        return self.cursor

    def CheckUser(self, first_name, username, chat_id, language_code, type):
        sql = "SELECT count(*) FROM heroku_c93f6b06b535bb4.user WHERE Name = '%s'"   % first_name
        self.GetCursor()
        self.cursor.execute(sql)
        for x in self.cursor:
            if int(x[0]) == 0:
                print(x[0])
                self.Insert(first_name,username, chat_id, language_code, type)
        self.cursor.close()

    def Insert(self, first_name, username, chat_id, language_code, type):
        s = "INSERT INTO heroku_c93f6b06b535bb4.user(Name, Username, chatID, TypeChat) VALUES(%s, %s, %s, %s);"
        val = (first_name,  username, chat_id, type)
        self.cursor.execute(s, val)
        self.db.commit()
        sql = "SELECT id_user FROM heroku_c93f6b06b535bb4.user WHERE Name = '%s'" % first_name
        self.cursor.execute(sql)
        id = None
        for x in self.cursor:
            id = x[0]
        s = "INSERT INTO heroku_c93f6b06b535bb4.bot(LanguageBot, id_user) VALUES(%s, %s);"
        val = (language_code, id)
        self.cursor.execute(s, val)
        self.db.commit()