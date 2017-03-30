from django.db import models
from random import randint

class PhrasePairManager(models.Manager):
    def get_random_phrases(self, count):
        max_num = PhrasePair.objects.order_by('-num')[0].num
        idx = randint(0,max_num)
        text = PhrasePair.objects.filter(num__gte = idx).order_by('num')[:count]
        #import ipdb; ipdb.set_trace()
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

