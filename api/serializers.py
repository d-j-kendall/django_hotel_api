from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from api.models import Customer, Reservation, Transaction, RoomType


class CustomerSerializers(serializers.Serializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    street_address = serializers.CharField(required=True)
    city = serializers.CharField(required=True)
    state_province = serializers.CharField(required=True)
    email_address = serializers.CharField(required=True)

    class Meta:
        model = Customer
        fields = '__all__'

    def __init__(self, data):
        super(CustomerSerializers, self).__init__(self, data=data)


    def save(self, validated_user_data):
        user = Customer(
            first_name=validated_user_data['first_name'],
            last_name=validated_user_data['last_name'],
            street_address=validated_user_data['street_address'],
            city=validated_user_data['city'],
            state_province=validated_user_data['state_province'],
            email_address=validated_user_data['email_address'],
        )
        user.save()
        return user

class ReservationSerializer(ModelSerializer):

    customer_id = serializers.IntegerField(required=True)
    check_in = serializers.DateField(required=True)
    check_out = serializers.DateField(required=True)
    room_type_id = serializers.IntegerField(required=True)
    no_occupants = serializers.IntegerField(required=True)

    class Meta:
        model = Reservation
        fields = '__all__'

    def __init__(self, data):
        super(ReservationSerializer,self).__init__(self, data=data)

    def save(self, validated_user_data):
        res = Reservation(customer_id=Customer.objects.get(id=validated_user_data['customer_id']),
                          check_in=validated_user_data['check_in'],
                          check_out=validated_user_data['check_out'],
                          room_type_id=RoomType.objects.get(id=validated_user_data['room_type_id']),
                          no_occupants=validated_user_data['no_occupants'])
        res.save()
        return res
