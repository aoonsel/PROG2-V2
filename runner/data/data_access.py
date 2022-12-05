import sqlite3
from os import path

def save_workout(date, exercise, reps, weight):
    connection = sqlite3.connect(path.join('data', 'workouts.db'))
    cursor = connection.cursor()

    cursor.execute('INSERT INTO workouts (date, excercise, reps, weight) VALUES (?, ?, ?, ?)',
                    (date, exercise, reps, weight)
                  )

    connection.commit()
    connection.close()

def get_workouts():
    connection = sqlite3.connect(path.join('data', 'workouts.db'))
    cursor = connection.cursor()

    result = cursor.execute('SELECT * FROM workouts')
    
    return result.fetchall()
