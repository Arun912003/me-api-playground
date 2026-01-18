from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    education = models.TextField()
    skills = models.JSONField()
    github = models.URLField()
    linkedin = models.URLField()
    portfolio = models.URLField()

    def __str__(self):
        return self.name


class Project(models.Model):
    profile = models.ForeignKey(Profile, related_name="projects", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    links = models.JSONField()
