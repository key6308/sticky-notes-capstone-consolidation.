Setup and running the project
=============================

Install dependencies
--------------------

Create and activate a virtual environment, then run::

   python -m pip install -r requirements.txt

Prepare the database
--------------------

Run::

   python manage.py migrate

Start the development server
----------------------------

Run::

   python manage.py runserver

Then open ``http://127.0.0.1:8000/`` in a browser.

Docker
------

With Docker Desktop running, use::

   docker compose up --build

Then open ``http://127.0.0.1:8000/``.
