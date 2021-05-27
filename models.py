from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Form(models.Model):
    student = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    last_saved = models.DateTimeField(blank=True, null=True)

class Assessment(models.Model):
    form = models.ForeignKey('form_builder.Form', on_delete=models.CASCADE)
    type = models.CharField(max_length=20)
    created_date = models.DateTimeField(default=timezone.now)
    
    def get_competencies(self):
        return self.competencies.filter(assessment=self.pk)
    
class Competency(models.Model):
    assessment = models.ForeignKey('form_builder.Assessment', related_name='competencies', on_delete=models.CASCADE)
    title = models.TextField()  
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title
    
    def get_performance_statements(self):
        return self.performances.filter(competency=self.pk)

class Performance(models.Model):
    competency = models.ForeignKey('form_builder.Competency', related_name='performances', on_delete=models.CASCADE)
    sn = models.IntegerField()
    label = models.TextField()
    label_type = models.CharField(max_length=18)
    criteria = models.TextField()
    outcome_title = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.sn
    
    def get_outcomes(self):
        return self.outcomes.filter(performance=self.pk)

class Outcome(models.Model):
    performance = models.ForeignKey('form_builder.Performance', related_name='outcomes', on_delete=models.CASCADE)
    outcome_type = models.CharField(max_length=2)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.outcome_type
