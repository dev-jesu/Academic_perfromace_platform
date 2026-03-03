# Academic Performance Assessment Platform

A comprehensive platform for college academic performance assessment, mentorship tracking, and results management.

## Tech Stack
- **Backend**: FastAPI (Python 3.12+)
- **Database**: Supabase (PostgreSQL)
- **Frontend**: React (Vite)
- **State Management**: Zustand
- **API Client**: Axios with JWT Interceptors

## Project Structure
```text
/
├── backend/                # FastAPI Backend
│   ├── app/                # Application Logic
│   │   ├── routers/        # API Routes (Auth, Students, etc.)
│   │   ├── models.py       # Pydantic Schemas
│   │   ├── database.py     # Supabase Client Init
│   │   ├── init_db.py      # Schema Initialization Script
│   │   ├── seed_db.py      # Sample Data Seeding Script
│   │   └── main.py         # App Entry Point
│   └── requirements.txt    # Python Dependencies
├── frontend/               # React (Vite) Frontend
│   ├── src/
│   │   ├── api/            # Axios Client
│   │   ├── components/     # UI Components (Dashboard, StudentList)
│   │   ├── store/          # Zustand Global State
│   │   └── App.jsx         # Routing & Protected Routes
│   └── package.json        # Frontend Dependencies
├── docs/                   # Documentation & Diagrams
├── .env.example            # Environment Template
└── README.md               # Project Overview
```

## Installation & Setup

### 1. Prerequisites
- Python 3.9+ and Node.js (Latest LTS)
- Supabase Account & Project

### 2. Backend Setup
1. **Clone & Navigate**:
   ```bash
   git clone <your-repo-url>
   cd miniProject
   ```

2. **Virtual Environment**:
   ```bash
   python -m venv venv
   # Windows:
   .\venv\Scripts\activate
   # Linux/Mac:
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r backend/requirements.txt
   ```

4. **Environment Variables**:
   Create a `.env` file in the root based on `.env.example`.

5. **Initialize Database**:
   ```bash
   python backend/app/init_db.py
   ```

6. **Seed Database (Optional)**:
   If you have the `seed_db.py` script locally:
   ```bash
   python backend/app/seed_db.py
   ```

7. **Run Server**:
   ```bash
   uvicorn backend.app.main:app --reload
   ```

### 3. Frontend Setup
1. **Navigate & Install**:
   ```bash
   cd frontend
   npm install
   ```

2. **Run Dev Server**:
   ```bash
   npm run dev
   ```

## Documentation
Refer to the `docs/` folder for:
- [DB Schema](file:///docs/db_schema.md)
- [Tech Stack Justification](file:///docs/tech_stack.md)
- [UI Generation Prompt](file:///docs/ui_prompt.md)

## Branching Strategy
- `main`: Stable production code.
- `dev`: Active integration.
- `feature/*`: Specific feature branches.
