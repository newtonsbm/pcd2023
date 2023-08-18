# file padarias/views.py

from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .models import Padaria, Cesta, Produto, Assinatura

def index(request):
    count_padarias = Padaria.objects.count()
    count_cestas = Cesta.objects.count()
    count_produtos= Produto.objects.count()
    context = {
        'count_padarias': count_padarias,
        'count_cestas': count_cestas,
        'count_produtos': count_produtos,
    }
    return render(request, 'index.html', context=context)

def sobre(request):
    return render(request, 'sobre.html')

@login_required
def minha_conta(request):
    return render(request, 'minha_conta.html')

@login_required
def sugestao(request):
    if request.method == 'POST':
        email = request.user.email
        titulo = request.POST.get('titulo')
        mensagem = request.POST.get('mensagem')
        nps = request.POST.get('nps')
        print(f"-------------------------------------------------------------------------")
        print(f"Enviando sugestão de {email} com título '{titulo}' e mensagem '{mensagem}'")
        print(f"NPS: {nps}")
        print(f"-------------------------------------------------------------------------")
        return redirect('minha_conta')
    return render(request, 'sugestao.html')

class PadariaListView(generic.ListView):
    model = Padaria
    # defaults
    queryset = Padaria.objects.all()
    context_object_name = 'padaria_list'
    template_name = 'padarias/padaria_list.html'
    paginate_by = 2

class PadariaDetailView(generic.DetailView):
    model = Padaria
    # defaults
    context_object_name = 'padaria'
    template_name = 'padarias/padaria_detail.html'

class CestaListView(generic.ListView):
    model = Cesta

class CestaDetailView(generic.DetailView):
    model = Cesta

class AssinaturaCreateView(generic.CreateView):
    model = Assinatura
    fields = ['cesta', 'observacao']
    template_name = 'padarias/assinatura_form.html'
    success_url = reverse_lazy('minha_conta')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(message="Assinatura criada com sucesso!", request=self.request)
        return super().form_valid(form)

class AssinaturaUpdateView(generic.UpdateView):
    model = Assinatura
    fields = ['cesta', 'observacao']
    template_name = 'padarias/assinatura_form.html'
    success_url = reverse_lazy('minha_conta')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(message="Assinatura atualizada com sucesso!", request=self.request)
        return super().form_valid(form)

class AssinaturaDeleteView(generic.DeleteView):
    model = Assinatura
    success_url = reverse_lazy('minha_conta')
    # defaults
    context_object_name = 'assinatura'
    template_name = 'padarias/assinatura_confirm_delete.html'

    def form_valid(self, form):
        messages.success(message="Assinatura cancelada com sucesso!", request=self.request)
        return super().form_valid(form)



