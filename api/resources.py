from tastypie.resources import ModelResource
import api.serializers
from tastypie.authentication import *
from api.models import *


class ReservationResource(ModelResource):

    class Meta:
        queryset = Reservation.objects.all()
        resource_name = 'reservation'


class CustomerResource(ModelResource):

    class Meta:
        serializer_class = api.serializers.CustomerSerializers
        queryset = Customer.objects.all()
        filtering = {'id': ['exact', 'in']}
        resource_name = 'customer'
        list_allowed_methods = ['get','post','put','delete']