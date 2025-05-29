from django.db import models

# Create your models here.

class NurseVisit(models.Model):
    name = models.CharField(max_length=100, verbose_name="Аты-жөні")
    group = models.CharField(max_length=50, verbose_name="Тобы")
    reason = models.TextField(verbose_name="Себебі")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Уақыты")

    def __str__(self):
        return f"{self.name} - {self.group}"