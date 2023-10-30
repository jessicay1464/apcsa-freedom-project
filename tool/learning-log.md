# Tool Learning Log

Tool: **Python Django**

Project: **I am deciding to create a website for students to learn more about using plain Javascript to create a RPG game, with my partner Angela that is creating the game for my website and me, creating the game for the website, we will combine Javascript and Python together to create this website/ our project.**

---

10/24/23:
* [Link](https://docs.djangoproject.com/en/4.2/) to the intro of documentations of how I can import Django to my browser.
* [Link](https://youtu.be/rHux0gMZ3Eg?si=eNJpyaKKprEuYUhT) to introduce me to the purpose of Django and what it is mainly used for.
 * Django is a free and open source framework for building web apps with Python.
 * There are two sides of the program that one side is the client page and one is the server page, and that the client is needed to request the page, while the server will later to return the page.
 **Steps** to import documentations<br>
 1) create a folder `storefront`<br>
 2) go inside the folder<br>
 3) `pipenv install django`<br>
 4) `django-admin`- to start a new project<br>

 I learned that even though you deleted the folder for your project, when we use `django-admin startproject projectName .`, we are able to create a project in our own directory right now. When you don't have a project inside your server or nothing inside the setting inside your project, when you run your server, it can cause multiple errors.
  * When you run `python manage.py runserver`, you are able to get a list of different next steps that you can run inside the server, such as `run-server`, `load data`, `changing data`, `shell`...etc.<br>

**Challenges:** There are folders and files that contain the same name, that makes it confusing to which file we are editing in and how we can solve this issue.<br>
**Next steps:** I would want to expand more in documentations and be more familiar in the different files that are created and why it was created and how I can use them to create a website for a project.<br>

10/26/23:
* [Link](https://docs.djangoproject.com/en/4.2/) to the intro of documentations of how I can import Django to my browser.
* Today I mainly went back to this link to  look at the starting lesson, which is the `model layer` part of Django.
* I learned ...
```python
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
```
 * In this part of the code, the `first_name` and `last_name` are known as the fields of this model.
 * Each field is specified as a class attribute, and each attribute maps to a data base column
 * A database based of `PERSON` model. 
 ```python
 from django.db import models
 class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
 ```
 * `A-HA MOMENTS:` I learned that when we use `max_length=30;` makes the input of the user a limit of 30 character.
 * Based on the documentation, we use `myapp_person` because it is a [name](https://docs.djangoproject.com/en/4.2/ref/models/options/#table-names) for the table. (They can be overridden)
 * `id` [field](https://docs.djangoproject.com/en/4.2/topics/db/models/#automatic-primary-key-fields) is added automatically (can also be overridden)
 * `CREATE TABLE` --> backend database
 
**Questions**: How can tables be relevant to a project that I am doing this year? How can I apply this to a project that I am making this year?



<!-- 
* Links you used today (websites, videos, etc)
* Things you tried, progress you made, etc
* Challenges, a-ha moments, etc
* Questions you still have
* What you're going to try next
-->
