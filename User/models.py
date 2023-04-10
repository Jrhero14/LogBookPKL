from django.db import models

# Create your models here.

class imgDoc(models.Model):
    date_created = models.DateField(auto_now_add=True, editable=False)
    dirname = models.CharField(max_length=255, null=True)
    filename = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.filename

class Log(models.Model):
    date_created = models.DateField(auto_now_add=True, editable=False)
    dateLog = models.DateField(null=False)
    logDiary = models.TextField(null=False)
    filesDocumentation = models.ManyToManyField(imgDoc, null=True)

    def __str__(self):
        return f'{self.dateLog} | {self.logDiary[0:150]}...'
