AppMate
===============================================================================

Appmate is your friend.


Requirements
----------------------------------------------------------------------

::

    pip install -r ./requirements.txt


Create DataBase
----------------------------------------------------------------------

::

    python manage.py migrate
    python manage.py createsuperuser



Activate Model
----------------------------------------------------------------------

::

    # edit the app/models.py
    python manage.py makemigrations app
    python manage.py migrate app


Run
----------------------------------------------------------------------

::

    python manage.py runserver


And, enjoy!

