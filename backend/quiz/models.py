from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=500)
    question_type = models.CharField(
        max_length=20,
        choices=[
            ('text', 'Text Input'),
            ('multiple', 'Multiple Choice'),
            ('boolean', 'True/False')
        ],
        default='multiple'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text 