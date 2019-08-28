from server import db
from datetime import datetime
from passlib.apps import custom_app_context as pwd_context

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))
	timestamps = db.relationship('Timestamp', backref='user', lazy='dynamic')

	def hash_password(self, password):
		self.password_hash = pwd_context.encrypt(password)

	def verify_password(self, password):
		return pwd_context.verify(password, self.password_hash)

	def __repr__(self):
		return '<User {}>'.format(self.username)

class Timestamp(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	stamp_type = db.Column(db.String(140))
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return '<Timestamp: {} @ {}>'.format(self.stamp_type, self.timestamp)