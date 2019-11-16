from django.shortcuts import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import *

from api.models import *
import dm_hotel.settings
from django.template import RequestContext


def index(request):
    return render_to_response('home/index.html')


def create_cust(request):
    return render_to_response('home/create_customer.html')


@api_view(['GET', 'POST'])
def make_reservation(request):
    if len(request.POST) == 0:
        return render_to_response('home/make_reservation.html')
    else:
        if request.method == 'POST':
            serializer = ReservationSerializer(request.data)
            if serializer.is_valid():
                serializer.save(request.data)
                return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def check_reservation(request):
    reservation = Reservation.objects.get(confirmation_number=request.GET['id'])
    customer = reservation.customer_id
    room_type = reservation.room_type_id.type
    res = {
        'reservation': reservation,
        'customer' : customer,
        'room_type': room_type
    }
    return render_to_response('templates/check_reservation.html', res)
