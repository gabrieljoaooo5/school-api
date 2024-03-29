from django.contrib import admin
from django.urls import path,include
from school.views import StudentsViewSet, CoursesViewSet, EnrollmentsViewSet, StudentEnrollmentsList, EnrolledStudentsList
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('students', StudentsViewSet, basename='Students')
router.register('courses', CoursesViewSet, basename='Courses')
router.register('enrollments', EnrollmentsViewSet, basename='Enrollments')

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('admin-panel/', admin.site.urls),
    path('', include(router.urls) ),
    path('students/<int:pk>/enrollments/', StudentEnrollmentsList.as_view()),
    path('courses/<int:pk>/enrollments/', EnrolledStudentsList.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)