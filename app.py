from PyQt5 import QtWidgets,uic
import pyrebase
from PyQt5.QtCore import Qt,pyqtSignal,QTimer
from PyQt5.QtCore import QSize
from datetime import date

from PyQt5.QtGui import QImage, QPalette, QBrush, QMovie 
from firebase import firebase as fb
import time
import sys

class main_window(QtWidgets.QMainWindow):
	signal_dash = pyqtSignal()
	def __init__(self):
		super(main_window,self).__init__()
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

		uic.loadUi('a.ui',self)
		self.pushButton_4.hide()
		self.pushButton_3.hide()
		self.anime.hide()
		self.label_3.setStyleSheet(" background-image: url(bg.webp);")
		self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
		self.mv = QMovie('load.gif')
		self.anime.setMovie(self.mv)
		self.pushButton_2.clicked.connect(self.signup_page)
		self.pushButton.clicked.connect(self.login_ver)
		self.show()
		self.pushButton_3.clicked.connect(self.cloudin)
	def login_ver(self):
		firebase = pyrebase.initialize_app(self.firebaseConfig)
		auth = firebase.auth()
		email = self.lineEdit.text()
		password = self.lineEdit_2.text()
		with open("info.txt","w") as f:
			email = self.lineEdit.text()
			password = self.lineEdit_2.text()
			f.write(email)
		if(len(password)<6):
			self.status.setText("WeakPassword")
		else:

			try:
				user = auth.sign_in_with_email_and_password(email,password)
				self.signal_dash.emit()
			except:
				self.status.setText("Login failed")
	def stopan(self):
		self.mv.stop()
	def signup_page(self):
		self.anime.show()
		self.mv.start()
		self.label.setText("Sign up")
		self.label_2.setText("Already have an account")
		self.pushButton_2.hide()
		self.pushButton_4.show()
		self.pushButton.hide()
		self.pushButton_3.show()
		self.widget_3.setStyleSheet("background-color:rgb(144, 0, 72);")	
		self.mv.stop()
		self.anime.hide()
	def cloudin(self):
		with open("info.txt","w") as f:
			email = self.lineEdit.text()
			password = self.lineEdit_2.text()
			f.write(email)
		if(len(password)<6):
			self.status.setText("WeakPassword")
		else:
			try:
				self.anime.show()
				self.mv.start()
				firebase = pyrebase.initialize_app(self.firebaseConfig)
				auth = firebase.auth()
				user = auth.create_user_with_email_and_password(email,password)
				timer= QTimer(self)
				timer.singleShot(5000,self.stopan)
				self.signal_dash.emit()
				#self.anime.hide()
			except Exception as e:
				print(e)
				self.mv.stop()
				self.anime.hide()
				self.status.setText("User Exists")



class dash_window(main_window):
	def __init__(self):
		super(dash_window,self).__init__()
		uic.loadUi("dash.ui",self)
		self.subm.hide()
		self.rest.hide()
		self.resb.hide()
		self.rest_2.hide()
		self.label_4.hide()
		self.f1.hide()
		self.subm_2.hide()
		self.label_3.hide()
		self.label_5.hide()
		self.msgb.hide()
		self.comboBox.hide()
		self.cl.clicked.connect(self.retrieve)
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
		self.pushButton.clicked.connect(self.editor)
		self.img.setStyleSheet(" background-image: url(userp.png);border-width:2px;border-radius:40px;")
		with open("info.txt","r") as f:
			self.usern.setText("  "+str(str(f.read()).split('@')[0]))
		self.show()
	def retrieve(self):
		firebase = pyrebase.initialize_app(self.firebaseConfig)
		auth = firebase.auth()
		user1 = auth.sign_in_with_email_and_password("test2@gmail.com","123456")
		stri= str(user1['localId'])
		firebase = fb.FirebaseApplication("https://memoir-journal-app.firebaseio.com/"+stri+'/'+self.ls[0]+'-'+self.ls[1],None)

		curr_date = str(self.cl.selectedDate().toString("yyyy/MM/dd"))
		
		result = firebase.get("https://memoir-journal-app.firebaseio.com/"+stri+'/'+self.ls[0]+'-'+self.ls[1]+":",'')
		
		self.f1.hide()
		#self.label5.hide()
		self.comboBox.hide()
		self.msgb.hide()
		self.subm_2.hide()
		self.subm.hide()
		self.rest_2.show()
		self.rest.show()
		self.resb.show()
		
		for x,y in result.items():
				for key in y:

				#print(str(y[key]))
				
					if(str(y[key])==curr_date):
						self.rest_2.setText(str(y['date']))
						self.rest.setText(str(y['title']))
						self.resb.setPlainText(str(y['message']))
			
		#print(result)
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
		self.label_3.show()
		self.textBrowser.hide()
		self.msgb.show()
		self.subm.clicked.connect(self.tocloud)
		self.label_5.setText("  "+self.ls[2]+"/"+self.ls[1]+"/"+self.ls[0])
	def tocloud(self):
		firebase = pyrebase.initialize_app(self.firebaseConfig)
		auth = firebase.auth()
		user1 = auth.sign_in_with_email_and_password("test2@gmail.com","123456")
		data = {
		"date":self.ls[0]+"/"+self.ls[1]+"/"+self.ls[2],
		"title":str(self.f1.text()),
		"message":str(self.msgb.toPlainText())
		}
		stri= str(user1['localId'])
		print(user1)
		firebase = fb.FirebaseApplication("https://memoir-journal-app.firebaseio.com/"+stri+'/'+self.ls[0]+'-'+self.ls[1],None)
		result = firebase.post("https://memoir-journal-app.firebaseio.com/"+stri+'/'+self.ls[0]+'-'+self.ls[1]+":",data)
		print("success")





class controller():
	def __init__(self):
		super().__init__()
		pass
	def login(self):
		self.sin1 = main_window()
		self.sin1.show()
		self.sin1.signal_dash.connect(self.to_dash)
	def to_dash(self):
		self.dash1 = dash_window()
		self.dash1.show()

app = QtWidgets.QApplication(sys.argv)
win = controller()
win.login()
if(__name__ == '__main__'):
	app.exec_()
