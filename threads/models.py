from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from django.conf import settings


class Subject(models.Model):

    name = models.CharField(max_length=255, default='SOME STRING')
    description = HTMLField()

    def __unicode__(self):
        return self.name


class Thread(models.Model):

    name = models.CharField(max_length=255, default='SOME STRING')
    DOB = models.CharField(max_length=255, default='SOME STRING')
    diagnosis = models.CharField(max_length=255, default='SOME STRING')
    GMFCS = models.CharField(max_length=255, default='SOME STRING')
    therapist = models.CharField(max_length=255, default='SOME STRING')
    lying = models.CharField(max_length=255, default='SOME STRING')
    sitting = models.CharField(max_length=255, default='SOME STRING')
    standing = models.CharField(max_length=255, default='SOME STRING')
    walking = models.CharField(max_length=255, default='SOME STRING')
    Hipxray = models.CharField(max_length=255, default='SOME STRING')
    NextHipxray = models.CharField(max_length=255, default='SOME STRING')
    spineXray = models.CharField(max_length=255, default='SOME STRING')
    NextspineXray = models.CharField(max_length=255, default='SOME STRING')
    BTXA = models.CharField(max_length=255, default='SOME STRING')
    baclofen = models.CharField(max_length=255, default='SOME STRING')
    SDR = models.CharField(max_length=255, default='SOME STRING')
    other = models.CharField(max_length=255, default='SOME STRING')
    PreviousOrthopaedicManagement = models.CharField(max_length=255, default='SOME STRING')
    OrthopaedicGoals = models.CharField(max_length=255, default='SOME STRING')
    FunctionalGoals = models.CharField(max_length=255, default='SOME STRING')
   
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='threads')
    subject = models.ForeignKey(Subject, related_name='threads')
    created_at = models.DateTimeField(default=timezone.now)


class Post(models.Model):

    thread = models.ForeignKey(Thread, related_name='posts')
    comment = HTMLField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts')
    created_at = models.DateTimeField(default=timezone.now)


