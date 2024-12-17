import sqlite3
from config import DATABASE


class DB_Manager:
    def __init__(self, DATABASE):
        self.database = DATABASE
        

    def create_tables(self):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.execute('CREATE TABLE users(user_id INTEGER,interests TEXT, skills TEXT,education TEXT,current_job TEXT)')
            conn.execute('CREATE TABLE careers (career_id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT UNIQUE,description TEXT,required_skills TEXT, education_level TEXT,average_salary REAL, job_outlook TEXT,pros TEXT,cons TEXT,related_careers TEXT)')
            conn.commit()


    def __execute(self, sql, data):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.execute(sql, data)
            conn.commit()


    def __select_data(self, sql, data = tuple()):
        conn = sqlite3.connect(self.database)
        with conn:
            cur = conn.cursor()
            cur.execute(sql, data)
            return cur.fetchall()
        
    
    def __select_data(self, sql, data = tuple()):
        conn = sqlite3.connect(self.database)
        with conn:
            cur = conn.cursor()
            cur.execute(sql, data)
            return cur.fetchall()
        

    def insert_skills(self, data):
        sql = "INSERT INTO users (skills) values(?)"
        self.__execute(sql, data)
    def del_skills(self, data):
        sql = "TRUNCATE users (skills)"
        self.__execute(sql, data)


    def insert_obr(self, data):
        sql = "INSERT INTO users (education) values(?)"
        self.__execute(sql, data)


    def insert_interesti(self, data):
        sql = "INSERT INTO users (interests) values(?)"
        self.__execute(sql, data)


    def viev_int(self, data):
        sql="SELECT interests from users"
        return self.__select_data(sql, data)

if __name__ == '__main__':
    manager = DB_Manager(DATABASE)



