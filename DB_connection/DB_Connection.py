import psycopg2

class DB:
    
    def db_connect(self):
        con = psycopg2.connect(
            host = "localhost",
            user = "postgres",
            database = "E_commerce",
            password = "Meher@900"
        )
        return con

    def select_items(self):
        my_database = DB.db_connect(self)
        cur = my_database.cursor()
        cur.execute("SELECT item FROM master")
        rows = cur.fetchall()
        return rows.sort()
        
if __name__ == "__main__":
    e_commerce_DB = DB()
    print(e_commerce_DB.select_items())