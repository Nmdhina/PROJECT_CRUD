from django.db import models

CHOICES = {
    ('biology','Biology'),
    ('computer science','Computer Science'),
    ('accounts','Accounts'),
    ('others','Others')
}

class students(models.Model):
    name = models.CharField(max_length=50)
    std = models.CharField(max_length=50)
    section = models.CharField(max_length=50, choices=CHOICES)
    age = models.PositiveIntegerField()
    address = models.TextField()
    photo = models.ImageField(upload_to='students/')
    
    def __str__(self):
        return self.name