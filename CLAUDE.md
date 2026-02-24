# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Architecture

This is a FastAPI application following **clean architecture** with strict layered separation:

- **Router → Service → Repository** (strict downward dependency)
- **Router** (`src/router/`): HTTP layer - handles requests/responses, validation, and error codes
- **Service** (`src/service/`): Business logic - loan calculations, amortization schedules, coordination between repositories
- **Repository** (`src/repository/`): Data access - SQLModel-based database operations
- **Model** (`src/model/`): SQLModel (DB tables) and Pydantic (API schemas)

The database is initialized in `src/service/database_service.py` with `init(db_uri)` and manages a global ENGINE for SQLModel sessions.

## Domain Model

- **Users** and **Loans** have a many-to-many relationship via the **UserLoan** join table
- Loans can be shared between multiple users
- Core business logic includes loan amortization calculations and monthly summaries

## Development Commands

### Setup
```bash
# Install Python 3.12.4
pyenv install 3.12.4
pyenv local 3.12.4
pyenv exec python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Environment
Create `.env` file:
```
DB_URI=sqlite:///database.db
```

### Running
```bash
# Start development server with auto-reload
uvicorn src.main:app --reload

# API documentation available at http://127.0.0.1:8000/docs
```

### Testing
```bash
# Run all tests (unit + integration)
pytest tests

# Run specific test file
pytest tests/unit/service/test_loan_service.py

# Run tests in a specific directory
pytest tests/unit
pytest tests/integration
```

Test structure:
- `tests/unit/` - Unit tests for routers and services (uses mocks via pytest-mock)
- `tests/integration/` - Integration tests for repositories (uses real database)

### Code Quality
```bash
# Format code
ruff format

# Lint code
ruff check
```

### Docker
```bash
# Run via Docker Compose (port 8000)
docker compose up
```

## CI/CD

CircleCI is configured with workflows:
- **main branch** → deploys to dev environment (Heroku)
- **tags `v*`** → deploys to stage environment
- **tags `rel-*`** → deploys to prod environment

Tests run via `python -m pytest` in CircleCI.


See @README.md for project overview
See @docs/api-patterns.md for API conventions


-----

# Project: py-api

This project is structured as a modular, layered FastAPI application, following clean architecture principles to ensure maintainability and testability. It demonstrates my understanding of clean, well-built code. Feel free to copy / learn. Enjoy!

## Code Style

- Ruff default configuration

### Setup

- See @README.md for setup instructions

## Architecture

- See @README.md for architecture details

## Important Notes

- NEVER commit .env files
