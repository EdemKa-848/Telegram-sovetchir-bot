import sqlite3
from config import DATABASE

class DB_Manager:
    def __init__(self, database):
        self.database = database

    def create_tables(self):
        conn = sqlite3.connect(self.database)
        with conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    interests TEXT,
                    skills TEXT,
                    education TEXT,
                    current_job TEXT)
            ''')



    def execute(self, sql, data=()):
        conn = sqlite3.connect(self.database)
        try:
            with conn:
                conn.execute(sql, data)
                conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Ошибка выполнения SQL: {e}")
            return False


    def __select_data(self, sql, data=()):
        conn = sqlite3.connect(self.database)
        try:
            with conn:
                cur = conn.cursor()
                cur.execute(sql, data)
                return cur.fetchall()
        except sqlite3.Error as e:
            print(f"Ошибка выборки данных: {e}")
            return None


    def insert_interests(self, user_id):
        sql = "INSERT INTO users (interests) values(?)"
        self.execute(sql, user_id)


    def insert_skills(self, user_id):
        sql = "INSERT INTO users (skills) values(?)"
        self.execute(sql, user_id)


    def insert_education(self, user_id):
        sql = "INSERT INTO users (education) values(?)"
        self.execute(sql, user_id)


    def insert_job(self, user_id):
        sql = "INSERT INTO users (current_job) values(?)"
        self.execute(sql, user_id)


    def delete_interest(self, user_id):
        sql = "DELETE FROM users WHERE interests = ?"
        self.execute(sql, (user_id,))
    

    def delete_skill(self, user_id):
        sql = "DELETE FROM users WHERE user_id = ?"
        self.execute(sql, (user_id,))
    

    def delete_education(self):
        sql = "DELETE FROM users"
        self.execute(sql)
    

    def delete_current_job(self):
        sql = "DELETE FROM users"
        self.execute(sql)


    def view_interests(self, user_id):
        sql = "SELECT interests FROM users WHERE user_id = ?"
        return self.__select_data(sql, (user_id,))


    def view_skills(self, user_id):
        sql = "SELECT skills FROM users WHERE user_id = ?"
        self.__select_data(sql, (user_id,))


    def view_education(self, user_id):
        sql = "SELECT education FROM users WHERE user_id = ?"
        self.__select_data(sql, (user_id,))


    def view_current_job(self, user_id):
        sql = "SELECT current_job FROM users WHERE user_id = ?"
        self.__select_data(sql, (user_id,))



if __name__ == "__main__":
    manager = DB_Manager(DATABASE)

