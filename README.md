# Django Todo Project

A simple todo list application built with Django.

## Description

This project allowed me to learn and practice the basics of Django web development. It includes features such as:

- Create todo items with a title and description
- Mark todo items as complete or incomplete
- View all todo items or only incomplete/complete items
- Edit existing todo items
- Delete todo items

The main features used in Django include:

- Models to define the Todo item
- Views to display and handle form submissions
- Templates to display the UI
- URLs to map requests to views

## Setup

1. Clone the repo:
   
git clone https://github.com/shyamsai0611/djangoTodoProj.git


2. Create a virtual environment and activate it:
   
python -m venv env
source env/bin/activate


3. Run makemigrations:
   
python manage.py makemigrations


4. Run migrations:
   
python manage.py migrate


5. Create a superuser:
   
python manage.py createsuperuser yourname


6. Run the development server:
    
python manage.py runserver


7. Visit http://127.0.0.1:8000 to view the app.

## Usage

- Browse, create, edit, and delete todo items
- Mark items as complete/incomplete
- Filter items by status
