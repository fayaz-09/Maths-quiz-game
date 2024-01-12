import sqlite3
new_db = sqlite3.connect('QuizDB.db')

c=new_db.cursor()

c.execute("SELECT * FROM User")
row = c.fetchall()
print(row)

c.execute("SELECT * FROM Topics")
row = c.fetchall()
print(row)

c.execute("SELECT * FROM QuestionType")
row = c.fetchall()
print(row)

c.execute("SELECT * FROM Questions")
row = c.fetchall()
print(row)

c.execute("SELECT * FROM Score")
row = c.fetchall()
print(row)

c.execute("SELECT * FROM Topicfeedback")
row = c.fetchall()
print(row)

new_db.close()
