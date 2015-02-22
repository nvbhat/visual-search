from django.views import generic

class HomepageView(generic.TemplateView):
    template_name = 'homepage_tix_zoom.html'