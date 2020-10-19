from django.urls import path, include

from . import views


app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
]



# users/ login/ [name='login']
# users/ logout/ [name='logout']
# users/ password_change/ [name='password_change']
# users/ password_change/done/ [name='password_change_done']
# users/ password_reset/ [name='password_reset']
# users/ password_reset/done/ [name='password_reset_done']
# users/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
# users/ reset/done/ [name='password_reset_complete']
