from django import forms
from .models import Thread, Post


class ThreadForm(forms.ModelForm):
    name = forms.CharField(label="Client Name")
    DOB = forms.CharField(label="Date Of birth")
    diagnosis = forms.CharField(label="Diagnosis")
    GMFCS = forms.CharField(label="GMFCS Level")
    therapist = forms.CharField(label="Therapist")
    lying = forms.CharField(label="Lying")
    sitting = forms.CharField(label="Sitting")
    standing = forms.CharField(label="Standing")
    walking = forms.CharField(label="Walking")
    Hipxray = forms.CharField(label="Date of last Hip x-ray")
    NextHipxray = forms.CharField(label="Next Hip X-ray due")
    spineXray = forms.CharField(label="Date of last spine x-ray")
    NextspineXray = forms.CharField(label="Next spine X-ray due")
    BTXA = forms.CharField(label="BTX-A")
    baclofen = forms.CharField(label="Baclofen")
    SDR = forms.CharField(label="SDR")
    other = forms.CharField(label="Other")
    PreviousOrthopaedicManagement = forms.CharField(label="Previous Orthopaedic Management")
    OrthopaedicGoals = forms.CharField(label="Orthopaedic Goals")
    FunctionalGoals = forms.CharField(label="Functional Goals")

    class Meta:
        model = Thread
        fields = ['name', 'DOB', 'diagnosis', 'GMFCS', 'therapist', 'lying', 'sitting', 'standing', 'walking',
                  'Hipxray', 'NextHipxray', 'spineXray', 'NextspineXray', 'BTXA', 'baclofen',
                  'PreviousOrthopaedicManagement', 'OrthopaedicGoals', 'FunctionalGoals']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['comment']



