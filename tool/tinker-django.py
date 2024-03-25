from django.http import HttpResponse
from django.template import loader

def members(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())

# above is used to render what is inside the html and then trnasfereed used the data from python
# back into the work branch of django and back into print out in webpage.