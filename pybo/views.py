from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from pybo.models import Question
from pybo.forms import QuestionForm


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
    content = {'question': question}
    return render(request, 'pybo/question_detail.html', content)


def answer_create(request, question_id):
    """
        pybo 답변 등록
    """
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'))
    return redirect('pybo:detail', question_id=question_id)


def question_create(request):
    """
        pybo 질문 등록
    """
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')
        else:
            form = QuestionForm()
    form = QuestionForm()
    return render(request, 'pybo/question_form.html', {'form': form})
