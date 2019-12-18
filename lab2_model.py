import psycopg2
import random, string
import datetime 
                
        
def connect_db():
    try:
        res = psycopg2.connect(host="localhost", port="5432", 
                                database="Online_book_store", user="postgres", 
                                password='qwerty')
    except (Exception, psycopg2.Error) as error:
        res = False
        print(error)
    return res 

    
def select(table, fields = "*", where = ""):
    conn = connect_db()
    if not conn: return False
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT " + fields + " FROM " + table + ' ' + where)
        res = cursor.fetchall()
    except (Exception, psycopg2.Error) as error:
        res = False
        print(error)
    conn.commit()
    cursor.close()
    conn.close()
    return res
    
    
def insert(table, fields = "", values = ""):
    conn = connect_db()
    if not conn: return False
    cursor = conn.cursor()
    if type(values) is list:
        values = ["'{0}'".format(x) for x in values]
        values = ', '.join(values)
    if type(fields) is list:
        fields = ', '.join(fields)
    try:
        cursor.execute("INSERT INTO " + table + '(' + fields + ')' +
                             " VALUES " + '(' + values + ')')
        res = True
    except (Exception, psycopg2.Error) as error:
        res = False
        print(error)
    conn.commit()
    cursor.close()
    conn.close()
    return res
    
    
def delete(table, where = ""):
    conn = connect_db()
    if not conn: return False
    cursor = conn.cursor()
    if type(where) is list:
        where[1] = "'" + where[1] + "'"
        where = " = ".join(where)
    try:
        cursor.execute("DELETE FROM " + table + ' WHERE ' +  where)
        res = True
    except (Exception, psycopg2.Error) as error:
        res = False
        print(error)
    conn.commit()
    cursor.close()
    conn.close()
    return res
    
    
def update(table, set = "", where = ""):
    conn = connect_db()
    if not conn: return False
    cursor = conn.cursor()
    if type(where) is list:
        where[1] = "'" + where[1] + "'"
        where = " = ".join(where)
        set[1] = "'" + set[1] + "'"
        set = " = ".join(set)
    try:
        cursor.execute("UPDATE " + table + ' SET ' + set + ' WHERE ' +  where)
        res = True
    except (Exception, psycopg2.Error) as error:
        res = False
        print(error)
    conn.commit()
    cursor.close()
    conn.close()
    return res

    
def random_author(num):
    conn = connect_db()
    if not conn: return False
    cursor = conn.cursor()
    try:
        cursor.execute("insert into author (author_pen_name, born, died) select * FROM rand_author({})".format(num))
        res = True
    except (Exception, psycopg2.Error) as error:
        res = False
        print(error)
    conn.commit()
    cursor.close()
    conn.close()
    return res

    
def full_text_search(table, where, mode):
    conn = connect_db()
    if not conn: return False
    cursor = conn.cursor()
    try:
        if mode == '1':
            cursor.execute("select * from {} where {}".format(table, where))
            res = cursor.fetchall()
        elif mode == '2':
            cursor.execute("select * from {} where not ({})".format(table, where))
            res = cursor.fetchall()
    except (Exception, psycopg2.Error) as error:
        res = None
        print(error)
    conn.commit()
    cursor.close()
    conn.close()
    return res

