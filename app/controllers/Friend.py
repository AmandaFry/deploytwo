from system.core.controller import *
from flask import Flask, flash, session, request, redirect

class Friend(Controller):
    def __init__(self, action):
        super(Friend, self).__init__(action)
        self.load_model('FriendModel')
        # self.db = self._app.db

    def dashboard(self):
        friends = self.models['FriendModel'].my_friends()
        # print ('%' * 25)
        # print friends
        # print ('%' * 25)
        not_friends = self.models['FriendModel'].not_friends()
        # print ('!' * 25)
        # print not_friends
        # print ('!' * 25)
        return self.load_view('dashboard.html', friends=friends, not_friends=not_friends)

    def profile(self,id):
        profile = self.models['FriendModel'].profile(id)
        # print ('%' * 25)
        # print profile
        # print ('%' * 25)
        return self.load_view('profile.html', profile=profile)

    def add_friend(self, id):
        add_friend = self.models['FriendModel'].add_friend(id)
        # print ('!' * 25)
        # print add_friend
        # print ('!' * 25)
        return redirect ('/dashboard')

    def remove_friend(self, id):
        remove_friend = self.models['FriendModel'].remove_friend(id)
        print ('!' * 25)
        print remove_friend
        print ('!' * 25)
        return redirect ('/dashboard')
