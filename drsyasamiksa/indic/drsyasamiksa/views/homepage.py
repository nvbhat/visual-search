from django.views import generic
from django.http import *
from django.shortcuts import render_to_response
from django.template import RequestContext
#from django.utils import simplejson
import socket
#from django.shortcuts import render_to_response
from django.http import HttpResponse

#def main(request):
   #return render_to_response('homepage_tix_zoom.html', context_instance=RequestContext(request))

class HomepageView(generic.TemplateView):
      template_name = 'homepage_tix_zoom.html'

   
