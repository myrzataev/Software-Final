from django.core.exceptions import ValidationError
from django.db import models


class TestSet(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Question(models.Model):
    text = models.TextField()
    test_set = models.ForeignKey(TestSet, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    def clean(self):
        super().clean()

        if not self.answer_set.filter(is_correct=True).exists():
            raise ValidationError('Должен быть хотя бы 1 правильный вариант.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


class Answer(models.Model):
    text = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    def clean(self):
        super().clean()

        if self.is_correct and self.question.answer_set.filter(is_correct=True).exists():
            raise ValidationError('Вопрос уже содержит правильный ответ.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)