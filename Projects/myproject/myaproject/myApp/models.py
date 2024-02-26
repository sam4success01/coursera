from django.db import models

# Create your models here.


class Logger(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    contact_no = models.CharField('Phone Number', max_length=300, default="")
    time = models.TimeField()
    notes = models.CharField(max_length=300, blank=True)
    time_log = models.TimeField(help_text="Enter exact time")
    
    def __str__(self):
        return self.first_name
    

class NewMenus(models.Model):
    name = models.CharField(max_length = 200)
    price = models.IntegerField()

    def __str__(self):
        return self.name



class MenuCategory(models.Model):
    menu_category_name = models.CharField(max_length = 200)


class Menu(models.Model):
    menu_item = models.CharField(max_length = 200)
    price = models.IntegerField(null=False)
    category_id = models.ForeignKey(MenuCategory, on_delete=models.PROTECT, default=None)