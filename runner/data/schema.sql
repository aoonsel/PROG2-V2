DROP TABLE IF EXISTS workouts;

CREATE TABLE workouts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    excercise INTEGER NOT NULL,
    weight INTEGER NOT NULL,
    reps INTEGER NOT NULL
);
