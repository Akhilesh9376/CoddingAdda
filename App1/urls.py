from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('',views.Home,name="Home"),
    path('team',views.Team,name='Team'),
    path('contact',views.Contact,name='Contact'),
    path('pricing',views.Price,name="Price"),
    path('blog',views.blog,name="Blog"),
    path('blog/post/<int:post_id>/', views.post, name="post"),
    path('services/fullstackdeveloper',views.fsd,name="fsd"),
    path('services/digitalmarketing',views.dm,name='dm'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

