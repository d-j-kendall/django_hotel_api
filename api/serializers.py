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

    class Meta:
        model = Reservation
        fields = (
            'confirmation_number',
            'customer_id',
            'check_in',
            'check_out',
            'checked_in',
            'checked_out',
            'room_number',
            'room_type_id',
            'no_occupants',
            'guaranteed',
            )
        