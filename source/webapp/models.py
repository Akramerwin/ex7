from django.db import models
from django.urls import reverse

class Poll(models.Model):
    question = models.TextField(null=False, blank=False, verbose_name='question')
    q_date = models.DateTimeField(verbose_name='q_date', auto_now_add=True)

    def __str__(self):
        return f'{self.question}, {self.q_date}'

    def get_absolute_url(self):
        return reverse('detailq', kwargs={'pk': self.pk})

class Choice(models.Model):
    text = models.TextField(null=False, blank=False, verbose_name='text')
    poll = models.ForeignKey('webapp.Poll', on_delete=models.CASCADE, related_name='poll', verbose_name='poll')

    def __str__(self):
        return f'{self.text}, {self.poll}'

class Answer(models.Model):
    Poll_a = models.ForeignKey('webapp.Poll', related_name='poll_a', verbose_name='poll_a', on_delete=models.CASCADE)
    a_date = models.DateTimeField(auto_now_add=True, verbose_name='a_date')
    Choice_a = models.ForeignKey('webapp.Choice', related_name='choice_a', verbose_name='choice_a', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.Poll_a}, {self.Choice_a}'

