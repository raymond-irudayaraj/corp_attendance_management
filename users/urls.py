from django.urls import path
from users import views
  
urlpatterns = [
    path('user_list/', views.UserList.as_view()),
    #Upload xls
    # path('bulk_add/', views.UserList.as_view()),
]