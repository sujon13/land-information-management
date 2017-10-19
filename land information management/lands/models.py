from django.db import models

# Create your models here.


class User(models.Model):
    user_id=models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    password=models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30, blank=True)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.user_id

class Roles(models.Model):
    roles_id=models.OneToOneField(User)
    role_status=models.IntegerField()

    def __str__(self):
        return self.role_status






class Land(models.Model):
    land_id=models.CharField(max_length=100)
    owners=models.ManyToManyField(User)
    division=models.CharField(max_length=100)
    zilla=models.CharField(max_length=100)
    upazilla=models.CharField(max_length=100)
    mouja=models.CharField(max_length=100)
    dag_no=models.IntegerField()
    catagory=models.CharField(max_length=100)
    area=models.FloatField()
    up_for_sale=models.CharField(max_length=100)

    def __str__(self):
        return self.land_id


class Tax(models.Model):

    tax_id=models.ForeignKey(Land)
    #tax_id=models.CharField(max_length=50)
    year=models.IntegerField()
    paid=models.IntegerField()

    def __str__(self):
        return u'%s %d' %(self.tax_id,self.year)





class UserLand(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    land = models.ForeignKey(Land, on_delete=models.CASCADE)
