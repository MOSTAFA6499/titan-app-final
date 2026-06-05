from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [('starter','شروع کننده'),('advisor','مشاور'),('manager','منیجر'),('pre_leadership','Pre Leadership'),('leadership','Leadership'),('owner','مالک سازمان')]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='starter')
    phone = models.CharField(max_length=15, blank=True)
    team = models.ForeignKey('Team', on_delete=models.SET_NULL, null=True, blank=True)
    upline = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

class Team(models.Model):
    TEAM_TYPES = [('titan_the_great','Titan The Great'),('titanpro','TitanPro'),('alpha','Alpha'),('titan','Titan'),('immortal','Immortal'),('golden_knights','Golden Knights')]
    name = models.CharField(max_length=50, choices=TEAM_TYPES)
    leader = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
