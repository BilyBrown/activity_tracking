-- db/schema.sql

CREATE TABLE IF NOT EXISTS exercises (
	exercise_uid        INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	name                TEXT NOT NULL UNIQUE -- normal name, deadlift, kb swing, etc.
);

CREATE TABLE IF NOT EXISTS activities (
	activity_uid        INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	activity_date       DATE NOT NULL,
	exercise_id            INTEGER NOT NULL,
        reps                INTEGER,
        sets                INTEGER,
        mass_kg            REAL,
        rest_sec            INTEGER,
        duration_min        REAL,
        distance_km         REAL,
        notes               TEXT,

	FOREIGN KEY (exercise_id) REFERENCES exercises(exercise_uid)
);

