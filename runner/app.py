from data.data_access import save_workout
from flask import Flask, render_template, redirect, request
from os.path import abspath

app = Flask('runner', template_folder=abspath('templates'))

workouts = {0: 'Squat', 1: 'Bench Press', 2: 'Deadlift'}

@app.route('/')
def home():
    return render_template('index.html', workouts=workouts)

@app.route('/save', methods=['POST'])
def save():
    date = request.form['date']
    excercise = request.form.get('excercise')
    reps = request.form['reps']
    weight = request.form['weight']

    save_workout(date, excercise, reps, weight)
    
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
