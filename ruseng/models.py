from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from random import randint

class PhrasePairManager(models.Manager):
    def get_random_phrases(self, user):
        try:
            settings = Settings.objects.get(user=user)
            count = settings.phrase_count
        except ObjectDoesNotExist:
            count = 1

        max_num = PhrasePair.objects.order_by('-num')[0].num
        idx = randint(0,max_num)
        text = PhrasePair.objects.filter(num__gte = idx).order_by('num')[:count]
        data = {'one':[], 'two':[]}
        for t in text:
            data['one'].append(t.phrase_one)
            data['two'].append(t.phrase_two)
        print('{} - {}'.format(idx,data))
        return data


class PhrasePair(models.Model):
    phrase_one = models.TextField()
    phrase_two = models.TextField()
    num = models.IntegerField(db_index=True)

    objects = PhrasePairManager()

class Settings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # max phrase count on screen
    phrase_count = models.IntegerField()

    #API settings
    api_url = models.URLField()
    api_token = models.CharField(max_length=256)

    # default API deck name to store phrase
    default_deck = models.CharField(max_length=256)

