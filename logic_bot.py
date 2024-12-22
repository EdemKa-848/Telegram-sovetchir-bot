import sqlite3
from config import DATABASE

class DB_Manager:
    def __init__(self, database):
        self.database = database

    def create_tables(self):
        conn = sqlite3.connect(self.database)
        try:
            with conn:
                conn.execute('''
                    CREATE TABLE IF NOT EXISTS users (
                        user_id INTEGER PRIMARY KEY,
                        interests TEXT,
                        skills TEXT,
                        education TEXT,
                        current_job TEXT
                    )
                ''')
        except sqlite3.Error as e:
            print(f"Ошибка создания таблиц: {e}")
            return False # Сигнализируем об ошибке
        return True # Успешное создание


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


    def delete_interest(self, user_id): # Удаление части строки
        sql = "UPDATE users SET interests = REPLACE(interests, ?, '') WHERE user_id = ?"
        return self.execute(sql, (user_id))


    def delete_skill(self, user_id):
        sql = "UPDATE users SET skills = REPLACE(skills, ?, '') WHERE user_id = ?"
        return self.execute(sql, (user_id))


    def delete_education(self, user_id):
        sql = "UPDATE users SET education = REPLACE(education, ?, '') WHERE user_id = ?"
        return self.execute(sql, (user_id))


    def delete_current_job(self, user_id):
        sql = "UPDATE users SET current_job = REPLACE(current_job, ?, '') WHERE user_id = ?"
        return self.execute(sql, (user_id))



    def view_interests(self, user_id=None):
        sql = "SELECT interests FROM users"
        if user_id:
            sql += " WHERE user_id = ?"
            result = self.__select_data(sql, (user_id,))
            return result[0][0] if result else None
        else:
            return self.__select_data(sql)


    def view_skills(self, user_id):
        sql = "SELECT skills FROM users WHERE user_id = ?"
        result = self.__select_data(sql, (user_id,))
        return result[0][0] if result else None


    def view_education(self, user_id):
        sql = "SELECT education FROM users WHERE user_id = ?"
        result = self.__select_data(sql, (user_id,))
        return result[0][0] if result else None


    def view_current_job(self, user_id):
        sql = "SELECT current_job FROM users WHERE user_id = ?"
        result = self.__select_data(sql, (user_id,))
        return result[0][0] if result else None


if __name__ == "__main__":
    manager = DB_Manager(DATABASE)

