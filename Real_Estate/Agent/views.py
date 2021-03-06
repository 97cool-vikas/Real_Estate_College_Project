from django.views.generic import ListView
from .models import Agent
from django.views.generic import FormView, DetailView
from django.views.generic.edit import UpdateView
from .forms import AgentCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy


# Create your views here.
class AgentListView(ListView):
    model = Agent


class AgentUpdateView(UpdateView) :
    model = Agent
    template_name_suffix = 'update_form'
    fields = ('telephone', 'picture', 'description', 'address')


class AgentDetailView(DetailView) :
    model = Agent


class AgentCreateView(FormView):
    template_name = 'Agent/agent_create_form.html'
    form_class = AgentCreationForm
    success_url = reverse_lazy('Agent:success_create')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
def agent_page(request, *args, **kwargs):
    return render(request, 'agent/agent_index.html')

def success_agent_create(request):
    return render(request, 'Agent/success_agent_create.html')
