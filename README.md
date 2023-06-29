# GreenHouse
A repository about greenhouse managment.

The full stack application is written in python using Django Rest Framework.

The application is a final exam for Coding Factory, AUEB, Athens, Greece.

Mostly written in Greek with some names in English.

# Execution Steps || Βήματα εκτέλεσης:
### 1) Create Virtual Environment ||Δημιουργία virtual environment

`python -m venv venv`

### 2) Activate virtual environment || Ενεργοποίηση virtual environment

`venv\Scripts\activate`

### 3) Install requirement packages || Εγκατάσταση των απαραίτητων πακέτων

`pip intall requirements.txt`

### 4) Make migrations || Δημιουργία migrations

`python manage.py makemigrations`

### 5) Migrate

`python manage.py migrate`

### 6) Create superuser (administaror) || Δημιουργία διαχειριστή (υπερχρήστη της εφαρμογής)
`python manage.py createsuperuser`

### 7) Runserver || Εκτέλεση του κώδικα
`python manage.py runserver`
