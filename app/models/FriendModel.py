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
        # notIn =''
        # query = "SELECT users.first_name, users.alias, users.id FROM users LEFT JOIN friendslist ON users.id = friendslist.user_id WHERE users.id != :id"
        #query = "SELECT * from users WHERE users.id !=:id AND users.id NOT IN (SELECT users.id as UsersID FROM users JOIN friendslist ON users.id = friendslist.user_id WHERE users.id = :id);"
        query = "SELECT * from users WHERE users.id !=:id AND users.id NOT IN (select friend_id from friendslist where user_id = :id);"
        data = { 'id' : session['id']}
        # query = "SELECT  users.first_name, users.alias, friendslist.friend_id as friendID, users.id as UsersID FROM users JOIN friendslist ON users.id = friendslist.user_id WHERE users.id = :id"
        # data = { 'id' : session['id']}
        # partial_notfriend = self.db.query_db(query, data)
        # print ('&' * 25)
        # print partial_notfriend
        # print ('&' * 25)

        # for i in partial_notfriend:
        #     # print ('*' * 25)
        #     # print 'from server', i['friendID']
        #     # print ('*' * 25)
        #     # notInOne = int(i['friendID'])
        #     # print ('*' * 25)
        #     # print 'The notinOne', notInOne
        #     # print ('*' * 25)
        #     # notIn+= notIn+ ', ' +str(notInOne)
        #     notIn+=str(i['friendID']) + ', '

        # notIn = notIn + str(session['id'])
        # print ('*' * 25)
        # print 'Final notin', notIn
        # print ('*' * 25)
        # # query = "SELECT * from users WHERE users.id NOT IN (:friends) AND users.id !=:id"
        # query = "SELECT * from users WHERE users.id NOT IN (:friends)"
        # data = { 'friends': notIn }
        notFriends = self.db.query_db(query, data)

        # print ('^' * 25)
        # print not_friends
        # print ('^' * 25)
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
