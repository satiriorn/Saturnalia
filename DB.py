import mysql.connector, os, json

class DataBase:
    def __init__(self):
        self.cursor = None
        self.db = None

    def GetValue(self):
        value = None
        for x in self.cursor:
            value = x[0]
        return value

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

    def GetIdUser(self, chat_id):
        sql = "SELECT id_user FROM heroku_c93f6b06b535bb4.user WHERE chatID = '%s'" % chat_id
        self.cursor.execute(sql)
        return self.GetValue()

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
        id = self.GetIdUser(chat_id)
        s = "INSERT INTO heroku_c93f6b06b535bb4.bot(LanguageBot, id_user) VALUES(%s, %s);"
        val = (language_code, id)
        self.cursor.execute(s, val)
        self.db.commit()

    def InsertSysMeme(self, chat_id, status, interval):
        sql = "INSERT INTO heroku_c93f6b06b535bb4.job_queue(Span, status_sys_meme, id_user)VALUES(%s, %s, %s);"
        val = (interval, status, self.GetIdUser(chat_id))
        self.UpdateSys(sql, val)

    def InsertSysWeather(self, chat_id, status):
        sql = "INSERT INTO heroku_c93f6b06b535bb4.job_queue(status_sys_weather, id_user)VALUES(%s, %s);"
        val = (status, self.GetIdUser(chat_id))
        self.UpdateSys(sql, val)

    def UpdateSysWeather(self, chat_id, status):
        sql = "UPDATE heroku_c93f6b06b535bb4.job_queue SET status_sys_weather=%s WHERE id_user =%s;"
        val = (status, self.GetIdUser(chat_id))
        self.UpdateSys(sql, val)

    def UpdateSysMeme(self, chat_id, status, interval):
        sql = "UPDATE heroku_c93f6b06b535bb4.job_queue SET Span =%s, status_sys_meme=%s WHERE id_user =%s;"
        val = (interval, status, self.GetIdUser(chat_id))
        self.UpdateSys(sql,val)

    def UpdateSys(self,sql,val):
        self.GetCursor()
        self.cursor.execute(sql,val)
        self.db.commit()

    def UsersSysMeme(self):
        sql="SELECT chatID, j.Span, j.status_sys_meme FROM heroku_c93f6b06b535bb4.user u, heroku_c93f6b06b535bb4.job_queue j WHERE u.id_user = j.id_user;"
        self.GetCursor()
        self.cursor.execute(sql)
        self.db.commit()
        return self.cursor

    def UsersSysWeather(self):
        sql="SELECT chatID, j.status_sys_weather FROM heroku_c93f6b06b535bb4.user u, heroku_c93f6b06b535bb4.job_queue j WHERE u.id_user = j.id_user;"
        self.GetCursor()
        self.cursor.execute(sql)
        self.db.commit()
        return self.cursor

    def VerificationLanguage(self, chat_id,preferred_language, Translatelanguage = True):
        self.GetCursor()
        id = self.GetIdUser(chat_id)
        if Translatelanguage:
            sql = "UPDATE heroku_c93f6b06b535bb4.bot SET TranslateLanguage = %s WHERE id_user =%s;"
        else:
            sql = "UPDATE heroku_c93f6b06b535bb4.bot SET LanguageBot = %s WHERE id_user =%s;"
        val =(preferred_language, id)
        self.cursor.execute(sql, val)
        self.db.commit()

    def GetTranslateLanguage(self,chat_id):
        self.GetCursor()
        id = self.GetIdUser(chat_id)
        sql = "SELECT TranslateLanguage FROM heroku_c93f6b06b535bb4.bot WHERE id_user = '%s'" % id
        self.cursor.execute(sql)
        return self.GetValue()

    def GetLanguageBot(self, chat_id):
        self.GetCursor()
        id = self.GetIdUser(chat_id)
        sql = "SELECT LanguageBot FROM heroku_c93f6b06b535bb4.bot WHERE id_user = '%s'" % id
        self.cursor.execute(sql)
        res = self.GetValue()
        return (lambda self, res :"uk" if res == None else res)(self, res)

    def GetJsonLanguageBot(self, chat_id):
        lang = self.GetLanguageBot(chat_id)
        patch ="languages/{0}.json".format(lang)
        with open(patch, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            json_file.close()
        return data