import mysql.connector, os, json, badge

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
        sql = "SET @@auto_increment_increment=1;"
        self.cursor.execute(sql)
        return self.cursor

    def GetIdUser(self, chat_id):
        sql = "SELECT id_user FROM heroku_c93f6b06b535bb4.user WHERE chatID = '%s'" % chat_id
        self.cursor.execute(sql)
        return self.GetValue()

    def SearchBook(self, Name):
        sql = "SELECT Name FROM heroku_c93f6b06b535bb4.book WHERE Name LIKE '%{0}%';".format(Name)
        self.GetCursor()
        self.cursor.execute(sql)
        return self.cursor
    
    def GetFile(self, Name):
        sql = "SELECT file_id FROM heroku_c93f6b06b535bb4.book WHERE Name = '%s';" %Name
        self.GetCursor()
        self.cursor.execute(sql)
        return self.GetValue()

    def GetIdBook(self, Name):
        sql = "SELECT id_book FROM heroku_c93f6b06b535bb4.book WHERE Name = '%s';"% Name
        self.GetCursor()
        self.cursor.execute(sql)
        return self.GetValue()

    def AddBookInListRead(self, chat_id, NameBook):
        id_user = self.GetIdUser(chat_id)
        id_book = self.GetIdBook(NameBook)
        sql = "INSERT INTO heroku_c93f6b06b535bb4.list_read_book(id_user, id_book) VALUES({0},{1});".format(id_user, id_book)
        self.GetCursor()
        self.cursor.execute(sql)
        self.db.commit()

    def CheckUser(self, first_name, username, chat_id, language_code, type):
        sql = "SELECT count(*) FROM heroku_c93f6b06b535bb4.user WHERE chatID = '%s'"   % chat_id
        self.GetCursor()
        self.cursor.execute(sql)
        for x in self.cursor:
            if int(x[0]) == 0:
                self.Insert(first_name,username, chat_id, language_code, type)

    def BookSystem(self, Book):
        Book.Author = int(self.CheckAuthor(Book))
        sql = "SELECT count(*) FROM heroku_c93f6b06b535bb4.book WHERE Name = '%s'" % Book.Name
        self.GetCursor()
        self.cursor.execute(sql)
        for x in self.cursor:
            return (lambda x: int(x[0]) != 0 if self.CheckTypeFile(Book) else self.InsertBook(Book))(x)

    def CheckTypeFile(self, Book):
        sql = "SELECT {0} FROM heroku_c93f6b06b535bb4.book WHERE Name = '%s'".format(badge.fileformat[Book.format]) %Book.Name
        self.GetCursor()
        self.cursor.execute(sql)
        x = self.GetValue()
        return (lambda x: x=="" if self.UpdateFileId(Book)else False)(x)

    def UpdateFileId(self, Book):
        print("Update")
        sql = "UPDATE heroku_c93f6b06b535bb4.book SET {0} =(%s)WHERE id_book =%s;".format(str(badge.fileformat[Book.format]))
        val = (Book.file_id, self.GetIdBook(Book.Name))
        self.GetCursor()
        self.cursor.execute(sql,val)
        self.db.commit()
        return True

    def CheckAuthor(self, Book):
        sql = "SELECT * FROM heroku_c93f6b06b535bb4.author WHERE Name = '%s'" % Book.Author
        self.GetCursor()
        self.cursor.execute(sql)
        x = self.GetValue()
        if x == None:
            self.InsertAuthor(Book)
            return self.CheckAuthor(Book)
        else:
            return x

    def InsertAuthor(self, Book):
        sql = "INSERT INTO heroku_c93f6b06b535bb4.author(Name) VALUES('%s');" % Book.Author
        self.GetCursor()
        self.cursor.execute(sql)
        self.db.commit()

    def InsertBook(self, Book):
        format = badge.fileformat[Book.format]
        sql = "INSERT INTO heroku_c93f6b06b535bb.book(Name, {0}, id_author, book_lang) VALUES(%s, %s, %s, %s);".format(str(format))
        val = (Book.Name, str(Book.file_id), Book.Author, Book.book_lang)
        self.cursor.execute(sql, val)
        self.db.commit()
        return True

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

    def InsertFile(self, fileID):
        sql = "INSERT INTO heroku_c93f6b06b535bb4.file(TelegramFileID)VALUES('%s');"%fileID
        self.GetCursor()
        self.cursor.execute(sql)
        self.db.commit()

    def InsertSysWeather(self, chat_id, status):
        sql = "INSERT INTO heroku_c93f6b06b535bb4.job_queue(status_sys_weather, id_user)VALUES(%s, %s);"
        val = (status, self.GetIdUser(chat_id))
        self.UpdateSys(sql, val)

    def InsertSysAnimal(self, chat_id, status):
        sql = "INSERT INTO heroku_c93f6b06b535bb4.job_queue(status_sys_sweet_animal, id_user)VALUES(%s, %s);"
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

    def UpdateSysAnimal(self, chat_id, status):
        sql = "UPDATE heroku_c93f6b06b535bb4.job_queue SET status_sys_sweet_animal=%s WHERE id_user =%s;"
        val = (status, self.GetIdUser(chat_id))
        self.UpdateSys(sql, val)

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

    def UsersSysAnimal(self):
        sql="SELECT chatID, j.status_sys_sweet_animal FROM heroku_c93f6b06b535bb4.user u, heroku_c93f6b06b535bb4.job_queue j WHERE u.id_user = j.id_user;"
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

    def GetCountAnimal(self, chat_id):
        sql = "SELECT j.count_animal FROM heroku_c93f6b06b535bb4.user u, heroku_c93f6b06b535bb4.job_queue j WHERE u.id_user = j.id_user and u.chatID ='%s';"%chat_id
        self.GetCursor()
        self.cursor.execute(sql)
        self.db.commit()
        return self.GetValue()

    def GetFileId(self, x):
        sql = "SELECT TelegramFileID FROM heroku_c93f6b06b535bb4.file  WHERE fileID ='%s';"%x
        self.GetCursor()
        self.cursor.execute(sql)
        self.db.commit()
        return self.GetValue()

    def UpCountAnimal(self, chat_id):
        x = self.GetCountAnimal(chat_id)
        print(x)
        x+=1
        sql = "UPDATE heroku_c93f6b06b535bb4.job_queue SET count_animal=%s WHERE id_user =%s;"
        val =(x, self.GetIdUser(chat_id))
        self.UpdateSys(sql, val)

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