# Django Tutorial Polls App

This repository contains the complete code for the [Django](https://www.djangoproject.com/) project's [tutorial](https://docs.djangoproject.com/en/2.1/intro/tutorial01/) `polls` app. The code should mirror the code you've written at the end of [Part 7](https://docs.djangoproject.com/en/2.1/intro/tutorial07/). 

The `SECRET_KEY` variable in `mysite/settings.py` has been scrubbed, and instructions for regenerating the key are available in the accompanying DigitalOcean [tutorial](https://www.digitalocean.com/community/tutorials).

This app is meant to be used as a reference Django app for several DigitalOcean tutorials, and should not be deployed in production.

----

### Quickstart

Polls is a simple Django app to conduct Web-based polls. For each question, visitors can choose between a fixed number of answers.


1. Add `polls` to your `INSTALLED_APPS` setting like this:

```python
INSTALLED_APPS = [
        ...
        'polls',
    ]
```

2. Include the polls URLconf in your project `urls.py` like this:

```python
path('polls/', include('polls.urls')),
```

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/polls/ to participate in the poll.