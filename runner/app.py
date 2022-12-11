from data.data_access import save_workout, get_workouts
from flask import Flask, render_template, redirect, request
from os.path import abspath

app = Flask('runner', template_folder=abspath('templates'))

excercises = {0: 'Squat', 1: 'Bench Press', 2: 'Deadlift'}
queries = {0: 'Highest Weight', 1: 'Highest Reps', 2: 'Highest Volume'}

@app.route('/')
def home():
    return render_template('index.html', excercises=excercises, queries=queries)

@app.route('/save', methods=['POST'])
def save():
    date = request.form['date']
    excercise = request.form.get('excercise')
    reps = int(request.form['reps'])
    weight = float(request.form['weight'])
    volume = reps * weight

    save_workout(date, excercise, reps, weight, volume)
    
    return redirect('/')

@app.route('/api/data', methods=['GET'])
def data():
    workouts = []
    for workout in get_workouts():
        workouts.append({
        'date': workout[1],
        'excercise': excercises[workout[2]],
        'weight': workout[3],
        'reps': workout[4],
        'volume': workout[5]})

    return {'data': workouts}

if __name__ == "__main__":
    app.run(debug=True)
