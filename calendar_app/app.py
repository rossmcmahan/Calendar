from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import calendar
import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

users = {}
tasks = {}

class User(UserMixin):
	def __init__(self, id, username, password):
		self.id = id
		self.username = username
		self.password = password
users = {
    "1": User(id = "1",
              username = "debug_user",
              password = "debug_password")
}

@login_manager.user_loader
def load_user(user_id):
	return users.get(user_id)

@app.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		if username in [user.username for user in users.values()]:
			flash('Username already exists.')
			return redirect(url_for('register'))
		user_id = str(len(users)+1)
		users[user_id] = User(user_id, username, password)
		flash('Registration successful. Please log in.')
		return redirect(url_for('login'))
	return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		user = next((user for user in users.values() if user.username == username and user.password == password), None)
		if user:
			login_user(user)
			return redirect(url_for('index'))
		flash('Invalid username or password.')
	return render_template('login.html')
@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('login'))

@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
	now = datetime.datetime.now()
	year = now.year
	month = now.month
	day = now.day

	if request.method == 'POST':
		year = int(request.form.get('year', year))
		month = int(request.form.get('month', month))
		day = int(request.form.get('day', day))
		task_date = f"{year}-{month}-{day}"

		if 'task' in request.form:
			task = request.form.get('task')
			if current_user.id not in tasks:
				tasks[current_user.id] = {}
			if task_date not in tasks[current_user.id]:
				tasks[current_user.id][task_date] = []
			tasks[current_user.id][task_date].append(task)
		elif 'delete_task' in request.form:
			task_to_delete = request.form.get('delete_task')
			if task_date in tasks.get(current_user.id, {}):
				tasks[current_user.id][task_date].remove(task_to_delete)
				if not tasks[current_user.id][task_date]:
					del tasks[current_user.id][task_date]

	cal = calendar.HTMLCalendar(calendar.SUNDAY)
	month_calendar = cal.formatmonth(year, month)

	# Highlight the selected day
	month_calendar = month_calendar.replace(f'>{day}<', f' class="selected-day">{day}<')

	task_date = f"{year}-{month}-{day}"
	day_tasks = tasks.get(current_user, {}).get(task_date, [])

	return render_template('calendar.html', calendar=month_calendar, year=year, month=month, day=day, tasks=day_tasks)


if __name__ == '__main__':
	app.run(debug = True)