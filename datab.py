import sqlite3

conn = sqlite3.connect('tasks.bd')
cur=conn.cursor()

def init(): 
    cur.execute("""CREATE TABLE IF NOT EXISTS TASKS(
        task TEXT);""")
    conn.commit()

def addToDb(task):
    init()
    cur.execute("""INSERT INTO tasks (task) VALUES (?)""", (task,))  
    conn.commit()

def deleteTask(task):
    init()
    cur.execute("""DELETE FROM tasks WHERE task=(?)""", (task,))  
    conn.commit()

def updateTask(taskOld, task):
    init()
    cur.execute("""UPDATE tasks SET task=(?) WHERE task=(?)""", (task, taskOld))  
    conn.commit()

def getFromDB():
    cur.execute("SELECT task FROM tasks")
    tasks = cur.fetchall()
    list=[]
    for row in tasks:
        list.append(row[0])
    return list

