from django.urls import path, include
from authy.views import Profile,login, signup, PsswordChange, PasswordChangeDone
from django.contrib.auth import views as authViews

urlpatterns = [
    path('profile/', Profile, name='profile'),
    path('login/', authViews.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', authViews.LogoutView.as_view(), {'next_page' : 'index'}, name='logout'),
    path('signup/', signup, name="signup"),
    path('changepassword/', PsswordChange, name='change_password'),
    path('changepasswordone/', PasswordChangeDone, name='change_password_done'),
    # path('passwordreset/', authViews.PasswordResetView.as_view(), name='password_reset'),
    # path('passwordreset/done', authViews.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>', authViews.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', authViews.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('', include('django.contrib.auth.urls'))

]
