import csv
import psycopg2
from connect import connect
from config import config

conn = connect()
cursor = conn.cursor()
TABLE = "phonebook"
# TASK 1. CREATING TABLE phonebook
cursor.execute('''
CREATE TABLE IF NOT EXISTS phonebook(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) UNIQUE NOT NULL
)
''')
conn.commit()
# TASK 2. READING CSV:
def reading_csv():
    try:
        with open("Practice 7/contacts.csv", 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if (not row or len(row) < 2):
                    print("Skipping:", row)
                    continue
                name = row[0].strip()
                phone = row[1].strip()
                try:
                    query = f"INSERT INTO {TABLE} (name, phone) VALUES (%s, %s)"
                    cursor.execute(query, (name, phone))
                except psycopg2.errors.UniqueViolation:
                    conn.rollback()
                    print("Duplicate phone", phone)
        conn.commit()

    finally:
        cursor.close()
        conn.close()

#TASK 3. READING FROM CONSOLE
def reading_from_console():
    name = input()
    phone = input()
    try:
        query = f"INSERT INTO {TABLE} (name, phone) VALUES (%s, %s)"
        cursor.execute(query, (name, phone))
    except psycopg2.errors.UniqueViolation:
        conn.rollback()
        print("Duplicate phone:", phone)
    conn.commit()
    cursor.close()
    conn.close()


#TASK 4. UPDATING ROWS

def update_rows(name = None, phone = None):
    try:
        if name and phone:
            try:
                query = f"UPDATE {TABLE} SET phone = %s where name  = %s"
                cursor.execute(query, (phone, name))
            except psycopg2.errors.UniqueViolation:
                conn.rollback()
                print("Duplicate phone:", phone)
        else:
            print("Invalid input")
            return
    except psycopg2.Error as e:
        print("Error:", e)
    conn.commit()
    cursor.close()
    conn.close()

# TASK 5. FILTERING AND FETCHING

def filtering(name = None, phone_preffix = None):
    try:
        query = f"SELECT * FROM {TABLE} WHERE 1=1"
        params = []

        if name:
            query += " AND name ILIKE %s"
            params.append(f"%{name}%")
        if phone_preffix:
            query += " AND phone like %s"
            params.append(f"%{phone_preffix}%")
        
        cursor.execute(query, params)
        res = cursor.fetchall()
        if res:
            for row in res:
                print(row)
        else:
            print("No contacts found")
    except psycopg2.Error as e:
        print("Error:", e)

# filtering(name="Bob")
# filtering(phone_preffix="+7708")

# TASK 6 DELETING ROWS

def deleting(name = None, phone = None):
    try:
        if name:
            query = f"DELETE FROM {TABLE} WHERE name = %s"
            cursor.execute(query, (name,))
        elif phone:
            query = f"DELETE FROM {TABLE} WHERE phone = %s"
            cursor.execute(query, (phone,))
        else:
            print("Invalid input")
            return
        conn.commit()
        if cursor.rowcount > 0:
            print("Contact deleted successfully")
        else:
            print("No contact found")
        cursor.close()
    except psycopg2.Error as e:
        print("Error:", e)
        conn.rollback()

# deleting("Jhon")