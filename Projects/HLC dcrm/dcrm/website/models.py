from django.db import models

from datetime import date

# Create your models here.

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")
    

class UsheringData(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    date = models.DateField(default=date.today)
    session = models.CharField(max_length=100)
    minister = models.CharField(max_length=100)
    message = models.CharField(max_length=300)
    no_of_male = models.PositiveIntegerField(null=True, blank=True)
    no_of_female = models.PositiveIntegerField(null=True, blank=True)
    no_of_boys = models.PositiveIntegerField(null=True, blank=True)
    no_of_girls = models.PositiveIntegerField(null=True, blank=True)
    no_of_ymale = models.PositiveIntegerField(null=True, blank=True)
    no_of_yfemale = models.PositiveIntegerField(null=True, blank=True)
    no_of_yboys = models.PositiveIntegerField(null=True, blank=True)
    no_of_ygirls = models.PositiveIntegerField(null=True, blank=True)
    no_of_cmale = models.PositiveIntegerField(null=True, blank=True)
    no_of_cfemale = models.PositiveIntegerField(null=True, blank=True)
    no_of_cboys = models.PositiveIntegerField(null=True, blank=True)
    no_of_cgirls = models.PositiveIntegerField(null=True, blank=True)
    no_of_tmale = models.PositiveIntegerField(null=True, blank=True)
    no_of_tfemale = models.PositiveIntegerField(null=True, blank=True)
    no_of_tboys = models.PositiveIntegerField(null=True, blank=True)
    no_of_tgirls = models.PositiveIntegerField(null=True, blank=True)
    instagram = models.PositiveIntegerField(null=True, blank=True)
    youtube = models.PositiveIntegerField(null=True, blank=True)
    mixlr = models.PositiveIntegerField(null=True, blank=True)
    facebook = models.PositiveIntegerField(null=True, blank=True)
    website = models.PositiveIntegerField(null=True, blank=True)
    offering_main = models.FloatField(null=True, blank=True)
    tithe = models.FloatField(null=True, blank=True)
    seed = models.FloatField(null=True, blank=True)
    vow = models.FloatField(null=True, blank=True)
    firstfruit = models.FloatField(null=True, blank=True)
    cheque = models.FloatField(null=True, blank=True)
    pos = models.FloatField(null=True, blank=True)
    offering_children = models.FloatField(null=True, blank=True)
    offering_teenagers = models.FloatField(null=True, blank=True)
    foreign_currency = models.CharField(max_length=300)
    

    def __str__(self):
        return str(self.date)
    
    def total_no_of_main(self):
        return self.no_of_male + self.no_of_female + self.no_of_boys + self.no_of_girls
    
    def total_no_of_yoruba(self):
        return self.no_of_ymale + self.no_of_yfemale + self.no_of_yboys + self.no_of_ygirls
    
    def total_no_of_children(self):
        return self.no_of_cmale + self.no_of_cfemale + self.no_of_cboys + self.no_of_cgirls
    
    def total_no_of_teenagers(self):
        return self.no_of_tmale + self.no_of_tfemale + self.no_of_tboys + self.no_of_tgirls
    
    def total_no_of_online(self):
        return self.instagram + self.youtube + self.mixlr + self.facebook + self.website 
    
    def total_no_of_offering(self):
        return self.offering_main + self.tithe + self.seed + self.vow + self.firstfruit + self.offering_children + self.offering_teenagers