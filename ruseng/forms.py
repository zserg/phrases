from django import forms

class SettingsForm(forms.Form):
    phrase_count = forms.IntegerField(label='Phrase count')
    api_url = forms.URLField(label='API URL')
    api_token = forms.CharField(label='API token')
    default_deck = forms.CharField(label='Default deck name')


