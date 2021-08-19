from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required

import datetime
import calendar as cal

calendar = Blueprint('calendar', __name__)
days = []

@calendar.route('/calendar')
@login_required
def view():
    days = fill_days(datetime.date.today())
    return render_template('calendar.html', data=days)

def fill_days(some_date):
    days = []

    #days in month
    num_days = cal.monthrange(some_date.year, some_date.month)[1] 

    month_start_day = datetime.datetime(some_date.year, some_date.month, 1)
    month_start_day_weekday = month_start_day.weekday()

    #last month
    for last_month_day_weekday in range(0,month_start_day_weekday):
        day = [
            0,
            cal.day_name[last_month_day_weekday],
            False # = this month
        ]
        days.append(day)

    #this month
    for this_month_day in range(0,num_days):
        cur_weekday = (month_start_day_weekday + this_month_day) % 7
        day = [
            this_month_day,
            cal.day_name[cur_weekday],
            True # = this month
        ]
        days.append(day)

    #next month
    this_month_lastday_weekday = (month_start_day_weekday + num_days) % 7
    for next_month_day_weekday in range(this_month_lastday_weekday, 7):
        day = [
            0,
            cal.day_name[next_month_day_weekday],
            False
        ]
        days.append(day)
    
    return days

    
    



    
    

