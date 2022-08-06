from django.shortcuts import render
from .models import Rock
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def rocks_index(request):
  rocks = Rock.objects.all()
  return render(request, 'rocks/index.html', {'rocks': rocks})

def rocks_detail(request, rock_id):
  rock = Rock.objects.get(id=rock_id)
  return render(request, 'rocks/detail.html', {'rock': rock})

class RockCreate(CreateView):
  model = Rock
  fields = '__all__'
  success_url= '/rocks/'

class RockUpdate(UpdateView):
  model = Rock
  fields= ['type', 'color', 'description', 'location']

class RockDelete(DeleteView):
  model = Rock
  success_url= '/rocks/'