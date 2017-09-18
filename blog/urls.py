from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^users/',include('users.urls',namespace='users')),
	url(r'^users/', include('django.contrib.auth.urls')),
	url(r'',include('blogs.urls',namespace='blogs')),
	url(r'^comments/',include('comments.urls',namespace='comments')),
	url(r'^message/',include('message.urls',namespace='message')),
	url(r'^action/',include('action.urls',namespace='action')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)