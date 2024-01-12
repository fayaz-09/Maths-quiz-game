import tkinter
import sqlite3
import random
import time

randlist = []
answerlist = []
userid = []
scorelist = []
correctanswers = []
class Play():
    def __init__(self, parent):
        top = self.top = tkinter.Toplevel(parent)
        self.currentscore = 0
        self.qnum = 0
        self.questionbox = tkinter.Label(top, width=30, height=2, background = 'red')
        self.questionbox.grid(row=2, column=4, columnspan=4)
        self.questionnum = tkinter.Label(top, width=30, height=2, background = 'red',text=' ')
        self.questionnum.grid(row=1, column=4,columnspan=4)
        self.hider = tkinter.Label(top, width=30, height=6, background = 'red')
        self.hider.grid(row=3, column=4, columnspan=4, rowspan=2)
        self.choice = tkinter.OptionMenu(top, var, 'all topics','addition','subtraction','multiplication')
        self.choice.grid(row=1, column=0, columnspan=2)
        self.info = tkinter.Label(top, text='select the topic you would like the quiz to cover')
        self.info.grid(row=0, column=0, columnspan=2)
        self.start = tkinter.Button(top, text='start',command=self.Startquiz)
        self.start.grid(row=2, column=0, columnspan=2)
        self.answer1 = tkinter.Button(top, width=13, height=2, background='aqua')
        self.answer2 = tkinter.Button(top, width=13, height=2, background='aqua')
        self.answer3 = tkinter.Button(top, width=13, height=2, background='aqua')
        self.answer4 = tkinter.Button(top, width=13, height=2, background='aqua')
        self.answer1.grid(row=3, column=4, columnspan=2)
        self.answer2.grid(row=3, column=6, columnspan=2)
        self.answer3.grid(row=4, column=4, columnspan=2)
        self.answer4.grid(row=4, column=6, columnspan=2)
        self.answer1.lower()
        self.answer2.lower()
        self.answer3.lower()
        self.answer4.lower()
        self.useranswer = tkinter.Entry(top)
        self.useranswer.grid(row=3, column=5, columnspan=2)
        self.useranswer.lower()
        self.confirmanswer = tkinter.Button(top, width=13, height=2, text='confirm answer', command=self.Checkanswer)
        self.confirmanswer.grid(row=4, column=5, columnspan=2)
        self.confirmanswer.lower()
        self.quitbutton = tkinter.Button(top, text='quit',command=self.quitquiz)
        self.quitbutton.grid(row=3, column=0, columnspan=2)
        self.nextq = tkinter.Button(top, text='next question',state='disabled',command=self.Playquiz)
        self.nextq.grid(row=4, column=0, columnspan=2)
        self.score = tkinter.Label(top, width=30, height=2, background = 'red', text='score: ',anchor='w')
        self.score.grid(row=5, column=4, columnspan=4)

    def Startquiz(self):
        self.choice.config(state='disabled')
        self.start.config(state='disabled')
        self.nextq.config(state='normal')
        num = 3
        topic = var.get()
        if topic == 'all topics':
            c.execute('SELECT QuestionID FROM Questions')
            count = len(c.fetchall())
            while num >=0:
                questionID = random.randint(1,count)
                if questionID not in randlist:
                    randlist.append(questionID)
                    num = num - 1
        else:
            c.execute("SELECT TopicID FROM Topics WHERE Topic= '%s'" % topic)
            topicID = str(c.fetchone()).strip("(),'")

            while num >=0:
                c.execute("SELECT QuestionID FROM Questions WHERE TopicID= '%s' ORDER BY RANDOM() LIMIT 1" % topicID)
                questionID = str(c.fetchone()).strip("(),'")
                if questionID not in randlist:
                    randlist.append(questionID)
                    num = num - 1
                  
       

            

    def Playquiz(self):
        self.answer1.lower()
        self.answer2.lower()
        self.answer3.lower()
        self.answer4.lower()
        self.useranswer.lower()
        self.confirmanswer.lower()
        self.nextq.config(state='disabled')
        self.confirmanswer.config(state='normal')
        topic = var.get()
        x = 0
        num = 3
        self.qnum = self.qnum + 1
        optionlist = [self.answer1,self.answer2,self.answer3,self.answer4]
        templist = []
        if not randlist:
            self.questionbox.config(text = 'game over')
            self.nextq.config(state='disabled')
            user = userid[0]
            date = time.strftime("%d/%m/%Y")
            c.execute('INSERT INTO Score(UserID, dateofattempt, Score, topiccovered) VALUES(?,?,?,?)',(user, date, self.currentscore,topic))
            new_db.commit()
            
        else:
            self.questionnum.config(text='question: '+str(self.qnum))
            questionID = randlist[0]
            c.execute("SELECT Question FROM Questions WHERE QuestionID = '%s'" % questionID)
            question = str(c.fetchone()).strip("(),'")
            self.questionbox.config(text = question)
            c.execute("SELECT QTID FROM Questions WHERE QuestionID = '%s'" % questionID)
            QTID = str(c.fetchone()).strip("(),'")
            c.execute("SELECT Type FROM Questiontype WHERE QTID = '%s'" % QTID)
            questiontype = str(c.fetchone()).strip("(),'")
            if questiontype == 'Multiple Choice':
                c.execute("SELECT Answer FROM Questions WHERE QuestionID = '%s'" % questionID)
                answer = str(c.fetchone()).strip("(),'")
                c.execute("SELECT IncorrectAnswer1 FROM Questions WHERE QuestionID = '%s'" % questionID)
                wronganswer1 = str(c.fetchone()).strip("(),'")
                c.execute("SELECT IncorrectAnswer2 FROM Questions WHERE QuestionID = '%s'" % questionID)
                wronganswer2 = str(c.fetchone()).strip("(),'")
                c.execute("SELECT IncorrectAnswer3 FROM Questions WHERE QuestionID = '%s'" % questionID)
                wronganswer3 = str(c.fetchone()).strip("(),'")
                answerlist.append(answer)
                correctanswers.append(answer)
                answerlist.append(wronganswer1)
                answerlist.append(wronganswer2)
                answerlist.append(wronganswer3)
                self.answer1.lift()
                self.answer2.lift()
                self.answer3.lift()
                self.answer4.lift()
                while num >=0:
                    z = random.randint(0,num)
                    if optionlist[x] not in templist:
                        templist.append(optionlist[x])
                        num = num-1
                        optionlist[x].config(text=answerlist[z])
                        if answerlist[z] == answer:
                            optionlist[x].config(command=self.Correctanswer)
                        else:
                            optionlist[x].config(command=self.Incorrect)  
                        x = x+1
                        answerlist.pop(z)
            elif questiontype == 'Long Answer':
                c.execute("SELECT Answer FROM Questions WHERE QuestionID = '%s'" % questionID)
                answer = str(c.fetchone()).strip("(),'")
                correctanswers.append(answer)
                self.useranswer.lift()
                self.confirmanswer.lift()
           

    def Correctanswer(self):
        self.answer1.lower()
        self.answer2.lower()
        self.answer3.lower()
        self.answer4.lower()
        questionID = randlist[0]
        c.execute("SELECT Scorereward FROM Questions WHERE QuestionID = '%s'" % questionID)
        reward = str(c.fetchone()).strip("(),'")
        reward = int(reward)
        self.currentscore = self.currentscore + reward
        strscore = str(self.currentscore)
        self.score.config(text='score: '+strscore)
        userID = userid[0]
        c.execute("SELECT TopicID FROM Questions WHERE QuestionID = '%s'" % questionID)
        topicID = str(c.fetchone()).strip("(),'")
        c.execute("SELECT FeedbackID FROM Topicfeedback WHERE TopicID = '%s' AND UserID = '%s'" % (topicID,userID))
        feedbackID = str(c.fetchone()).strip("(),'")
        c.execute("SELECT Numanswered FROM Topicfeedback WHERE FeedbackID = '%s'" % feedbackID)
        numans = str(c.fetchone()).strip("(),'")
        c.execute("SELECT PercentageCorrect FROM Topicfeedback WHERE FeedbackID = '%s'" % feedbackID)
        percent = str(c.fetchone()).strip("(),'")
        numans = int(numans)
        percent = int(percent)
        numcorrect = (percent/100)*numans
        newnumans = numans+1
        newnumcorrect = numcorrect+1
        newpercent = round((newnumcorrect/newnumans)*100)
        c.execute("UPDATE Topicfeedback SET Numanswered = '%s',PercentageCorrect = '%s' WHERE FeedbackID = '%s'" % (newnumans,newpercent,feedbackID))
        new_db.commit()
        if newpercent >= 90:
            c.execute("SELECT commentID FROM Comments WHERE percent = '%s'" % 90)
            commentID = str(c.fetchone()).strip("(),'")
            c.execute("UPDATE Topicfeedback SET commentID = '%s' WHERE FeedbackID = '%s'" % (commentID,feedbackID))
            new_db.commit()
        elif newpercent >= 70:
            c.execute("SELECT commentID FROM Comments WHERE percent = '%s'" % 70)
            commentID = str(c.fetchone()).strip("(),'")
            c.execute("UPDATE Topicfeedback SET commentID = '%s' WHERE FeedbackID = '%s'" % (commentID,feedbackID))
            new_db.commit()
        elif newpercent >= 50:
            c.execute("SELECT commentID FROM Comments WHERE percent = '%s'" % 50)
            commentID = str(c.fetchone()).strip("(),'")
            c.execute("UPDATE Topicfeedback SET commentID = '%s' WHERE FeedbackID = '%s'" % (commentID,feedbackID))
            new_db.commit()
        else:
            c.execute("SELECT commentID FROM Comments WHERE percent = '%s'" % 49)
            commentID = str(c.fetchone()).strip("(),'")
            c.execute("UPDATE Topicfeedback SET commentID = '%s' WHERE FeedbackID = '%s'" % (commentID,feedbackID))
            new_db.commit()
        
        self.questionbox.config(text = 'correct answer')
        randlist.remove(questionID)
        self.nextq.config(state='normal')

    def Incorrect(self):
        self.answer1.lower()
        self.answer2.lower()
        self.answer3.lower()
        self.answer4.lower()
        q = self.qnum - 1
        answer = correctanswers[q]
        questionID = randlist[0]
        userID = userid[0]
        c.execute("SELECT TopicID FROM Questions WHERE QuestionID = '%s'" % questionID)
        topicID = str(c.fetchone()).strip("(),'")
        c.execute("SELECT FeedbackID FROM Topicfeedback WHERE TopicID = '%s' AND UserID = '%s'" % (topicID,userID))
        feedbackID = str(c.fetchone()).strip("(),'")
        c.execute("SELECT Numanswered FROM Topicfeedback WHERE FeedbackID = '%s'" % feedbackID)
        numans = str(c.fetchone()).strip("(),'")
        c.execute("SELECT PercentageCorrect FROM Topicfeedback WHERE FeedbackID = '%s'" % feedbackID)
        percent = str(c.fetchone()).strip("(),'")
        numans = int(numans)
        percent = int(percent)
        numcorrect = (percent/100)*numans
        newnumans = numans+1
        newpercent = round((numcorrect/newnumans)*100)
        c.execute("UPDATE Topicfeedback SET Numanswered = '%s',PercentageCorrect = '%s' WHERE FeedbackID = '%s'" % (newnumans,newpercent,feedbackID))
        new_db.commit()
        if newpercent >= 90:
            c.execute("SELECT commentID FROM Comments WHERE percent = '%s'" % 90)
            commentID = str(c.fetchone()).strip("(),'")
            c.execute("UPDATE Topicfeedback SET commentID = '%s' WHERE FeedbackID = '%s'" % (commentID,feedbackID))
            new_db.commit()
        elif newpercent >= 70:
            c.execute("SELECT commentID FROM Comments WHERE percent = '%s'" % 70)
            commentID = str(c.fetchone()).strip("(),'")
            c.execute("UPDATE Topicfeedback SET commentID = '%s' WHERE FeedbackID = '%s'" % (commentID,feedbackID))
            new_db.commit()
        elif newpercent >= 50:
            c.execute("SELECT commentID FROM Comments WHERE percent = '%s'" % 50)
            commentID = str(c.fetchone()).strip("(),'")
            c.execute("UPDATE Topicfeedback SET commentID = '%s' WHERE FeedbackID = '%s'" % (commentID,feedbackID))
            new_db.commit()
        else:
            c.execute("SELECT commentID FROM Comments WHERE percent = '%s'" % 49)
            commentID = str(c.fetchone()).strip("(),'")
            c.execute("UPDATE Topicfeedback SET commentID = '%s' WHERE FeedbackID = '%s'" % (commentID,feedbackID))
            new_db.commit()
        self.questionbox.config(text = 'incorrect answer the correct answer is :'+answer)
        randlist.remove(questionID)
        self.nextq.config(state='normal')

    def Checkanswer(self):
        useranswer = self.useranswer.get()
        questionID = randlist[0]
        c.execute("SELECT Scorereward FROM Questions WHERE QuestionID = '%s'" % questionID)
        reward = str(c.fetchone()).strip("(),'")
        reward = int(reward)
        c.execute("SELECT Answer FROM Questions WHERE QuestionID = '%s'" % questionID)
        answer = str(c.fetchone()).strip("(),'")
        userID = userid[0]
        c.execute("SELECT TopicID FROM Questions WHERE QuestionID = '%s'" % questionID)
        topicID = str(c.fetchone()).strip("(),'")
        c.execute("SELECT FeedbackID FROM Topicfeedback WHERE TopicID = '%s' AND UserID = '%s'" % (topicID,userID))
        feedbackID = str(c.fetchone()).strip("(),'")
        c.execute("SELECT Numanswered FROM Topicfeedback WHERE FeedbackID = '%s'" % feedbackID)
        numans = str(c.fetchone()).strip("(),'")
        c.execute("SELECT PercentageCorrect FROM Topicfeedback WHERE FeedbackID = '%s'" % feedbackID)
        percent = str(c.fetchone()).strip("(),'")
        numans = int(numans)
        percent = int(percent)
        numcorrect = (percent/100)*numans
        newnumans = numans+1
        if useranswer == answer:
            self.currentscore = self.currentscore + reward
            strscore = str(self.currentscore)
            self.questionbox.config(text = 'correct answer')
            self.score.config(text='score: '+strscore)
            newnumcorrect = numcorrect+1
        else:
            self.questionbox.config(text = 'incorrect answer the correct answer is: '+answer)
            newnumcorrect = numcorrect

        newpercent = round((newnumcorrect/newnumans)*100)
        c.execute("UPDATE Topicfeedback SET Numanswered = '%s',PercentageCorrect = '%s' WHERE FeedbackID = '%s'" % (newnumans,newpercent,feedbackID))
        new_db.commit()
        if newpercent >= 90:
            c.execute("SELECT commentID FROM Comments WHERE percent = '%s'" % 90)
            commentID = str(c.fetchone()).strip("(),'")
            c.execute("UPDATE Topicfeedback SET commentID = '%s' WHERE FeedbackID = '%s'" % (commentID,feedbackID))
            new_db.commit()
        elif newpercent >= 70:
            c.execute("SELECT commentID FROM Comments WHERE percent = '%s'" % 70)
            commentID = str(c.fetchone()).strip("(),'")
            c.execute("UPDATE Topicfeedback SET commentID = '%s' WHERE FeedbackID = '%s'" % (commentID,feedbackID))
            new_db.commit()
        elif newpercent >= 50:
            c.execute("SELECT commentID FROM Comments WHERE percent = '%s'" % 50)
            commentID = str(c.fetchone()).strip("(),'")
            c.execute("UPDATE Topicfeedback SET commentID = '%s' WHERE FeedbackID = '%s'" % (commentID,feedbackID))
            new_db.commit()
        else:
            c.execute("SELECT commentID FROM Comments WHERE percent = '%s'" % 49)
            commentID = str(c.fetchone()).strip("(),'")
            c.execute("UPDATE Topicfeedback SET commentID = '%s' WHERE FeedbackID = '%s'" % (commentID,feedbackID))
            new_db.commit()
                
        randlist.remove(questionID)
        self.nextq.config(state='normal')
        self.confirmanswer.config(state='disabled')

    def quitquiz(self):
        self.top.destroy()
        
                
        
            
                    
                            
class CreateAcc():
    def __init__(self, parent):
        top = self.top = tkinter.Toplevel(parent)
        tkinter.Label(top, text="please fill in the following details to create a new account").grid(row=0, columnspan=2)
        tkinter.Label(top, text="firstname:").grid(row=1, column=0)
        tkinter.Label(top, text="surname:").grid(row=2, column=0)
        tkinter.Label(top, text="date of birth:").grid(row=3, column=0)
        tkinter.Label(top, text="username:").grid(row=4, column=0)
        tkinter.Label(top, text="password:").grid(row=5, column=0)
        tkinter.Label(top, text="repeat password").grid(row=6, column=0)
        self.label = tkinter.Label(top, text="  ")
        self.label.grid(row=6, column=2)
        self.usererror = tkinter.Label(top, text="  ")
        self.usererror.grid(row=4, column=2)
        self.e3 = tkinter.Entry(top)
        self.e4 = tkinter.Entry(top)
        self.e5 = tkinter.Entry(top)
        self.e6 = tkinter.Entry(top)
        self.e7 = tkinter.Entry(top)
        self.e3.grid(row=1, column=1)
        self.e4.grid(row=2, column=1)
        self.e5.grid(row=4, column=1)
        self.e6.grid(row=5, column=1)
        self.e7.grid(row=6, column=1)
        self.s1 = tkinter.Spinbox(top, from_=0, to=30)
        self.s2 = tkinter.Spinbox(top, from_=0, to=12)
        self.s3 = tkinter.Spinbox(top, from_=1970, to=2016)
        self.s1.grid(row=3, column=1,)
        self.s2.grid(row=3, column=2,)
        self.s3.grid(row=3, column=3,)
        self.CreateButton = tkinter.Button(top, text='create account', command=self.Create)
        self.CreateButton.grid(row=7, column=0)
        w, h = top.winfo_screenwidth(), top.winfo_screenheight()
        top.overrideredirect(1)
        top.geometry("%dx%d+0+0" % (w, h))
        
    def Create(self):
        firstname = self.e3.get()
        surname = self.e4.get()
        username = self.e5.get()
        password = self.e6.get()
        password2 = self.e7.get()
        day = self.s1.get()
        month = self.s2.get()
        year = self.s3.get()
        bList =[]
        newaccount = False
        x = 1
        c.execute("SELECT Username FROM User")
        count = len(c.fetchall())
        print(count)
        for i in range(1,count):
            c.execute("SELECT Username FROM User WHERE UserID= '%s'" % i)
            Username = str(c.fetchone()).strip("(),'")
            bList.append(Username)
        print(bList)
        for index in range(1,len(bList)):
            currentvalue = bList[index]
            position = index
            while position>0 and ''.join(str(ord(c)) for c in bList[position-1]) < ''.join(str(ord(c)) for c in currentvalue):
                bList[position]=bList[position-1]
                position = position-1
            bList[position] = currentvalue
        print(bList)
        lower = 0
        upper = len(bList)-1
        print(upper)
        found = False
        while lower <= upper and not found:
            middle = (lower+upper) // 2
            if ''.join(str(ord(c)) for c in bList[middle]) < ''.join(str(ord(c)) for c in username):
                lower= middle + 1
            elif ''.join(str(ord(c)) for c in bList[middle]) > ''.join(str(ord(c)) for c in username):
                upper = middle
            else:
                found = True
        if found:
            self.usererror.config(text='an account with this username already exists please enter a different username')
        else:
            if password == password2:
                newaccount = True
                c.execute('INSERT INTO User(Username, Password, DOB, Firstname,Surname) VALUES(?,?,?,?,?)',(username, password, day+'/'+month+'/'+year, firstname, surname))
                new_db.commit()
            
            else:
                self.label.config(text='passwords are not identical please re-enter')
        if newaccount == True:
            c.execute("SELECT UserID FROM User WHERE Username= '%s'" % username)
            UID = str(c.fetchone()).strip("(),'")
            UID = int(UID)
            while x <= 3:
                c.execute('INSERT INTO Topicfeedback(TopicID, UserID, Numanswered, PercentageCorrect,CommentID) VALUES(?,?,?,?,?)',(x, UID, 0, 0, 0))
                new_db.commit()
                x = x+1
            self.top.destroy()
            
class Record():
    def __init__(self, scoreid=0 ,userid=0,date='', score=0,topic=''):
        self.userid = userid
        self.score = score
        self.date = date
        self.topic = topic
        self.scoreid = scoreid            
      
class Leaderboard():
    def __init__(self, parent):
        top = self.top = tkinter.Toplevel(parent)
        tkinter.Label(top ,text='leaderboard').grid(row=0, column=0)
        tkinter.Label(top ,text='choose leaderboard type').grid(row=1, column=0)
        self.choice = tkinter.OptionMenu(top, var1, 'personal leaderboard','all users')
        self.choice.grid(row=1, column=1)
        self.confirm = tkinter.Button(top, text='confirm', command = self.order)
        self.confirm.grid(row=2,column=0)
        self.quitbutton = tkinter.Button(top, text='quit',command=self.quitleaderboard)
        self.quitbutton.grid(row=2, column=1)
        myframe=tkinter.Frame(top,relief='sunken',width=300,height=200,bd=1)
        myframe.grid(row=3,column=0, columnspan=3)

        self.canvas=tkinter.Canvas(myframe)
        self.frame=tkinter.Frame(self.canvas)
        myscrollbar=tkinter.Scrollbar(myframe,orient="vertical",command=self.canvas.yview)
        self.canvas.config(yscrollcommand=myscrollbar.set)
        myscrollbar.pack(side="right",fill="y")
        self.canvas.pack(side="left")
        self.canvas.create_window((0,0),window=self.frame,anchor='nw')
        self.frame.bind("<Configure>",self.myfunction)

        tkinter.Label(self.frame,text='rank').grid(row=0,column=0)
        tkinter.Label(self.frame,text='user').grid(row=0,column=1)
        tkinter.Label(self.frame,text="topic covered").grid(row=0,column=2)
        tkinter.Label(self.frame,text="score").grid(row=0,column=3)
        tkinter.Label(self.frame,text="date").grid(row=0,column=4)
       



    
    def order(self):
        self.confirm.config(state='disabled')
        userID = userid[0]
        choice = var1.get()
        aList = []
        i = 0
        if choice == 'personal leaderboard':
            c.execute("SELECT * FROM Score WHERE UserID= '%s'" % userID)
            q = c.fetchall()
            for row in q:
                print(row[0])
                aList.append(Record(int(row[0]),int(row[1]),row[2],int(row[3]),row[4]))
                

        else:
            c.execute("SELECT * FROM Score")
            q = c.fetchall()
            for row in q:
                print(row[0])
                aList.append(Record(int(row[0]),int(row[1]),row[2],int(row[3]),row[4]))

        for index in range(1,len(aList)):
            currentvalue = aList[index]
            position = index
            while position>0 and aList[position-1].score < currentvalue.score:
                aList[position]=aList[position-1]
                position = position-1
            aList[position] = currentvalue


        for record in aList:
            i = i+1
            userID = record.userid
            c.execute("SELECT Username FROM User WHERE UserID = '%s'" % userID)
            username = str(c.fetchone()).strip("(),'")
            tkinter.Label(self.frame,text= i).grid(row=i,column=0)
            tkinter.Label(self.frame,text= username).grid(row=i,column=1)
            tkinter.Label(self.frame,text=record.topic).grid(row=i,column=2)
            tkinter.Label(self.frame,text=record.score).grid(row=i,column=3)
            tkinter.Label(self.frame,text=record.date).grid(row=i,column=4)

        

        
    
             
    def myfunction(self,canvas):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"),width=300,height=200)


            
    def quitleaderboard(self):
        self.top.destroy()        


class Feedback():
    def __init__(self, parent):
        top= self.top = tkinter.Toplevel(parent)
        tkinter.Label(top,text="Feedback").grid(row=0,column=0)
        tkinter.Label(top,text="choose a topic").grid(row=1,column=0)
        self.topicchoice = tkinter.OptionMenu(top, var2, 'addition','subtraction','multiplication')
        self.topicchoice.grid(row=1,column=1)
        self.confirm = tkinter.Button(top, text='confirm',command=self.showfeedback)
        self.confirm.grid(row=7,column=0)
        self.quitbutton = tkinter.Button(top, text='quit',command=self.quitfeedback)
        self.quitbutton.grid(row=7, column=1)
        tkinter.Label(top,text='Topic').grid(row=3,column=0)
        tkinter.Label(top,text="Total questions answered").grid(row=4,column=0)
        tkinter.Label(top,text='Percentage of correct answers').grid(row=5,column=0)
        tkinter.Label(top,text="Feedback").grid(row=6,column=0)
        self.topic = tkinter.Label(top,text='')
        self.topic.grid(row=3,column=2)
        self.num = tkinter.Label(top,text="")
        self.num.grid(row=4,column=2)
        self.percent = tkinter.Label(top,text='')
        self.percent.grid(row=5,column=2)
        self.feedback = tkinter.Label(top,text="")
        self.feedback.grid(row=6,column=2)
        w, h = top.winfo_screenwidth(), top.winfo_screenheight()
        top.overrideredirect(1)
        top.geometry("%dx%d+0+0" % (w, h))


    def showfeedback(self):
        self.topic.config(text='')
        self.num.config(text='')
        self.percent.config(text='')
        self.feedback.config(text='')
        userID = userid[0]
        choice = var2.get()
        c.execute("SELECT TopicID FROM Topics WHERE Topic = '%s'" % choice)
        topicID = str(c.fetchone()).strip("(),'")
        c.execute("SELECT FeedbackID FROM Topicfeedback WHERE TopicID = '%s' AND UserID = '%s'" % (topicID,userID))
        feedbackID = str(c.fetchone()).strip("(),'")
        c.execute("SELECT Numanswered FROM Topicfeedback WHERE FeedbackID = '%s'" % feedbackID)
        numanswered = str(c.fetchone()).strip("(),'")
        c.execute("SELECT PercentageCorrect FROM Topicfeedback WHERE FeedbackID = '%s'" % feedbackID)
        percentage = str(c.fetchone()).strip("(),'")
        c.execute("SELECT commentID FROM Topicfeedback WHERE FeedbackID = '%s'" % feedbackID)
        commentID = str(c.fetchone()).strip("(),'")
        c.execute("SELECT comment FROM Comments WHERE commentID = '%s'" % commentID)
        comment = str(c.fetchone()).strip("(),'")
        self.topic.config(text=choice)
        self.num.config(text=numanswered)
        self.percent.config(text=percentage+'%')
        self.feedback.config(text=comment)

    def quitfeedback(self):
        self.top.destroy()  
    
class SignIn():
    def __init__(self, parent):
        top = self.top = tkinter.Toplevel(parent)
        tkinter.Label(top, text="username:").grid(row=0, column=0)
        tkinter.Label(top, text="password:").grid(row=1, column=0)
        self.l1 = tkinter.Label(top, text=" ")
        self.l2 = tkinter.Label(top, text=" ")
        self.l1.grid(row=0, column=2)
        self.l2.grid(row=1, column=2)
        self.e1 = tkinter.Entry(top)
        self.e2 = tkinter.Entry(top)
        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.mySubmitButton = tkinter.Button(top, text='Sign In', command=self.send)
        self.mySubmitButton.grid(row=2, column=0)
        self.createacc = tkinter.Button(top, text='create account', command=self.opencreate).grid(row=2, column=1)
        w, h = top.winfo_screenwidth(), top.winfo_screenheight()
        top.overrideredirect(1)
        top.geometry("%dx%d+0+0" % (w, h))
        
    def send(self):
        self.l1.config(text='')
        self.l2.config(text='')
        username = self.e1.get()
        password = self.e2.get()
        c.execute("SELECT UserID FROM User WHERE Username= '%s'" % username)
        UID = str(c.fetchone()).strip("(),'")
        c.execute("SELECT Password FROM User WHERE Username= '%s'" % username)
        pass2 = str(c.fetchone()).strip("(),'")
        if pass2 == 'None':
            self.l1.config(text='username is incorrect')
        elif password == pass2:
            buttonsignin.config(text='signed in as: '+username, state='disabled')
            buttonhistory.config(state='normal')
            buttonplayquiz.config(state='normal')
            buttonfeedback.config(state='normal')
            userid.append(UID)
            self.top.destroy()
        else:
            self.l2.config(text='password is incorrect')
            
        

    def opencreate(self):
        inputDialog = CreateAcc(mygui)
        mygui.wait_window(inputDialog.top)

                
def endprogram():
    mygui.destroy()

def signin():
    inputDialog = SignIn(mygui)
    mygui.wait_window(inputDialog.top)
    
def playgame():
    inputDialog = Play(mygui)
    mygui.wait_window(inputDialog.top)

def DisplayLeaderboard():
    inputDialog = Leaderboard(mygui)
    mygui.wait_window(inputDialog.top)
    
def Displayfeedback():
    inputDialog = Feedback(mygui)
    mygui.wait_window(inputDialog.top)
        
mygui = tkinter.Tk()

new_db = sqlite3.connect('QuizDB.db')
c=new_db.cursor()

var = tkinter.StringVar(mygui)
var.set('all topics')

var1 = tkinter.StringVar(mygui)
var1.set('personal leaderboard')

var2 = tkinter.StringVar(mygui)
var2.set('addition')

w, h = mygui.winfo_screenwidth(), mygui.winfo_screenheight()
mygui.overrideredirect(1)
mygui.geometry("%dx%d+0+0" % (w, h))

buttonplayquiz = tkinter.Button(mygui, text = 'Play',state = 'disabled', command = playgame)
buttonplayquiz.place(x=10,y=10)
buttonsignin = tkinter.Button(mygui, text = 'Sign in', command = signin)
buttonsignin.place(x=10,y=40)
buttonhistory = tkinter.Button(mygui, text = 'leaderboards',state = 'disabled',command = DisplayLeaderboard)
buttonhistory.place(x=10,y=70)
buttonfeedback = tkinter.Button(mygui, text = 'Feedback',state = 'disabled',command=Displayfeedback)
buttonfeedback.place(x=10,y=100)
buttonquit = tkinter.Button(mygui, text = 'Quit', command= endprogram)
buttonquit.place(x=10,y=130)


mygui.mainloop()
