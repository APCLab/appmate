AppMate
===============================================================================

Appmate is your friend.


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


Activate Model
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    # edit the app/models.py
    python manage.py makemigrations app
    python manage.py migrate app


Run
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

::

    python manage.py runserver

And, enjoy!


Add a New Model
----------------------------------------------------------------------

#. Define your model(s) in ``app/models.py``.

#. Enable them in admin panel: ``app/admin.py``.

#. Create a serializer for rest framework in ``app/serializers.py``.

#. Show them in views: ``app/views.py``.

#. Register to rest framework router in ``core/urls.py``.

#. Do the database migration::

   python manage.py makemigrations app
   python manage.py migrate app
