from django import forms

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control'}))