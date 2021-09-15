from django.urls import path
from logs import views
  
urlpatterns = [
    path('login/', views.login.as_view()),
    path('logout/', views.logout.as_view()),
    path('delete/', views.logDelete.as_view()),
    path('i_login/', views.iLogin.as_view()),
    path('i_logout/', views.iLogout.as_view()),
    # #Download xls
    path('logs/', views.userLogs.as_view()),
    path('all_logs/', views.allLogs.as_view()),
    path('change/', views.changeWW.as_view()),
    path('download_report/', views.downloadReport.as_view()),
    path('bulk_upload/', views.uploadWW.as_view()),
]