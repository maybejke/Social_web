from django.urls import path, reverse_lazy
from .views import dashboard
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login, PasswordChangeView, \
    PasswordChangeDoneView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, \
    PasswordResetCompleteView

from .views import user_login

app_name = 'account'

# urlpatterns = [
#     path('login/', user_login, name='login'),
urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('login/', LoginView.as_view(template_name='account/registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='account/registration/logout.html'), name='logout'),
    path('logout_then_login', logout_then_login, name='logout_then_login'),
    # change password
    path('password_change/', PasswordChangeView.as_view(success_url=reverse_lazy('account:password_change_done'),
                                                        template_name='account/registration/password_change.html'),
         name='password_change'),
    path('password_change_done/',
         PasswordChangeDoneView.as_view(template_name='account/registration/password_change_done.html'),
         name='password_change_done'),
    # reset password
    path('password_reset/',
         PasswordResetView.as_view(template_name='account/registration/password_reset_form.html',
                                   email_template_name='account/registration/password_reset_email.html',
                                   success_url='done/'),
         name='password_reset'),
    path('password_reset_complete/',
         PasswordResetCompleteView.as_view(template_name='account/registration/password_reset_complete.html'),
         name='password_reset_complete'),
    path('password_reset/done/',
         PasswordResetDoneView.as_view(template_name='account/registration/password_reset_done.html'),
         name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='account/registration/password_reset_confirm.html',
         success_url='/account/password_reset_complete/'),
         name='password_reset_confirm'),

]
# ]

