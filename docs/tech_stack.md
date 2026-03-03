# Tech Stack & Architecture

## Justification
- **FastAPI**: High‑performance Python web framework, easy to write async endpoints, automatic OpenAPI docs, and great for building RESTful APIs.
- **Supabase**: Managed PostgreSQL with built‑in authentication, real‑time, storage and auto‑generated client libraries. It provides a serverless backend that pairs well with FastAPI for data persistence.
- **Why not MERN/PERN**: The project focuses on a lightweight backend API and a PostgreSQL database. FastAPI + Supabase reduces the overhead of managing a separate Node.js server and offers better type safety with Python.

## System Flow Diagram
```mermaid
flowchart TD
    A[Client (Future Frontend)] -->|HTTP API| B[FastAPI Backend]
    B -->|SQL Queries| C[Supabase PostgreSQL]
    C -->|Auth & Real‑time| D[Supabase Auth & Realtime]
    B -->|Auth Checks| D
    B -->|File Storage| E[Supabase Storage]
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style C fill:#bfb,stroke:#333,stroke-width:2px
    style D fill:#ffb,stroke:#333,stroke-width:2px
    style E fill:#fbf,stroke:#333,stroke-width:2px
```

The diagram illustrates the high‑level interactions between the client, FastAPI, and Supabase services.
