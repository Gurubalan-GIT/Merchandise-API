# Merchandise-API

This is an ongoing merchandise API created with Django backend. Front-end will have a React counterpart.

## Running the application

- Place this inside a folder and create a `Pipfile`, the pipfile consists of -

  ```
  [[source]]
  url = "https://pypi.org/simple"
  verify_ssl = true
  name = "pypi"

  [packages]
  django = "==3.0.8"
  django-cors-headers = "\*"

  [dev-packages]

  [requires]
  python_version = "3.8"
  ```

- Run `pipenv install` & `pipenv shell` to start the environment.
- Run `python3 manage.py makemigrations` to detect and make migrations.
- Run `python3 manage.py migrate` to execute migrations into database.
- Run `python3 manage.py runserver` to start the application.

## Pointers to note

- To avoid OS conflicts `pipenv` (A Virtual environment) is used, this way it won't matter which OS you're trying this out on.
- For example -> `python -m pip install <package>` becomes `pipenv install <package>`
