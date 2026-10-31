Development Guide
================

This page explains how the Sticky Notes application is organized and how to
make changes to the project.

Project Structure
-----------------

The project contains the following main components:

* ``sticky_notes/`` contains the Django project settings and URL configuration.
* ``notes/`` contains the sticky note application, including models, forms,
  views, URLs, and automated tests.
* ``templates/`` contains the HTML templates used to display the application.
* ``docs/`` contains the Sphinx documentation.
* ``diagrams/`` contains the project diagrams.

Database
--------

The application uses SQLite for local development. The ``StickyNote`` model
stores each note's title and content.

When database models change, create and apply migrations:

::

   python manage.py makemigrations
   python manage.py migrate

Testing
-------

Run the automated Django tests with:

::

   python manage.py test

Documentation
-------------

Build the Sphinx documentation with:

::

   python -m sphinx -b html docs docs/_build/html

Open ``docs/_build/html/index.html`` in a browser to view the generated
documentation.

Development Notes
-----------------

Keep secret keys and local environment settings out of version control.
Use Git branches to separate documentation and container-related changes
from the main application branch.
