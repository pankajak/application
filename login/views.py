from login.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.template import loader

@csrf_protect
def register(request):
	  if request.method == 'POST':
	  	 form = RegistrationForm(request.POST)
	  	 print request.POST['username']
	  	 if form.is_valid():
	  	 	user = User.objects.create_user(
	  	 	username=form.cleaned_data['username'],
	  	 	password=form.cleaned_data['password1'],
	  	 	email=form.cleaned_data['email']
	  	 	)
	  	 	return HttpResponseRedirect('/register/success/')
	  else:
	  	  form = RegistrationForm()
	  variables = RequestContext(request,{
	  'form': form
	  	})

	  return render_to_response(
	  'registration/register.html',
	  variables,
	  )

def register_success(request):
	  return render_to_response(
	  'registration/success.html',
	  )

def index(request):
	template = loader.get_template('registration/index.html')
	context = {}
	return HttpResponse(template.render(context, request))

def logout_page(request):
	  logout(request)
	  return HttpResponseRedirect('/')

@login_required
def home(request):
	return HttpResponse("You're looking at home ")

	return render_to_response(
	  'home.html',
	  {  'user': request.user }
	)

# Added by PK
def login(request):
	return HttpResponse("Login page!!")
