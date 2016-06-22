from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver



# Create your models here.

class Chirp(models.Model):
    body = models.CharField(max_length=141)
    created = models.DateTimeField(auto_now_add=True)
    bird = models.ForeignKey('auth.User')

    class Meta:
        ordering = ['-created']

class StopWord(models.Model):
    word = models.CharField(max_length=26)


class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    favorite_bird = models.CharField(max_length=100, null=True)

@receiver(post_save, sender=StopWord)
def say_hello(**kwargs):
    print("Hello world")

@receiver(post_save, sender='auth.User')
def create_user_profile(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')

    if created:
        Profile.objects.create(user=instance)
