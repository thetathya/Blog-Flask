from flask import Flask,render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'c08e4cb4224a825ca0145b5f52ff48e1'

posts = [
	{
		'author': 'XYZ',
		'title': 'Learning 1.5x Speed',
		'content': 'First post content',
		'date_posted': 'April 20,2018'
	},
	{
		'author': 'ABCD',
		'title': 'Learning 1.25x Speed',
		'content': 'Second post content',
		'date_posted': 'April 21,2018'
	}
]

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html',posts=posts)

@app.route("/about")
def about():
	return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@blog.com' and form.password.data == 'password':
			flash(f'You have logged in.', 'success')
			return redirect(url_for('home'))
		else:
			flash(f'Login unsuccessfull', 'danger')
	return render_template('login.html', title='Login', form=form)