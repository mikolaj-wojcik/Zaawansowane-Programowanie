from time import sleep
import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect("ZP.db")
    c = conn.cursor()
    c.execute('''
            create table if not exists queue (id integer primary key,
            status text)
    ''')

    while (True):

        result = c.execute('''select id, status from queue where status = 'pending' order by id asc''')
        res = result.fetchone()
        res = (res[0], 'in_progress')
        c.execute(f'''update queue set status = '{res[1]}'  where id = {res[0]}''')
        conn.commit()
        sleep(30)
        res = (res[0], 'done')
        c.execute(f'''update queue set status = '{res[1]}'  where id = {res[0]}''')
        conn.commit()
