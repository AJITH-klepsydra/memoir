from PyQt5 import QtWidgets,uic
import pyrebase
from PyQt5.QtCore import Qt,pyqtSignal,QTimer
from PyQt5.QtCore import QSize
from datetime import date
import random
import webbrowser
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPalette, QBrush, QMovie 
from firebase import firebase as fb
import time
import sys

class main_window(QtWidgets.QMainWindow):
	signal_dash = pyqtSignal(str,str)
	def __init__(self):
		super(main_window,self).__init__()
		uic.loadUi('a.ui',self)
		syle1='''
		QPushButton{
		background-color: rgb(88, 178, 23);
		font: 15pt "Open Sans";
		border-radius:1px;color: rgb(255, 255, 255);
		}
		QPushButton:hover{
		background-color: rgb(0, 255, 0);
		font: 15pt "Open Sans";
		border-radius:1px;color: rgb(255, 255, 255);
		}
		'''
		self.firebaseConfig ={
			"apiKey": "AIzaSyA--z3Dm4GF7GR4hd0OAvEc-IFkHlIe5Zs",
    		"authDomain": "memoir-journal-app.firebaseapp.com",
    		"databaseURL": "https://memoir-journal-app.firebaseio.com",
    		"projectId": "memoir-journal-app",
    		"storageBucket": "memoir-journal-app.appspot.com",
    		"serviceAccount": "/home/klepsydra/Downloads/memoir-journal-app-firebase-adminsdk-u7p51-61a578d0bc.json",
    		"messagingSenderId": "26624224100",
    		"appId": "1:26624224100:web:fc61853f8851b03c2be871",
    		"measurementId": "G-44TC6S38Y4"
		}
		self.pushButton_4.hide()
		self.pushButton_3.hide()
		self.pushButton.setStyleSheet(syle1)
		self.pushButton_3.setStyleSheet(syle1)
		self.pushButton.setShortcut('return')
		self.pushButton_3.setShortcut('return')
		self.label_3.setStyleSheet(" background-image: url(bg.webp);")
		self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
		self.pushButton_2.clicked.connect(self.signup_page)
		self.pushButton.clicked.connect(self.login_ver)
		self.password = self.lineEdit_2.text()
		self.email = self.lineEdit.text()
		self.show()
		self.pushButton_3.clicked.connect(self.cloudin)
	def login_ver(self):
		self.password = self.lineEdit_2.text()
		self.email = self.lineEdit.text()
		firebase = pyrebase.initialize_app(self.firebaseConfig)
		auth = firebase.auth()
		self.password = self.lineEdit_2.text()
		self.email = self.lineEdit.text()
		email = self.lineEdit.text()
		self.password = self.lineEdit_2.text()

		if(len(self.password)<6):
			self.status.setText("WeakPassword")
		else:

			try:
				user = auth.sign_in_with_email_and_password(self.email,self.password)
				self.signal_dash.emit(self.password,self.email)
			except:
				self.status.setText("Login failed")

	def signup_page(self):
		self.password = self.lineEdit_2.text()
		self.email = self.lineEdit.text()
		self.label.setText("Sign Up ")
		self.label_2.setText(" ")
		self.pushButton_2.hide()
		self.pushButton.hide()
		self.pushButton_3.show()

		self.widget_3.setStyleSheet("background-color:rgb(144, 0, 72);")	
	def cloudin(self):
		self.password = self.lineEdit_2.text()
		self.email = self.lineEdit.text()

		if(len(self.password)<6):
			self.status.setText("WeakPassword")
		else:
			try:
				firebase = pyrebase.initialize_app(self.firebaseConfig)
				auth = firebase.auth()
				user = auth.create_user_with_email_and_password(self.email,self.password)
				self.signal_dash.emit(self.password,self.email)
			except Exception as e:
				self.status.setText("User Exists")
class dash_window(main_window):
	def __init__(self,passw,emil):
		super(dash_window,self).__init__()
		style1='''
			QPushButton{
			font: 120pt "OpenSymbol";
			background-color: rgb(97, 168, 124);
			color: rgb(22, 37, 44);
			border-radius:75px;
			}
			QPushButton:hover{
			font: 120pt "OpenSymbol";
			background-color: rgb(203, 232, 148);
			color: rgb(171, 69, 22);
			border-radius:75px;
			}
		'''

		uic.loadUi("dash.ui",self)
		self.subm.hide()
		self.rest.hide()
		self.resb.hide()
		self.label_6.hide()
		self.email=emil
		self.password=passw
		self.rest_2.hide()
		self.label_4.hide()
		self.f1.hide()
		self.subm_2.hide()
		self.label_3.hide()
		self.label_5.hide()
		ls_q=["\" Each new Day is blank page in the diary of your life.The Secret of Success is in turning that diary in to the best story you possibly can \"",
			  "\"I Can shake of everything as I write, my sorrows disappear, my courage is reborn\"",
			  "\" Writing a diary is like living your memories at present\"",
   			  "\"The life of every person is like a diary in which he means to write one and writes another \"",
              "\" Dear Diary, Oh it's all too much to explain and you wouldn't believe it anyway I'm going to bed\"",
              "\"I really don't know what's happened to me, but I have changed from top to toe. I am living in a strange mixture of memories of yesterday and today.\"",
              "\" Memory.. is the diary that we all carry with us\"",
              "\"I'm actually not funny.I'm just mean and people think i'm joking \"",
              "\"Once I loved her.. : ( \"",
              "\"Is it me... (please let it be me)\"",
              "\"Every night, I laid awake with your memories flooding through my eyes with the hope to be with you when sleep arrived.\"",
              "\"I will kill myself soon. But until then how do l tame my pain?\"",
              "\"I stand still inhaling the beauty of our memories,Flashbacks of our togetherness burn my flesh and I breathe love through every single skin pore. \"",
              "\"Sometimes things are better left unsaid until you're free of them.\"",
              "\"Never Love Someone Over Your Nerves! And You Can't even Help it Happening \""]
		self.textBrowser.setPlainText(ls_q[random.randint(0,len(ls_q)-1)])
		self.textBrowser.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(0, 0, 0, 0));border-radius:10px;font: 57 20pt \"Tlwg Typewriter\";color: rgb(135, 155, 99);")
		self.pushButton.setStyleSheet(style1)
		#self.pushButton_5.setStyleSheet(style2)
		self.pushButton_7.clicked.connect(self.editor)
		self.msgb.hide()
		self.comboBox.hide()
		self.cl.clicked.connect(self.retrieve)
		self.pushButton_6.clicked.connect(self.info)
		self.firebaseConfig ={
			"apiKey": "AIzaSyA--z3Dm4GF7GR4hd0OAvEc-IFkHlIe5Zs",
    		"authDomain": "memoir-journal-app.firebaseapp.com",
    		"databaseURL": "https://memoir-journal-app.firebaseio.com",
    		"projectId": "memoir-journal-app",
    		"storageBucket": "memoir-journal-app.appspot.com",
    		"serviceAccount": "/home/klepsydra/Downloads/memoir-journal-app-firebase-adminsdk-u7p51-61a578d0bc.json",
    		"messagingSenderId": "26624224100",
    		"appId": "1:26624224100:web:fc61853f8851b03c2be871",
    		"measurementId": "G-44TC6S38Y4"
		}
		today =date.today()
		today=str(today)
		self.ls= today.split('-')
		self.bgl.setStyleSheet(" background-image: url(bgdash.jpg);")
		#self.pushButton_5.setStyleSheet(" background-image: url(infoicon.jpg);")
		self.pushButton.clicked.connect(self.editor)
		self.img.setStyleSheet(" background-image: url(userp.png);border-width:2px;border-radius:40px;")
		with open("info.txt","r") as f:
			self.usern.setText("  "+str(self.email.split('@')[0]))
		self.show()
	def info(self):
		self.obj = info()
		self.obj.show()
		self.obj.setWindowTitle("Info")

	def retrieve(self):
		QtWidgets.QApplication.setOverrideCursor(Qt.WaitCursor)
		email= self.email
		self.mv= QMovie('sad1.gif')
		self.mv1= QMovie('ecstatic.gif')
		email_ls = email.split('@')
		firebase = pyrebase.initialize_app(self.firebaseConfig)
		auth = firebase.auth()
		user1 = auth.sign_in_with_email_and_password(self.email,self.password)
		stri= str(user1['localId'])
		curr_date = str(self.cl.selectedDate().toString("yyyy/MM/dd"))
		self.ls1 = curr_date.split('/')
		firebase = fb.FirebaseApplication("https://memoir-journal-app.firebaseio.com/"+email_ls[0]+self.password+'/'+self.ls1[0]+'-'+self.ls1[1],None)
		result = firebase.get("https://memoir-journal-app.firebaseio.com/"+email_ls[0]+self.password+'/'+self.ls1[0]+'-'+self.ls1[1]+":",'')
		
		self.f1.hide()
		#self.label5.hide()
		self.comboBox.hide()
		self.msgb.hide()
		self.textBrowser.hide()
		self.subm_2.hide()
		self.subm.hide()
		self.rest_2.show()
		self.rest.show()
		self.resb.show()
		count =0
		for x,y in result.items():
				for key in y:

				#print(str(y[key]))
				
					if(str(y[key])==curr_date):
						count=count+1
						
						self.label_6.show()
						self.label_6.setMovie(self.mv)
						self.mv.start()

						self.rest_2.setText(str(y['date']))
						self.rest.setText(str(y['title']))
						self.resb.setPlainText(str(y['message']))
		if(count ==0 ):
			self.label_6.show()

			self.rest_2.setText("No data")
			self.rest.setText('No data')
			self.resb.setPlainText('No data')

			
		QtWidgets.QApplication.restoreOverrideCursor()
	def editor(self):
		self.comboBox.show()
		self.subm_2.show()
		self.label_4.show()
		self.label_5.show()
		self.f1.show()
		self.rest.hide()
		self.rest_2.hide()
		self.resb.hide()
		self.subm.show()
		self.subm.setText("submit")
		self.label_3.show()
		self.textBrowser.hide()
		self.msgb.show()
		self.subm.clicked.connect(self.tocloud)
		self.label_5.setText("  "+self.ls[2]+"/"+self.ls[1]+"/"+self.ls[0])
	def tocloud(self):
		QtWidgets.QApplication.setOverrideCursor(Qt.WaitCursor)
		firebase = pyrebase.initialize_app(self.firebaseConfig)
		auth = firebase.auth()
		

		user1 = auth.sign_in_with_email_and_password(str(self.email),str(self.password))
		data = {
		"date":self.ls[0]+"/"+self.ls[1]+"/"+self.ls[2],
		"title":str(self.f1.text()),
		"message":str(self.msgb.toPlainText()),
		"theme":str(self.comboBox.currentText())
		}
		email=self.email 
		
		email_ls = email.split('@')
		firebase = fb.FirebaseApplication("https://memoir-journal-app.firebaseio.com/"+email_ls[0]+self.password+'/'+self.ls[0]+'-'+self.ls[1],None)
		result = firebase.post("https://memoir-journal-app.firebaseio.com/"+email_ls[0]+self.password+'/'+self.ls[0]+'-'+self.ls[1]+":",data)
		self.subm.setText("done")
		QtWidgets.QApplication.restoreOverrideCursor()
		

class info(main_window):
	def __init__(self):
		super(info,self).__init__()
		uic.loadUi('info.ui',self)
		self.fb_6.clicked.connect(self.fb1)
		self.mv = QMovie('esctatic.gif')
		self.bgl.setMovie(self.mv)
		self.mv.start()
		self.show()
	def fb1(self):
		webbrowser.open("https://github.com/AJITH-klepsydra/memoir")


class controller():
	def __init__(self):
		super().__init__()
		pass
	def login(self):
		self.sin1 = main_window()
		self.sin1.show()
		self.sin1.signal_dash.connect(self.to_dash)
		self.sin1.setWindowTitle("Login")
	def to_dash(self,passw,emil):
		self.sin1.hide()
		self.dash1 = dash_window(passw,emil)
		self.dash1.setWindowTitle("Memoir")
		self.dash1.show()


app = QtWidgets.QApplication(sys.argv)
win = controller()
win.login()
if(__name__ == '__main__'):
	app.exec_()
