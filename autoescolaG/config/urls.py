from django.contrib import admin
from django.urls import path
from app.views import IndexView, AlunoView, InstrutorView, VeiculoView, AulaPraticaView, AulaTeoricaView, PagamentoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('alunos/', AlunoView.as_view(), name='aluno'),  # Detail view  
    path('instrutores/', InstrutorView.as_view(), name='instrutor'),
    path('veiculos/', VeiculoView.as_view(), name='veiculo'),
    path('aulas-praticas/', AulaPraticaView.as_view(), name='aula-pratica'),
    path('aulas-teoricas/', AulaTeoricaView.as_view(), name='aula-teorica'),
    path('pagamento/<int:pagamento_id>/', PagamentoView.as_view(), name='pagamento'),
]
