from django.db import models
from django.urls import reverse

DAYS = (
  ('M', 'Monday'),
  ('T', 'Tuesday'),
  ('W', 'Wednesday'),
  ('Th', 'Thursday'),
  ('F', 'Friday'),
  ('S', 'Saturday'),
  ('Sun', 'Sunday')
)

class Rock(models.Model):
  type = models.CharField(max_length=100)
  color = models.CharField(max_length=50)
  description = models.TextField(max_length=300)
  location = models.CharField(max_length=50)

  def __str__(self):
    return self.type

  def get_absolute_url(self):
      return reverse("rocks_detail", kwargs={"rock_id": self.id})

class Cleaning(models.Model):
  day = models.CharField(
    max_length=8,
    choices=DAYS,
    default=DAYS[0][0]
    )
  month = models.CharField(
    'Month Cleaned',
    max_length=8,
    )

  rock = models.ForeignKey(Rock, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_day_display()} in {self.month}"

  # class Meta:
  #   ordering = ['-date']


  