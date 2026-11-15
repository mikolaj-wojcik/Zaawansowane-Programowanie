

from time import sleep
import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect("ZP.db")
    c = conn.cursor()
    c.execute('''
            create table if not exists queue (id integer primary key,
            status text)
    ''')

    while(True):
        sleep(1)
        c.execute('''Insert into queue (status) values ('pending') ''')
        conn.commit()