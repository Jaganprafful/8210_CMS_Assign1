from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView, DetailView
from .models import models, Comment, Vehicle
from .models import Client
from django.urls import reverse_lazy, reverse


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'client_list.html'
    login_url = 'login'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, **args):
        context = super().get_context_data(**args)

        # Super users can see all clients
        if self.request.user.is_superuser:

            context['object_list'] = Client.objects.all()

        else:
            # Filtering the object list by the current user
            context['object_list'] = Client.objects.filter(author=self.request.user)

        return context


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'client_detail.html'
    login_url = 'login'


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    fields = ('name', 'notes', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone', 'acct_number')
    template_name = 'client_edit.html'


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = 'client_delete.html'
    success_url = reverse_lazy('client_list')


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    template_name = 'client_new.html'
    fields = ('name', 'notes', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone', 'acct_number')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'comment_new.html'
    fields = ('comment',)
    login_url = 'login'

    def form_valid(self, form):
        form.instance.client = get_object_or_404(Client, pk=self.kwargs['pk'])
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('client_detail', args=(self.kwargs['pk'],))


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ('comment',)
    template_name = 'comment_edit.html'

    def get_success_url(self):
        return reverse('client_detail', args=(self.kwargs['clientPk'],))


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'comment_delete.html'

    def get_success_url(self):
        return reverse('client_detail', args=(self.kwargs['clientPk'],))


class VehicleCreateView(LoginRequiredMixin, CreateView):
    model = Vehicle
    template_name = 'vehicle_new.html'
    fields = ('client', 'make', 'model', 'VIN', 'purchaseDate', 'lastServiceDate')
    success_url = reverse_lazy('client_list')

    def get_form(self, form_class=None):
        form = super(VehicleCreateView, self).get_form(form_class)

        form.fields['purchaseDate'].label = "Date of Purchase"
        form.fields['lastServiceDate'].label = "Date of Last Service"
        return form

    def form_valid(self, form):
        form.instance.client = get_object_or_404(Client, pk=self.kwargs['pk'])
        form.instance.author = self.request.user
        return super().form_valid(form)


class VehicleUpdateView(LoginRequiredMixin, UpdateView):
    model = Vehicle
    fields = ('client', 'make', 'model', 'VIN', 'purchaseDate', 'lastServiceDate')
    template_name = 'vehicle_edit.html'

    def get_success_url(self):
        return reverse('client_detail', args=(self.kwargs['clientPk'],))

    def get_form(self, form_class=None):
        form = super(VehicleUpdateView, self).get_form(form_class)

        form.fields['purchaseDate'].label = "Date of Purchase"
        form.fields['lastServiceDate'].label = "Date of Last Service"

        return form


class VehicleDeleteView(LoginRequiredMixin, DeleteView):
    model = Vehicle
    template_name = 'vehicle_delete.html'

    def get_success_url(self):
        return reverse('client_detail', args=(self.kwargs['clientPk'],))
