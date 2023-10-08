from django.db import models

# Create your models here.
class LoginDetails(models.Model):
    #UserID = models.CharField(max_length=50, unique=True)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Email = models.EmailField()
    Password = models.CharField(max_length=128)  # You should consider using a secure password hashing method, not plain text.

    def __str__(self):
        return self.UserID  # You can change this to display a different field in the admin panel or elsewhere

    class Meta:
        verbose_name_plural = "Login Details"