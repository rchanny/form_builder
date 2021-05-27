from django import forms
from django.forms import widgets
from .models import Form, Assessment, Competency, Performance, Outcome

assessment_types = [
    ('','Choose a value'),
    ('report','Project Report'),
    ('presentation', 'Project Presentation')
]

performance_types = [
    ('abilities','ABILITIES (A)'),
    ('knowledge','KNOWLEDGE (K)')
]

outcome_types = [
    ('c', 'C'),
    ('nyc','NYC'),
]

class AssessmentForm(forms.ModelForm):
    type = forms.CharField(label="", widget=forms.Select(choices=assessment_types, attrs={'class': 'form-select form-select-sm'}))
    class Meta:
        model = Assessment
        fields = ('type',)


class CompetencyForm(forms.ModelForm):
    class Meta:
        model = Competency 
        fields = ('title',)

        widgets = {
            'title': forms.TextInput(attrs={'placeholder':'Type here...', 'class': 'form-control'})
        }

class PerformanceForm(forms.ModelForm):
    sn = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='')
    label = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Type here...','rows': 4,'class': 'form-control'}), label="")
    label_type = forms.CharField(widget=forms.RadioSelect(choices=performance_types, attrs={'class': 'form-check-input'}))
    criteria = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Type here...','rows': 4, 'class': 'form-control'}), label="")
    outcome_title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Input value','class': 'form-control'}), label='')

    class Meta:
        model = Performance 
        fields = ('sn','label','label_type','criteria','outcome_title')


class OutcomeForm(forms.ModelForm):
    outcome_type = forms.ChoiceField(label="", choices=outcome_types, widget=forms.Select(attrs={'class':'form-select form-select-sm'}))
    class Meta:
        model = Outcome
        fields = ('outcome_type',)

        



