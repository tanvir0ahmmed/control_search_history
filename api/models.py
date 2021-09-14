from django.db import models

# Create your models here.
class UserSearchHistory(models.Model):
    username = models.CharField(max_length=20,unique=False)
    search_keyword = models.CharField(max_length=200,unique=False)
    searched_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return str(self.search_keyword) + ' ' + str(self.searched_at)
    
class Smartphone(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name