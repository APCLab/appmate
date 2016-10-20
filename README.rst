AppMate
===============================================================================

Appmate is your friend.

Python support: 3.4 and 3.5


Quick Start
----------------------------------------------------------------------

Requirements
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    pip install -r ./requirements.txt


Create DataBase
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    python manage.py migrate
    python manage.py createsuperuser


Development Setup
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    npm install


    npm install -g webpack
    webpack  # or webpack --progress --colors --watch



Run the Development Server
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    python manage.py runserver

And, enjoy!


Add a New Model
----------------------------------------------------------------------

#. Define your model(s) in ``app/appmate.yml``.

#. Compile the Jinja templates::

    (cd app && make)

#. Do the database migration::

    python manage.py makemigrations app
    python manage.py migrate app
