#!/usr/bin/python

import linecache
import re
import random
import urllib2
from HTMLParser import HTMLParser
import sys

source = 'wordreference'
#source = 'lingvo'

eng500file = "eng500.csv"
words_total = 5004

engrus = []

class LingvoHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.flag  = 0
        self.flag_r = 0
        self.flag_e = 0
        self.cnt = 0
        self.rus = ''
        self.eng = ''

    def handle_starttag(self, tag, attrs):
      if tag == 'tr':
         for name,value in attrs:
           if name == 'class' and value == 'l-examples__tr js-examples-table-trans':
#               print name, value
                self.flag = 1
                self.eng = ''
      if tag == 'div' and self.flag == 1:
          for name,value in attrs:
            if name == 'class' and value == 'l-examples__text js-first-source-text':
                 self.flag_e = 1;

      if tag == 'div' and self.flag == 1:
          for name,value in attrs:
            if name == 'class' and value == 'l-examples__text js-second-source-text':
                 self.flag_r = 1;

    def handle_endtag(self, tag):
         if tag == 'tr':
            self.flag = 0
            self.cnt = 0
            if self.eng != '':
                engrus.append((self.rus,self.eng))
            self.rus = ''
            self.eng = ''
         if tag == 'div':
            self.flag_e = 0
            self.flag_r = 0


    def handle_data(self, data):
        if self.flag == 1:
            if self.flag_e == 1:
               data = re.sub(u'[\n\t]+',u' ',data,re.U)
               self.eng += data
            if self.flag_r == 1:
               #data = re.sub(r'^[ \t]+',r' ',data.decode('utf-8'))           
#               print "1:%s"%data
#               print type(data)
               data = re.sub(u'[\n\t]+',u' ',data,re.U)
#               print "2:%s"%data
#               print type(data)
               self.rus += data

#HTML Parser for wordreference.com
class WordreferenceHTMLParser(HTMLParser):  
    def __init__(self):
        HTMLParser.__init__(self)
        self.flag  = 0
        self.flag_r = 0
        self.flag_e = 0
        self.cnt = 0
        self.rus = ''
        self.eng = ''

    def handle_starttag(self, tag, attrs):
      if tag == 'td':
          for name,value in attrs:
            if name == 'class' and value == 'FrEx':
                 self.flag_e = 1;
                 self.flag_r = 0;

      if tag == 'td':
          for name,value in attrs:
            if name == 'class' and value == 'ToEx':
                 self.flag_r = 1;
                 self.flag_e = 0;
    
    def handle_endtag(self, tag):
         if tag == 'tr' and self.flag_r == 1:
            if self.eng != '':
                engrus.append((self.rus,self.eng))
            self.rus = ''
            self.eng = ''
            self.flag_e = 0
            self.flag_r = 0


    def handle_data(self, data):
       if self.flag_e == 1:
           #data = re.sub(u'[\n\t]+',u' ',data,re.U)
           self.eng += data

       if self.flag_r == 1:
           data = re.sub(u'[\n\t]+',u' ',data,re.U)
           self.rus += data

def get_random():
    print ''
    print ''
    print "--- %s ----"%word
    if engrus:
      my = random.choice(engrus)
      print my[0]
      sys.stdout.write('->')
      raw_input()
      print my[1]

def get_all():
   for i in engrus:
      print "rus: %s| eng: %s"%(i[0],i[1])


f = open(eng500file,"r")

# instantiate the parser and fed it some HTML
if source == 'lingvo':
   parser = LingvoHTMLParser()
if source == 'wordreference':
   parser = WordreferenceHTMLParser()

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

  if source == 'lingvo':
      url = 'http://www.lingvo-online.ru/en/examples/en-ru/'+word
  if source == 'wordreference':
      url = 'http://www.wordreference.com/enru/'+word
     

  request = urllib2.Request(url)
  opener = urllib2.build_opener()
  request.add_header('User-Agent','Mozilla/5.0 (Windows NT 5.2; rv:2.0.1) Gecko/20100101 Firefox/4.0.1')
  response = opener.open(request)
  the_page = response.read()
  the_page = the_page.decode('utf-8','ignore')
  parser = WordreferenceHTMLParser()

  parser.feed(the_page)
  get_random()
  #get_all()



