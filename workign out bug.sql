use friendslist;

select * from users;



SELECT users.first_name, users.alias, users.id FROM users JOIN friendslist ON users.id = friendslist.friend_id WHERE friendslist.user_id != 6;

select * from friendslist;

SELECT  users.first_name, users.alias, friendslist.friend_id as friendID, users.id as UsersID FROM users JOIN friendslist ON users.id = friendslist.user_id WHERE users.id = 6;

SELECT * from users WHERE users.id NOT IN (2, 4, 1) AND users.id !=6;


SELECT * from users WHERE users.id NOT IN  (3,5,6,1);



SELECT * FROM users
WHERE users.id NOT IN 
(SELECT friendslist.friend_id FROM friendslist WHERE friend_id != 6)
AND users.id NOT IN 
(SELECT friendslist.user_id FROM friendslist WHERE friend_id != 6);

SELECT  users.first_name, users.alias, friendslist.friend_id as friendID, users.id as UsersID FROM users 
JOIN friendslist ON users.id = friendslist.user_id WHERE users.id = 6 AND (SELECT * from users WHERE users.id NOT IN (6, 2, 4, 1))

SELECT * FROM friendslist.users
LEFT JOIN friendslist ON friendslist.user_id = users.id
LEFT JOIN friendslist AS friend ON friend.friend_id = users.id
WHERE users.id NOT IN(SELECT users.id FROM users LEFT JOIN friendslist ON friendslist.user_id = users.id
LEFT JOIN friendslist AS friend ON friend.friend_id = users.id WHERE users.id != 6 AND friendslist.user_id != 6)
OR friendslist.user_id IS NULL AND users.id != 6
GROUP BY users.id;
