# Entry 4
##### 3/11/24

### How have I been learning my tool?
 * In these few weeks of tinkering, I some sort of overcome an issue. I have been watching the [python web tutorial](https://youtu.be/kng-mJJby8g?si=hR6tSHfeDS22fvKg). Also, I have been learning abotu both Flask and DJango and learned all the backends of the topic, but I found out that it was very difficult to create and build a product with only Flask and DJango, therefore, I asked Mr. Mueller to give me some advice and he told me to look through the templates from `DJango`, `Flask`, and last but not least,`Jinja`. `Jinja` was actually really new to me.
 * But before that, I have did some Flask tinkering too, in the [replit tinkering](https://replit.com/@jessicay1464/CleanAuthenticCryptos), and is linked below in the source. In this case, I followed the tutorial and continued my coding from last week. Below is the code in the for creating the different routes such as in a repo, we have different folders and files that we go through.
   * `/` is similar to `and` and also saying to `go to the next one`. At the same time, I learned that `__name__` is the first arguement that you pass in to blueprint in order to send. Also, you must have the the `__name__` before or else the `blueprint` will not be found and that there will be an error.
```python
from flask import Blueprint

view = Blueprint(__name__, "views")

@view.route("/")
def home():
  return "home page"
```
 * During the next week, I have been learning about the different templates that are coming with the data and the library. 
   * `rendering_template:` The good part about this is that we can pass in any data value into this template that later we can be rendered by it. In the `html` page, we have been tinkering about the `python` page, that later we can be passed into the `html` file through rendering it. 
   ```python
   return render__template("index.html", name=username)
   ```
   * This is mainly when we would want to have a portfolio for this code but when we define the code above, we follow the route to the profile page and then inside the profile, to find the username. 
     * What this will return is what in the `index.html` file that will be find in the `name` variable that later will be useful to get the name of the specific user. 
 * Last week, I have talked with Mr. Mueller about deep diving inside on how I can use the code that I have so far to help me build a my webpage or how can I coorperate how I can coorporate my project into our topic. In this case, Mr. Mueller have helped through the way that I can `research the templates` that are provided for us. In this case, we have learned about the three different Platforms based on what Mr. Mueller had recommended me on. 
 * All these platforms are all web frameworks in Python that we can use to help us build a webpage through the use of Python language.
#### `Flask`
  * The source that I have been using is [Flask Templates](https://flask.palletsprojects.com/en/2.3.x/tutorial/templates/)
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
            ...
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
 * I haved learned that the `g.username` is an automatic value inside the flask 
   * In this case, when the user is logged in, it can be a log-in link or a logout link that can be displayed. When we have a header, a title and a content. This can be useful in a way that everytime there is a new user, we will have this page created. We can also have a register and a login page template that I will look into later.
#### `Jinja`
   * Jinga behaves the most similar with Python. To add on, Jinja's syntax is from the static data in the [template](https://jinja.palletsprojects.com/en/3.1.x/templates/)
   * Any syntax value between the `{{ }}` is an expression that will be output to the fianl document
   * For all the `{% %}` denotes a control flow in common to the `if` and `for`. 
     * `{% ... %}` for Statements
     * `{{ ... }}` for Expressions to print to the template output
     * `{# ... #}` for Comments 
       * such as in Java, we have `//` and in Python, we have `#` as our Python comment
     * `{% if True %}` --> similar to `if`
       * `{% end if %}` --> similar to else (if this statement is true and the statement ends)

 #### `DJango`
   * Will be best for a webpage API based on the template [DJango templates](https://docs.djangoproject.com/en/5.0/ref/templates/language/).
   * In the templates, we have a text file, and that in this template, it will contain variables that will later get evaluated and that also includes the logic of the template
   * `{{ variable }}`
     * can contain alphabets and characters and underscore
     * no spaces and no underscore and may also not be a number.
   * In DJango, when we use the `.` inside the varubale name , it means that it will repalce the `title` attribute with the section object.
     * This will be a replacement 
     * similar to entering a object and a method.
   * when we have `|`, we can also select a value to add design to it such as fonts, linkbreaks, how to join words and methods that we can change the group of words in the output.

### How have we been building our MVP?
 * Looking on how we have been learning our MVP is in a way that we are currently in the state of setting up all the little pieces in a folder that later we will be using to help us build out our project itself later on. Angela and I have been spending time learning our tool but at the same time, we also have been creating all the sprites. This can be helpful for our game later so that we can just make sure that the game works the way it is. Or I can mention, the functionality of the game. To add on, we have also build up a repository that helped us organized the different files that we have, for each tool that we have because Angela and I are doing different tools, therefore this can be very helpful for us to make sure that we have the different tools organized in the correct folder. Also, for me, I have been learning through the different templates from all `DJango`, `Jinja`, and also `Flask`. This us because we are learning the different templates that makes sure that which one suits me the best for our project. 
 
### EDP (Software Engineering Process)
 * I am currently in the pace of `Step 3: Brainstorm possible solutions`, `Step 4: Planning the Most Promising solution` and also the `Step 5: Create a Prototype`. First of all, I say that we are Brainstorming possible solutions because we are learning the outcomes that we can make using python and my tool that help me build out our freedom project. This is because we have different scenes. Leading that, my partner and I build out the different versions of the game on paper first because we believe that on paper, we can visually see how we will be making the project. Furthermore, this bring us to the planning the most promising solution in a way that we have been linking out what we will be doing every single day. In this process, we have overcome some challenges such as sometimes, the code will not work as expected. Also, I would like to say somedays, we might not be able to finish the what we wanted on time. After planning out what our project will be like, we would need to start making the prototype, our project. In this case, we are taking a step now to finish all the sprites that will be appearing in the game. All three of these processes are combined in this case because building, but in some parts that I wasn't able to cover, I still had to learn on some parts of the code to help me further more understand and help my project

### Skills
 * Two skills that I have been learning with my project is `Organization` but also `How to Google`. For instance, I would say Organization because with the correct organization, our project will be organized that can help me and my partner understand the process more easily. This is because we both are visual learners, and being organized can help us structure our minds much more easily. In addition, Angela has also helped me created a repo that has also helped us a lot by making sure that all the documents are in the correct area, but also adding in file in the correct folder. This had helped us a lot too. At the same time, I would say How to Google because the use of google had helped me with my tool and is a very cool way to help me in giving me ideas and finding sources that can help me such as videos and documentaries. Moreover, after learning my tool, I was somewhat confused in a way that I didn't know how I can use my tool for the project. As I mentioned above, I asked Mr.Mueller on the different tools that later helped me dive into the different more tools that helped me with the outcome I would want. Later on, when we want to learn more about each tool, I have also find a lot of sources from Google to help me. Overall, this is why I would convey that the skills that we have learned is `Organization` and `How to Google`.

### Sources
 * [python web tutorial](https://youtu.be/kng-mJJby8g?si=hR6tSHfeDS22fvKg)
 * [Jinja templates](https://jinja.palletsprojects.com/en/3.1.x/templates/)
 * [DJango templates](https://docs.djangoproject.com/en/5.0/ref/templates/language/)
 * [Flask Templates](https://flask.palletsprojects.com/en/2.3.x/tutorial/templates/)
 * [replit tinkering](https://replit.com/@jessicay1464/CleanAuthenticCryptos)

[Previous](entry03.md) | [Next](entry05.md)

[Home](../README.md)