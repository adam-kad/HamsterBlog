from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(label='Email', required=True)
    subject = forms.IntegerField(min_value=11, label='Number', required=True)
    your_name = forms.CharField(label='Name', max_length=50, required=True)
    message = forms.CharField(label='Message', widget=forms.Textarea, required=True)

