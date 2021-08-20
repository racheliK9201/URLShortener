import sqlite3

#class db creates define a database that contains one table with 4 columns:
# id, long_url, short_url, name
#all col are unique
class db:
    # create database and tables if not exists, and create a connection

    def __init__(self):
        self.connect()
        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS urls
        (long_url VARCHAR UNIQUE,
         short_url VARCHAR UNIQUE,
         name VARCHAR UNIQUE)
        ''')
        print("cur",self.cur)

    # get short URL, look for it in the database,
    # and return match long URL if exists, or None if not.
    def find_short_url(self,url):
        self.cur.execute('''
        SELECT long_url FROM urls WHERE short_url=?
        ''', (url,))
        result = self.cur.fetchone()
        if type(result) == tuple:
            return result[0]
        return result

    # get long URL, look for it in the database,
    # and return match short URL if exists, or None if not.
    def find_long_url(self, url):
        self.cur.execute('''
        SELECT short_url FROM urls WHERE long_url=?
        ''', (url,))
        result = self.cur.fetchone()
        if type(result) == tuple:
            return result[0]
        return result

    # insert to table a new short URL and map it to the match long URL
    def insert_new_mapping(self, long_url, short_url, name):
        self.cur.execute('''
        INSERT INTO urls (long_url,short_url,name)
        VALUES(?,?,?)
        ''', (long_url, short_url, name))
        self.con.commit()
        print("inserted", long_url, ",", short_url, name)

    # return a list with all values of database
    def select_all(self):
        self.cur.execute('''
        SELECT * FROM urls
        ''')
        # self.con.commit()
        return self.cur.fetchall()

    # create a connection to database
    def connect(self):
        self.con = sqlite3.connect("UrlShortener.db", check_same_thread=False)
        self.cur = self.con.cursor()

    # close the connection to database
    def close(self):
        self.con.commit()
        self.con.close()

    # clear the database
    def delete_all(self):
        self.cur.execute('''
           DELETE FROM urls
           ''')
        self.con.commit()

    # get a short URL and delete it's row from the table.
    def delete_one(self, name):
        self.cur.execute('DELETE  FROM urls where short_url= ? ', (name,))
        self.con.commit()






