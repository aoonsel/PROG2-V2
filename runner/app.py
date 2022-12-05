from data.data_access import save_workout, get_workouts
from flask import Flask, render_template, redirect, request
from os.path import abspath

app = Flask('runner', template_folder=abspath('templates'))

excercises = {0: 'Squat', 1: 'Bench Press', 2: 'Deadlift'}

@app.route('/')
def home():
    return render_template('index.html', excercises=excercises)

@app.route('/save', methods=['POST'])
def save():
    date = request.form['date']
    excercise = request.form.get('excercise')
    reps = request.form['reps']
    weight = request.form['weight']

    save_workout(date, excercise, reps, weight)
    
    return redirect('/')

@app.route('/api/data', methods=['GET'])
def data():
    workouts = []
    for workout in get_workouts():
        workouts.append({
        'date': workout[1],
        'excercise': excercises[workout[2]],
        'weight': workout[3],
        'reps': workout[4]})

    return {'data': workouts}

if __name__ == "__main__":
    app.run(debug=True)
