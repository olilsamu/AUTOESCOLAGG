from django.db import models

from django.db import models
from django.contrib.auth.models import User

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Instrutor(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    habilitacao_categoria = models.CharField(max_length=2)  # Exemplo: A, B, C, D, E
    data_admissao = models.DateField()

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    modelo = models.CharField(max_length=50)
    placa = models.CharField(max_length=7, unique=True)
    categoria = models.CharField(max_length=2)  # Exemplo: A, B, C, D, E
    ano = models.IntegerField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.modelo} - {self.placa}"


class AulaPratica(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    instrutor = models.ForeignKey(Instrutor, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.SET_NULL, null=True)
    data_hora = models.DateTimeField()
    duracao = models.DurationField()  # Duração da aula
    status = models.CharField(max_length=20, choices=[('agendada', 'Agendada'), ('concluida', 'Concluída'), ('cancelada', 'Cancelada')], default='agendada')

    def __str__(self):
        return f"Aula de {self.aluno} com {self.instrutor} em {self.data_hora}"


class AulaTeorica(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    tema = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[('agendada', 'Agendada'), ('concluida', 'Concluída'), ('cancelada', 'Cancelada')], default='agendada')

    def __str__(self):
        return f"Aula teórica: {self.tema} - {self.aluno}"


class Pagamento(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateTimeField()
    metodo_pagamento = models.CharField(max_length=20, choices=[('boleto', 'Boleto'), ('cartao', 'Cartão'), ('pix', 'Pix')])

    def __str__(self):
        return f"Pagamento de {self.aluno} no valor de {self.valor}"

