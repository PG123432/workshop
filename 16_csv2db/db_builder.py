#Team Atom - Patrick Ging Qina Liu Joshua Kleopfar
#SoftDev
#skeleton/stub :: SQLITE3 BASICS
#Oct 21 2021

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events




c.execute("CREATE TABLE IF NOT EXISTS roster(name TEXT, age INTEGER, id INTEGER, UNIQUE(id));")          # test SQL stmt in sqlite3 shell, save as string
c.execute("CREATE TABLE IF NOT EXISTS classes ( name TEXT, mark INTEGER, id INTEGER, UNIQUE(name, mark, id));")


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
try:
	with open('students.csv', newline='') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			c.execute("INSERT INTO roster (name, age, id) VALUES (?, ?, ?);", (row['name'], row['age'], row['id']))
	with open('courses.csv', newline='') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			c.execute("INSERT INTO classes (name, mark, id) VALUES (?, ?, ?);", (row['code'], row['mark'], row['id']))
except sqlite3.IntegrityError:
	print("You have tried to enter a duplicate")

c.execute("SELECT * FROM roster")

print(c.fetchall())

c.execute("SELECT * FROM classes")

print(c.fetchall())

db.commit() #save changes
db.close()  #close database
