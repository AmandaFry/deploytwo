from system.core.controller import *
from flask import Flask, session, flash, request, redirect

class User(Controller):
	def __init__(self, action):
		super(User, self).__init__(action)
		self.load_model('UserModel')

	def index(self):
		#this page is needed for initil page load
		return self.load_view('index.html')

	def process_login(self):
		#information
		user_info = {
			'emial':request.form['email'],
			'passw':request.form['[passw']
		}
		#sending informaiton to model
		user_login = self.models['UserModel'].login_user(user_info)

		#informaiton returned from model
		if user_login['status']==False
			# returned to logon page and show error
			for message in user_login['errors']:
				flash(message)
			return redirect('/')
		else:
			session['id']=user_login['user']['0']['id']
			session['name']=user_login['user'][0]['first_name'] + ' ' + user_login['user'][0]['last-name']
			return redirect('/dashboard')

	def process_registration(self):
		user_info = {
			'f_name':request.form['f_name'],
			'l_name':request.form['l_name'],
			'email': request.form['email'],
			'passw':request.form['passw'],
			'conf_passw':request.form['conf_passw'],
			'birthday':request.form['birthday']
		}

		register=self.models['Loginreg'].register_user(user_info)

		if register['status']==False
			for message in register['errors']:
				flash(message)
			return redirect('/')
		else:
			flash('SUCCESFULLY REGISTERED, PLEASE LOGIN!')
			return redirect('/')

	def logout(self):
		session.clear()
		return redirect('/')
