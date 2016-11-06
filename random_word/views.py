#-*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, render_to_response
from django.views import generic
from datetime import datetime, date, time, timezone
from random import randrange, randint
from .models import WordPractice

def index(request):
	template = 'index.html'
	return render_to_response(template, {'how_to':True})

def random_word(request, num, seq=''):
	template = "index.html"
	context = {}
	all_word = WordPractice.objects.all()
	list_index = []
	for i in range(int(num)):
		random_index = randrange(0, len(WordPractice.objects.all()) )
		if seq != 'has_seq':
			list_index.append(all_word[random_index].word)
		else:
			context['seq'] = 'has_seq'
			list_index.append(str(i+1)+') ' + all_word[random_index].word)
	context['words'] = list_index
	return render_to_response(template, context)

def get_major_word(start, end):
	major_words = []
	for i in range(start, end+1):
		major_words.append(WordPractice.objects.get(major_num=i) )
	return major_words

def random_interval(request):
	ran_num = randint(0, 9)
	l = get_major_word(ran_num*10, ran_num*10+10)
	return render_to_response("index.html",{'major_words': l} )

def random_num(request):
	list_num = []
	for i in range(10):
		list_num.append(randrange(0, 101))
	return render_to_response("index.html", {'list_num':list_num})

def show_major(request):
	return render_to_response("index.html", {'major_words': WordPractice.objects.filter(is_major= True).order_by('major_num')})

def add_word(request):
	return HttpResponse("add_word")

def add_word_csv(request):
	import csv
	with open('words.csv', 'rt') as f:
		reader = csv.DictReader(f)
		for row in reader:
			new_word = WordPractice.objects.create(word=row['word'] )
			if row['is_major']:
				new_word.is_major = True 
			if row['major_num'] != '':
				new_word.major_num = int(row['major_num'])
			new_word.save()
	return HttpResponse("Upload database success.")