# Tool Learning Log

Tool: **Python Django**

Project: **I am deciding to create a website for students to learn more about using plain Javascript to create a RPG game, with my partner Angela that is creating the game for my website and me, creating the game for the website, we will combine Javascript and Python together to create this website/ our project.**

---

### 10/24/23:
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

### 10/26/23:
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

### 11/27/23 - 12/1/2023:
 * [Django](https://docs.djangoproject.com/en/4.2/topics/)
 * The link above had shown me the pathway that I have learn with using Django the different types of code, mainly the "foriegn key"
 * For instance, this week, I learned about the `foriegn key`.
```python
class Car(models.Model):
    company_that_makes_it = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
    )
```
 * In this code above, I learned that when I include `name.ForiegnKey()` is considered as a `model class`
 * it must be called or at the beginning of the code, you should have this line of code `class ForeignKey(to, on_delete, **options)`
 * Well, what is the purpose of doing this?
   * This can help us find the recursive relationships and that when we have many-to-one relationships with itself, we can use `models.ForeignKey('self', on_delete=models.CASCADE)` to compare one model and another model.
 * When I compare this to `Java`, it is significant that when we call the function from another class, and that in this role, it is considered as model.
 * `A-HA MOMENTS:` when we create a new class, we don't use `{ }`, but instead,we use `:` and `( )`. Similar to Java, we create a new instance, and that it should be creared new, but in this case here, when we create a new class, we should just justify it inside the new `model` that it has been off
  * **Next Steps**: Learning how can we make our own `models` and learn more about the `different concepts` such as making a basic webpage out of DJango

**Installing Python**
 * I also learned about the introduction of installing Python into my server.But mainly, I spend time doing this because I have a chromebook at home and that this would be very difficult to do because, we can't just download it, but we have to install it to our terminal and connect it to my code.cs50.io
 * [Python Install](https://www.youtube.com/watch?v=fM6Cv9Wm0vw&t=173s)
 * [Download](https://www.python.org/downloads/)
 * **Challenging**: It was somewhat challenging when I was following though the video linked above, and that we have to have our own terminal and to use a certain code, to connect it to my server in code.cs50.io.
 * **Further Steps**: To learn more the code in the terminal and to follow the steps in my personal computer to see how it works.

### 12/4/2023 - 12/10/2023:
 * [replit tinkering](https://replit.com/@jessicay1464/GlisteningGloomyEvaluations#main.py)
 * [Python document](https://docs.python.org/3/tutorial/index.html)
 * [Python tutorial](https://www.youtube.com/watch?v=hEgO047GxaQ&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=2)
 * In this case, I learned to make an array inside the code that I was putting in replit file that is linked above. Below the link is another link. This is where I choose a lesson, and today, I chose Lesson 1.1 and started by copying and pasting code into my replit folder and run to see what it gives us. However, it has come to my eyes that when I run this part of code, there was an error.
 * Looking back at what I have been learning the past few days on the ideas on comments, where `#` is the comment symbols in python and since this array hasn't been stored in any variable, it doesn't mean anything that has caused this error.
 ```python
 ['BANANA', 'APPLE', 'LIME'] # incorrect
 # ['BANANA', 'APPLE', 'LIME'] # correct
 ```
 * to print out a statement from python, we use `print()`. And yes `;`, the semicolons at the end of each code isn't mandatory or we can say that we don't even need it.
 * There was also a line of code that was also very giving me a hard time to understand.
 ```python
 loud_fruits = [fruit.upper() for fruit in fruits]
 ```
 * I saw that in this line of code, we have a variable that isn't declared with a data type, because as we learn, we learned that datatypes aren't as mandatory.
 * As we can see here, there is a `fruit.upper()`. I wonder what `.upper()` does. So I went to [w3schools](https://www.w3schools.com/python/trypython.asp?filename=demo_ref_string_upper) and see that this is for to upper Case and inside, we called the singular form from the array to change each item to an uppercase.
 * **What I want to try**: Since in Java, we learned about the idea of indexes, so I would want to try that in Python, whether or not it also works too.
 * **A-HA** moments: In the example above, I tried what I want to try and I selected one item from the array to make it uppercase. it inside a variableName called `banana`. And that this had led me to understand that indexes also work in this case in python. But also in w3schools, it had let me discover that when we use `.lower()`, it will help us to have a lowercase word
 ```python
 banana = fruits[0].upper()
 ```
 * In this lesson, I learned a lot and many concepts about the idea of arrays in Python, but next time, I would like to learn loops in Python and try to connect it to the arrays, such as looping throgh an array.

 ### 12/18/2023 - 1/2/2024 (Winter Break):
 * [w3schools loops] (https://www.w3schools.com/python/python_for_loops.asp)
   * Compared to the array that I have created, I wanted to add on to the array concept and learn about loops so that I can iterate through an array.
 * [add loop tinkering](https://replit.com/@jessicay1464/GlisteningGloomyEvaluations#main.py)
   * `for-loop` - similar in java, but different formatting
```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
```
 * When we look at the loop, it is similar that in java, we both have the `for` loop.
 * In the format of the `python` code, we have
```python
arrayName = [item1, item2, item3 ...]
for singularVar in arrayName:
  # code to run
```
 * In the code above, we first have to have an array of item, and that based of my replit tinkering and that I changed many values inside the array and set up multiple conditions on why certain code is in that way. For instance, I have changed to see for the `singularVar` name to a different letter to see if the different name is acceptable or does it must have to be `x`, therefore when I changed the value, I was successfully understanding that it was just a name and that, it won't create an error.
 * At the same time, I have learned about the code in Java how an array can only have 1 type of datatype. In this case, in `w3schools`, it provides me with and example of String
```python
fruits = ["apple", "banana", "cherry", 1]
```
 * At first, I was predicting that python would be similar to Java that it would only take in one type of data type. However, that was not the case. Above, when I add an integer, and run the code, there wasn't any errors, and that a major takeaway is that the arrays can take all type of data.
 * But I predict that this might because we aren't declaring an exact type of datatype. But maybe when I specifically declare which data type I want or will be using and that it might accept only one type of data.
<br>

**Looping Through a String**: <br>
 * We might not want our code to loop through just an array, but also looping through words in a specific array. Therefore, the format for that would be
```python
for singularVar in "wordThatYouWantToLoopThrough":
  print singularVar
```
 * The code above would help loop through the String, the letter of the word.
<br>

**A-HA Moments**: In this case, while I was tinkering through the code and writing code for the for loop in python, I found out that the code format and what it does is very similar to the enhanced for loop in Java, and that was also known as the for-each loop.
<br>
**Try Next**: I would want to try to connect all the values and the code back into the freedom project and create a little website, but maybe before that, I should learn about some code about the examples of the creating a website and select some parts that may be useful in my project.

### 1/3/24 - 1/14/24
 * [python web tutorial](https://youtu.be/kng-mJJby8g?si=hR6tSHfeDS22fvKg)
   * to create a python website, we need to install Flask into our VS-CODE using the code `pip install flask`
   * `from flask import Flask`
     * depending on your server and what it takes, it might have to be specific on which version you will be using mentioned in the front of the code named above.
   * create two `python files` -- `app.py` and `views.py`.<br>
**`views.py`**

```python
app = Flask(__name__)

if __name__ == '__main__':
  app.run(debug=True, port=8000)
```

 * The value stored the `debug=True` and `port=8000` is stored and that it is similar to the css style that styles the word in the what the programmer will be typing in.
   * This is mutable, which means that the value can and will be able to change depending on the programmer.
<br>

**`app.py`**

```
from flask import Blueprint
# view.py
# @app.route("/")
# def home():
# return "this is the home page"
```
 * Above, when you run this code, the home page will be shown in the webpage.
 * I have tried to follow this tutorial to follow the steps as listed above, however, this was a challenge for me because I only have a chromebook and that when I have tried to install, the video only provided me with macbook and that this didn't work for me, therefore, during my tinkering and learning my tools later, I would like to watch more videos that has an install in python. However, I have finished watching this tutorial and got the idea of hwo we can combine the use of python and Flask to halp me learn the structure of the website and that I have learned a lot.
 * Later on after a few days, I have got an understanding in the different numbers and the datatype of numbers that are existed in python.
   * I have decided to learn this part because it can help me learn the different datatypes that python teaches.
   * `int`
   `x = 1; #integer` - a number, integer (positive)
   * `float`
   `y = 2.8 #float` - a positive, negative, or containing more than one decimal point
   * `complex`
   `z = 1j # complex` - "j as an variable"
   * `type()` - to help verify an object
   * [replit tinkering](https://replit.com/@jessicay1464/GlisteningGloomyEvaluations#main.py)
   * I ahve continued to add on to my tinkering in python, and that since I have been very familiar with the use of `int` and `float`, I spent more time in `complex`. I saw that there was a variable name. I have wated to try to add on anotehr variable other than `j` however, it didn't let me.<br>

**A-HA MOMENTS**: In this round of tinkering, I have learned a new tool, minaly Flask that can be used to help me in building my project with the use of python. I have learn the code to create the route to install and generate the running based of the video, But also understand that `complex` only takes in the letter `j` and nothing <br>
**TRY NEXT:** As I mentioned above, I need to dig a little deeper in learning the installing the python into my chromebook. Or the backhand is to use my partners computer to help install.

### 1/22/24 - 1/30/24
 * [replit tinkering](https://replit.com/@jessicay1464/CleanAuthenticCryptos)
 * [python web tutorial](https://youtube/kng-mJJby8g?si=hR6tSHfeDS22fvKg)
 * Based on the tutorial above, we have seen how to create use python and flask to create this web design.
 * I have followed the tutorial to help me guide through this process
```python
from flask import Flask, render_template, request

app = Flask('app')

@app.route('/')
def hello_world():
    print(request.headers)
    return render_template(
        'index.html',
        user_id=request.headers['X-Replit-User-Id'],
```
 * In this code above, I have followed the tutorial and learned to create a little project that we have created where the user login and says hello to the username.
 * `@app.route` will make the code back to recall what you code have been creating. It is like saying, "Now let's run the code."
 * `'index.html',`
   * Inside, I played around with the `styles.css` and the `HTML` file to help me see with numbers and and classes are connected with each other. There was also a login page in the tutorial that I would want to change some parts of a code to see what else I can input. Connecting this to our freedom project, there are some parts where we would want to connect it to our project such as using the webpage that I have cerated using python to create this menu that can be useful in creating our overall freedom project.
   * I learned that the purpose of writing this in the HTML is to set them into classes so that we can later use `style.css` connected to the `python` that we can later style and the project in any way that we want to make the webview what want it to look like.
 * Following the tutorial, I continued with learning my tool with the assistance of FLASK to help with python in learning the code and making sure that it prints out the code the way we want it to be and look like. In this case, we need a `view.py`. This was what I wrote in the learning log referred to last week. In `view.py` we can use this code to help me view the code later on in the webview.
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
  return "this is the home page"

if __name__ == '__main__':
  app.run(debug=True, port=8000)
```
 * The purpose of writing t this is that `hello_world()` is similar to a function
 * Everytime that is called, we will see the return statement `return "this is the home page"`
 * Therefore, everytime we can use this function everytime it will be called, it will print it out in the webview.

**A-HA MOMENTS**: In this round of tinkering, I was continuing my project with my journey in tinkering my tools. I was able to use the tutorial that I have learned last time to help me learn and connect what I used in Flask and Python to help me create thsi webpage. I have also learned how to create the route in between `main.py` and `view.py` on how we use what we type in `main.py` to help me type code in python so that we can learn the project that we are learning and later use `view.py` to view our output.
```python
if __name__ == '__main__':
  app.run(debug=True, port=8000)
```
If we didn't have this part of the code, the code won't run because the main part over here is to have `app.run` to help the overall code to run and be printed
<br>

**TRY NEXT:** I would need to use more of what we learned in python, in the weeks (such as variables, datatypes, and many more to help us understand the topic) before to include user inputs to save and use the data to make my webpage more interactive.

### 1/31/24 - 2/4/24
 * [replit tinkering](https://replit.com/@jessicay1464/CleanAuthenticCryptos)
 * [python web tutorial](https://youtu.be/kng-mJJby8g?si=hR6tSHfeDS22fvKg)
 * For my part of the project, I have continued learning my project by using the same two sources that I have used last weeek.
 * This is because, I was having issues in understanding the purpose of the code and didn't have the understanding with the routes. I started with writing on a seperate file, but I was stuck becasue I didn't understand what I was typing in to my code, therefore, this has let me spent another week in understanding the routes of the code, more specifically to understand what I can do to help me in my future coding in project.
 * In this case, I followed the tutorial and continued my coding from last week.
 * Below is the code in the for creating the different routes.
 * `/` is similar to `and` and also saying to `go to the next one`.
```python
from flask import Blueprint

view = Blueprint(__name__, "views")

@view.route("/")
def home():
  return "home page"
```
 * `__name__` is the first arguement that you pass in to blueprint in order to send
   * You must have the the `__name__` before or else the `blueprint` will not be found and that there will be an error.

**A-HA MOMENTS**: In this round of tinkering, I have understand the routes of the concepts. I found out that when I create the code below, i can create multiple routes that can lead to the webpage. Therefore, we must have different ("/") names after the parentheses. However, we can have multiple, but we can the same return messages.
```python
@view.route("/")
def home():
  return "home page"
```

**TRY NEXT:** Next time, I would want to continue our process of the code. Due to the reason that now I still couldn't see the output that we have typed in the code, I would have to create a `tinker.html` to help connect my python into the html code. This can help me preview my code that I have seen in the video.

### 2/26/24 - 3/4/24
 * [replit tinkering](https://replit.com/@jessicay1464/CleanAuthenticCryptos)
 * [python web tutorial](https://youtu.be/kng-mJJby8g?si=hR6tSHfeDS22fvKg)
 * Continuing from the tinkering from last week, I have started to learn from the 9:22 (continuing on what I have been learning from last week). I have also play back a little bit because I have forgottn
   * `rendering_template:` The good part about this is that we can pass in any data value into this template that later we can be rendered by it.
   * For instance, in the `html` page, we have been tinkering about the `python` page, that later we can be passed into the `html` file through rendering it.
   * `def` define
   * When we type in the code,
   ```python
   return render__template("index.html", name=username)
   ```
   * This is mainly when we would want to have a portfolio for this code but when we define the code above, we follow the route to the profile page and then inside the profile, to find the username.
     * What this will return is what in the `index.html` file that will be find in the `name` variable that later will be useful to get the name of the specific user.
 * I have also played about the making up names and different variable names to see what is connected inside between the `html` file and the `python` files. I learned that we can identify the variable as any variable, but in this case, we have to direct the template that we are currently in to help us go through the flow.
 * Regarding to the syntax errors, it is very significant that we don't need `;` but for some parts, we need semi colons, instead of curly brackets as we learn from the `java`
 <br>
 <br>

 **A HA Moments**: A A-Ha moment that I = have discovered in this round of tinkering is how when we what to pass in the data value from `Python` to `HTML` we can set them a `div` and use `{{variableName}}` to help us understand what we will be passing in. Make sure that when we pass in these types of datas, we should have to send in the data through the use of `{{}}` and not just one. But also, I have learned that when we want to pass into the data, it doesn't have to be tagged in the one data type, but instead, we should have it tagged where ever you want this name to be
 ```python
   <h1>Hello {{name}}</h1>
 ```
 **Try Next:** I have tried to follow every step of the tutorial. But next step, I would like to continuing finish watching this tutorial and learn how I can use this to help me code my webpage that I have been learning such as importing images and many more. At the same time, I will also help Angela in drawing the characters that we have been designing for our games later on in the project.

### 3/4/2024 - 3/10/2024
 * [Jinja templates](https://jinja.palletsprojects.com/en/3.1.x/templates/)
 *  [DJango templates](https://docs.djangoproject.com/en/5.0/ref/templates/language/)
 * [Flask Templates](https://flask.palletsprojects.com/en/2.3.x/tutorial/templates/)
 * Last week, I have talked with Mr. Mueller about deep diving inside on how I can use the code that I have so far to help me build a my webpage or how can I coorperate how I can coorporate my project into our topic. In this case, Mr. Mueller have helped through the way that I can `research the templates` that are provided for us. In this case, we have learned about the three different Platforms based on what Mr. Mueller had recommended me on.
 * All these platforms are all web frameworks in Python that we can use to help us build a webpage through the use of Python language.
 * `Flask`
   * In this case, this is a base layout of the application. In this page, can have a title page, a headers page, log out page corporated for the page.
   * This template is directly imported in the `template` file.
   *
   ```python
   <!doctype html>
    <title>{% block title %}{% endblock %} - Flaskr</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
    <nav>
      <h1>Flaskr</h1>
      <ul>
        {% if g.user %}
          <li><span>{{ g.user['username'] }}</span>
          <li><a href="{{ url_for('auth.logout') }}">Log Out</a>
        {% else %}
          <li><a href="{{ url_for('auth.register') }}">Register</a>
          <li><a href="{{ url_for('auth.login') }}">Log In</a>
        {% endif %}
      </ul>
    </nav>
    <section class="content">
      <header>
        {% block header %}{% endblock %}
      </header>
      {% for message in get_flashed_messages() %}
        <div class="flash">{{ message }}</div>
      {% endfor %}
      {% block content %}{% endblock %}
    </section>
   ```

 * I haved learned that the g.username is an automatic value inside the flask
   * In this case, when the user is logged in, it can be a log-in link or a logout link that can be displayed.
   * In this case, we have a header, a a title and a content.
   * This can be useful in a way that everytime there is a new user, we will have this page created.
   * At the same time, we can also have a register and a login page template that I will look into later.
 * `Jinja`
   * Jinga behaves the most similar with Python.
   * Jinja's syntax is from the static data in the template
   * Any syntax value between the `{{ }}` is an expression that will be output to the fianl document
   * For all the `{% %}` denotes a control flow in common to the `if` and `for`.
     * `{% ... %}` for Statements
     * `{{ ... }}` for Expressions to print to the template output
     * `{# ... #}` for Comments
       * such as in Java, we have `//` and in Python, we have `#` as our Python comment
     * `{% if True %}` --> similar to `if`
       * `{% end if %}` --> similar to else (if this statement is true and the statement ends)
 * `DJango`
   * Will be best for a webpage API.
   * In the templates, we have a text file, and that in this template, it will contain variables that will later get evaluated and that also includes the logic of the template
   * `{{ variable }}`
     * can contain alphabets and characters and underscore
     * no spaces and no underscore and may also not be a number.
   * In DJango, when we use the `.` inside the varubale name , it means that it will repalce the `title` attribute with the section object.
     * This will be a replacement
     * similar to entering a object and a method.
   * when we have `|`, we can also select a value to add design to it such as fonts, linkbreaks, how to join words and methods that we can change the group of words in the output.

**A-HA MOMENTS**: I have learned that based on these templates (Flask) is that no matter how you want your templates to be viewed in your server, you won't be able to preview it, and this is because when we are calling `rendering_templates()` function, we aren't temporarily inside the directory `flask` package. Instead of the HTML structure in each template, it will extend the base template and overrride specific sections. Since we have the templated file inside the file, we have also use the file to make multiple templates, as a way that we can use multiple sub-classes, for one simgle class.
<br>

**Next Step**: I will continuing tinker with these tools to help me find out which tool can be the best for me in this case. But also, I will start building out the base MVP with Python, and later cooperating harder platforms into my project. I will also watch tutorials and continuing with templates from Replit. At the same time, I will also be uploading sprites with my partner, Angela, to follow the MVP plan.

### 3/19/2024 - 3/24/2024
 * [Django Template 2](https://www.w3schools.com/django/django_templates.php)
 * Django tinkering file `linked inside the tool folder`
 * [Django video](https://www.youtube.com/watch?v=ZNrlc6TPcrU)
 * This week, I haven't done a lot, but I have doen a few steps that helped me throughout building my MVP.
 * Before in the past, I started tinkering and building out my project inside replit from scratch, but now, I have watched more tutorials that have helped my installing from GitHub. I am currently following the tutorial and following the steps that comes to building this project. I have created one file called the `tinker.html` and `tinker-django.py`.
 * Inside the html code, I have learned that how you would want your project to printed out and how you would want your `html` page want to look like. Therefore, inside my `html` page, I have include a heading `<h1>` and also a `<p>`.
```html
<!DOCTYPE html>
<html>
<body>
<h1>Hello World! My name is Jessica</h1>
<p>This is tinkering for my freedom project</p>
</body>
</html>
```
 * At the same time, I have also learned in importing the dataset thorugh the use of the python file. The purpose of this file is to generate what is currently in the HTML to help us print and show through the python file.
```python
from django.http import HttpResponse
from django.template import loader

def members(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())
```
 * As mentioned before, when we `.get_template('myfirst.html')`, we can grab what is inside the html file page and print it out.
 * After learning all the different Django codes, we have followed up with building our MVP. In this case, me and Angela have been drawing out our sprites. At the same time, we have also been importing the background sprites.
 * Such as what we have learned in SEP 10, we have also drawn a wireframe that has helped us build our project even much more easier.
 * We each have started building our own folder in the same repo that has helped us think through the thought process, and we have started importing some code one each of our end
   * In this process, we have also thinking about how we can connect the project together
   * This was one of our biggest decisions over here because it was difficult that we have two different coding languages. So it was pretty difficult.

**A-HA MOMENTS**: Similar to what I have learned before from Flask, in these templates, I have learned that for all datatypes to be printed from the webpage for us to view, I have learned that we must have to print out the code through creating the route for HTML. This route will travel though the different types of data inside the `py` file and grab the information and continue the route or later on when we would want to print, it will just come out inside the viewing page. Overall, this week, I haven't done a lot, but I have tried my best to continue my project.
<br>

**Next Step**: Further on later in the project, it would be best to continuing collaborating with my partner, Angela. We have already finished drawing all the sprites for our game later on. At the same time, we have been importing all of our sprites inside our folder incide the `freedom-project` repo. After that, Angela and I have seperated off to continue our project on our own. I would love to found out how I can view my outputs after using Django and become more familiar with it. After that, i would love to find out how we can also apply `styles.css` into my webpage to make it look more visually appealing. At the same time, since Grace and Vivian are also using teh sam  tool to me, I believe that it would be best to as them for some tips and asking for some help.

 <!--
* Links you used today (websites, videos, etc)
* Things you tried, progress you made, etc
* Challenges, a-ha moments, etc
* Questions you still have
* What you're going to try next
-->
