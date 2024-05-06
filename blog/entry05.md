# Entry 5
##### 5/1/24

### How I have been learning my tool?
 * Regarding on how I have been learning my tool, I have spent time watching a video that helped me learned how I can `import` our own file. In the code, ...
```python
from django.shortcuts import render 

def posts_list(request):
  return render(request,'')
```
 * In this case, I learned that I have to use request to help the backend code to be linked into your directory. This is similar to routing and this would also be a good way to show what file you what to be imported in that file. 
 * While watching this video, the programmer has also initiated that `!` is a shortcut from VS Code that helped us become and have the code for the automatic templates after the first installations. 
 * To add on, I have also learned that you need an `urls.py` to have all the pathway to be shown from the python files, and not the other files. To add on, when looking through the difference between `load` and `pathway`, it is considered that we need to use load when we want to get a data from another file and another folder, but when we are using that data and running that data in the case, we will be need to using render to help us run the data that the load is doing.
```python
from django.urls import path
from . import views

urlpatterns = {
  path('admin/', admin.site.urls),
  path('', views.homepage),
  path('about/', views.about)
}
```
 * I have also learned that the HTML code was also an important factor in python and that there is a way to connect both the languages. In the example that I have created while looking at the [DJANGO TEMPLATES](https://www.w3schools.com/django/django_templates.php), it had helped me learned that here are tags that are created that are in the coding language of HTML, but later on, we actually seeing that these are created from the data from the coding language of python, but are imported into html that can be very helpful in a way that we have the inputed data from python, and then tag it inside the HTML tag through the use of `{{ varName }}`. The `{}` are considered to be the python django code.
 * Furthermore, after typing out my code and wanting it to try and running it, I have forgot how to run the code in my terminal, therefore, it was serious that I had to look through my notes and because of my detail looking into the code wasn't specifically enough, this has brought mt attention to asking Grace and Vivian for their advice on how to create the code. In this case, it was significant that what they told me was `python manage.py runserver`. Therfore, when I look back at my code once again, I once know what has happened in my learning-log, I thought that that was menat to be in the code section, however it was in the terminal section and this has brought a huge support for me.  

### How have I built my MVP?
 * Building my MVP was a fun and interesting moment. On the other hand, me and my partner Angela, has planned out all the prototype we want outside already months ago. Therefore, this time, we have spent a lot of time on drawing the sprites and the background. 
 * For when downloading the Django library, I have learned that it was significant to have the extension inside my server in `VS code`. However, I still need to install and identify the project that I will be creating. In this case, I made it named `instructions`. 
 * In this case, the website that helped me the most was * [Django installing](https://docs.djangoproject.com/en/5.0/intro/tutorial01/). This is because it had helped me learned a shortcut to having all the file and the starter code for my project. However, I have started to have all the project. But I was very curious on the code would run me. Therefore, I have started to use the shortcut to build a serparate project and that it totally worked. So I have deleted my original file, and started a new one, and the code was `django-admin startproject mysite`. 
 * In `mysite`, I imported `instructions` because it was what my project was about. 
```python
instructions/
    manage.py
    instructions/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
``` 
 * From here, I have overcome an issue. This is that when I run `python manage.py runserver`, it doesn't work again.
 * I was finding the issue and finally, when reading the issue from the comments, I learned that since, we are running `manage.py` from the parent directory, the code won't work, because the issue with me is that I have a `manage.py` already inside my code, it was wasn't normal to have a second `manage.py`, and so the backend code don't know which one to run.
 * In `views.py`, this is where I include the project that I want to make. Inside here, I have included `html` and `django` code to help me file out the `html` file. 
```python
from django.http import HttpResponse

def instructions_view(request):
    html = """
    <html>
        <body>
            <!-- HTML -->
        </body>
    </html>
    """
return HttpResponse(html);

```
 * In `urls.py`, this is where I include and load all my templates and importing the pathway.
```python
from django.urls import path
from . import views
from django.http import HttpResponse
from django.template import loader

urlpatterns = [
    path('instructions/', views.instructions_view, name='instructions'),
]

def members(request):
  template = loader.get_template('instructions.html')
  return HttpResponse(template.render())

INSTALLED_APPS = 
...
```
### Skills
Skills that I have accomplished when completing the building of the structure of MVP were time management, problem decomposition and communitcation. For instance, the first skill that I have accomplished was time-management because we have spent so much time building, but also there were also days where i procrastinate a lot and that is not good. Therefore, during the spring break, I was able to make an scehdule for myself and work on the seperate parts and work on them for each day. This had greatly helped me turn in the work on time, but being able to spend time on the parts equallly in time. At the same time, I would also say problem decomposition because while creating my MVP/prototype, there are still many concepts that I still have not been very familiar and I would have to slowly break down the problem that I have so far and research the issue that I have so far and fix the conflict. Next, was communication because I have a partner and that I have communicated with her in working on the connection of our project and how we can make that work. I have also communicated with another group with DJango that helped me answer the question how I run the server with Django. 

### EDP (Engineering Design Process)
Currently, I am in the middle of the Steps 3, 4, 5. These are considered as `Researching the problem, Planning the most promising solution, Creating a prototype`. First of all, I say I was still researching the problem because I was creating the prototype, my MVP, I was still looking up the issues that I was having in Python and Django, researching the tiny issues that I had missed out accidentally that can help me throughout the process of building up my code. This is also a process that I have still been learning my code. Also, I also added in planning the most promising solution because me and my partner Angela, was also making a planning out on paper such as how we want the character to look like on how out project would look like. Lastly, I was also saying creating a prototype because this time, we are in the process of creating a MVP, the Minimum Viable Product (MVP). This was a part of me and my partner in the process of making a product or the prototype.

### Sources
 * [DJANGO EXAMPLES and templates](https://www.w3schools.com/django/django_prepare_template.php)
 * [DJANGO TEMPLATES](https://www.w3schools.com/django/django_templates.php)
 * [Django installing](https://docs.djangoproject.com/en/5.0/intro/tutorial01/)

[Previous](entry04.md) | [Next](entry06.md)

[Home](../README.md)