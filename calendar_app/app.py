from flask import Flask, render_template, request
import calendar
import datetime

app = Flask(__name__)

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

	cal = calendar.HTMLCalendar(calendar.SUNDAY)
	month_calendar = cal.formatmonth(year, month)

	# Highlight the selected day
	month_calendar = month_calendar.replace(f'>{day}<', f' class="selected-day">{day}<')

	return render_template('calendar.html', calendar=month_calendar, year=year, month=month, day=day)


if __name__ == '__main__':
	app.run()