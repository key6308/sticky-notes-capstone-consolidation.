# Sticky Notes App — Capstone Consolidation

This is my Django Sticky Notes project. I made it so a user can add notes, view them, edit them, and delete them. This project is for learning and demonstration, not a production deployment.

## What is included?

- Django app for creating, viewing, editing, and deleting sticky notes
- SQLite database for local development
- `requirements.txt` to install packages
- `.gitignore` to avoid uploading generated files and secrets
- Sphinx documentation source in `docs/`
- Docker setup with `Dockerfile` and `docker-compose.yml`
- UML diagrams in `diagrams/`

## Run it with Python

You need Python 3.10 or newer installed.

1. Open a terminal in this project folder.
2. Create a virtual environment:

   **Windows**
   ```powershell
   py -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

   **macOS/Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the packages:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Set up the database:

   ```bash
   python manage.py migrate
   ```

5. Start the website:

   ```bash
   python manage.py runserver
   ```

6. Open `http://127.0.0.1:8000/` in your browser.

## Run the tests

```bash
python manage.py test
```

## Build the Sphinx documentation

Install the requirements first, then run:

```bash
python -m sphinx -b html docs docs/_build/html
```

Open `docs/_build/html/index.html` to view the generated documentation.

## Run it with Docker

Install Docker Desktop first. Then, from this project folder, run:

```bash
docker compose up --build
```

Open `http://127.0.0.1:8000/` in your browser. To stop the app, press `Ctrl+C` in the terminal.

## Git branches required for the assignment

The assignment asks for a `docs` branch and a `container` branch, then both branches should be merged into `main`. Follow the `GITHUB_STEPS.md` file for the GitHub upload steps.

## Notes about settings

The project uses a local SQLite database by default. Do not add passwords, access tokens, or your real production secret key to a public repository. The Docker configuration is for local development, not a production server.
