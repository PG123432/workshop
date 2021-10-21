#Team Atom - Patrick Ging Qina Liu Joshua Kleopfar
#SoftDev  
#skeleton/stub :: SQLITE3 BASICS
#Oct 21 2021

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events




#command = "CREATE TABLE roster(name TEXT, age INTEGER, id INTEGER);"          # test SQL stmt in sqlite3 shell, save as string
#command = "CREATE TABLE classes ( name TEXT, mark INTEGER, id INTEGER);"


'''
Roster - meant to have student names, age of student, and id
	name : TEXT
	age  : INTEGER
	id   : INTEGER

Classes - meant to have course names, course mark, and id
	name : TEXT
	mark : INTEGER
	id   : INTEGER
'''





c.execute(command)    # run SQL statement



db.commit() #save changes
db.close()  #close database
