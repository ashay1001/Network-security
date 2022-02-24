import sqlite3 as lite

def sqlDemo():
    dbname = 'Demo1.db'
    conn = lite.connect(dbname)
    cursor = conn.cursor()
    tablename = 'features'
    stmt = 'Create table if not exists ' + tablename + '( GroupId integer, sumPktLen integer, mnPktLen float, sdPktLen float)'
    cursor.execute(stmt)
    conn.commit()
    


if __name__ == "__main__":
    sqlDemo()