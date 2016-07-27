from system.core.controller import *
from flask import Flask, flash, session, request, redirect

class Friend(Controller):
    def __init__(self, action):
        super(Friend, self).__init__(action)
        self.load_model('FriendModel')

    def dashboard(self):
        # need this if people just type in the dashbaord you need to be pass login to get here.
        try:
            session['id']
        except:
            return redirect ('/')

        friends = self.models['FriendModel'].myFriends()
        notFriends = self.models['FriendModel'].notFriends()
        return self.load_view('dashboard.html', friends=friends, notFriends=notFriends)

    def profile(self,id):
        profile = self.models['FriendModel'].profile(id)
        return self.load_view('profile.html', profile=profile)

    def addFriend(self, id):
        addFriend = self.models['FriendModel'].addFriend(id)
        return redirect ('/dashboard')

    def removeFriend(self, id):
        removeFriend = self.models['FriendModel'].removeFriend(id)
        print ('!' * 25)
        print removeFriend
        print ('!' * 25)
        return redirect ('/dashboard')
