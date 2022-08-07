from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('rocks/', views.rocks_index, name='rocks_index'),
  path('rocks/<int:rock_id>/', views.rocks_detail, name='rocks_detail'),
  path('rocks/create/', views.RockCreate.as_view(), name='rocks_create'),
  path('rocks/<int:pk>/delete/', views.RockDelete.as_view(), name='rocks_delete'),
  path('rocks/<int:pk>/update/', views.RockUpdate.as_view(), name='rocks_update'),
  path('rock/<int:rock_id>/add_cleaning/', views.add_cleaning, name='add_cleaning'),
  path('paintings/create/', views.PaintingCreate.as_view(), name='paintings_create'),
  path('paintings/<int:pk>/', views.PaintingDetail.as_view(), name='paintings_detail'),
  path('paintings/', views.PaintingList.as_view(), name='paintings_index'),
  path('paintings/<int:pk>/update/', views.PaintingUpdate.as_view(), name='paintings_update'),
  path('paintings/<int:pk>/delete/', views.PaintingDelete.as_view(), name='paintings_delete')

]