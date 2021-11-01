from . import db
from datetime import date, datetime
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__='users' # good practice to specify table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
	#password is never stored in the DB, an encrypted password is stored
	# the storage should be at least 255 chars long
    password_hash = db.Column(db.String(255), nullable=False)
    number = db.Column(db.Integer,index=True, unique=True, nullable=False)
    address = db.Column(db.String(100), index=True, nullable=False)
    # relation to call user.comments and comment.created_by
    comments = db.relationship('Comment', backref='user')



class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), index=True, unique=True, nullable=False)
    venue = db.Column(db.String(80), index=True, unique=False, nullable=False)
    event_date = db.Column(db.String(20), index=True, unique=False, nullable=False)
    description = db.Column(db.String(200), index=True, unique=False, nullable=False)
    category = db.Column(db.String(80), index=True, unique=False, nullable=False)
    image = db.Column(db.String(400), index=True, unique=True, nullable=False)
    price = db.Column(db.String(10), index=True, unique=False, nullable=False)
    status = db.Column(db.String(20), index=True, unique=False, nullable=False)
    avai_tickets = db.Column(db.Integer,index=True, unique=False, nullable=False)
    # ... Create the Comments db.relationship
	# relation to call destination.comments and comment.destination
    comments = db.relationship('Comment', backref='event')

    
	
    def __repr__(self): #string print method
        return "<Name: {}>".format(self.name)

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())
    #add the foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))


    def __repr__(self):
        return "<Comment: {}>".format(self.text)

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    date_booked = db.Column(db.DateTime, default=datetime.now())
    #add the foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))


    def __repr__(self):
        return "<Comment: {}>".format(self.text)