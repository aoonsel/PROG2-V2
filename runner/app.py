from data_access import save_activity
from util import to_seconds, to_minutes, to_pace
from flask import Flask, render_template, redirect, request
from os.path import abspath

app = Flask('runner', template_folder=abspath('templates'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save():
    date = request.form['date']
    distance = float(request.form['distance'])
    hours = int(request.form['hours'])
    minutes = int(request.form['minutes'])
    seconds = int(request.form['seconds'])
    
    duration_in_s = to_seconds(hours, minutes, seconds)
    duration_in_min = to_minutes(hours, minutes, seconds)
    pace = to_pace(distance, duration_in_min)

    save_activity({'date': date, 'distance': distance, 'duration': duration_in_s, 'pace': pace})
    
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
