import os
import psycopg2
from dotenv import load_dotenv

# Load .env from the root directory
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '..', '.env'))

SQL_SCHEMA = """
CREATE TABLE IF NOT EXISTS student (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    major VARCHAR(100),
    cgpa NUMERIC(3,2)
);

CREATE TABLE IF NOT EXISTS course (
    id SERIAL PRIMARY KEY,
    code VARCHAR(10) UNIQUE NOT NULL,
    title VARCHAR(200) NOT NULL,
    credits INT NOT NULL
);

CREATE TABLE IF NOT EXISTS enrollment (
    id SERIAL PRIMARY KEY,
    student_id INT REFERENCES student(id),
    course_id INT REFERENCES course(id),
    semester VARCHAR(20),
    grade NUMERIC(4,2)
);

CREATE TABLE IF NOT EXISTS mentor (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS mentorship (
    id SERIAL PRIMARY KEY,
    mentor_id INT REFERENCES mentor(id),
    student_id INT REFERENCES student(id),
    start_date DATE,
    end_date DATE
);

CREATE TABLE IF NOT EXISTS assessment (
    id SERIAL PRIMARY KEY,
    enrollment_id INT REFERENCES enrollment(id),
    type VARCHAR(50),
    score NUMERIC(5,2),
    date_taken DATE
);
"""

def init_db():
    db_url = os.environ.get("DATABASE_URL")
    if not db_url:
        print("Error: DATABASE_URL not found.")
        return

    try:
        print(f"Connecting to database...")
        conn = psycopg2.connect(db_url)
        conn.autocommit = True
        cur = conn.cursor()
        
        print("Executing schema initialization...")
        cur.execute(SQL_SCHEMA)
        
        print("Database initialized successfully!")
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Failed to initialize database: {e}")

if __name__ == "__main__":
    init_db()
