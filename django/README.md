# Django

Run a Django app under Gunicorn with its settings from Corrie Config: read them in settings.py, run migrations through the launcher and restart within a minute of a save. Complete, tested example.

The full walkthrough, with the commands to run and what you should see, is in the guide: https://config.corrie.io/docs/django

Files in this folder:

- `manage.py`
- `mysite/__init__.py`
- `mysite/settings.py`
- `mysite/urls.py`
- `mysite/wsgi.py`
- `requirements.txt`

To try it you need a Corrie Config key for an environment. You can make one on the free plan at https://config.corrie.io/signup?ref=config-examples
