from django.contrib import admin
from django.urls import path, include
from Book import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookList/',views.BookList.as_view(),name="bookList"),
    path('bookRud/<int:pk>/',views.BookListRUD.as_view(),name="bookRud"),
    path('auth/',include('rest_framework.urls',
                         namespace='rest_framework')),

    path('gettoken/',TokenObtainPairView.as_view(),name="token-obtain"),
    path('refreshtoken/',TokenRefreshView.as_view(),name="token-refresh"),
    path('verifytoken/',TokenVerifyView.as_view(),name="token-verify"),

]
