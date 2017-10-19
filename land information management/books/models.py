from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30,blank=True)
    country = models.CharField(max_length=50)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True)

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()

    def __str__(self):
        return self.title


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
        return u'%s %d' %(self.tax_id,self.date)





