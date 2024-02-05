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
```
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

<!--
* Links you used today (websites, videos, etc)
* Things you tried, progress you made, etc
* Challenges, a-ha moments, etc
* Questions you still have
* What you're going to try next
-->
