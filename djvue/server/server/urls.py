from django.conf.urls import url, include
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.urls import path
from restapi.views import *
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('authors', AuthorViewSet)
#router.register('creazione', AuthoriViewSet)
router.register('books', BookViewSet) 
router.register('countries', CountryViewSet) 
router.register('editors', EditorViewSet) 
router.register('genres', GenreViewSet) 
router.register('volumes', VolumeViewSet) 
#router.register('prenotations', PrenotationViewSet) 
router.register('loans', LoanViewSet) 


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]