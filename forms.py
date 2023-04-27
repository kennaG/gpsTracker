from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from hrapp.models import *

from django import forms
from django.forms import ModelForm


# class Timelogs(ModelForm):
# 	class Meta:
# 		model = Timelogs
# 		fields = ["description","assignment_date"]

# class timerequest(ModelForm):
# 	class Meta:
# 		model = timerequests
# 		fields = ["employee_id","manager_id","start_date",
# 		"end_date","number_of_days","Notes"]