
CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    date_of_birth TEXT,
    education TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    country TEXT
);



-- CREATE TABLE questions(
--     questions_id INTEGER PRIMARY KEY AUTOINCREMENT,
--     user_id INTEGER,
--     created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
--     q_1 TEXT,
--     q_2 TEXT,
--     q_3 TEXT,
--     q_4 TEXT,
--     q_5 TEXT,
--     q_6 TEXT,
--     q_7 TEXT,
--     q_8 TEXT,
--     q_9 TEXT,
--     q_10 TEXT,
--     q_11 TEXT,
--     q_12 TEXT,
--     q_13 TEXT,
--     q_14 TEXT,
--     q_15 TEXT,
--     FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
-- );

CREATE TABLE questions(
    questions_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    questions TEXT,
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
    non_technical_skills TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);

CREATE TABLE pastjobs(
    past_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    company TEXT,
    position TEXT,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
  
);

