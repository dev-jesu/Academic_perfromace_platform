# Academic Performance Assessment Platform

A comprehensive platform for college academic performance assessment, mentorship tracking, and results management.

## Tech Stack
- **Backend**: FastAPI (Python)
- **Database**: Supabase (PostgreSQL)
- **Frontend**: (Phase 2 - Planned)
- **Deployment**: (Phase 3 - Planned)

## Project Structure
```text
/
├── backend/            # FastAPI Backend
│   ├── app/            # Application Logic
│   └── requirements.txt # Python Dependencies
├── docs/               # Documentation & Diagrams
│   ├── tech_stack.md   # Justification & System Flow
│   ├── db_schema.md    # ER Diagram & SQL
│   └── ui_prompt.md    # Wireframe Prompt for Stitch
├── .env.example        # Environment Template
├── .gitignore          # Git Exclusions
└── README.md           # Project Overview
```

## Installation & Setup

### Prerequisites
- Python 3.9+
- Pip
- Supabase Account

### Backend Setup
1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd miniProject
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r backend/requirements.txt
   ```

4. **Environment Variables**:
   Copy `.env.example` to `.env` and fill in your Supabase credentials.
   ```bash
   cp .env.example .env
   ```

5. **Run the server**:
   ```bash
   uvicorn backend.app.main:app --reload
   ```
   The API will be available at [http://localhost:8000](http://localhost:8000).
   Swagger documentation is at [http://localhost:8000/docs](http://localhost:8000/docs).

## Branching Strategy
- `main`: Production-ready code.
- `dev`: Integration branch for features.
- `feature/*`: Specific feature development branches.

## Documentation
Refer to the `docs/` folder for detailed architectural and design documentation.
