from django.contrib.auth.models import User
from django.db import models
from users.models import User

# Create your models here.

class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    total_logins = models.IntegerField(null=True, default=1)
    total_logouts = models.IntegerField(null=True, default=0)
    attendance_status = models.CharField(null=True, max_length=9)
    working_window = models.IntegerField(null=True, default=0)
    active_window  = models.IntegerField(null=True, default=0)
    is_completed = models.BooleanField(null=True, default=False)

    def __str__(self):
        return self.user.username

class Logs(models.Model):
    logid = models.ForeignKey(Attendance, on_delete=models.CASCADE) 
    type = models.BooleanField(null=True, default=False) # 0 - logged out | 1 - logged in
    time = models.TimeField(auto_now=True, auto_now_add=False)
    active_time = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.logid.user.username + ' - ' + str(self.logid.date) 

