# core package
import sqlite3
import os

# locate database files using relative paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "..", "database", "data.db")

# set connect the datbase
conn = sqlite3.connect(db_path, check_same_thread=False)
c = conn.cursor()



# make a creating food table function
def create_food_table():
    c.execute('CREATE TABLE IF NOT EXISTS food(food_type TEXT, amount INTEGER, company TEXT)')

# make a creating beverage table function
def create_beverage_table():
    c.execute('CREATE TABLE IF NOT EXISTS beverage(beverage_type TEXT, amount INTEGER, method TEXT, company TEXT)')



# make an adding data to the food table function
def add_food_data(food_type, food_amount, company):
    c.execute('INSERT INTO food(food_type, amount, company) VALUES (?,?,?)', (food_type, food_amount, company))
    conn.commit()

# make an adding data to the beverage table function
def add_beverage_data(beverage_type, beverage_amount, method, company):
    c.execute('INSERT INTO beverage(beverage_type, amount, method, company) VALUES (?,?,?,?)', (beverage_type, beverage_amount, method, company))
    conn.commit()
    
    
 
 
 
 
 