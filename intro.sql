CREATE TABLE users(
    user_id INTEGER PRIMARY KEY,
    full_name TEXT NOT NULL,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL,
    age INTEGER
);

CREATE TABLE questions(
    questions_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    q_1 TEXT,
    q_2 TEXT,
    q_3 TEXT,
    q_4 TEXT,
    q_5 TEXT,
    q_6 TEXT,
    q_7 TEXT,
    q_8 TEXT,
    q_9 TEXT,
    q_10 TEXT,
    q_11 TEXT,
    q_12 TEXT,
    q_13 TEXT,
    q_14 TEXT,
    q_15 TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE personal_info (
    personal_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER ,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    date_of_birth TEXT NOT NULL,
    education TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    country TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE department (
    department_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER ,
    department TEXT NOT NULL CHECK (department IN ('IT', 'Sales')),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE skills(
    skills_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER ,
    technical_skills TEXT,
    non_technical_skill TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);