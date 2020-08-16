 
Installation Instructions:

Step 01: First Install Python 3.6 or above with path configured.
Step 02: Open Command Prompt(Windows) or Terminal(Linux) and type
         pip install -r requirements.txt
         or for Linux
         sudo pip3 install -r requirements.txt
Step 03: Setup sqlite in OS if not.
Step 04: Migrating databases,Open Command Prompt or Terminal at project's main directory, type:
         python manage.py makemigrations
         python manage.py migrate
Step 04: Now Create superuser i.e. admin again type in command prompt or terminal:
         python manage.py createsuperuser
Step 05: To run the developmental server
         python manage.py runserver
Step 06: Explore the project by registering a new user.
