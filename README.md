# rivannastreamwatch
API for storing Rivanna Stream water quality data!

The backend for a react-native application to record and report data on the fly!

API Models and start for providing an alternative data store for the form found at http://www.rivanna-stormwater.org/ -> Report Water Pollution -> Click Here

# Getting Started

- clone the repository to your local machine
-(in a python virtualenv...) `pip install -r requirements.txt`
- `cd rivannastreamwatch`
- `python manage.py migrate`
- `python manage.py runserver`

The API now should be running on `http://localhost:8000/reports/`
