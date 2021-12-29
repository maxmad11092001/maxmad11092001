from django.db import models
from django.utils.regex_helper import Choice

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    time_pub = models.DateField()

    class Choice(models.Model):
        question = models.ForeignKey(Question, on_delete=models.CASCADE)
        Choice_text = models.CharField(max_length=100)
        vote = models.IntegerField(default=0)