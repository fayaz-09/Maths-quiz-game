import sqlite3
new_db = sqlite3.connect('QuizDB.db')

c=new_db.cursor()

c.executescript('''
CREATE TABLE User
(UserID INTEGER PRIMARY KEY AUTOINCREMENT,
Username varchar(40) NOT NULL,
Password varchar(40) NOT NULL,
DOB varchar(10) NOT NULL,
Firstname varchar(40) NOT NULL,
Surname varchar(40) NOT NULL);
''')

c.executescript('''
CREATE TABLE Topics
(TopicID INTEGER PRIMARY KEY AUTOINCREMENT,
Topic varchar(40) NOT NULL);
''')

c.executescript('''
CREATE TABLE QuestionType
(QTID INTEGER PRIMARY KEY AUTOINCREMENT,
Type varchar(30) NOT NULL);
''')

c.executescript('''
CREATE TABLE Questions
(QuestionID INTEGER PRIMARY KEY AUTOINCREMENT,
TopicID int NOT NULL,
QTID int NOT NULL,
Question varchar(400) NOT NULL,
Answer varchar(400) NOT NULL,
IncorrectAnswer1 varchar(400),
IncorrectAnswer2 varchar(400),
IncorrectAnswer3 varchar(400),
Scorereward int NOT NULL,
FOREIGN KEY(TopicID)REFERENCES Topics(TopicID),
FOREIGN KEY(QTID)REFERENCES QuestionType(QTID));
''')

c.executescript('''
CREATE TABLE Comments
(commentID INTEGER PRIMARY KEY AUTOINCREMENT,
percent int NOT NULL,
comment varchar(300) NOT NULL);
''')

c.executescript('''
CREATE TABLE Topicfeedback
(FeedbackID INTEGER PRIMARY KEY AUTOINCREMENT,
TopicID int NOT NULL,
UserID int NOT NULL,
Numanswered int NOT NULL,
PercentageCorrect int NOT NULL,
commentID int NOT NULL,
FOREIGN KEY(UserID)REFERENCES User(UserID),
FOREIGN KEY(commentID)REFERENCES Comments(commentID),
FOREIGN KEY(TopicID)REFERENCES Topics(TopicID));
''')

c.executescript('''
CREATE TABLE Score
(ScoreID INTEGER PRIMARY KEY AUTOINCREMENT,
UserID int NOT NULL,
dateofattempt int NOT NULL,
Score int NOT NULL,
topiccovered varchar(60) NOT NULL,
FOREIGN KEY(UserID)REFERENCES User(UserID));
''')
new_db.commit()
new_db.close()
