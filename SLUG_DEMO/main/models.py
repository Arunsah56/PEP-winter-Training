# from django.db import models
# from django.urls import reverse
# from django.utils.text import slugify
    
# class Article(models.Model):
#     title = models.CharField(max_length= 200)
#     body = models.TextField()
#     slug = models.SlugField(unique=True, blank=True, null=True)

#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.title)
#         super().save(*args, **kwargs)
    
#     def __str__(self):
#         return self.title
    
#     def get_absolute_url(self):
#         # return reverse("article_detail", args=[str(self.id)])
#         return reverse("article_detail", kwargs=[str(self.slug)])
    
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})
