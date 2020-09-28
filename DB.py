import mysql.connector, os

class DataBase:
    def __init__(self):
        self.cursor = None
        self.db = None

    def GetCursor(self):
        if self.cursor and self.db:
            self.cursor.close()
            self.db.close()
        self.db = mysql.connector.connect(
            host=os.getenv("HOST"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            database="heroku_c93f6b06b535bb4"
        )
        self.cursor = self.db.cursor(buffered=True)
        return self.cursor

    def GetIdUser(self, first_name):
        sql = "SELECT id_user FROM heroku_c93f6b06b535bb4.user WHERE Name = '%s'" % first_name
        self.cursor.execute(sql)
        id = None
        for x in self.cursor:
            id = x[0]
        return id

    def CheckUser(self, first_name, username, chat_id, language_code, type):
        sql = "SELECT count(*) FROM heroku_c93f6b06b535bb4.user WHERE Name = '%s'"   % first_name
        self.GetCursor()
        self.cursor.execute(sql)
        for x in self.cursor:
            if int(x[0]) == 0:
                print(x[0])
                self.Insert(first_name,username, chat_id, language_code, type)

    def Insert(self, first_name, username, chat_id, language_code, type):
        s = "INSERT INTO heroku_c93f6b06b535bb4.user(Name, Username, chatID, TypeChat) VALUES(%s, %s, %s, %s);"
        val = (first_name,  username, chat_id, type)
        self.cursor.execute(s, val)
        self.db.commit()
        id = self.GetIdUser(first_name)
        s = "INSERT INTO heroku_c93f6b06b535bb4.bot(LanguageBot, id_user) VALUES(%s, %s);"
        val = (language_code, id)
        self.cursor.execute(s, val)
        self.db.commit()

    def VerificationLanguage(self, first_name,preferred_language, Translatelanguage = True):
        self.GetCursor()
        id = self.GetIdUser(first_name)
        if Translatelanguage:
            sql = "UPDATE heroku_c93f6b06b535bb4.bot SET TranslateLanguage = %s WHERE id_user =%s;"
        else:
            sql = "UPDATE heroku_c93f6b06b535bb4.bot SET LanguageBot = %s WHERE id_user =%s;"
        val =(preferred_language, id)
        self.cursor.execute(sql, val)
        self.db.commit()

    def GetLanguage(self,first_name, Translatelanguage = True):
        self.GetCursor()
        id = self.GetIdUser(first_name)
        if Translatelanguage:
            sql = "SELECT TranslateLanguage FROM heroku_c93f6b06b535bb4.bot WHERE id_user = '%s'" % id
        else:
            sql = "SELECT LanguageBot FROM heroku_c93f6b06b535bb4.bot WHERE id_user = '%s'" % id
        self.cursor.execute(sql)
        lang = None
        for x in self.cursor:
            lang = x[0]
        return lang
