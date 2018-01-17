from django.db import models

# Create your models here.


class Users(models.Model):
    username_text = models.CharField(max_length=30)
    password_text = models.CharField(max_length=30)
    user_phone = models.IntegerField(default=0)
    user_emil = models.EmailField
    user_address = models.CharField(max_length=200)
    user_card = models.IntegerField(default=0)
    user_sex = models.CharField(max_length=10)
    user_birthday = models.DateTimeField('user birthday')

    def __str__(self):
        return self.username_text
