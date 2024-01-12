import sqlite3

new_db = sqlite3.connect('QuizDB.db')

c=new_db.cursor()

c.executescript('''
INSERT INTO Topics(Topic)
VALUES ('addition');
INSERT INTO Topics(Topic)
VALUES ('subtraction');
INSERT INTO Topics(Topic)
VALUES ('multiplication');
''')

c.executescript('''
INSERT INTO QuestionType(Type)
VALUES ('Multiple Choice');
INSERT INTO QuestionType(Type)
VALUES ('Long Answer');
''')

c.executescript('''
INSERT INTO Comments(percent, comment)
VALUES (90, 'You have a very high percentage of correct answers in this topic either move onto harder questions from exam papers or try another topic');
INSERT INTO comments(percent, comment)
VALUES (70, 'You have an average percentage of correct answers in this topic either practice more questions on this topic or move onto harder questions from exam papers');
INSERT INTO comments(percent, comment)
VALUES (50, 'You have a low percentage of correct answers in this topic so practicing questions on this topic is advised');
INSERT INTO comments(percent, comment)
VALUES (49, 'You have a very low percentage of correct answers in this topic so it is advised that you go over this topic and make sure you understand it before attempting more questions');
''')

c.executescript('''
INSERT INTO Questions(TopicID, QTID, Question, Answer, IncorrectAnswer1, IncorrectAnswer2,  IncorrectAnswer3, Scorereward)
VALUES (1,1,'What is 1+1?',2,4,3,5,10);
INSERT INTO Questions(TopicID, QTID, Question, Answer, IncorrectAnswer1, IncorrectAnswer2,  IncorrectAnswer3, Scorereward)
VALUES (1,1,'What is 2+1?',3,4,2,5,15);
INSERT INTO Questions(TopicID, QTID, Question, Answer, IncorrectAnswer1, IncorrectAnswer2,  IncorrectAnswer3, Scorereward)
VALUES (1,1,'What is 4+1?',5,4,3,2,10);
INSERT INTO Questions(TopicID, QTID, Question, Answer, IncorrectAnswer1, IncorrectAnswer2,  IncorrectAnswer3, Scorereward)
VALUES (1,1,'What is 2+2?',4,2,3,5,10);
INSERT INTO Questions(TopicID, QTID, Question, Answer, IncorrectAnswer1, IncorrectAnswer2,  IncorrectAnswer3, Scorereward)
VALUES (1,2,'What is 10+10?',20,' ',' ',' ',20);
INSERT INTO Questions(TopicID, QTID, Question, Answer, IncorrectAnswer1, IncorrectAnswer2,  IncorrectAnswer3, Scorereward)
VALUES (1,2,'What is 10+20?',30,' ',' ',' ',25);
INSERT INTO Questions(TopicID, QTID, Question, Answer, IncorrectAnswer1, IncorrectAnswer2,  IncorrectAnswer3, Scorereward)
VALUES (2,1,'What is 2-1?',1,4,3,5,10);
INSERT INTO Questions(TopicID, QTID, Question, Answer, IncorrectAnswer1, IncorrectAnswer2,  IncorrectAnswer3, Scorereward)
VALUES (2,1,'What is 3-1?',2,1,3,5,5);
INSERT INTO Questions(TopicID, QTID, Question, Answer, IncorrectAnswer1, IncorrectAnswer2,  IncorrectAnswer3, Scorereward)
VALUES (2,1,'What is 10-6?',4,2,3,5,10);
INSERT INTO Questions(TopicID, QTID, Question, Answer, IncorrectAnswer1, IncorrectAnswer2,  IncorrectAnswer3, Scorereward)
VALUES (2,2,'What is 20-1?',19,' ',' ',' ',15);
INSERT INTO Questions(TopicID, QTID, Question, Answer, IncorrectAnswer1, IncorrectAnswer2,  IncorrectAnswer3, Scorereward)
VALUES (2,2,'What is 20-10?',10,' ',' ',' ',20);
INSERT INTO Questions(TopicID, QTID, Question, Answer, IncorrectAnswer1, IncorrectAnswer2,  IncorrectAnswer3, Scorereward)
VALUES (3,1,'What is 1x2?',2,4,3,5,10);
INSERT INTO Questions(TopicID, QTID, Question, Answer, IncorrectAnswer1, IncorrectAnswer2,  IncorrectAnswer3, Scorereward)
VALUES (3,1,'What is 2x3?',6,4,3,5,10);
INSERT INTO Questions(TopicID, QTID, Question, Answer, IncorrectAnswer1, IncorrectAnswer2,  IncorrectAnswer3, Scorereward)
VALUES (3,1,'What is 2x2?',4,6,3,5,10);
INSERT INTO Questions(TopicID, QTID, Question, Answer, IncorrectAnswer1, IncorrectAnswer2,  IncorrectAnswer3, Scorereward)
VALUES (3,2,'What is 5x5?',25,' ',' ',' ',15);
INSERT INTO Questions(TopicID, QTID, Question, Answer, IncorrectAnswer1, IncorrectAnswer2,  IncorrectAnswer3, Scorereward)
VALUES (3,2,'What is 10x2?',20,' ',' ',' ',20);
''')

new_db.commit()
new_db.close()
