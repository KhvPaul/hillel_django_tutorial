import datetime

from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .forms import NameForm, QuestionCreateForm
from .models import Choice, Question


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, '../templates/polls/index.html', context)
#
#
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    # def get_queryset(self):
    #     """Return the last five published questions."""
    #     return Question.objects.order_by('-pub_date')[:5]

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def current_datetime(request):
    now = datetime.datetime.now()
    return HttpResponse(f"{now}", status=201)


def your_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if False:
            # process the data in form.cleaned_data as required
            form.clean()
            form.cleaned_data.get("name")
            ...
            # redirect to a new URL:
            return redirect(reverse("your-name"))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'example.html', {'form': form})


def create_question(request):
    if request.method == "POST":
        form = QuestionCreateForm(request.POST)
        if form.is_valid():
            # q = Question.objects.create(**form.cleaned_data)
            # q = Question(**form.cleaned_data)
            obj = form.save()
            # print("Created")
            return redirect(reverse("polls:detail", args=(obj.id,)))
    else:
        form = QuestionCreateForm(initial={"pub_date": datetime.datetime.now()})
    return render(request, "polls/create_question.html", {'form': form})


def update_question(request, pk):
    obj = get_object_or_404(Question, pk=pk)
    if request.method == "POST":
        form = QuestionCreateForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect(reverse("polls:index"))
    else:
        form = QuestionCreateForm(instance=obj)
    return render(request, "polls/update_question.html", {'form': form, "obj": obj})
