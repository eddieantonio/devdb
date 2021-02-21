devdb
=====

An example Django app I made to explain what the Django ORM is, and what
the heck a migration really is.

Watch me build this app here: https://www.youtube.com/watch?v=26bvrkNACyI

Setup
-----

You will need **Python 3.8+**.

 1. Clone this repo
 2. Create a _virtual environment_ and then activate it:

```sh
python3 -m venv .venv
source .venv/bin/activate
```

 3. Install dependencies with `pip`:

```sh
pip install -r requirements.txt
```

 4. Run migrations (which we learn all about in this video!):

```sh
python3 manage.py migrate
```

 5. (optional) Create a superuser so you can use the admin interface:

```sh
python3 manage.py createsuperuser
```


Run
---

Run the server!

```sh
python3 manage.py runserver
```

You can now visit the site at <http://localhost:8000/>

Visit the admin at <http://localhost:8000/admin/>

License
-------

© 2021 Eddie Antonio Santos. Licensed under the terms of the MIT
License. See `LICENSE` for details.
