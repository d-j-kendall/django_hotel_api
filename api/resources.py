from tastypie.resources import ModelResource
from api.models import *


class ReservationResource(ModelResource):

    class Meta:
        queryset = Reservation.objects.all()
        resource_name = 'reservation'


class CustomerResource(ModelResource):

    class Meta:
        queryset = Customer.objects.all()
        resource_name = 'customer'