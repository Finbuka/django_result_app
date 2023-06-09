from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required 
from . import views as def_views
from .forms import ChangePass,customPasswordResetForm
from django.urls import reverse_lazy



urlpatterns = [
    path('sign_in/', def_views.SignIn.as_view(),name="sign_in"),
    path('sign_up/', def_views.SignUp.as_view(),name="sign_up"),
    path('sign_out/', auth_views.LogoutView.as_view(next_page ='sign_in'),name='sign_out'),

    path('mail/', def_views.mail),

    path('result_page/<int:year>/', login_required(def_views.ResultPage.as_view()),name="result_page"),
    path('stats/', login_required(def_views.Stats.as_view()),name="stats"),
    path('profile/', login_required(TemplateView.as_view(template_name='dashboard.html')),name='dashboard'),
    path('settings/',login_required(def_views.UpdateProfile.as_view()),name='settings'),

    path('about/', TemplateView.as_view(template_name='about.html'),name='about'),
    path('contact/',  def_views.mail,name='contact'),


    path('password_change/',auth_views.PasswordChangeView.as_view(form_class = ChangePass,
                                                                  template_name = "pass_reset.html"),name='password_change'),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(template_name = "passwd_ch_done.html"),name='password_change_done'),
    path('password_reset/',auth_views.PasswordResetView.as_view( template_name="forgot-password.html",
                                                                success_url = reverse_lazy("password_reset_done"),
                                                                form_class = customPasswordResetForm ) ,name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),


    path('', def_views.Index.as_view(),name="index"),
]
