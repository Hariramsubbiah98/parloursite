from django import forms
from .models import CallbackRequest,ReviewAndRating,blogcat

class CallbackRequestForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Name'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Email Address'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the Mobile Number'}))
    service = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'What you are interested in'}))
    message = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Say us something else'}))

    class Meta:
        model = CallbackRequest
        fields = ['name', 'email', 'phone_number', 'message', 'service']



class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewAndRating
        fields = ['author', 'title', 'rating', 'status', 'image', 'text', 'ip_address']
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter rating', 'min': 0, 'max': 5}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your review', 'rows': 3}),
            'ip_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter IP Address'}),
        }

    def clean_ip_address(self):
        ip_address = self.cleaned_data.get('ip_address')
        return ip_address
        
        
        
class blogcatform(forms.ModelForm):
    class Meta:
        model = blogcat
        fields = ['title','text','image','author','description_title1','description1','description_title2','description2']
        widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Title'}),
        'text' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Short description'}),
        'image': forms.FileInput(attrs={'class': 'form-control-file'}),
        'author':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Author name'}),
        'slug' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name for url creation'}),
        'description_title1': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your Sub Title 1'}),
        'description1':forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your Sub description 1'}),
        'description_title2': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your Sub Title 1'}),
        'description2':forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your Sub description 1'}),
        'About_Author':forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe about Author'}),
    
        }