from django.shortcuts import redirect, render
from .models import Rock, Painting
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CleaningForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def rocks_index(request):
  rocks = Rock.objects.filter(user=request.user)
  return render(request, 'rocks/index.html', {'rocks': rocks})

@login_required
def rocks_detail(request, rock_id):
  rock = Rock.objects.get(id=rock_id)

  paintings_available = Painting.objects.exclude(id__in = rock.paintings.all().values_list('id'))

  cleaning_form = CleaningForm()

  return render(request, 'rocks/detail.html', {'rock': rock, 'cleaning_form': cleaning_form, 'paintings': paintings_available})

@login_required
def add_cleaning(request, rock_id):
  form = CleaningForm(request.POST)
  if form.is_valid():
    new_cleaning = form.save(commit=False)
    new_cleaning.rock_id = rock_id
    new_cleaning.save()
  return redirect('rocks_detail', rock_id=rock_id)

class RockCreate(LoginRequiredMixin, CreateView):
  model = Rock
  fields = ['type', 'color', 'description', 'location']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  success_url= '/rocks/'

class RockUpdate(LoginRequiredMixin, UpdateView):
  model = Rock
  fields= ['type', 'color', 'description', 'location']

class RockDelete(LoginRequiredMixin, DeleteView):
  model = Rock
  success_url= '/rocks/'

class PaintingCreate(LoginRequiredMixin, CreateView):
  model = Painting
  fields = '__all__'

class PaintingList(LoginRequiredMixin, ListView):
  model = Painting

class PaintingDetail(LoginRequiredMixin, DetailView):
  model = Painting

class PaintingUpdate(LoginRequiredMixin, UpdateView):
  model = Painting
  fields = ['title', 'color']

class PaintingDelete(LoginRequiredMixin, DeleteView):
  model = Painting
  success_url = '/paintings/'

@login_required
def assoc_painting(request, rock_id, painting_id):
  Rock.objects.get(id=rock_id).paintings.add(painting_id)
  return redirect('rocks_detail', rock_id=rock_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in
      login(request, user)
      return redirect('rocks_index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
  # Same as: return render(request, 'signup.html', {'form': form, 'error_message': error_message})
