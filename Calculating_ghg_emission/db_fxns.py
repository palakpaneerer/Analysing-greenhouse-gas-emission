# core package
import sqlite3
import os

# locate database files using relative paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "..", "database", "data.db")

# set connect the datbase
conn = sqlite3.connect(db_path, check_same_thread=False)
c = conn.cursor()



# make a creating a new table function 
def create_event_table():
    c.execute('''
            CREATE TABLE IF NOT EXISTS event (
                name TEXT,
                address TEXT,
                start_day DATE,
                end_day DATE,
                indoor BOOLEAN,
                outdoor BOOLEAN,
                online BOOLEAN,
                main_category TEXT,
                sub_category TEXT
            )
        ''')
    
# make a creating food table function
def create_food_table():
    c.execute('CREATE TABLE IF NOT EXISTS food(food_type TEXT, amount INTEGER, company TEXT)')

# make a creating beverage table function
def create_beverage_table():
    c.execute('CREATE TABLE IF NOT EXISTS beverage(beverage_type TEXT, amount INTEGER, method TEXT, company TEXT)')





# make a viewing event table function
def view_event():
    c.execute('SELECT * FROM event')
    data = c.fetchall()
    return data

# make a viewing food table function
def view_food():
    c.execute('SELECT * FROM food')
    data = c.fetchall()
    return data

# make a viewing beverage table function
def view_beverage():
    c.execute('SELECT * FROM beverage')
    data = c.fetchall()
    return data



