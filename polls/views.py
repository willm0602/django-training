from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView
from django.utils import timezone
from .models import Question, Choice

# Create your views here.

class IndexView(ListView):
	template_name = "index.html"
	context_object_name = "latest_question_list"

	def get_queryset(self):
		return Question.objects.filter(
			pub_date__lte = timezone.now()
		).order_by('-pub_date')[:5]

class DetailView(DetailView):
	template_name = "detail.html"
	model = Question

class ResultsView(DetailView):
	model = Question
	template_name = "results.html"


def vote(request, question_id):
	TEMPLATE_NAME = 'detail.html'
	question = get_object_or_404(Question, pk = question_id)

	try:
		selection = question.choice_set.get(pk = request.POST['choice'])

	except (KeyError, Choice.DoesNotExist):
		return(render(request, TEMPLATE_NAME, {
			'question': question,
			'error_message': 'no choice selected!'
		}))
	else:
		selection.votes = selection.votes + 1
		selection.save()
		return(HttpResponseRedirect(reverse('polls:results', args = (question.id,))))
