#from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
# from .models import Question
# from django.template import loader
#
#
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

    # Leave the rest of the views (detail, results, vote) unchanged
#
#
# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s." % question_id)
#
#
# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)
#
#
# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)

from django.shortcuts import render,get_object_or_404
# from django.http import HttpResponse
# from django.template import loader
# from django.http import Http404
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    """commented , since this part is needed only if we are not using template"""
    """starts"""
    # output = ",".join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    """Ends"""
    # template = loader.get_template("polls/index.html")
    context ={'latest_question_list': latest_question_list}
    return render(request, "polls/index.html", context)
    # return HttpResponse(template.render(context, request))


def detail(request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        return render(request, "polls/details.html", {'question': question})
