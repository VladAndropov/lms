from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response

# Create your views here.

def basic_one(request):
	view1 = "basic_one"
	html = "<html><body>this %s view</body></html>" % view1
	return HttpResponse(html)

def template_two(request):
	t = get_template('myview.html')
	html = t.render(Context({'name': "the text for view2 func"}))
	return HttpResponse(html)

def template_three(request):
	
	return render_to_response('myview.html',{'name':"text of template three func"})