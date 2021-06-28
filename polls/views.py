from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request, 'polls/index.html', {})

def test(request):
	#return redirect('/sla/')
	return render(request, 'polls/test.html', {})
