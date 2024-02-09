from django import forms


class Emailforms(forms.Form):
    name=forms.CharField(max_length=255)
    email=forms.EmailField()
    to=forms.EmailField()
    comments=forms.TimeField(required=False,widget=forms.Textarea)
    file = forms.FileField()
    image = forms.ImageField()