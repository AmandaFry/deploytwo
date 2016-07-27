from system.core.controller import *
from flask import Flask, session, flash, request, redirect

class User(Controller):
    def __init__(self, action):
        super(User, self).__init__(action)
        self.load_model('UserModel')

    def index(self):
        #It is needed for inital page load
        return self.load_view('index.html')

    def login(self):
        #information collected to logon
        user_info = {
            'email' : request.form['email'],
            'passw' : request.form['passw']
        }
        #sending information to model
        user_login = self.models['UserModel'].login_user(user_info)
        
        #information returned from model
        if user_login['status']  == False:
            #return to logon page and show errors
            for message in user_login['errors']:
                flash(message)
            return self.load_view('index.html')
        else:
            #login and store name and id in session
            session['id'] = user_login['user'][0]['id']
            session['name'] = user_login['user'][0]['first_name'] + ' ' + user_login['user'][0]['last_name']
            return redirect('/dashboard')
 

    def register(self):
        #information collected to register
        user_info = {
            'f_name' : request.form['f_name'],
            'l_name' : request.form['l_name'],
            'alias' : request.form['alias'],
            'email' : request.form['email'],
            'passw' : request.form['passw'],
            'conf_passw' : request.form['conf_passw'],
            'birthday' : request.form['birthday']
        }

        #sending information to model
        user_register = self.models['UserModel'].register_user(user_info)

        #process returned information
        if user_register['status'] == False:
            for message in user_register['errors']:
                flash(message)
            return self.load_view('index.html')
        else:
            flash('SUCCESFULLY REGISTERED, PLEASE LOGIN!')
            return redirect('/')

    def logout(self):
        #clear user inforamtion from session
        session.clear()
        return redirect('/')