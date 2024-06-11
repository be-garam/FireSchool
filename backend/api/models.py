import datetime

from django.db import models
from django.utils import timezone

class School(models.Model):
    name = models.CharField(max_length=200) # 학교 명
    urls = models.JSONField() # # URL 목록을 저장하는 JSON 필드
    contents = models.TextField(default="") # crawled data
    date_added = models.DateTimeField('date added', default=timezone.now)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['date_added']),
        ]

    def __str__(self):
        return self.name

class SchoolData(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='data')
    links = models.JSONField() # links extracted from the contents
    files = models.JSONField() # files extracted from the contents
    keywords = models.JSONField() # keywords extracted from the contents
    date_crawled = models.DateTimeField('date crawled', default=timezone.now)

    def __str__(self):
        return self.school.name + "'s data"

class SuggestedSchool(models.Model):
    user_name = models.CharField(max_length=200) # user's name
    school_name = models.CharField(max_length=200) # suggested school's name
    school_link = models.CharField(max_length=200) # suggested school's link
    date_suggested = models.DateTimeField('date suggested', default=timezone.now)

    def __str__(self):
        return self.user_name + " suggested " + self.school_name

class UserReport(models.Model):
    school_name = models.CharField(max_length=200) # school's name
    error = models.TextField() # error message
    date_reported = models.DateTimeField('date reported', default=timezone.now)

    def __str__(self):
        return self.school_name + " reported error"