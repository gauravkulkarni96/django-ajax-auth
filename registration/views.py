# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login
from forms import SignUpForm
from tokens import account_activation_token
from django.http import HttpResponse, HttpResponseRedirect
import json


def home(request):
	return render(request, 'home.html')

def loginUser(request):
	email= request.POST.get('email')
	password = request.POST.get('password')
	# stayloggedin = request.GET.get('stayloggedin')
	# if stayloggedin == "true":
	  #  pass
	# else:
	  #  request.session.set_expiry(0)
	user = authenticate(email=email, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			return HttpResponse(json.dumps({"message": "Success"}),content_type="application/json")
		else:
			return HttpResponse(json.dumps({"message": "inactive"}), content_type="application/json")
	else:
		return HttpResponse(json.dumps({"message": "invalid"}),content_type="application/json")
	return HttpResponse(json.dumps({"message": "denied"}),content_type="application/json")

def signup(request):
	if request.user.is_authenticated():
		return redirect('/')
	if request.method == 'POST':
		fname = request.POST.get('first_name')
		lname = request.POST.get('last_name')
		email = request.POST.get('email')
		password1 = request.POST.get('password1')
		password2 = request.POST.get('password2')
		data = {'first_name':fname, 'last_name':lname, 'email':email, 'password2':password2, 'password1':password1}
		form = SignUpForm(data = data)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_active = True
			user.save()
			return HttpResponse(json.dumps({"message": "Success"}),content_type="application/json")
		else:
			return HttpResponse(json.dumps({"message":form.errors}),content_type="application/json")
	else:
		form = SignUpForm()
	return HttpResponse(json.dumps({"message": "Denied"}),content_type="application/json")
	# return render(request, 'registration/signup.html', {'form':form})