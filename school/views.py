from rest_framework import viewsets, generics
from school.models import Student, Course, Enrollment
from school.serializer import StudentSerializer, StudentSerializerV2, CourseSerializer, EnrollmentSerializer, StudentEnrollmentsListSerializer, EnrolledStudentsListSerializer

class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    def get_serializer_class(self):
        if (self.request.version == 'V2'):
            return StudentSerializerV2
        else:
            return StudentSerializer

class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class EnrollmentsViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class StudentEnrollmentsList(generics.ListAPIView):
    def get_queryset(self):
        queryset = Enrollment.objects.filter(student_id=self.kwargs['pk'])
        return queryset
    serializer_class = StudentEnrollmentsListSerializer

class EnrolledStudentsList(generics.ListAPIView):
    def get_queryset(self):
        queryset = Enrollment.objects.filter(course_id=self.kwargs['pk'])
        return queryset
    serializer_class = EnrolledStudentsListSerializer