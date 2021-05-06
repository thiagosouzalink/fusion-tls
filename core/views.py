from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Servico, Funcionario, Preco, Feature, Cliente
from .forms import ContatoForm


class IndexView(FormView):

    template_name = "core/index.html"
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        # Recupera o contexto da página
        context = super(IndexView, self).get_context_data(**kwargs)
        # Adiciona dados no contexto
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        context['precos'] = Preco.objects.order_by("?").all()
        context['clientes'] = Cliente.objects.order_by("?").all()
        
        features = Feature.objects.order_by("?").all()
        if features:
            if len(features) < 2:
                context['features_left'] = features
                context['features_right'] = []
            else:
                features_metade = int(len(features) / 2)
                context['features_left'] = features[:features_metade]
                context['features_right'] = features[features_metade:]
        else:
            context['features_left'] = []
            context['features_right'] = []

        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, "E-mail enviado com sucesso!")
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, "Erro ao enviar e-mail.")
        return super(IndexView, self).form_invalid(form, *args, **kwargs)


        




