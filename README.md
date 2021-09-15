**********************************
        API Endpoints
**********************************
superuser: 20210003441
password: Getmein 1

user1: 20210003001
password: Getmein 1

user2: 20210003002
password: Getmein 1

user3: 20210003003
password: Getmein 1

--------------------------------------------

API: POST http://127.0.0.1:8000/auth/users/
API description: CREATING USER
API request payload: 
'Email'
'First name'
'Last name'
'Start time'
--:--:--
'End time'
--:--:--
'Phone'
'Username'
'Password'

--------------------------------------------

API: GET http://127.0.0.1:8000/user/user_list/
API description: GET ALL USERS

--------------------------------------------

API: POST http://127.0.0.1:8000/auth/jwt/create/
API description: TOKEN GENERATION
API request payload:
'Username'
'Password'

--------------------------------------------

API: POST http://127.0.0.1:8000/auth/jwt/refresh/
API description: REFRESH GENERATION
API request payload:
'Refresh token'

--------------------------------------------

API: POST http://127.0.0.1:8000/logs/login/
API description: USER LOGIN - This is the API for user to login
at the beginning of the workday.

--------------------------------------------

API: POST http://127.0.0.1:8000/logs/logout/
API description: USER LOGOUT - This is the API for user to logout
at the end of the workday.

--------------------------------------------

API: POST http://127.0.0.1:8000/logs/i_login/
API description:  USER AFTER BREAK LOGIN - This API is used for resuming
breaks allowed during the worktime.

--------------------------------------------

API: POST http://127.0.0.1:8000/logs/i_logout/
API description:  USER BREAK LOGOUT - This API is used for takinf
breaks during the worktime.

--------------------------------------------

API: GET http://127.0.0.1:8000/logs/logs/?date=15-09-2021
API description:  USER LOGIN REPORT - This API is for individual user log report.
Can be fetched datewise passing date in payload. If not date is passed
responds with currend day logs.
API request payload:
'date'

--------------------------------------------

API: GET http://127.0.0.1:8000/logs/all_logs/?date=15-09-2021
API description:  USER LOGIN REPORT - This API is for all user log report.
Can be fetched datewise passing date in payload. If not date is passed
responds with currend day logs. This API can be accessed by Admin users only.
API request payload:
'date'

--------------------------------------------

API: POST http://127.0.0.1:8000/logs/change/?start=10:30:00&end=15:00:00
API description:  CHANGE USER START AND END TIME - API is used to change users
start_time and end_time.
API request payload:
'start'
'end

--------------------------------------------

API: POST http://127.0.0.1:8000/logs/change/?start=10:30:00&end=15:00:00
API description:  CHANGE USER START AND END TIME - API is used to change users
start_time and end_time.
API request payload:
'start'
'end'

--------------------------------------------

API: GET http://127.0.0.1:8000/logs/download_report/?date=15-09-2021
API description:  DOWNLOAD USER LOG REPORTS - Pass the date for downloading 
the user logs report in excel format.
API request payload:
'date'

--------------------------------------------

API: GET http://127.0.0.1:8000/logs/bulk_upload/
API description:  DOWNLOAD FORMAT FOR BULK UPLOAD - This API will 
respond with the excel file for sample formating.

--------------------------------------------

API: POST http://127.0.0.1:8000/logs/bulk_upload/
API description:  BULK UPLOAD USER START_TIME AND END_TIME - This API will 
allow the admin to update the user start_time and end_time.
API request payload:
'excel_file'