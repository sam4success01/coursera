from django.urls import path

from . import views




urlpatterns = [
    path('', views.home, name='home'),
    path('report', views.report, name='report'),
    path('reports', views.reports, name='reports'),
    path('attendance', views.attendance, name='attendance'),
    path('main_attendance', views.MainAttendanceWizard.as_view(), name='main_attendance'),
    path('mainattendance_report', views.mainattendance_report, name='mainattendance_report'),
    path('yorubaattendance_report', views.yorubaattendance_report, name='yorubaattendance_report'),
    path('childrenattendance_report', views.childrenattendance_report, name='childrenattendance_report'),
    path('teenagersattendance_report', views.teenagersattendance_report, name='teenagersattendance_report'),
    path('onlineattendance_report', views.onlineattendance_report, name='onlineattendance_report'),
    path('offering_report', views.offering_report, name='offering_report'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('record/<int:pk>', views.customer_record, name='record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update_record'),
    path('edit_record/<int:record_id>/', views.edit_record, name='edit_record'),
    path('delete_records/<int:record_id>/', views.delete_records, name='delete_records'),
    path('import-csv/', views.import_csv, name='import_csv'),
    path('download_report/', views.download_report, name='download_report'),

]