# py-api

### Project Structure & Architecture

This project is structured as a modular, layered FastAPI application, following clean architecture principles to ensure maintainability and testability. It demonstrates my understanding of clean, well-built code. Feel free to copy / learn. Enjoy!

#### 🏗️ Layered Architecture

The codebase is organized into distinct layers within `src/`:

*   **Entry Point (`src/main.py`)**: Initializes the FastAPI application, logging, and database connections.
*   **Routers (`src/router/`)**: The "Controller" layer. Defines API endpoints, handles HTTP requests/responses, and performs basic validation.
*   **Services (`src/service/`)**: The "Business Logic" layer. Contains core logic (e.g., loan calculations) and coordinates between repositories.
*   **Repositories (`src/repository/`)**: The "Data Access" layer. Uses `SQLModel` to interact with the database, isolating data persistence logic.
*   **Models (`src/model/`)**: Defines data structures using `SQLModel` (for DB tables) and `Pydantic` (for API schemas).
*   **Utilities (`src/util/`)**: Shared helper functions (e.g., UUID validation).

#### 🛠️ Design Principles

1.  **Separation of Concerns**: Each layer has a specific responsibility (HTTP, Logic, Data).
2.  **Dependency Flow**: Strict downward dependency: **Router → Service → Repository**.
3.  **Modern Stack**: Leverages **FastAPI**, **SQLModel**, **Pytest** for testing, and **Ruff** for linting/formatting.
4.  **Configuration**: Environment-based configuration via `.env` files.
5.  **DevOps Ready**: Includes **Docker** and **Docker Compose** configurations for containerization.


##### Setup
    # clone repo
    git clone https://github.com/scranth/py-api.git

    # install python
    pyenv local 3.12.4
    pyenv exec python -m venv .venv
    source .venv/bin/activate  (mac)

    # install requirements
    pip install -r requirements.txt

##### Use
    # start
    uvicorn src.main:app --reload

    # create .env file with the following
    DB_URI=sqlite:///database.db

    # test
    pytest tests

    # format
    ruff format

    # lint
    ruff check

    # docker
    docker compose up

    # docs
    http://127.0.0.1:8000/docs

### License

[The MIT License](http://opensource.org/licenses/MIT)
