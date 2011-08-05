from django.shortcuts import render_to_response
from django.template import RequestContext

def home(request):
    return render_to_response('home.html', {'str': 'DESU'},
                              context_instance=RequestContext(request))

def phpinfo(request):
    return render_to_response('phpinfo.html',
                              context_instance=RequestContext(request))
