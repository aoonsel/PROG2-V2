import sqlite3
from os import path

connection_path = path.join('data', 'workouts.db')
query_base = 'SELECT * FROM workouts WHERE excercise = {} ORDER BY "{}" DESC, "date" LIMIT 1'
insert_base = 'INSERT INTO workouts (date, excercise, reps, weight, volume) VALUES (?, ?, ?, ?, ?)'

query_id_to_col_name = {0: 'weight', 1: 'reps', 2: 'volume'}

def save_workout(date, exercise, reps, weight, volume):
    connection = sqlite3.connect(path.join('data', 'workouts.db'))
    cursor = connection.cursor()

    cursor.execute(insert_base, (date, exercise, reps, weight, volume))

    connection.commit()
    connection.close()

def get_workout_for_query(query_id, excercise):
    connection = sqlite3.connect(connection_path)
    cursor = connection.cursor()

    query = query_base.format(excercise, query_id_to_col_name[query_id])
    result = cursor.execute(query)
    
    return result.fetchmany()

def get_workouts():
    connection = sqlite3.connect(connection_path)
    cursor = connection.cursor()

    result = cursor.execute('SELECT * FROM workouts')
    
    return result.fetchall()
