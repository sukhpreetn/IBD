from django.urls import path , include
from . import views
from django.views.generic.base import TemplateView # new


app_name = 'ibd'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', TemplateView.as_view(template_name='ibd/index.html'), name='index'),  # new
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('donorlist/', views.DonorList.as_view()),
    path('donordetail/<pk>/', views.DonorDetail.as_view()),
    path('adddonor/', views.AddDonor.as_view()),
    path('updatedonor/<pk>/', views.UpdateDonor.as_view()),
    path('login/', views.login, name='login'),
    path('unsubscribe/', views.unsubscribe, name='unsubscribe'),
    path('forgetpwd/', views.forgetpwd, name='forgetpwd'),
    path('poster/', views.poster, name='poster'),
    path('privacypolicy/', views.privacypolicy, name='privacypolicy'),
    path('welcome/', views.welcome, name='welcome'),
    path('register/', views.register, name='register'),
    path('registersucess/', views.registersucess, name='registersucess'),
    path('note/', views.note, name='note'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('update_profile/<int:pk>/', views.update_profile, name='update_profile'),
    path('updatesucess/<int:pk>/', views.updatesucess, name='updatesucess'),
    path('user_history/<int:pk>/', views.user_history, name='user_history'),
    path('chng_pwd/<int:pk>/', views.chng_pwd, name='chng_pwd'),
    path('pwdchangesucess/<int:pk>/', views.pwdchangesucess, name='pwdchangesucess'),
    path('notmatch/', views.notmatch, name='notmatch'),
    path('logout/', views.logout, name='logout'),
    path('inthenews/', views.inthenews, name='inthenews'),
    path('donorsfaqs/', views.donorsfaqs, name='donorsfaqs'),

]