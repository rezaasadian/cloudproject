from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from Project1 import views


router = DefaultRouter()
router.register('doctors', views.DoctorViewSet_user)
router.register('admin/doctors', views.DoctorViewSet_admin)
router.register('DoctorTime', views.VisitTimeViewSet_user)
router.register('admin/DoctorTime', views.VisitTimeViewSet_admin)
router.register('admin/visittime', views.UserVisitTimeViewSet_admin)
router.register('comment', views.CommentOnDoctor_user)
router.register('favorite', views.UserFavoriteViewSet)

urlpatterns = [
     url('newuser', views.create_user),
     url('profile', views.UserProfileViewSet),
]

urlpatterns += router.urls
