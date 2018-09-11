# app.py 



from flask import Flask, request, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://usr:pass@localhost:5432/flaskmovie'
app.debug = True
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(80), unique = True)
	email = db.Column(db.String(120), unique = True)

	def __init__(self,username,email):
		self.username = username
		self.email = email

	def __repr__(self):
		return '<User %r>' % self.username

@app.route('/')
def index():
	return render_template('add_user.html')

@app.route('/post_user', methods=['Post'])
def post_user():
	user = User(request.form['Username'],request.form['Email'])
	db.session.add(user)
	db.session.commit()
	return redirect(url_for('index'))



	if __name__ == "__main__":
		app.run()



