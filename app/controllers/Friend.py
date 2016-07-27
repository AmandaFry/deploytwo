from system.core.controller import *
from flask import Flask, flash, session, request, redirect

class Friend(Controller):
    def __init__(self, action):
        super(Friend, self).__init__(action)
        self.load_model('FriendModel')
        # self.db = self._app.db

    def dashboard(self):
        friends = self.models['FriendModel'].myFriends()
        # print ('%' * 25)
        # print friends
        # print ('%' * 25)
        notFriends = self.models['FriendModel'].notFriends()
        # print ('!' * 25)
        # print not_friends
        # print ('!' * 25)
        return self.load_view('dashboard.html', friends=friends, notFriends=notFriends)

    def profile(self,id):
        profile = self.models['FriendModel'].profile(id)
        # print ('%' * 25)
        # print profile
        # print ('%' * 25)
        return self.load_view('profile.html', profile=profile)

    def addFriend(self, id):
        addFriend = self.models['FriendModel'].addFriend(id)
        # print ('!' * 25)
        # print addFriend
        # print ('!' * 25)
        return redirect ('/dashboard')

    def removeFriend(self, id):
        removeFriend = self.models['FriendModel'].removeFriend(id)
        print ('!' * 25)
        print removeFriend
        print ('!' * 25)
        return redirect ('/dashboard')
