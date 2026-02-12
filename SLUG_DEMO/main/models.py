from django.db import models
from django.urls import reverse
# Create your models here.
class Course_detail(models.Model):
    course_name = models.CharField(max_length=155)
    course_code = models.CharField(max_length=155)
    course_description = models.TextField()

    def __str__(self):
        return self.course_name
    
    def get_absolute_url(self):
        return reverse("model_detail", args=[str(self.id)])
    
class Post(models.Model):
    title = models.CharField(max_length= 200)
    content = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.title.replace(" ", "-").lower()
        super().save(*args, **kwargs)   

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.slug)])    
    