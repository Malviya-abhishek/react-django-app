from django.db import models

# Create your models here.
class Article(models.Model):
    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    title = models.CharField(max_length=120)
    content = models.TextField()

    
    def __str__(self):
        return self.title


