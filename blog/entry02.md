# Entry 2
##### 12/11/23

During these few weeks, I have been learning my tool and updating my `learning-log.md` every week. During the first week, I have learned about the introduction and the installation of Django. The link that I put below are the videos and the documentations that I used to learn the intro of documentations of how I can import Django to my browser and also attached a link that introduce me to the purpose of Django and what it is mainly used for such as the advanced interactive web designs. In this case, I have learned to make a folder that I have tried and followed the tutorial, but it has failed, therefore, I jot down my steps, and continued on. 
#### Steps to import documentation
 * create a folder `storefront`
 * go inside the folder
 * `pipenv` install django
 * `django-admin` to start a new project

#### Important Notes
 * `django-admin startproject projectName .` - I have learned in this case that although I have deleted a folder inside my directory, I can still get the code back by using the template above, but that it only works in your own directory
 * When you have a empty server or ntohing inside the setting inside your object, it can not compile and run correctly.

In the Django official website, I look through the directory document.
In here, I learned about the code that was explained and that made me process through what each part of the code was about. 
```python
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
...
```
In this part of the code, the `first_name` and `last_name` are known as the field of this model. In this case, I learned about the field in this case, field is known as a class attribite and that each sttribute is connected to a column, as if this is a grid, but created by `python`.
Another example would be how the `max_length` is set to a number and that this means that every number is only a limit that the character that the user inputs.
<br>

Later on, I have learned about the `foreign keys`
```python
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
```
 * When we are having a class, we have `name.ForeignKey()` and that is considered as `model class`
   * This must be called in the beginning of the code because, it can lead to help you to have options to chose such as what the user do, to react or respond to it such as `class ForeignKey(to, on_delete, **options)` The purpose of this is to comapre nultiple models together. 
Some moments that satisfied me, or interested me was when I like to compare code to what I have learned before, I learned, such as `Java` and `Javascript` and that I learned that, When we create a new class, we don't use `{ }`, but instead,we use `:` and `( )`. Similar to Java, we create a new instance, and that it should be declared new, but in this case here, when we create a new class, we should just justify it inside the new `model` that it has been off.

During the next week, however, when I was in school, I have watched a tutorial that it may be helpful to learn Python first (such as learning the basics) and then continue learning Django because Django is the advanced version, therefore, it may not be helpful to start the advance because it may be diffcult to understand. As if I was walking up the steps, and suddenly, a step fell off. 
Therefore, I paused a bit what I was doing in Django and switched gears to Python.<br>
During this process, I was able to use replit to conduct what I learned for Python. In this case, I learned to make an array inside the code that I was putting in replit file that is linked above. Below the link is another link. This is where I choose a lesson, and today, I chose Lesson 1.1 and started by copying and pasting code into my replit folder and run to see what it gives us. However, it has come to my eyes that when I run this part of code, there was an error.
```python
['BANANA', 'APPLE', 'LIME'] # incorrect
# ['BANANA', 'APPLE', 'LIME'] # correct
```
 * Looking back at what I have been learning the past few days on the ideas on comments, where `#` is the comment symbols in python and since this array hasn't been stored in any variable, it doesn't mean anything that has caused this error.
 * This code above may be simple, but I have learned a lot in this such as to print out a statement from python, we use `print()`. And yes `;`, the semicolons at the end of each code isn't mandatory or we can say that we don't even need it.
I even typed in the code
```python
loud_fruits = [fruit.upper() for fruit in fruits]
```
 * This code above is kind of confusing me such as what is `for fruits in fruits`. We have a variable that isn't declared with a data type, because as we learned before, in the previous lessons in `Django`, datatypes aren't as mandatory.
 * But also, in the code above, there is a `fruit.upper()`. I wonder what `.upper()` does. So I went to w3schools (also linked below in sources) and see that this is for to upper Case and inside, we called the singular form from the array to change each item to an uppercase.
   * This had helped me understand that `.lower()` was to help us with to change a single word to `lowerCase`.

### FP goals for the winter break 
During this winter break, I would want to learn more about the different concepts about Python such as Arrays, lists, Printing out, indexes, and making an interactive code. However, because I only spent time learning in every concepts seperately and that made me have a lack of knowledge on how to connect these code together, such as the importance of the variable names. But also, that now I learned some methods about learning my tool, it has come to a point that I would need to learn the for-loop and connect it with an array. Another goal that I would wnat to work with my partner, Angela is to help connect the two tools together. This is because, we believed that it might take a pretty long time to connect them together, that made us have a plan to connect these two projects together during this break, maybe at first the link of her game into my website, or even I will use python that can be imported into javascript (her advanture game with only plain Javascript). 

### Skills
During these few weeks of learning my tool, I have learned a lot, but at the same time, I have thought about how the code that I have been recently learning will be a great way that I can use to corporate it into my project later on. Well, throughout these weeks of tinkering, I have achieved different skills. For instance, **Organization** and **Attention to Detail**. First of all, I chose Organization because what do we do with all the learning that we learn about our tool. Of course, we should put it into our `learning-log.md`. This was greatly helpful because in the past, we put the code into the SEP 10 and or 11 google docs. This was beneficial because in `github`, we can just use backticks. This can help us by just typing in the backticks and that helps us organize the code but also put our links in one big safe space. Another example would be Attention to Detail because in the Python System, some codes are different in Python, such as `//`. This is what we use in Java and Javascript, but in this case, we use `#` and that this had brought me lots of errors while running the code. This is why I say **Organization** and **Attention to Detail**.


### EDP (Engineering Design Process)
In this process, we are now in step 2 of the engineering design process where we **Researching the Problem**. In this case, we are using every Monday to learn our tool that we chose. For instance, we tinker, watch tutorials, take = notes in our `learning-log.md` as a guide to help us go through our process and learn the process. In the last step, we found out what tool we want to use through our project and what we can make out of the project and at the same time, we can corporate and connect how we can use the tool and use the tool to create a project that we want. In this case, I chose Python/Django. Since this is a whole new process when we are learning our tool that can help us later on build our project in the Spring. This was a difficult process because there were many parts of the code that I didn't really understand. But something that helped me was to watch tutorials going online and breaking down the parts and writing comments as we went through the process had helped me a lot.


### Sources
* [Link](https://docs.djangoproject.com/en/4.2/) to the intro of documentations of how I can import Django to my browser
* [Django](https://docs.djangoproject.com/en/4.2/topics/) topics
* [Python Install](https://www.youtube.com/watch?v=fM6Cv9Wm0vw&t=173s)
* [Download](https://www.python.org/downloads/)
* [replit tinkering](https://replit.com/@jessicay1464/GlisteningGloomyEvaluations#main.py)
  * [w3schools](https://www.w3schools.com/python/trypython.asp?filename=demo_ref_string_upper)
* [Python document](https://docs.python.org/3/tutorial/index.html)
* [Python tutorial](https://www.youtube.com/watch?v=hEgO047GxaQ&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=2)


[Previous](entry01.md) | [Next](entry03.md)


[Home](../README.md)

