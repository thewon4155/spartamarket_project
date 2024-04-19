# spartamarket_project

0. ERD(Entity Relationship Diagram)
   +------------------+       +------------------+
   |     User         |       |     Product      |
   +------------------+       +------------------+
   | - id             | 1----*| - id             |
   | - username       |       | - title          |
   | - email          |       | - description    |
   | - password       |       | - price          |
   | - date_joined    |       | - owner (FK User)|
   +------------------+       +------------------+
            |
            | 0..*       
            |
   +------------------+
   |    Bookmark      |
   +------------------+
   | - id             |
   | - user (FK User)|
   | - product (FK Product)|
   +------------------+

1. Project abstract: (2024.04.16 ~ 2024.04.19.)
a Django based website that runs apps of User, Product, Bookmark and allows Users to select items of preference

2. Software Used:
Main Framework: Django 5.0.4, Python 3.12.1
DB: SQlite3
Frontend: HTML

3. Operating Functions:
Post CR(Only Create and Read are currently functional). Signup, login functions are also supported.
But haven't figured the merge of 'Bookmark' into the above function.

4. How to Run(Terminal):
python -m venv myenv : Create venv virtual environment

pip install django : install Django

python manage.py makemigrations
python manage.py migrate            : apply to DB

python manage.py runserver : Run

5.. Restrictions/Limitations:
After making a new 'Bookmark' application, the applications somehow are colliding and an error occurs.
The error code seems to be related with __init.py.__ but its an empty path way, which has nothing to do with.
