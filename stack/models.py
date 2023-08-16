from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class Questions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = RichTextField(blank=True, null = True)

    def __str__(self) -> str:
        return f"{self.user} asks {self.question}"

class Answers(models.Model):
    post = models.ForeignKey(Questions, on_delete=models.CASCADE)
    answer = RichTextField(blank=True, null = True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.posted_by} answers {self.post.question} by saying {self.answer}"