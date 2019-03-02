from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from accounts import views as accounts_views
from blog import views as blog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', accounts_views.register, name='register'),
    path('profile/', accounts_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
    path('user/<str:username>', blog_views.UserPostListView.as_view(), name='user-post'),
    path('create/', blog_views.PostCreateView.as_view(), name='post-create'),
    path('blog/', include('blog.urls')), 
    path('contact/', include('contact.urls')),
    path('', include('pages.urls')),  
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
