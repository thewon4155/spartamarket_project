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
Main Framework: Django, Python
DB: SQlite
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
