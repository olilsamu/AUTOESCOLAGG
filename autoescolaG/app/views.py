from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Aluno, Instrutor, Veiculo, AulaPratica, AulaTeorica, Pagamento

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class AlunoView(View):
    def get(self, request, *args, **kwargs):
        aluno = Aluno.objects.all()   # Use Aluno instead of AlunoView
        return render(request, 'aluno.html', {'aluno': aluno})  

class InstrutorView(View):
    def get(self, request, *args, **kwargs):
        instrutores = Instrutor.objects.all()
        return render(request, 'instrutor.html', {'instrutores': instrutores})

class VeiculoView(View):
    def get(self, request, *args, **kwargs):
        veiculos = Veiculo.objects.all()
        return render(request, 'veiculos.html', {'veiculos': veiculos})

class AulaPraticaView(View):
    def get(self, request, aula_pratica_id, *args, **kwargs):
        aula_pratica = get_object_or_404(AulaPratica, id=aula_pratica_id)
        return render(request, 'aula_pratica.html', {'aula_pratica': aula_pratica})

class AulaTeoricaView(View):
    def get(self, request, *args, **kwargs):
        aulas_teoricas = AulaTeorica.objects.all()
        return render(request, 'aula_teorica.html', {'aulas_teoricas': aulas_teoricas})

class PagamentoView(View):
    def get(self, request, pagamento_id, *args, **kwargs):
        pagamento = get_object_or_404(Pagamento, id=pagamento_id)
        return render(request, 'pagamento.html', {'pagamento': pagamento})
