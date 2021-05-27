from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Form, Assessment, Competency, Performance, Outcome
from .forms import AssessmentForm, CompetencyForm, PerformanceForm, OutcomeForm
from django.views.generic import (FormView)
from django.urls import reverse_lazy
from json import dumps

# Create your views here.
def main_page(request):
    tmpl_vars = {
        'assessment_form': AssessmentForm(),
        'competency_form': CompetencyForm(),
        'performance_form': PerformanceForm(), 
        'outcome_form': OutcomeForm(),
    }
    return render (request, 'form_builder/assessment.html',tmpl_vars)


   

