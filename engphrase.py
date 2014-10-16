#!/usr/bin/python

import linecache
import re
import random
import urllib2
from HTMLParser import HTMLParser
import sys

eng500file = "eng500.csv"
words_total = 5004

engrus = []

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.flag = 0
        self.cnt = 0
        self.rus = ''
        self.eng = ''

    def handle_starttag(self, tag, attrs):
      if tag == 'div':
         for name,value in attrs:
           if name == 'class' and value == 'b-translation__example':
#               print name, value
                self.flag = 1
#      if tag == 'span' and self.flag == 1:
#          for name,value in attrs:
#            if name == 'class' and value == 'b-translation__text':
#                 print name, value

    def handle_endtag(self, tag):
         if tag == 'div':
            self.flag = 0
            self.cnt = 0
            if self.eng != '':
                engrus.append((self.rus,self.eng))
            self.rus = ''
            self.eng = ''


    def handle_data(self, data):
        if self.flag == 1:
            if self.cnt == 0:
               self.eng = data
            if self.cnt == 2:
               self.rus = data
            self.cnt+=1


f = open(eng500file,"r")

while(1):
  engrus = []
  num =random.randint(1,words_total) 
  #num = 100

  line = linecache.getline(eng500file,num)
  m = re.search(",([a-z]*),",line)
  if m:
    #print m.group(1)
    word = m.group(1)
  else: 
    word = "null"


  response = urllib2.urlopen('http://slovary.yandex.ru/'+word+'/en')
  the_page = response.read()
  #print the_page
  the_page = the_page.decode('utf-8','ignore')



  # instantiate the parser and fed it some HTML
  parser = MyHTMLParser()
  parser.feed(the_page)

  my = random.choice(engrus)
  print ''
  print ''
  print "--- %s ----"%word
  print my[0]
  sys.stdout.write('->')
  raw_input()
  print my[1]
   


