from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from webapp.models import TestSet, Question, Answer


# Главная страница
def index(request):
    return render(request, 'index.html')


# Список тестов
@login_required
def test_list_view(request):
    test_sets = TestSet.objects.all()
    return render(request, 'test_list_view.html', {'test_sets': test_sets})


# Детальный просмотров тестов
@login_required
def test_detail_view(request, test_set_id):
    test_set = get_object_or_404(TestSet, pk=test_set_id)
    return render(request, 'test_detail_view.html', {'test_set': test_set})


# Пройти тест
@login_required
def test_pass_view(request, test_set_id):
    test_set = get_object_or_404(TestSet, pk=test_set_id)
    questions = Question.objects.filter(test_set=test_set)
    if request.method == 'POST':
        correct_answers_count = 0
        for question in questions:
            correct_answers = [int(answer_id) for answer_id in
                               Answer.objects.filter(question=question, is_correct=True).values_list('id', flat=True)]
            submitted_answers = [int(answer.strip()) for answer in
                                 request.POST.getlist(f'answer_{question.id}', [])]
            print(correct_answers)
            print(submitted_answers)
            if any(answer in correct_answers for answer in submitted_answers):
                correct_answers_count += 1
        total_questions = questions.count()
        correct_percentage = (correct_answers_count / total_questions) * 100
        return render(request, 'test_result.html', {'test_set': test_set, 'correct_percentage': correct_percentage,
                                                    'correct_answers_count': correct_answers_count,
                                                    'total_questions': total_questions})
    return render(request, 'test_pass_view.html', {'test_set': test_set, 'questions': questions})

