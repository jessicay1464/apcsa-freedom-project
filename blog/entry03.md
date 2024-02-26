# Entry 3
##### 2/5/24

### Content 
Throughout these weeks of tinkering, I have been absoluting stunned with my learning with my tool because I have been following a tutorial and that have introduced me to a lot of topics such as the use of Flask. I learned that Flask is a programming library that has languages that have helped me in the use of designing web pages. Such as the use of Django, they have a similar achievement. For instance, we have learned about the different files that we have to create and learn such as the creation of the `view.py` and the `main.py`. <br>
<br>
In this process, I have been learning about the topic about the idea of Flask through the use of Replit. This tinkering, I have link below in the sources. In the process of tinkering, I have learned 

```python
app = Flask(__name__)

if __name__ == '__main__':
  app.run(debug=True, port=8000)
```
In the code above, we have learned about the idea of how we can connect the two files together. Such as the `main.py` and the `app.py`. In this case, I have learned that the value stored the `debug=True` and `port=8000` is stored and that it is similar to the css style that styles the word in the what the programmer will be typing in. But also, I have learned that this is mutable, which means that the value can and will be able to change depending on the programmer. When I have learned the code, 
```python
from flask import Blueprint
# view.py
# @app.route("/")
# def home():
# return "this is the home page"
```
In this code above, we will find that when you run this code, the `return "this is the home page"` will be shown in the webpage. Throughout this process, I have tried to follow this tutorial to follow the steps as listed above, I was to watch more videos that has an install in python. However, I have finished watching this tutorial and got the idea of how we can combine the use of `python` and `Flask` to help me learn the structure of the website and that I have learned a lot. Later on after a few days, I have got an understanding in the different numbers and the datatype of numbers that are existed in python. Later on during the week, I have continued with my learning my tool with  
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
In this code above, I have followed the tutorial and learned to create a little project that we have created where the user login and says hello to the username. In this case, I have learned about how
 * At first, I don't know what was the `@app.route` was used. Therefore, I went onto google to help me understand what this was used for, therefore, as I go onto google, I have undrstand that `@app.route` will make the code back to recall what you code have been creating. It is like saying, "Now let's run the code."
 * `'index.html',` 
   * In the tinkering with python, I have also learned to use `index.html` and `styles.css` to create it more visually appealing. Inside, I played around with the `styles.css` and the `HTML` file to help me see with numbers and and classes are connected with each other. There was also a login page in the tutorial that I would want to change some parts of a code to see what else I can input. Connecting this to our freedom project, we would want to use the webpage that I have created using python to create this menu that can be useful in creating our overall freedom project.
   * The purpose of writing this in the HTML is to set them into classes so that we can later use `style.css` connected to the `python` that we can later style and the project in any way that we want to make the webview what want it to look like.
 * Following the tutorial, I continued with learning my tool with the assistance of FLASK to help with python in learning the code and making sure that it prints out the code the way we want it to be and look like. In this case, we need a `view.py`. This was what I wrote in the learning log referred to last week. In `view.py` we can use this code to help me view the code later on in the webview.

### What is my plan for the Spring Break
During the Spring Break, I would like to create a MVP for our project that we have planned out on paper. My partner will be working on her side of the game and then for my side, I will use python to create a part of my webpage. We will be creating a webpage that contains a the menu that can be used for her game. At the same time, I will be incorporating what we learned with the inputs of data and many more to help me ti mka  my webpage more interactive and more fun. This time, we have already have a way to connect our tools but now, we just need a little something that we cerate to test this hypothesis out, and this took a really long time because we have been focusing a lot on the tiny details and learning the tool in parts and therefore, during the break, we would want to  test out our tools and create a MVP and after break, we would want to make it more appealing. 

### Skills
 Two skills that I have accomplished while tinkering in these few weeks of tinkering will be `How to Google` and `Problem Decomposition` because in these cases, I was able to use Googl e, as a tool to help me understand and learn the tool. In some cases, when I look through some parts of the code, I have met some misunderstandings and difficulties. With the help of Google, I was able to continue with my journey with Python and finding out how we can continue with my project with the connection of python through the videos and webpages such as [w3schools](https://www.w3schools.com/python/). To add on, I would also say Problem Decomposition because although I was able to use Python to print out the words that I wanted, I found out that it was really difficult to create into a webpage due to the reason that it was really more in common to backend of the code and more making the webpage more visually appearing. However, linking it back to the other skill that I have accomplished in on being able to How to Google, I was able to use Google to help me discovered the other platform and was `Flask` that I can also use to help me create my webpage. Overall, being able to `How to Google` was a skill that I have achieved that I was able to use in `Problem Decompositioning`.

### EDP
During these few weeks of tinkering our tool and processing, I can say that we are still in the process of `Researching the Problem` but at the same time, moving ourselves into the Step 3 and that is to `Brainstorm Possible Solutions`. For instance, we have been tinkering and learning with our tools and being more into a deep understanding of how to use and how we can incorporate that into our project in the future. Furthermore, I have been learning how use Python but also learning how to use Flask to help me in the designs of the webpage. On the other hand, my partner, Angela and I have been planning out and thinking how on how we would want our project to look like and incorporating how we can make the project the way we want. But also, we have also started to draw the sprites that we want to use to make the project after a few weeks.

### Sources
 * [python web tutorial](https://youtu.be/kng-mJJby8g?si=hR6tSHfeDS22fvKg)
 * [w3schools loops](https://www.w3schools.com/python/python_for_loops.asp) 
 * [python web tutorial](https://youtu.be/kng-mJJby8g?si=hR6tSHfeDS22fvKg)

[Previous](entry02.md) | [Next](entry04.md)

[Home](../README.md)