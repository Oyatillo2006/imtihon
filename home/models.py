from django.db import models

class Todo(models.Model):
    STATUS = (
        ("bajarildi", "Bajarildi"),
        ("bajarilmadi", "Bajarilmadi"),
        ("bajarilmoqda", "Bajarilmoqda")
    )

    title = models.CharField(max_length=100)
    time = models.DateTimeField()
    docs = models.TextField()
    status = models.CharField(max_length=15, choices=STATUS)

    def __str__(self):
        return self.title
