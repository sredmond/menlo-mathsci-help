web: gunicorn runp-heroku:app
init: python db_create.py && python add_subjects.py
upgrade: python db_upgrade.py