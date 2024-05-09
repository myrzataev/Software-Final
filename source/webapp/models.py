from django.db import models


class TestSet(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class Question(models.Model):
    text = models.TextField()
    photo = models.ImageField(upload_to='photo/', null=True, blank=True)
    audio = models.FileField(upload_to='audio/', null=True, blank=True)
    test_set = models.ForeignKey(TestSet, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    def clean(self):
        super().clean()

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

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)