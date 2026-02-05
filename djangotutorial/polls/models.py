from django.db import models

# Create your models here.
class users (models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    def __str__(self):
        return (f"{self.first_name} {self.last_name} {self.email}")
    
class FormModel(models.Model):
    title = models.CharField(max_length=200)
    discription = models.TextField()
    last_modified = models.DateTimeField(auto_now_add=True)
    #img = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.title