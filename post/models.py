from django.db import models
from a_users.models import Profile
from django.contrib.auth.models import User

class post_model(models.Model):
    content=models.CharField(max_length=300, blank=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    post_image=models.ImageField(default="post_image/jorge-zapata-4nXkhLCrkLo-unsplash.jpg",upload_to="post_image/")
    created=models.DateTimeField(auto_now=True)

   # date_posted=models.DateTimeField(auto_created=True)
    def __str__(self):
        return self.content