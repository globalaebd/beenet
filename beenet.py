from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
	return "We are down for maintenance. BEE Net @ www.globalaebd.org/BEE"

@app.route("/api")
def callAPI():
	from api import doAPI
	theResponse=doAPI.call()
	return theResponse

@app.route("/welcome")
def main_user_interface():
	entries=[]
	#return "Yup works"
	#return render_template("TEMP.html")
	return render_template('main_user_interface.html', entries=entries)

@app.route("/login",methods=['GET','POST'])
def login():
	if request.method == "POST":
		if request.form['username']!= "username":
			error = "Invalid username"
		elif request.form['password']!="password":
			error = "Invalide password"
		else: #The user is authenticated
			session['logged_in']=True
			flash("You were logged in")
			return redirect(url_for("main_user_interface"))
	return render_template("login.html",error=error)

@app.route("/register")
def register():
	return "THIS IS REGISTER"

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('You were logged out')
	return redirect(url_for('show_entries'))

if __name__ == "__main__":
	app.run()