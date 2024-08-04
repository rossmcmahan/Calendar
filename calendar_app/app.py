from flask import Flask, render_template, request, redirect, url_for
import calendar
import datetime

app = Flask(__name__)

tasks = {}

@app.route('/', methods=['GET', 'POST'])
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
			if task_date not in tasks:
				tasks[task_date] = []
			tasks[task_date].append(task)

	cal = calendar.HTMLCalendar(calendar.SUNDAY)
	month_calendar = cal.formatmonth(year, month)

	# Highlight the selected day
	month_calendar = month_calendar.replace(f'>{day}<', f' class="selected-day">{day}<')

	task_date = f"{year}-{month}-{day}"
	day_tasks = tasks.get(task_date, [])

	return render_template('calendar.html', calendar=month_calendar, year=year, month=month, day=day, tasks=day_tasks)


if __name__ == '__main__':
	app.run()