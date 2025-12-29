from django.db import models

class Produto(models.Model):
    MARCA_CHOICES = [
        ('volkswagen', 'Volkswagen'),
        ('hyundai', 'Hyundai'),
        ('nissan', 'Nissan'),
        ('toyota', 'Toyota'),
        ('chevrolet', 'Chevrolet'),
        ('fiat', 'Fiat'),
        ('byd', 'BYD'),
    ]
    TIPO_CHOICES = [
        ('eletrico', 'Elétrico'),
        ('hibrido', 'Híbrido'),
        ('combustao', 'Combustão'),
    ]
    ESTADO_CHOICES = [
        ('boa', 'Boa'),
        ('excelente', 'Excelente'),
        ('medio', 'Médio'),
    ]
    marca = models.CharField(max_length=20, choices=MARCA_CHOICES, default='volkswagen')
    modelo = models.CharField(max_length=50, default='Modelo')
    ano_fabricacao = models.IntegerField(default=2023)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, default='combustao')
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='boa')
    cor = models.CharField(max_length=20, default='Branco')
    foto = models.ImageField(upload_to='fotos/', blank=True, null=True)

    def __str__(self):
        return f"{self.marca} {self.modelo}"