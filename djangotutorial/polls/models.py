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
    
from django.contrib.auth.hashers import make_password, identify_hasher, check_password

class LoginUser(models.Model):
    # simple login user name model stored separately from dgango auth user

    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def set_password(self, raw_password: str) -> None:
        # Hash and set a raw password
        self.password = make_password(raw_password)

    def check_password(self, raw_password: str) -> bool:
        return check_password(raw_password, self.password)
    

    def save(self, *args, **kwargs):

        try:
            identify_hasher(self.password)
        except ValueError:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
    
  

class SingupUser(models.Model):

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def set_password(self, raw_password: str) -> None:
        self.password = make_password(raw_password)

    def check_password(self, raw_password: str) -> bool:
        return check_password(raw_password, self.password)
    
    def save(self, *args, **kwargs):
        try:
            identify_hasher(self.password)
        except ValueError:
            self.password = make_password(self.password)

        super().save(*args, **kwargs)

        # keep LoginUser in sync so login view works without extra logic 
        login_user, created = LoginUser.objects.get_or_create(username=self.username)
        login_user.password = self.password # already hased above 
        login_user.is_active = self.is_active
        login_user.save()

        def __str__(self):
            return self.username
        
# create your model here.

class tea(models.Model):
    user = models.ForeignKey(users, on_delete=models.CASCADE)
    text = models.TextField(max_length=240)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.text[:10]}"