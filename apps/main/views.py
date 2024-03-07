from django.views import generic


class HomePageView(generic.TemplateView):
    template_name = 'index.html'
    context_object_name = 'main'


class AboutPageView(generic.TemplateView):
    template_name = 'about.html'
    context_object_name = 'about'