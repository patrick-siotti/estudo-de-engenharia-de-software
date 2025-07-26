from django.db import models # type: ignore
from django.utils import timezone # type: ignore

class CondicaoCeu(models.TextChoices):
    ENSOLARADO = 'ensolarado'
    NUBLADO = 'nublado'
    CHUVOSO = 'chuvoso'

class PrevisaoSalva(models.Model):
    """Representa um registro de previsão salvo no banco de dados."""
    cidade = models.CharField(max_length=100)
    temperatura = models.IntegerField()
    condicao = models.CharField(max_length=50, choices=CondicaoCeu.choices)
    umidade = models.IntegerField()
    vento = models.IntegerField()
    data_consulta = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Previsão para {self.cidade} em {self.data_consulta.strftime('%d/%m/%Y %H:%M')}"

    class Meta:
        # Define o nome da tabela no banco de dados
        db_table = 'previsoes_salvas'