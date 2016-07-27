from system.core.model import Model
from flask import Flask, flash, session
from datetime import datetime
import re

NOSPACE_REGEX = re.compile(r'^[a-zA-Z0-9]*$')

class FriendModel(Model):
    def __init__(self):
        super(FriendModel, self).__init__()
 
    def myFriends(self):
        query = "SELECT users.first_name, users.alias, users.id FROM users JOIN friendslist ON users.id = friendslist.friend_id WHERE user_id =:id"
        data = { 'id' : session['id']}
        my_friends = self.db.query_db(query, data)
        return (my_friends)

    def notFriends(self):
        query = "SELECT * from users WHERE users.id !=:id AND users.id NOT IN (select friend_id from friendslist where user_id = :id);"
        data = { 'id' : session['id']}
        notFriends = self.db.query_db(query, data)
        return (notFriends)

    def profile(self, id):
        query = "SELECT * FROM users WHERE id = :id"
        data = { 'id' : id }
        profile = self.db.query_db(query, data)
        return (profile)

    def addFriend(self,id):
        query = "INSERT INTO friendslist (user_id, friend_id, created_at, updated_at) VALUES (:id, :friend_id, NOW(), NOW())"
        data = {
            'id' : session['id'],
            'friend_id' : id,
        }
        addFriend = self.db.query_db(query, data)
        return (addFriend)


    def removeFriend(self, id):
        query = "DELETE FROM friendslist WHERE user_id = :id AND friend_id = :friend_id"
        data = {
            'id' : session['id'],
            'friend_id' : id,
        }
        removeFriend = self.db.query_db(query, data)
        return {'status':True}
