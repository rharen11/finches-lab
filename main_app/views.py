from django.shortcuts import redirect, render
from .models import Rock
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CleaningForm

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def rocks_index(request):
  rocks = Rock.objects.all()
  return render(request, 'rocks/index.html', {'rocks': rocks})

def rocks_detail(request, rock_id):
  rock = Rock.objects.get(id=rock_id)
  cleaning_form = CleaningForm()
  return render(request, 'rocks/detail.html', {'rock': rock, 'cleaning_form': cleaning_form})

def add_cleaning(request, rock_id):
  form = CleaningForm(request.POST)
  if form.is_valid():
    new_cleaning = form.save(commit=False)
    new_cleaning.rock_id = rock_id
    new_cleaning.save()
  return redirect('rocks_detail', rock_id=rock_id)

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
