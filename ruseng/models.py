from django.db import models

class PhrasePairManager(models.Manager):
    def get_random_phrases(self):
        pass


class PhrasePair(models.Model):
    phrase_one = models.TextField()
    phrase_two = models.TextField()
    num = models.IntegerField(db_index=True)
