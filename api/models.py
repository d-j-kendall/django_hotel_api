from django.db import models

# Create your models here.


class Reservation(models.Model):

    confirmation_number = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey('Customer', on_delete=models.CASCADE,)
    check_in = models.DateField()
    check_out = models.DateField()
    checked_in = models.BooleanField(default=False)
    checked_out = models.BooleanField(default=False)
    room_number = models.IntegerField(default=0)
    room_type_id = models.ForeignKey('RoomType', on_delete=models.CASCADE, )
    no_occupants = models.IntegerField()
    guaranteed = models.BooleanField(default=False)

    def __str__(self):
        return self.confirmation_number


class Transaction(models.Model):

    id = models.AutoField(primary_key=True)
    confirmation_number = models.ForeignKey('Reservation', on_delete=models.CASCADE)
    transaction_amount = models.FloatField(default=0.00)

    def __str__(self):
        return '%s - %s' % (self.id, self.confirmation_number)


class Customer(models.Model):

    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=50)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=40)
    state_province = models.CharField(max_length=40)
    email_address = models.CharField(max_length=50)

    def __str__(self):
        return '%s %s'%(self.first_name, self.last_name)


class RoomType(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=20)

    def __str__(self):
        return str(type)

