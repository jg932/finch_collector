from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello finches!</h1>')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  return render(request, 'cats/index.html', { 'finches': finches })