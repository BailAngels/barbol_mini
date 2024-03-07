from django.views import generic
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from apps.flour.models import Flour


class FlourListView(generic.ListView):
    model = Flour
    template_name = 'flours/flour_list.html'
    context_object_name = 'flours'
    paginate_by = 12

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        flour_list = Flour.objects.all()

        paginator = Paginator(flour_list, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            flour_list = paginator.page(page)
        except PageNotAnInteger:
            flour_list = paginator.page(1)
        except EmptyPage:
            flour_list = paginator.page(paginator.num_pages)

        context['flour_list'] = flour_list
        return context


class FlourDetailView(generic.DetailView):
    model = Flour
    template_name = 'flours/flour_detail.html'
    context_object_name = 'flour_detail'
    pk_url_kwarg = 'pk'

    def get_queryset(self):
        return Flour.objects.all()
