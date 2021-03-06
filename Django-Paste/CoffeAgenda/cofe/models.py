from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Envento(models.Model):
    titulo = models.CharField(max_length=100)
    descrição = models.TextField(blank=True, null=True)
    date_event = models.DateTimeField(verbose_name="Data do evento")
    date_origin = models.DateTimeField(auto_now = True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Evento'

    def str(self):
        return self.titulo
        
    def get_date_event(self):
        return self.date_event.strftime('%d/%m/%Y %H:%M')

    def get_date_event_input(self):
        return self.date_event.strftime('%Y-%m-%dT%H:%M')

    def get_atrasados(self):
        if self.date_event < datetime.now():
            return True
        else:
            return False