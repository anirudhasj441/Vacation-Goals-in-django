from django.db import models

# Create your models here.

class Goals(models.Model):
    goal = models.CharField(max_length=50,null=True,blank=True)
    def __str__(self):
        return str(self.pk)
    class Meta:
        verbose_name_plural = "Goals"
    