from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.authtoken import views
from django.urls import path
from restapi.views import *
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id','username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    search_fields = [ 'username']
    filter_backends = (filters.SearchFilter,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('authors', AuthorViewSet)
router.register('loans', LoanViewSet)

router.register('books', BookViewSet) 
router.register('countries', CountryViewSet) 
router.register('editors', EditorViewSet) 
router.register('sezioni', SezioneViewSet) 
router.register('genres', GenreViewSet) 
router.register('volumes', VolumeViewSet) 
#router.register('prenotations', PrenotationViewSet) 
#router.register('search', QuestionsAPIView) 


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
  
    path('', include(router.urls)),
    path('restapi/', include('restapi.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth' ),
    

    #path('api/instances/', views.LoanViewSet.as_view(), name="instances"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)