from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    """
    App home page
    """
    if request.method == 'GET':
        text = PhrasePair.objects.get_random_phrases(owner=request.user)
        #import ipdb; ipdb.set_trace()
        context = {'user': request.user, 'text': text}
        return render(request, 'ruseng/index.html', context)

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
