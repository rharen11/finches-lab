from django.shortcuts import render

from django.http import HttpResponse

def home(request):
  return HttpResponse('<h1>Finches</h1>')

def about(request):
  return render(request, 'about.html')

class Rock:
  def __init__(self, color, description, location):
    self.color = color
    self.description = description
    self.location = location

rocks = [
  Rock('red', 'shiny', 'beach'),
  Rock('brown', 'lumpy', 'yard')
]

def rocks_index(request):
  return render(request, 'rocks/index.html', {'rocks': rocks})
