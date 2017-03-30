from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from ruseng.models import PhrasePair

@login_required
def home(request):
    """
    App home page
    """
    if request.method == 'GET':
        count = int(request.GET.get('count',1))
        text = PhrasePair.objects.get_random_phrases(count)
        #import ipdb; ipdb.set_trace()
        context = {'user': request.user, 'text': text}
        return render(request, 'ruseng/index.html', context)

@login_required
def get_data(request):
    count = int(request.GET.get('count',1))
    text = PhrasePair.objects.get_random_phrases(count)
    #import ipdb; ipdb.set_trace()
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
