from django.db import models

class WordPractice(models.Model):
	word = models.CharField(max_length=50)
	is_major = models.BooleanField(default=False)
	major_num = models.IntegerField(null=True, blank=True, default=None)

	def __str__(self):
		return self.word