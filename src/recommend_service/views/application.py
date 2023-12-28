from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.urls import reverse

from ..models import Unit, Recommendation


class UnitCreateView(LoginRequiredMixin, CreateView):
    model = Unit
    fields = ['name', 'description']
    template_name = 'unit_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('unit-list')

    def handle_no_permission(self):
        return HttpResponseForbidden()


class RecommendationCreateView(LoginRequiredMixin, CreateView):
    model = Recommendation
    fields = ['stars_count', 'review']
    template_name = 'recommendation_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.unit_id = self.kwargs['unit_id']  # Получаем unit_id из URL
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('recommendation-list')

    def handle_no_permission(self):
        return HttpResponseForbidden()
