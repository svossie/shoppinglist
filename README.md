# Shopping List application based on Django framework
## Introduction 
Problem with paper shopping lists are they always get lost or are outdated by the time you are in the shop.
This online shopping list app allows more than one person to contribute to the list either by adding, deleting or marking an item as bought.<br>
The app is mobile device friendly.
## Requirements
Python 3.4 or later<br>
Django 2.0 or later<br>
Linux based OS<br>
Apache HTTP server or Django built in server (Not recommended)
## Dependencies
None
## Installation
-- x.x.x.x is the IP address of the host machine<br>
git clone https://github.com/svossie/shoppinglist.git<br>
in django_prj/settings.py change ALLOWED_HOSTS = ['x.x.x.x']<br>
 in django_prj/settings.py<br>
python manage.py createsuperuser<br>
python manage.py migrate<br>
python manage.py makemigrations shop<br>
python manage.py migrate<br>
python manage.py runserver 0.0.0.0:8000<br>
## Configuration
Login to application admin: http://x.x.x.x:8000/admin/<br>
Create required users with permissions for shoppinglist<br>
Login with one of the created users: http://x.x.x.x:8000/admin/shop/shoppinglist/
## Notes 
## Revision Information 
## How it works
Uses a sqlite3 database which stores the list of configured items.
Currently all configured users are able to access the same shipping list.
