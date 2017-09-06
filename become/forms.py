from django import forms
from tutorprofile.models import TutorProfile

class BecomeForm(forms.ModelForm):
    #transcript = forms.FileField()
    anything_else = forms.CharField(label="Anything Else?", required=False)
    class Meta:
        model = TutorProfile
        fields = (
            'name',
            'school',
            'city',
            'email',
            'phone',
        )
