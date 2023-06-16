from django.db import models


class Tarea(models.Model):
    id = models.AutoField(primary_key=True)
    texto = models.CharField(max_length=50)
    prioridad = models.IntegerField()

    def __str__(self):
        return f'{self.texto}'

    class Meta:
        ordering = ['-prioridad', 'texto']
