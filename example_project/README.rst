#######################
Contact Demo Project
#######################

About
=====
This project serves two purposes:

- It's a quick demo of django-contact for people who wish to try it out.
- It's an easy way for contributors to the project to have both django-contact,
  and a project that uses it.

The rest of the README will assume that you want to set up the test project in
order to work on django-contact itself.

Prerequisites
=============

- python (either 3.7, or 3.x).
- pyenv makes it easy to manage your virtualenvs.

Installation
============

Clone this code into your project folder::

	git clone https://github.com/balexander85/django-contact.git

Create a virtual python environment for the project. The use of pyenv
is strongly recommended::

	cd django-contact/example_project
	pyenv virtualenv -v 3.*.* contact-env
	pyenv local contact-env


**Note**: if you plan to contribute code back to django-photologue, then you'll
probably want instead to fork the project on Github, and clone your fork instead.

Install requirements::

	pip install -r requirements.txt

**Note**: this will install Django library.

The project is set up to run SQLite in dev so that it can be quickly started
with no configuration required (you can of course specify another database in
the settings file). To setup the database::

	./manage.py migrate


And finally run the project (it defaults to a safe set of settings for a dev
environment)::

	./manage.py runserver

Open browser to http://127.0.0.1:8000

Thank you
=========
This example project is based on the `contact_demo project <https://github.com/balexander85/django-contact/tree/master/example_project>`_.


..
	Note: this README is formatted as reStructuredText so that it's in the same
	format as the Sphinx docs.