from django import forms
from .models import Article

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30,widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control'}))
    
    
class NewArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['editor', 'pub_date']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }