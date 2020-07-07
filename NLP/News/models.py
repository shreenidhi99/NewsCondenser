from django.db import models

# Create your models here.

class News_DB(models.Model):
    article_link=models.CharField(max_length=500,unique=True)
    article_title=models.CharField(max_length=500)
    article_timestamp=models.CharField(max_length=150)
    article_intro=models.TextField()
    article_body=models.TextField()

class Term(models.Model):
	keyword = models.CharField(max_length=100)
