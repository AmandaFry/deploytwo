from system.core.controller import *
from flask import Flask, session, flash, request, redirect

class User(Controller):
    def __init__(self, action):
        super(User, self).__init__(action)
        self.load_model('UserModel')

    def index(self):
        #It is needed for inital page load
        return self.load_view('index.html')

    def processLogin(self):
        #information collected to logon
        userInfo = {
            'email' : request.form['email'],
            'passw' : request.form['passw']
        }
        #sending information to model
        userLogin = self.models['UserModel'].loginUser(userInfo)
        
        #information returned from model
        if userLogin['status']  == False:
            #return to logon page and show errors
            for message in userLogin['errors']:
                flash(message)
            return self.load_view('index.html')
        else:
            #login and store name and id in session
            session['id'] = userLogin['user'][0]['id']
            session['name'] = userLogin['user'][0]['first_name'] + ' ' + userLogin['user'][0]['last_name']
            return redirect('/dashboard')
 

    def processRegister(self):
        #information collected to register
        userInfo = {
            'fName' : request.form['fName'],
            'lName' : request.form['lName'],
            'alias' : request.form['alias'],
            'email' : request.form['email'],
            'passw' : request.form['passw'],
            'confPassw' : request.form['confPassw'],
            'birthday' : request.form['birthday']
        }

        #sending information to model
        userRegister = self.models['UserModel'].registerUser(userInfo)

        #process returned information
        if userRegister['status'] == False:
            for message in userRegister['errors']:
                flash(message)
            return self.load_view('index.html')
        else:
            flash('SUCCESFULLY REGISTERED, PLEASE LOGIN!')
            return redirect('/')

    def logout(self):
        #clear user inforamtion from session
        session.clear()
        return redirect('/')