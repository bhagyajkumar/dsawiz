from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="")
