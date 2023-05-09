## Description
A dependent dropdown list using `rest_framework`. This is a form where one field is dependent on the other. The example is used is that of a country and a city. A city is dependent on the country. `Sokoto` is in `Nigeria` but not in `India` so we want to enable that user experience to filter cities based on the selected country.

## Installation
Follow the steps below to successfully install the project.

```
$ python -m pip install requirements.txt
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```

Once the server is started, visit [http://localhost:8000/] to view the project 

## Author
Gabriel Michael Ojomakpene(codewitgabi)\
09020617734
