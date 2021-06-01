import mysql.connector, os, json

class DataBase:
    def __init__(self, M):
        self._mafina = M
        self.cursor, self.db = None, None

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
        sql = "SELECT id_user FROM heroku_c93f6b06b535bb4.user WHERE chatID = '%s';" % chat_id
        self.cursor.execute(sql)
        return self.GetValue()

    def GetIDAuthor(self, Name):
        sql = """SELECT id_author FROM heroku_c93f6b06b535bb4.author WHERE Name = "{0}";""".format(Name)
        self.cursor.execute(sql)
        return self.GetValue()

    def SearchBook(self, Name):
        sql = """SELECT b.Name, aut.Name, b.book_lang FROM heroku_c93f6b06b535bb4.book b 
                 JOIN heroku_c93f6b06b535bb4.author aut 
                 ON aut.id_author=b.id_author
                 WHERE b.Name LIKE "%{0}%";""".format(Name)
        self.GetCursor()
        self.cursor.execute(sql)
        return self.cursor

    def BookSystem(self, Book):
        sql = """SELECT count(*) FROM heroku_c93f6b06b535bb4.book b 
                 JOIN heroku_c93f6b06b535bb4.author a 
                 ON a.id_author=b.id_author
                 WHERE b.Name = "{0}" and a.Name = "{1}";""".format(Book.Name, Book.Author)
        Book.Author = int(self.CheckAuthor(Book))
        self.GetCursor()
        self.cursor.execute(sql)
        for x in self.cursor:
            return (lambda x: self.CheckTypeFile(Book) if int(x[0]) != 0 else self.InsertBook(Book))(x)

    def CountBook(self):
        sql = "SELECT count(*) FROM book;"
        self.cursor.execute(sql)
        return self.GetValue()

    def GetBookViaAuthor(self, Name):
        sql = """SELECT b.Name, aut.Name, b.book_lang FROM heroku_c93f6b06b535bb4.book b 
                 JOIN heroku_c93f6b06b535bb4.author aut 
                 ON aut.id_author=b.id_author
                 WHERE aut.Name = "{0}";""".format(Name)
        self.GetCursor()
        self.cursor.execute(sql)
        return self.cursor

    def GetBookInReadList(self, chat_id):
        user_id = self.GetIdUser(chat_id)
        sql = """SELECT b.Name, a.Name, b.book_lang  FROM heroku_c93f6b06b535bb4.list_read_book lrb
                    JOIN heroku_c93f6b06b535bb4.book b
                        ON lrb.id_book = b.id_book
                            JOIN heroku_c93f6b06b535bb4.author a
                                ON b.id_author = a.id_author
	                WHERE lrb.id_user = "{0}";""".format(user_id)
        self.GetCursor()
        self.cursor.execute(sql)
        return self.cursor

    def DeleteBookInReadList(self, chat_id, Name):
        user_id = self.GetIdUser(chat_id)
        id_book = self.GetIdBook(Name)
        sql = """DELETE FROM heroku_c93f6b06b535bb4.list_read_book WHERE id_book = "{0}" and id_user = "{1}";""".format(id_book, user_id)
        self.GetCursor()
        self.cursor.execute(sql)
        self.db.commit()

    def SearchAuthor(self, Name):
        sql = """SELECT Name FROM heroku_c93f6b06b535bb4.author WHERE Name LIKE "%{0}%";""".format(Name)
        self.GetCursor()
        self.cursor.execute(sql)
        return self.cursor

    def GetAnswerSystem(self, chat_id):
        user_id = self.GetIdUser(chat_id)
        sql = "SELECT SystemOfAnswer FROM heroku_c93f6b06b535bb4.bot WHERE id_user = '%s'" % user_id
        self.GetCursor()
        self.cursor.execute(sql)
        return self.GetValue()

    def ChangeAnswerSystem(self, chat_id):
        user_id = self.GetIdUser(chat_id)
        value = self.GetAnswerSystem(chat_id)
        sql = "UPDATE heroku_c93f6b06b535bb4.bot SET SystemOfAnswer =(%s)WHERE id_user =%s;"
        v = (lambda x: False if x else True)(value)
        val = (v, user_id)
        self.GetCursor()
        self.cursor.execute(sql,val)
        self.db.commit()

    def GetFile(self, Name):
        sql = """SELECT file_id_epub, file_id_fb2, file_id_pdf FROM heroku_c93f6b06b535bb4.book WHERE Name = trim("{0}");""".format(Name)
        self.GetCursor()
        self.cursor.execute(sql)
        return self.cursor

    def GetIdBook(self, Name):
        sql = """SELECT id_book FROM heroku_c93f6b06b535bb4.book WHERE Name = "{0}";""".format(Name)
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
        sql = "SELECT count(*) FROM heroku_c93f6b06b535bb4.user WHERE chatID = '%s';"   % chat_id
        self.GetCursor()
        self.cursor.execute(sql)
        for x in self.cursor:
            if int(x[0]) == 0:
                self.Insert(first_name,username, chat_id, language_code, type)

    def CheckTypeFile(self, Book):
        sql = """SELECT {0} FROM heroku_c93f6b06b535bb4.book WHERE Name = "{1}"; """.format(self._mafina.fileformat[Book.format], Book.Name)
        self.GetCursor()
        self.cursor.execute(sql)
        x = self.GetValue()
        print(x)
        return (lambda x: self.UpdateFileId(Book) if x == "" else False)(x)

    def CheckAuthor(self, Book):
        sql = """SELECT * FROM heroku_c93f6b06b535bb4.author WHERE Name = trim("{0}"); """ .format(Book.Author)
        self.GetCursor()
        self.cursor.execute(sql)
        x = self.GetValue()
        if x == None:
            self.InsertAuthor(Book)
            return self.CheckAuthor(Book)
        else:
            return x

    def CheckUserInJob(self, chat_id):
        id_user = self.GetIdUser(chat_id)
        sql = """SELECT chatID, status_sys_sweet_animal, animal_frequency FROM heroku_c93f6b06b535bb4.user u, heroku_c93f6b06b535bb4.job_queue j WHERE u.id_user = {0};""".format(id_user)
        self.GetCursor()
        self.cursor.execute(sql)
        self.db.commit()
        return self.cursor

    def CheckCrypto(self, id, name):
        sql = """SELECT count(*) FROM heroku_c93f6b06b535bb4.Cryptocurrency WHERE id_user = {0} AND pair_crypto = "{1}";""".format(id, name)
        self.GetCursor()
        self.cursor.execute(sql)
        return self.GetValue()

    def InsertAuthor(self, Book):
        sql = """INSERT INTO heroku_c93f6b06b535bb4.author(Name) VALUES(trim("{0}"));""".format(Book.Author)
        self.GetCursor()
        self.cursor.execute(sql)
        self.db.commit()

    def InsertBook(self, Book):
        format = self._mafina.fileformat[Book.format]
        sql = """INSERT INTO heroku_c93f6b06b535bb4.book(Name,{0}, id_author, book_lang) VALUES("{1}", "{2}", "{3}", "{4}");""".format(str(format), Book.Name, Book.file_id, Book.Author, Book.book_lang)
        self.cursor.execute(sql)
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

    def InsertCrypto(self, name, chat_id, price):
        id = self.GetIdUser(chat_id)
        if (self.CheckCrypto(id, name)==0):
            sql = """INSERT INTO heroku_c93f6b06b535bb4.Cryptocurrency(pair_crypto, id_user, price) VALUES("{0}", {1}, {2});""".format(name, id, price)
            print(sql)
            self.GetCursor()
            self.cursor.execute(sql)
            self.db.commit()
        else:
            return 1

    def InsertSysWeather(self, chat_id, status):
        sql = "INSERT INTO heroku_c93f6b06b535bb4.job_queue(status_sys_weather, id_user)VALUES(%s, %s);"
        val = (status, self.GetIdUser(chat_id))
        self.UpdateSys(sql, val)

    def InsertSysAnimal(self, chat_id, status):
        sql = "INSERT INTO heroku_c93f6b06b535bb4.job_queue(status_sys_sweet_animal, id_user)VALUES(%s, %s);"
        val = (status, self.GetIdUser(chat_id))
        self.UpdateSys(sql, val)

    def UpdateFileId(self, Book):
        sql = """UPDATE heroku_c93f6b06b535bb4.book SET {0} =("{1}")WHERE id_book ="{2}";""".format(str(self._mafina.fileformat[Book.format]),str(Book.file_id), str(self.GetIdBook(Book.Name)))
        self.GetCursor()
        self.cursor.execute(sql)
        self.db.commit()
        return True

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
        sql="SELECT chatID, j.status_sys_sweet_animal, animal_frequency FROM heroku_c93f6b06b535bb4.user u, heroku_c93f6b06b535bb4.job_queue j WHERE u.id_user = j.id_user and j.status_sys_sweet_animal = 1;"
        self.GetCursor()
        self.cursor.execute(sql)
        self.db.commit()
        return self.cursor

    def UpdateFrequency(self, val, chat_id):
        id_user = self.GetIdUser(chat_id)
        sql ="""UPDATE job_queue SET animal_frequency =({0}) WHERE id_user = {1};""".format(val, id_user)
        self.GetCursor()
        self.cursor.execute(sql)
        self.db.commit()

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
        sql = "SELECT TelegramFileID FROM heroku_c93f6b06b535bb4.file  WHERE fileID ={0};".format(x)
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
        return data, lang