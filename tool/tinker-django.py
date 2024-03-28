from django.http import HttpResponse
from django.template import loader

def members(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())

# above is used to render what is inside the html and then trnasfereed used the data from python
# back into the work branch of django and back into print out in webpage.

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'members'
] 

# The code above is to show the rendered link that is happening with beyond and connecting the background
# and the current code that is happening. 
