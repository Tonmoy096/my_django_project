Day 1: Setting Up Django

1. Installing Django

I started by setting up Django in my development environment using pip install django. This installed Django and made the django-admin command available to create projects.

I checked the version with django-admin --version.


2. Creating a Project

I created a new Django project with django-admin startproject project_name. This generated the necessary files like manage.py and the core project_name directory.


3. Running the Development Server

I ran Django’s built-in development server with python manage.py runserver. This started the server locally (accessible at http://127.0.0.1:8000/), where I saw the default Django welcome page.


4. Project Structure

I became familiar with the Django project structure:

manage.py: Command-line tool to manage Django.

project_name/settings.py: Contains configurations (e.g., database, installed apps, middleware).

project_name/urls.py: URL dispatcher to map URLs to views.

project_name/wsgi.py: Used for deployment to production.




---

Day 2: Django Apps & URL Routing

1. Creating Apps

Django projects consist of multiple "apps". I created an app using python manage.py startapp app_name, generating a directory with files like models.py, views.py, and urls.py.


2. Configuring URLs

I mapped views to URLs using Django’s URL routing system. In the root urls.py, I included app-specific URLs using include():

from django.urls import path, include

urlpatterns = [
    path('app/', include('app_name.urls')),
]

Inside the app’s urls.py, I mapped views to specific URLs:

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]



---

Day 3: Views, Templates, and Static Files

1. Views

Views handle requests and return responses. I created basic views in views.py:

from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, World!")


2. Templates

I used Django’s template system to render dynamic HTML. Templates are stored in the templates/ directory.

I used the render() function to send data to templates:

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

Template Logic: I used loops and conditionals in templates to display dynamic content:

<ul>
  {% for item in items %}
    <li>{{ item.name }}</li>
  {% endfor %}
</ul>



3. Static Files

Static files (CSS, JS, images) are placed in the static/ directory. In templates, I linked them using {% static 'path' %}:

<link rel="stylesheet" type="text/css" href="{% static 'style.css' %}">



---

Day 4: Models & Databases

1. Models

Models define the structure of the database. I created models in models.py:

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()


2. Migrations

After defining models, I ran migrations to create database tables:

python manage.py makemigrations
python manage.py migrate


3. Interacting with the Database

I used Django’s ORM to query and manage the database:

Create:

Book.objects.create(title='Django for Beginners', author='John Doe', published_date='2025-01-01')

Retrieve:

books = Book.objects.all()




---

Day 5: Admin Interface

1. Registering Models with Admin

I registered models in admin.py to make them editable in Django’s admin interface:

from django.contrib import admin
from .models import Book

admin.site.register(Book)


2. Creating a Superuser

I created a superuser with python manage.py createsuperuser to access the admin interface.


3. Admin Interface

The admin interface allows me to add, edit, and delete data from the models via a web-based dashboard at /admin.



---

Day 6: Forms & Validation

1. Forms

Forms in Django handle user input and validation. I created a form in forms.py for my Book model:

from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']


2. Handling User Input

I rendered forms in templates and processed them in views:

def book_view(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'book_form.html', {'form': form})


3. Validation

Django automatically validates form fields for things like required fields or correct data types. I can also add custom validation logic.



---

Day 7: Views & Template Logic

1. Class-based Views (CBVs)

I used class-based views (CBVs) to create more structured and reusable views:

ListView for listing objects:

from django.views.generic import ListView
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'



2. Template Logic

In templates, I used logic to display data conditionally:

{% if book.author %}
    <p>{{ book.author }}</p>
{% else %}
    <p>Author not available</p>
{% endif %}



---

Day 8: Advanced Database Queries

1. Querying the Database

I deepened my understanding of Django’s ORM by filtering and querying the database:

Filtering:

books_by_author = Book.objects.filter(author='John Doe')



2. Ordering & Aggregation

I learned to order query results and aggregate data:

Ordering:

books = Book.objects.all().order_by('published_date')

Aggregation:

from django.db.models import Count
author_counts = Book.objects.values('author').annotate(num_books=Count('id'))




---

Summary of Key Concepts

Django Setup: I set up the project, created apps, and ran the development server.

Models & ORM: I defined models, used the ORM for database interactions, and learned how to handle migrations.

Admin Interface: I registered models to use Django’s admin interface for easy content management.

Forms & Validation: I worked with forms to handle user input and validate data.

Class-based Views: I explored CBVs to create reusable and structured views.

Advanced Queries: I learned to filter, order, and aggregate data efficiently using the ORM.
