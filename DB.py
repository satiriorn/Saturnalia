import mysql.connector, os, json, Thread

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
            database="vgjy6o15h95ug01f"
        )
        self.cursor = self.db.cursor(buffered=True)
        sql = "SET @@auto_increment_increment=1;"
        self.cursor.execute(sql)
        return self.cursor

    def GetIdUser(self, chat_id):
        sql = "SELECT id_user FROM vgjy6o15h95ug01f.user WHERE chatID = '%s';" % chat_id
        self.cursor.execute(sql)
        return self.cursor.fetchone()[0]
        #return self.GetValue()

    def GetUsername(self, chat_id):
        sql = "SELECT Username FROM vgjy6o15h95ug01f.user WHERE chatID = '%s';" % chat_id
        self.cursor.execute(sql)
        return self.GetValue()

    def GetIDAuthor(self, Name):
        sql = """SELECT id_author FROM vgjy6o15h95ug01f.author WHERE Name = "{0}";""".format(Name)
        self.cursor.execute(sql)
        return self.GetValue()

    def SearchBook(self, Name):
        sql = """SELECT b.Name, aut.Name, b.book_lang FROM vgjy6o15h95ug01f.book b 
                 JOIN vgjy6o15h95ug01f.author aut 
                 ON aut.id_author=b.id_author
                 WHERE b.Name LIKE "%{0}%";""".format(Name)
        self.GetCursor()
        self.cursor.execute(sql)
        return self.cursor

    def BookSystem(self, Book):
        sql = """SELECT count(*) FROM vgjy6o15h95ug01f.book b 
                 JOIN vgjy6o15h95ug01f.author a 
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
        sql = """SELECT b.Name, aut.Name, b.book_lang FROM vgjy6o15h95ug01f.book b 
                 JOIN vgjy6o15h95ug01f.author aut 
                 ON aut.id_author=b.id_author
                 WHERE aut.Name = "{0}";""".format(Name)
        self.GetCursor()
        self.cursor.execute(sql)
        return self.cursor

    def GetCountAnimal(self, chat_id):
        sql = "SELECT j.count_animal FROM vgjy6o15h95ug01f.user u, vgjy6o15h95ug01f.job_queue j WHERE u.id_user = j.id_user and u.chatID ='%s';"%chat_id
        self.GetCursor()
        self.cursor.execute(sql)
        self.db.commit()
        return self.GetValue()

    def GetAnswers(self, chat_id):
        id = self.GetIdUser(chat_id)
        sql = "SELECT text_answer FROM vgjy6o15h95ug01f.answers WHERE id_user ='%s';" % id
        self.GetCursor()
        self.cursor.execute(sql)
        return self.cursor

    def GetFileId(self, x):
        sql = "SELECT TelegramFileID FROM vgjy6o15h95ug01f.file  WHERE fileID ={0};".format(x)
        self.GetCursor()
        self.cursor.execute(sql)
        self.db.commit()
        return self.GetValue()

    def GetBookInReadList(self, chat_id):
        user_id = self.GetIdUser(chat_id)
        sql = """SELECT b.Name, a.Name, b.book_lang  FROM vgjy6o15h95ug01f.list_read_book lrb
                    JOIN vgjy6o15h95ug01f.book b
                        ON lrb.id_book = b.id_book
                            JOIN vgjy6o15h95ug01f.author a
                                ON b.id_author = a.id_author
	                WHERE lrb.id_user = "{0}";""".format(user_id)
        self.GetCursor()
        self.cursor.execute(sql)
        return self.cursor
    def GetCountOfFileAnimal(self):
        sql = """SELECT count(*) FROM file;"""
        self.GetCursor()
        self.cursor.execute(sql)
        return self.GetValue()

    def GetCryptoPairUser(self, chat_id, onlyname = False):
       # user_id = self.GetIdUser(chat_id)
        if onlyname: sql = """SELECT pair_crypto FROM vgjy6o15h95ug01f.Cryptocurrency с 
                                JOIN vgjy6o15h95ug01f.user u 
                                    USING (id_user)
                                        WHERE u.chatID = {0};""".format(chat_id)
        else: sql = """SELECT pair_crypto, id_user, price FROM vgjy6o15h95ug01f.Cryptocurrency с 
                                JOIN vgjy6o15h95ug01f.user u 
                                    USING (id_user)
                                        WHERE u.chatID = {0};""".format(chat_id)
        self.GetCursor()
        self.cursor.execute(sql)
        res = []
        for x in self.cursor:
            for y in range(len(x)):
                res.append(x[y])
        return res

    def GetFile(self, Name):
        sql = """SELECT file_id_epub, file_id_fb2, file_id_pdf FROM vgjy6o15h95ug01f.book WHERE Name = trim("{0}");""".format(Name)
        self.GetCursor()
        self.cursor.execute(sql)
        return self.cursor

    def GetIdBook(self, Name):
        sql = """SELECT id_book FROM vgjy6o15h95ug01f.book WHERE Name = "{0}";""".format(Name)
        self.GetCursor()
        self.cursor.execute(sql)
        return self.GetValue()

    def GetTranslateLanguage(self,chat_id):
        self.GetCursor()
        id = self.GetIdUser(chat_id)
        sql = "SELECT TranslateLanguage FROM vgjy6o15h95ug01f.bot WHERE id_user = '%s'" % id
        self.cursor.execute(sql)
        return self.GetValue()

    def GetLanguageBot(self, chat_id):
        self.GetCursor()
        id = self.GetIdUser(chat_id)
        sql = "SELECT LanguageBot FROM vgjy6o15h95ug01f.bot WHERE id_user = '%s'" % id
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

    def GetAllCryptoUsers(self):
        sql = """SELECT DISTINCT chatID FROM vgjy6o15h95ug01f.Cryptocurrency c
                    JOIN vgjy6o15h95ug01f.user u 
                        ON c.id_user=u.id_user;"""
        self.GetCursor()
        self.cursor.execute(sql)
        return self.cursor

    def DeleteBookInReadList(self, chat_id, Name):
        user_id = self.GetIdUser(chat_id)
        id_book = self.GetIdBook(Name)
        sql = """DELETE FROM vgjy6o15h95ug01f.list_read_book WHERE id_book = "{0}" and id_user = "{1}";""".format(id_book, user_id)
        self.GetCursor()
        self.cursor.execute(sql)
        self.db.commit()

    def DeleteCryptoPair(self, chat_id, name):
        user_id = self.GetIdUser(chat_id)
        sql = """DELETE FROM vgjy6o15h95ug01f.Cryptocurrency WHERE id_user = {0} and pair_crypto = "{1}";""".format(user_id, name)
        self.GetCursor()
        self.cursor.execute(sql)
        self.db.commit()

    def SearchAuthor(self, Name):
        sql = """SELECT Name FROM vgjy6o15h95ug01f.author WHERE Name LIKE "%{0}%";""".format(Name)
        self.GetCursor()
        self.cursor.execute(sql)
        return self.cursor

    def GetAnswerSystem(self, chat_id):
        user_id = self.GetIdUser(chat_id)
        sql = "SELECT SystemOfAnswer FROM vgjy6o15h95ug01f.bot WHERE id_user = '%s'" % user_id
        self.GetCursor()
        self.cursor.execute(sql)
        return self.GetValue()

    def ChangeAnswerSystem(self, chat_id):
        user_id = self.GetIdUser(chat_id)
        value = self.GetAnswerSystem(chat_id)
        sql = "UPDATE vgjy6o15h95ug01f.bot SET SystemOfAnswer =(%s)WHERE id_user =%s;"
        v = (lambda x: False if x else True)(value)
        val = (v, user_id)
        self.GetCursor()
        self.cursor.execute(sql,val)
        self.db.commit()

    def AddBookInListRead(self, chat_id, NameBook):
        id_user = self.GetIdUser(chat_id)
        id_book = self.GetIdBook(NameBook)
        sql = "INSERT INTO vgjy6o15h95ug01f.list_read_book(id_user, id_book) VALUES({0},{1});".format(id_user, id_book)
        self.GetCursor()
        self.cursor.execute(sql)
        self.db.commit()

    def CheckUser(self, first_name, username, chat_id, language_code, type):
        sql = "SELECT count(*) FROM vgjy6o15h95ug01f.user WHERE chatID = '%s';" % chat_id
        self.GetCursor()
        self.cursor.execute(sql)
        for x in self.cursor:
            print(x[0])
            if int(x[0]) == 0:
                self.Insert(first_name, username, chat_id, language_code, type)

    def CheckTypeFile(self, Book):
        sql = """SELECT {0} FROM vgjy6o15h95ug01f.book WHERE Name = "{1}"; """.format(self._mafina.fileformat[Book.format], Book.Name)
        self.GetCursor()
        self.cursor.execute(sql)
        x = self.GetValue()
        print(x)
        return (lambda x: self.UpdateFileId(Book) if x == "" else False)(x)

    def CheckAuthor(self, Book):
        sql = """SELECT * FROM vgjy6o15h95ug01f.author WHERE Name = trim("{0}"); """ .format(Book.Author)
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
        sql = """SELECT chatID, status_sys_sweet_animal, animal_frequency FROM vgjy6o15h95ug01f.user u, vgjy6o15h95ug01f.job_queue j WHERE u.id_user = {0};""".format(id_user)
        self.GetCursor()
        self.cursor.execute(sql)
        self.db.commit()
        return self.cursor

    def CheckCrypto(self, id, name):
        sql = """SELECT count(*) FROM vgjy6o15h95ug01f.Cryptocurrency WHERE id_user = {0} AND pair_crypto = "{1}";""".format(id, name)
        self.GetCursor()
        self.cursor.execute(sql)
        return self.GetValue()

    def InsertAuthor(self, Book):
        sql = """INSERT INTO vgjy6o15h95ug01f.author(Name) VALUES(trim("{0}"));""".format(Book.Author)
        self.GetCursor()
        self.cursor.execute(sql)
        self.db.commit()

    def InsertBook(self, Book):
        format = self._mafina.fileformat[Book.format]
        sql = """INSERT INTO vgjy6o15h95ug01f.book(Name,{0}, id_author, book_lang) VALUES("{1}", "{2}", "{3}", "{4}");""".format(str(format), Book.Name, Book.file_id, Book.Author, Book.book_lang)
        self.cursor.execute(sql)
        self.db.commit()
        return True

    def Insert(self, first_name, username, chat_id, language_code, type):
        s = "INSERT INTO vgjy6o15h95ug01f.user(Name, Username, chatID, TypeChat) VALUES(%s, %s, %s, %s);"
        val = (first_name,  username, chat_id, type)
        self.cursor.execute(s, val)
        self.db.commit()
        id = self.GetIdUser(chat_id)
        s = "INSERT INTO vgjy6o15h95ug01f.bot(LanguageBot, id_user) VALUES(%s, %s);"
        val = (language_code, id)
        self.cursor.execute(s, val)
        self.db.commit()

    def InsertSysMeme(self, chat_id, status, interval):
        sql = "INSERT INTO vgjy6o15h95ug01f.job_queue(Span, status_sys_meme, id_user)VALUES(%s, %s, %s);"
        val = (interval, status, self.GetIdUser(chat_id))
        self.UpdateSys(sql, val)

    def InsertFile(self, fileID):
        sql = "INSERT INTO vgjy6o15h95ug01f.file(TelegramFileID)VALUES('%s');"%fileID
        self.GetCursor()
        self.cursor.execute(sql)
        self.db.commit()

    def InsertNewAnswer(self, text, chat_id):
        id = self.GetIdUser(chat_id)
        sql = """INSERT INTO vgjy6o15h95ug01f.answers(text_answer, id_user) VALUES("{0}", {1});""".format(text, id)
        self.GetCursor()
        self.cursor.execute(sql)
        self.db.commit()

    def InsertCrypto(self, name, chat_id, price):
        id = self.GetIdUser(chat_id)
        if (self.CheckCrypto(id, name)==0):
            sql = """INSERT INTO vgjy6o15h95ug01f.Cryptocurrency(pair_crypto, id_user, price) VALUES("{0}", {1}, {2});""".format(name, id, price)
            print(sql)
            self.GetCursor()
            self.cursor.execute(sql)
            self.db.commit()
        else:
            return 1

    def InsertSysWeather(self, chat_id, status):
        sql = "INSERT INTO vgjy6o15h95ug01f.job_queue(status_sys_weather, id_user)VALUES(%s, %s);"
        val = (status, self.GetIdUser(chat_id))
        self.UpdateSys(sql, val)

    def InsertSysAnimal(self, chat_id, status):
        sql = "INSERT INTO vgjy6o15h95ug01f.job_queue(status_sys_sweet_animal, id_user)VALUES(%s, %s);"
        val = (status, self.GetIdUser(chat_id))
        self.UpdateSys(sql, val)

    def UpdateFileId(self, Book):
        sql = """UPDATE vgjy6o15h95ug01f.book SET {0} =("{1}")WHERE id_book ="{2}";""".format(str(self._mafina.fileformat[Book.format]),str(Book.file_id), str(self.GetIdBook(Book.Name)))
        self.GetCursor()
        self.cursor.execute(sql)
        self.db.commit()
        return True

    def UpdateSysWeather(self, chat_id, status):
        sql = "UPDATE vgjy6o15h95ug01f.job_queue SET status_sys_weather=%s WHERE id_user =%s;"
        val = (status, self.GetIdUser(chat_id))
        self.UpdateSys(sql, val)

    def UpdateSysMeme(self, chat_id, status, interval):
        sql = "UPDATE vgjy6o15h95ug01f.job_queue SET Span =%s, status_sys_meme=%s WHERE id_user =%s;"
        val = (interval, status, self.GetIdUser(chat_id))
        self.UpdateSys(sql,val)

    def UpdateSysAnimal(self, chat_id, status):
        sql = "UPDATE vgjy6o15h95ug01f.job_queue SET status_sys_sweet_animal=%s WHERE id_user =%s;"
        val = (status, self.GetIdUser(chat_id))
        self.UpdateSys(sql, val)

    def UpdateListing(self, chat_id, NewListing):
        sql = "UPDATE vgjy6o15h95ug01f.user SET Username=%s WHERE chatID =%s;"
        val = (NewListing, chat_id)
        self.UpdateSys(sql, val)

    def UpdateSys(self, sql, val):
        self.GetCursor()
        self.cursor.execute(sql,val)
        self.db.commit()

    def UsersSysMeme(self):
        sql="SELECT chatID, j.Span, j.status_sys_meme FROM vgjy6o15h95ug01f.user u, vgjy6o15h95ug01f.job_queue j WHERE u.id_user = j.id_user;"
        self.GetCursor()
        self.cursor.execute(sql)
        self.db.commit()
        return self.cursor

    def UsersSysAnimal(self):
        sql="SELECT chatID, j.status_sys_sweet_animal, animal_frequency FROM vgjy6o15h95ug01f.user u, vgjy6o15h95ug01f.job_queue j WHERE u.id_user = j.id_user and j.status_sys_sweet_animal = 1;"
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
        sql="SELECT chatID, j.status_sys_weather FROM vgjy6o15h95ug01f.user u, vgjy6o15h95ug01f.job_queue j WHERE u.id_user = j.id_user;"
        self.GetCursor()
        self.cursor.execute(sql)
        self.db.commit()
        return self.cursor

    def UpdateCryptoPair(self, chat_id, binance):
        id_user = self.GetIdUser(chat_id)
        sql = """UPDATE Cryptocurrency SET price =({0}) WHERE id_user = {1} AND pair_crypto = "{2}";""".format(binance['price'], id_user, binance['symbol'])
        self.GetCursor()
        self.cursor.execute(sql)
        self.db.commit()
        return self.cursor

    def UpCountAnimal(self, chat_id):
        x = self.GetCountAnimal(chat_id)
        print(x)
        x+=1
        sql = "UPDATE vgjy6o15h95ug01f.job_queue SET count_animal=%s WHERE id_user =%s;"
        val =(x, self.GetIdUser(chat_id))
        self.UpdateSys(sql, val)

    def VerificationLanguage(self, chat_id,preferred_language, Translatelanguage = True):
        self.GetCursor()
        id = self.GetIdUser(chat_id)
        if Translatelanguage:
            sql = "UPDATE vgjy6o15h95ug01f.bot SET TranslateLanguage = %s WHERE id_user =%s;"
        else:
            sql = "UPDATE vgjy6o15h95ug01f.bot SET LanguageBot = %s WHERE id_user =%s;"
        val =(preferred_language, id)
        self.cursor.execute(sql, val)
        self.db.commit()
