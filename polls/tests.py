from django.test import TestCase
from .models import Question
from django.utils import timezone
import datetime

# Create your tests here.

class QuestionMethodTests(TestCase):
	def test_from_future_passes(self):
		time = timezone.now() + datetime.timedelta(days = 30)
		future_question = Question(pub_date = time)
		self.assertIs(future_question.was_published_recently(), False)


	def test_was_published_recently_with_old_question(self):
		time = timezone.now() - datetime.timedelta(days = 1)
		old_question = Question(pub_date = time)
		self.assertIs(old_question.was_published_recently, False)

	def test_was_published_recently_with_recent_question(self):
		time = timezone.now()
		last_question = Question(pub_date = time)
		self.assertIs(last_question.was_published_recently(), True)


