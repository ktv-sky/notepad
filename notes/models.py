from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User


LABEL_CHOICES = (
    ('P', 'primary'),
    ('SE', 'secondary'),
    ('S', 'success'),
    ('DN', 'danger'),
    ('W', 'warning'),
    ('I', 'info'),
    ('L', 'light'),
    ('D', 'dark')
)

class Note(models.Model):
    title = models.CharField(max_length=100)
    due_date = models.DateField()
    label = models.CharField(choices=LABEL_CHOICES, max_length=2)
    finished = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_finish_item_url(self):
        return reverse('finish-note-item', kwargs={
            'id': self.id
        })

    def get_delete_item_url(self):
        return reverse('delete-note-item', kwargs={
            'id': self.id
        })

    def get_recover_item_url(self):
        return reverse('recover-note-item', kwargs={
            'id': self.id
        })
