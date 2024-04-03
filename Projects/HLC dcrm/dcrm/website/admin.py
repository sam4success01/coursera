from django.contrib import admin
from .models import Record, UsheringData

# Register your models here.

admin.site.register(Record)
admin.site.register(UsheringData)

# admin.site.register(YorubaAttendances)
# admin.site.register(ChildrenAttendances)
# admin.site.register(TeenagersAttendances)
# admin.site.register(OnlineAttendances)
# admin.site.register(offerings)