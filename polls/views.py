global list_register
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Register
from .forms import RegisterForm

list_register = Register.objects.all()

def index(request):
	form = RegisterForm(request.POST or None)

	if (form.is_valid()):
		form.save()
	return render(request, 'polls/index.html', {})

def test(request):
	#return redirect('/sla/')
	return render(request, 'polls/test.html', {})

def create_register(request):
	form = RegisterForm(request.POST or None)

	if (form.is_valid()):
		form.save()
	#return render(request, 'polls/index.html', {'form': form})

def return_url():
	pass
