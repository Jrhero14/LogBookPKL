from django.db import models

# Create your models here.
class Log(models.Model):
    date_created = models.DateField(auto_now_add=True, editable=False)
    dateLog = models.DateField(null=False)
    logDiary = models.TextField(null=False)

    def __str__(self):
        return f'{self.dateLog} | {self.logDiary[0:150]}...'
