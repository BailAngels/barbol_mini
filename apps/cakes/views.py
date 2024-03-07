from django.views import generic
from apps.cakes.models import Cake
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class CakeListView(generic.ListView):
    model = Cake
    template_name = 'cakes/cake_list.html'
    context_object_name = 'cakes'
    paginate_by = 12

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        cakes_list = Cake.objects.all()

        paginator = Paginator(cakes_list, self.paginate_by)
        page = self.request.GET.get('page')

        try:
            cakes_list = paginator.page(page)
        except PageNotAnInteger:
            cakes_list = paginator.page(1)
        except EmptyPage:
            cakes_list = paginator.page(paginator.num_pages)

        context['cakes_list'] = cakes_list
        return context


class CakeDetailView(generic.DetailView):
    model = Cake
    template_name = 'cakes/cake_detail.html'
    context_object_name = 'cake_detail'
    pk_url_kwarg = 'pk'

    def get_queryset(self):
        return Cake.objects.all()
