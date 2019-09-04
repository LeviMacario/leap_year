from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, Http404
from .forms import LeapYearForm


class ResultView(TemplateView):
    template_name = 'core/result.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        result = kwargs.get('result')
        year = kwargs.get('year')
        if result == 'bissexto':
            ctx['msg'] = 'O ano {0} é bissexto.'.format(year)
            ctx['status'] = 'success'
        elif result == 'nao-bissexto':
            ctx['msg'] = 'O ano {0} não é bissexto.'.format(year)
            ctx['status'] = 'danger'
        else:
            raise Http404
        return ctx


class IndexView(FormView):
    template_name = 'core/index.html'
    form_class = LeapYearForm
    success_url = '/result/{0}/{1}/'

    def form_valid(self, form):
        url = self.success_url.format(
            form.cleaned_data['year'],
            'nao-bissexto'
        )
        if form.is_leapyear():
            url = self.success_url.format(
                form.cleaned_data['year'],
                'bissexto'
            )
            return HttpResponseRedirect(url)
        return HttpResponseRedirect(url)