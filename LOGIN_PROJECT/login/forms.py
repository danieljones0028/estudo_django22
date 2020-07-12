from django import forms

class LoginForm(forms.Form):
    error_css_class = 'error'
    required_css_class = 'required'
    auto_id = True
    your_name = forms.CharField(label='Your name', max_length=100)