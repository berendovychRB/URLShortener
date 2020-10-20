from django import forms

from .validators import validate_url


class SubmitUrlForm(forms.Form):
    url = forms.CharField(label='',
                          validators=[validate_url],
                          widget= forms.TextInput(attrs={'placeholder': 'Long URL',
                                                         'class': 'form-control'}))

    # def clean(self):
    #     cleaned_data = super(SubmitUrlForm, self).clean()
    #     url = cleaned_data('url')
    #     url_validator = URLValidator()
    #     try:
    #         url_validator(url)
    #     except:
    #         raise forms.ValidationError('Invalid URL for this field')
    #     return url

    # def clean_url(self):
    #     url = self.cleaned_data['url']
    #     if 'http' in url:
    #         return url
    #     return 'http://' + url
