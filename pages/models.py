from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(blank=False)

    def __str__(self):
        return self.title
