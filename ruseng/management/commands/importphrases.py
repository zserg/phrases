from django.core.management.base import BaseCommand, CommandError
from django.db import reset_queries

from ruseng.models import PhrasePair
#from memory_profiler import profile

LIMIT = 100000
BULK_SIZE = 100000

class Command(BaseCommand):
    help = 'Import phrases from files to database'

    def add_arguments(self, parser):
        parser.add_argument('first_file')
        parser.add_argument('second_file')

    #@profile
    def handle(self, *args, **options):
        f1_name = options['first_file']
        f2_name = options['second_file']
        f1 = open(f1_name, 'r')
        f2 = open(f2_name, 'r')
        cnt = 0
        rows = []
        rows_cnt = 0

        for f1_line in f1:
            # if cnt == LIMIT:
            #     return
            f2_line = f2.readline()
            rows.append(PhrasePair(phrase_one=f1_line, phrase_two=f2_line, num=cnt))
            cnt+=1
            rows_cnt+=1
            if rows_cnt == BULK_SIZE:
                PhrasePair.objects.bulk_create(rows)
                rows = []
                rows_cnt = 0
                print(cnt)
                reset_queries()

        PhrasePair.objects.bulk_create(rows)
        print(cnt)

