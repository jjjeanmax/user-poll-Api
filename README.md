# user-poll-Api
User Poll API

>Django 2.2.10, Django REST framework.

## Functionality for the system administrator:

- adding/changing/deleting polls. Survey attributes: title, start date, end date, description. Once created, the "start date" field of the survey cannot be changed
- adding / changing / deleting questions in the survey. Question attributes: question text, question type (text answer, single choice answer, multiple choice answer)


## Functionality for system users:

- getting a list of active polls
- passing a survey: surveys can be completed anonymously, a numeric ID is passed to the API as a user identifier, by which the user's answers to questions are saved; one user can participate in any number of surveys
- receiving surveys completed by the user with details on the answers (what is selected) by unique user ID


## Authorization in the system (registration is not required)
- Access to API methods requires Token(Basic)

## Start

1. Create and activate virtual environment:

    `python -m venv venv`

2. Install packages:

    `pip install -r requirements.txt`

3. Run migrations:

    `python manage.py migrate`

4. Create superuser:

    `python manage.py createsuperuser`

4. Create config file:

    `configs.json`

6. Start django server:
    
    `$ python manage.py runserver`

### Documentation is available in docs:
> http://127.0.0.1:8000/docs/

