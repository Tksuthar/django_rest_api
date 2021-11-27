from django.db import models

class UserModel(models.Model):
    user_fname = models.CharField(max_length=100)
    user_lname = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)


    def __str__(self):
        return self.user_fname + self.user_lname
