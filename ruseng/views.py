from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from ruseng.models import PhrasePair, Settings
from ruseng.forms import SettingsForm

@login_required
def home(request):
    """
    App home page
    """
    if request.method == 'GET':
        text = PhrasePair.objects.get_random_phrases(user=request.user)
        #import ipdb; ipdb.set_trace()
        context = {'user': request.user, 'text': text}
        return render(request, 'ruseng/index.html', context)

@login_required
def get_data(request):
    text = PhrasePair.objects.get_random_phrases(user=request.user)
    return JsonResponse({'data':text})


def profile(request):
    """
    ...
    """
    if request.method == 'GET':
        pass

def about(request):
    """
    ...
    """
    if request.method == 'GET':
        return render(request, 'ruseng/about.html')


def settings(request):
    """
    Form for setting
    """
    if request.method == 'POST':
        #import ipdb; ipdb.set_trace()
        form = SettingsForm(request.POST)
        if form.is_valid():
            phrase_count = form.cleaned_data['phrase_count']
            api_url = form.cleaned_data['api_url']
            api_token = form.cleaned_data['api_token']
            default_deck = form.cleaned_data['default_deck']

            try:
                settings = Settings.objects.get(user=request.user)
                settings.phrase_count = phrase_count
                settings.api_url = api_url
                settings.api_token = api_token
                settings.default_deck = default_deck
                settings.save()

            except ObjectDoesNotExist:
                Settings.objects.create(user=request.user, phrase_count=phrase_count,
                                        api_url=api_url, api_token=api_token,
                                        default_deck=default_deck)
            return HttpResponseRedirect('/ruseng/')

    else:
        form_data = {}
        try:
            settings = Settings.objects.get(user=request.user)
            form_data['phrase_count'] = settings.phrase_count
            form_data['api_url'] = settings.api_url
            form_data['api_token'] = settings.api_token
            form_data['default_deck'] = settings.default_deck

        except ObjectDoesNotExist:
            form_data['phrase_count'] = 1
            form_data['api_url'] = ''
            form_data['api_token'] = ''
            form_data['default_deck'] = ''
        form = SettingsForm(form_data)

    return render(request, 'ruseng/settings.html', {'user': request.user, 'form':form})




