from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from pybo.models import Question


# Create your views here.
def index(request):
    """
        pybo 목록 출력
    """
    question_list = Question.objects.order_by('-create_date')
    content = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', content)


def detail(request, question_id):
    """
        pybo 내용 출력
    """
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    content = {'question':question}
    return render(request, 'pybo/question_detail.html', content)
