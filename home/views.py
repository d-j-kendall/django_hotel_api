from django.shortcuts import *
import dm_hotel.settings
from django.template import RequestContext


def index(request):
    return render_to_response('home/index.html')

