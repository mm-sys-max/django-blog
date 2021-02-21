from django.db import models

# Create your models here.



class Articles(models.Model):


    title = models.CharField(max_length = 50)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now = True)

    def __str__(self):
        title = f" name : {self.title}"
        return title
    def snipped(self):
        Text = f"{self.body[:25]} .... "
        return Text
