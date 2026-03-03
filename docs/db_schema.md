# DB Schema & ER Diagram

## ER Diagram (for erd.io)
```erDiagram
    STUDENT {
        int id PK "Primary Key"
        varchar name
        varchar email "Unique"
        varchar major
        float cgpa
    }
    COURSE {
        int id PK
        varchar code "Unique"
        varchar title
        int credits
    }
    ENROLLMENT {
        int id PK
        int student_id FK "References STUDENT.id"
        int course_id FK "References COURSE.id"
        varchar semester
        float grade
    }
    MENTOR {
        int id PK
        varchar name
        varchar email "Unique"
    }
    MENTORSHIP {
        int id PK
        int mentor_id FK "References MENTOR.id"
        int student_id FK "References STUDENT.id"
        date start_date
        date end_date
    }
    ASSESSMENT {
        int id PK
        int enrollment_id FK "References ENROLLMENT.id"
        varchar type "Exam, Assignment, Project"
        float score
        date date_taken
    }
    STUDENT ||--o{ ENROLLMENT : "enrolls in"
    COURSE ||--o{ ENROLLMENT : "has enrollments"
    STUDENT ||--o{ MENTORSHIP : "assigned to"
    MENTOR ||--o{ MENTORSHIP : "mentors"
    ENROLLMENT ||--o{ ASSESSMENT : "has assessments"
```

## Table Definitions (PostgreSQL)
```sql
CREATE TABLE student (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    major VARCHAR(100),
    cgpa NUMERIC(3,2)
);

CREATE TABLE course (
    id SERIAL PRIMARY KEY,
    code VARCHAR(10) UNIQUE NOT NULL,
    title VARCHAR(200) NOT NULL,
    credits INT NOT NULL
);

CREATE TABLE enrollment (
    id SERIAL PRIMARY KEY,
    student_id INT REFERENCES student(id),
    course_id INT REFERENCES course(id),
    semester VARCHAR(20),
    grade NUMERIC(4,2)
);

CREATE TABLE mentor (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL
);

CREATE TABLE mentorship (
    id SERIAL PRIMARY KEY,
    mentor_id INT REFERENCES mentor(id),
    student_id INT REFERENCES student(id),
    start_date DATE,
    end_date DATE
);

CREATE TABLE assessment (
    id SERIAL PRIMARY KEY,
    enrollment_id INT REFERENCES enrollment(id),
    type VARCHAR(50),
    score NUMERIC(5,2),
    date_taken DATE
);
```
