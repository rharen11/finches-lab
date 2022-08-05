from django.db import models

class Rock(models.Model):
  type = models.CharField(max_length=100)
  color = models.CharField(max_length=50)
  description = models.TextField(max_length=300)
  location = models.CharField(max_length=50)

  def __str__(self):
    return self.type