from django import forms
from default import models

class InsertEventForm(forms.ModelForm):

    class Meta:
        model = models.Event
        fields = "__all__"
        exclude = ("updated_at", "created_at",)