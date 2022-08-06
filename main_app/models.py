from django.db import models
from django.urls import reverse

class Rock(models.Model):
  type = models.CharField(max_length=100)
  color = models.CharField(max_length=50)
  description = models.TextField(max_length=300)
  location = models.CharField(max_length=50)

  def __str__(self):
    return self.type

  def get_absolute_url(self):
      return reverse("rocks_detail", kwargs={"rock_id": self.id})
  