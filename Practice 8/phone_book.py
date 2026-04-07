# phonebook.py
from connect import connect

conn = connect()
cursor = conn.cursor()

TABLE = "phonebook"

cursor.execute(f'''
CREATE TABLE IF NOT EXISTS {TABLE}(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    phone VARCHAR(20) UNIQUE NOT NULL
)
''')
conn.commit()

def search_records(pattern):
    cursor.callproc('search_by_pattern', [pattern])
    return cursor.fetchall()

print("Search results:", search_records('Ben'))

def insert_or_update_user(name, phone):
    cursor.execute('CALL insert_or_update(%s, %s)', (name, phone))
    conn.commit()

insert_or_update_user('Alice', '+777123456')

def insert_many_users(users_list):
    users_array = [list(user) for user in users_list]
    cursor.execute('CALL insert_many(%s)', (users_array, ))
    conn.commit()

users = [('John', '+777111222'), ('Charlie', '+7777333444')]
insert_many_users(users)

def get_paginated(page_num, page_size):
    cursor.callproc('get_paginated', [page_num, page_size])
    return cursor.fetchall()

print("Page 1:", get_paginated(1, 5))

def delete_record(identifier, delete_type='name'):
    cursor.execute('CALL delete_by(%s, %s)', (identifier, delete_type))
    conn.commit()


delete_record('777111222', 'phone')

cursor.close()
conn.close()