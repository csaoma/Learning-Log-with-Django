from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    # topic to the user wants to learn
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text



class Entry(models.Model):
    # Something specific learned

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    '''
    Topic is a foreign key instance. 
    It will connect the Topic Class to the Entry class through the database.
    
    The attribute on_delete will tell Django 
    that when a topic is deleted all entries associated 
    with it will also be deleted.
    '''
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='entries'

    def __str__(self):
        # Return string representation of the first 50 characters from the model
        return f'{self.text[:50]}...'
