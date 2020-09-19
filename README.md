## Project Title

### Web Project



### Functionalities implemented

    

### Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

    Python 3.6.9

### Installing

You'll need to have a virtual environment installed on your machine

    pip3 install virtualenv

Setup virtual environment

    virtualenv -p python3.6 .virtualenv

Activate virtual environment

    source .virtualenv/bin/activate

Install the requirements

    pip install -r requirements

Go to the folder youchooseDjango/settings and comment out the production_settings and uncomment the development settings so you can use the development setting to run this project locally on your machine

Make migrations, createsuperuser and run the server

    python manage.py makemigrations account polls
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py runserver

### Built With

    Python - Programming language used
    Django-rest-framework - The web framework used
    django-rest-swagger - Used to generate documentation for all the endpoints

### Important notes

The media files are being served through cloudinary, you will need to setup a cloudinary account if you dont have one, but if you do, the create a .env file in the root of this project and add the following

    CLOUD_NAME = "your cloud name"
    API_KEY = "your api key"
    API_SECRET = "your secret key"

### Authors

Baron Chibuikem (A fullstack software developer)

### Acknowledgments

Regards to everyone whose contributed in the development of this project.