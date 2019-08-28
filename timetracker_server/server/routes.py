from server import app, db
from flask_httpauth import HTTPBasicAuth
from server.models import User, Timestamp
from flask import request, abort, jsonify, url_for, g
from datetime import datetime

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
	user = User.query.filter_by(username=username).first()
	if not user or not user.verify_password(password):
		return False
	g.user = user
	return True

@app.route('/api/users/<int:id>')
def get_user(id):
	user = User.query.get(id)
	if not user:
		abort(400)
	return jsonify({'username': user.username})

@app.route('/api/users', methods=['POST'])
def new_user():
	username = request.json.get('username')
	email = request.json.get('email')
	password = request.json.get('password')
	if username is None or password is None or email is None:
		abort(400) # missing arguments
	if User.query.filter_by(username=username).first() is not None \
		or User.query.filter_by(email=email).first() is not None:
		abort(400) # existing user
	user = User(username=username, email=email)
	user.hash_password(password)
	db.session.add(user)
	db.session.commit()
	return jsonify({ 'username': user.username, 'email': user.email }), 201, {'Location': url_for('get_user', id=user.id, _external=True)}

@app.route('/api/users/<int:id>/timestamps', methods=['GET', 'POST'])
@auth.login_required
def timestamps(id):
	if g.user.id != id:
		abort(500) # existing user

	if request.method == 'GET':
		#extract timeframe query data if exists
		start = request.args.get('start')
		stop = request.args.get('stop')

		if not start and not stop:
			#return all
			return jsonify({'timestamps': [str(timestamp) for timestamp in g.user.timestamps]})
		else:
			#extract bounds and query DB
			fstring = '%y-%m-%dT%H-%M-%S'
			start_datetime = datetime.strptime(start, fstring) if start else datetime.min()
			stop_datetime = datetime.strptime(stop, fstring) if stop else datetime.now()

			results = g.user.timestamps.filter(Timestamp.timestamp >= start_datetime, Timestamp.timestamp <= stop_datetime)
			return jsonify({'timestamps': [str(timestamp) for timestamp in results]})
	elif request.method == 'POST':
		time = request.json.get('timestamp', datetime.now())

		t = Timestamp(stamp_type=request.json.get('stamp_type'), timestamp=time,\
			user=g.user)
		db.session.add(t)
		db.session.commit()
		return jsonify({ 'stamp_type': request.json.get('stamp_type'), 'time': time }), 201, {'Location': url_for('timestamps', id=id)}
	


