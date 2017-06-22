# FBAAS API

## Installation

Ensure that you have setuptools installed and run

```
# pip install -r requirements.txt
# python setup.py install
```

## Run

```
gunicorn --chdir /usr/share/python/fbaas/bin -k gevent -w 100 --bind 127.0.0.1:8000 -m 007 wsgi:app
```
