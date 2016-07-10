import sqlite3 as lite

def get_charset(database):
    '''Given the database filepath will return a Cursor interator that contains
    a tuple of (url_id, charset).'''

    sql = "SELECT url_id, charset from output"
    con    = lite.connect(database)
    cursor = con.cursor()
    result = cursor.execute(sql)

    return result
