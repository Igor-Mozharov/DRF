from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    date = models.DateField(blank=False, null=False)
    location = models.CharField(max_length=50, blank=False, null=False)
    organizer = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        ordering = ['date']


class EventRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'event')

    def __str__(self):
        return f'{self.user.username}: {self.event.title}'