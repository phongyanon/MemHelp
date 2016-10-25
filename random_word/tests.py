from django.test import TestCase, Client
#import unittest
from .models import WordPractice
from django.test.utils import setup_test_environment
setup_test_environment()

class Check_random_word_feature(TestCase):
	"""docstring for Check_random_word_feature"""
	def setUp(self):
		
		self.client = Client()
		for i in range(50): # create 50 nomal words.
			WordPractice.objects.create(word="normal_word"+str(i+1))
		for i in range(101): # create 100 major words.
			WordPractice.objects.create(word="major_word"+str(i+1), is_major=True, major_num=i)

	def test_random_10_no_number(self):
		response = self.client.get('/10/random_word/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual( len(response.context['words']), 10)
		self.assertEqual(type(response.context['words'][0]), str)

	def test_random_20_no_number(self):
		response = self.client.get('/20/random_word/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual( len(response.context['words']), 20)
		self.assertEqual(type(response.context['words'][0]), str)

	def test_random_10_with_number(self):
		response = self.client.get('/10/has_seq/random_word/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual( len(response.context['words']), 10)
		self.assertEqual(type(response.context['words'][0]), str)
		self.assertEqual( response.context['seq'], 'has_seq')

	def test_random_20_with_number(self):
		response = self.client.get('/10/has_seq/random_word/')
		self.assertEqual(response.status_code, 200)
		self.assertEqual( len(response.context['words']), 10)
		self.assertEqual(type(response.context['words'][0]), str)
		self.assertEqual( response.context['seq'], 'has_seq')

	def test_show_all_major(self):
		response = self.client.get('/show_major/')
		self.assertEqual(response.status_code, 200)
		test_words = response.context['major_words']
		all_major = True
		for test_word in test_words: # check all words is major word.
			if not test_word.is_major:
				all_major = False
		self.assertEqual(all_major, True)

	def test_random_interval(self):
		response = self.client.get('/random_interval/')
		self.assertEqual(response.status_code, 200)
		test_words = response.context['major_words']
		valid_words = True
		self.assertEqual(len(test_words)>=10, True)
		start_num = 0
		for test_word in test_words: # check all words is major word and is sequence major num.
			if (not test_word.is_major) or (start_num >= test_word.major_num):
				all_major = False
			else:
				start_num = test_word.major_num
		self.assertEqual(valid_words, True)

	def test_random_10_from_100(self):
		response = self.client.get('/random_num/')
		self.assertEqual(response.status_code, 200)
		test_nums = response.context['list_num']
		self.assertEqual(len(test_nums), 10)
		valid_nums = True
		for num in test_nums:
			if not ( (num >= 0) and (num <= 100) ):
				valid_nums = False
		self.assertEqual(valid_nums, True)

	def test_fill_new_word(self):
		pass