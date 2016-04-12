# django-blog
A very simple blog using Python and Django

<h1>Requirements
* Python 2.7.X
* Pip
* Virtual env (Optional) -  http://docs.python-guide.org/en/latest/dev/virtualenvs/

<h1>Installation
* Activate Virtual env (Optional) - http://docs.python-guide.org/en/latest/dev/virtualenvs/
```sh
$ Git clone https://github.com/malazay/django-blog.git
$ cd django-blog
$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
```

<h1>Run locally
* Activate Virtual env (Optional) - http://docs.python-guide.org/en/latest/dev/virtualenvs/
```sh
$ python manage.py runserver
```
<h1>Possible errors
* If the css is not loaded properly and you are on Mac OS X El capitan, you might need to give the static folder some access level:
```sh
$ sudo chmod -R 755 /django-blog/blog/static 
```
